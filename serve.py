#!/usr/bin/env python3
"""
The Unofficial Guide — the same pipeline, over HTTP.

    python serve.py                          run it locally on port 5000
    gunicorn serve:app                       run it the way a host runs it

Nothing new happens in this file. It is a wrapper: a request comes in, it
hands the question to `app.py::ask_pipeline` — the exact function the command
line uses — and hands the answer back as JSON. Retrieval, the relevance gate
and the grounded prompt all still live where they lived. If you change how
your system answers, you change it in those files and this one follows.

Two routes:

    POST /ask       {"question": "..."} in, the answer and its sources out
    GET  /health    is the service up, and is there an index to search

Why this exists: `app.py` runs once and exits, which is fine on your laptop
and impossible to deploy. A hosted service has to stay up and wait for
requests. This is the smallest thing that does that.

Unit 3 adds two things and nothing else:

    - every /ask writes one JSON line to logs/requests.jsonl: the question,
      the outcome, best distance, latency, tokens, cache hit and cost
    - `python serve.py` builds the search index first if there isn't one, so
      a clean checkout starts with one command
"""

import json
import os
import time
from datetime import datetime, timezone

from flask import Flask, jsonify, request

import config

app = Flask(__name__)


# ─── Request log (unit 3) ────────────────────────────────────────────────────

def _cost(prompt_tokens: int, output_tokens: int) -> float | None:
    """Dollars for one request, from the tokens Gemini reported. None if no price is set."""
    if config.PRICE_INPUT_PER_M is None or config.PRICE_OUTPUT_PER_M is None:
        return None
    return round(
        prompt_tokens / 1e6 * config.PRICE_INPUT_PER_M
        + output_tokens / 1e6 * config.PRICE_OUTPUT_PER_M,
        8,
    )


def _log_request(entry: dict) -> None:
    """Append one request to the log. A logging failure never fails the request."""
    try:
        config.REQUEST_LOG.parent.mkdir(parents=True, exist_ok=True)
        with config.REQUEST_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")
    except Exception as exc:  # noqa: BLE001
        print(f"!! could not write request log: {exc}")


@app.get("/health")
def health():
    """Is the service up, and is there an index to search?

    Two different questions, and the second one is the one that bites. A
    freshly deployed service answers this route happily while every /ask
    returns "no index" — hosts give you no disk that survives a restart, so
    the index has to be built as part of getting the service up. Checking
    here means you find that out in one request instead of five.
    """
    from store import index_exists

    ready = index_exists(config.CORPUS)
    return jsonify(
        {
            "status": "ok",
            "corpus": config.CORPUS,
            "index_ready": ready,
            "detail": (
                "ready"
                if ready
                else "no index for this corpus — run `python app.py index`"
            ),
        }
    )


@app.post("/ask")
def ask():
    """One question in, one grounded answer out.

    A refused question is a 200, not an error. The gate refusing is your
    system working — it is an answer, and the JSON says so with
    `"refused": true` so whatever calls this can tell the two apart.
    """
    from app import ask_pipeline
    import generate

    started = time.perf_counter()
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "question": None,
        "status": None,
        "outcome": None,          # answered / refused / bad_request / error
        "best_distance": None,
        "threshold": None,
        "sources": [],
        "model_calls": 0,
        "cache_hit": False,
        "prompt_tokens": 0,
        "output_tokens": 0,
        "cost_usd": None,
        "latency_ms": None,
        "error": None,
    }

    def finish(status: int, outcome: str) -> None:
        entry["status"] = status
        entry["outcome"] = outcome
        entry["latency_ms"] = round((time.perf_counter() - started) * 1000, 1)
        _log_request(entry)

    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        payload = {}
    raw = payload.get("question")
    question = raw.strip() if isinstance(raw, str) else ""
    entry["question"] = question or None

    if not question:
        finish(400, "bad_request")
        return (
            jsonify(
                {
                    "error": "Send JSON with a question in it, like "
                    '{"question": "is the housing lottery random?"}'
                }
            ),
            400,
        )

    # generate.py keeps running totals for the session; this request's share
    # is the difference before and after. (Fine for one local user; two
    # requests at the same moment would blur each other's counts.)
    tokens_before = generate.token_counts()
    calls_before = generate.call_count()
    hits_before = generate._cache_hits

    def record_usage() -> None:
        tokens_after = generate.token_counts()
        entry["prompt_tokens"] = tokens_after["prompt"] - tokens_before["prompt"]
        entry["output_tokens"] = tokens_after["output"] - tokens_before["output"]
        entry["model_calls"] = generate.call_count() - calls_before
        entry["cache_hit"] = generate._cache_hits > hits_before
        entry["cost_usd"] = _cost(entry["prompt_tokens"], entry["output_tokens"])

    try:
        outcome = ask_pipeline(question, corpus=config.CORPUS)
    except Exception as exc:  # noqa: BLE001 — a reader gets this, not a traceback
        record_usage()
        entry["error"] = f"{type(exc).__name__}: {exc}"
        finish(500, "error")
        return jsonify({"error": f"{type(exc).__name__}: {exc}"}), 500

    record_usage()
    entry["best_distance"] = round(outcome["best_distance"], 4)
    entry["threshold"] = outcome["threshold"]
    entry["sources"] = outcome["sources"]
    finish(200, "refused" if outcome["refused"] else "answered")

    return jsonify(
        {
            "question": question,
            "answer": outcome["answer"],
            "refused": outcome["refused"],
            "sources": outcome["sources"],
            "best_distance": round(outcome["best_distance"], 4),
            "threshold": outcome["threshold"],
            "corpus": config.CORPUS,
        }
    )


def main():
    # Hosts tell you which port to listen on through PORT, and they expect you
    # on 0.0.0.0. Binding 127.0.0.1 instead works perfectly on your laptop and
    # then answers nothing at all once deployed, because the host's router
    # can't reach a socket that only accepts connections from inside the
    # container. It is the single most common way a first deploy "succeeds"
    # and is unreachable.
    port = int(os.getenv("PORT", "5000"))

    # Debug mode reloads on save, which is handy, and prints a console that
    # runs arbitrary code, which is not something to leave switched on where
    # strangers can reach it. Off unless you ask for it.
    debug = os.getenv("AI201_DEBUG", "0") == "1"

    # Unit 3: one command from a clean checkout. chroma_db/ is gitignored, so a
    # fresh clone has no index and every /ask would fail. Build it first.
    from store import index_exists

    if not index_exists(config.CORPUS):
        import argparse
        from app import cmd_index

        print("No search index yet. Building it before the server starts.\n")
        cmd_index(argparse.Namespace(corpus=config.CORPUS, variant="default"))
        print()

    print(f"Request log: {config.REQUEST_LOG}")
    print(f"Serving The Unofficial Guide on http://localhost:{port}")
    print(f"Corpus: {config.CORPUS}    (Ctrl-C to stop)\n")
    print("Try it from another terminal:\n")
    print(f"  curl http://localhost:{port}/health")
    print(
        f"  curl -X POST http://localhost:{port}/ask \\\n"
        f"    -H 'Content-Type: application/json' \\\n"
        f"    -d '{{\"question\": \"is the housing lottery random?\"}}'\n"
    )

    app.run(host="0.0.0.0", port=port, debug=debug)


if __name__ == "__main__":
    main()
