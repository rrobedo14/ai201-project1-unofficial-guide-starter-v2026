# The Unofficial Guide

<!-- Rogelio Robedo (campus_life) -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

> I picked the campus life corpus because it provides practical, everyday information that makes navigating university life much easier. The system answers questions about campus dining hours, pricing, and locations, such as finding the closest dining hall to the library. Ultimately, it helps students optimize their schedules and budgets while getting around campus efficiently.

## Chunking Strategy

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.
 
     Milestone 3.-->

- **Chunk size: 700**
- **Overlap: 50**

> I initially set a much larger chunk size of 2000 with zero overlap, thinking that keeping massive blocks would preserve as much context as possible. However, after looking at the actual campus life documents, I realized that swallowed multiple distinct topics (like mixing dining hall hours with building locations) into a single block.
>
> I experimented with smaller fractional splits next, but they frequently chopped sentences in half. Settling on a chunk size of 700 with a 50-character overlap hit the sweet spot: it kept individual schedule or dining descriptions coherent and self-contained, while the small overlap ensured smooth continuity across chunk boundaries.

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

```text
======================================================================
Chunk 1  |  source: admin_add_drop_deadline.txt#0  |  produced by: chunker.py::split_documents
======================================================================
On the add/drop deadline

You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.
```

```text
======================================================================
Chunk 2  |  source: course_biol_160.txt#0  |  produced by: chunker.py::split_documents
======================================================================
BIOL 160 Cell Biology

I lived here my sophomore year. Format is lecture three times a week with a weekly lab. Assessment: four unit tests and a cumulative final. Not curved.

Expect 9 to 11 hours a week, the heaviest first-year course by reputation.

The one piece of advice: the unit tests come fast, roughly every three weeks; falling behind once is very hard to recover from.
```

```text
======================================================================
Chunk 3  |  source: course_hist_118_workload.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Workload for HIST 118 Modern World History

People keep asking so: a lot of reading, about 120 pages a week, but no problem sets. That's real time, not optimistic time.

It's front-loaded — the first month is heavier than the rest, partly because you're learning the format.
```

```text
======================================================================
Chunk 4  |  source: dining_pellew_dining_hall_followup.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.
```

```text
======================================================================
Chunk 5  |  source: housing_innisfree_hall.txt#0  |  produced by: chunker.py::split_documents
======================================================================
Innisfree Hall — what it's actually like

Transferred in last year, so take this with a grain of salt. Built 1991, renovated 2022. Rooms are doubles arranged as pairs sharing one bathroom between two rooms.

The good: the shared-bathroom-between-two-rooms arrangement is the best compromise on campus.

The bad: no air conditioning, which matters for the first three weeks of September.

Laundry costs $1.75 wash, $1.75 dry, app-based. On noise: moderate; the building is L-shaped and the short wing is much quieter.
```

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. 
     
     Milestone 4.--> 

```console
$ python app.py ask "When is the best time to visit the dining hall?" --show-prompt
  (best distance 0.377, cutoff 0.6)

======================================================================
System instruction sent with the prompt
======================================================================
You answer questions using only the documents provided to you.

Rules:
- Use only the information in the documents below. Do not use anything you know from elsewhere.
- If the documents don't cover the question, say you don't have enough information. Do not guess.
- Name the document your answer came from, using the filename given in each excerpt.
- Be brief. Two or three sentences is usually enough.

======================================================================
The assembled prompt, exactly as sent
======================================================================
Documents:

[from dining_pellew_dining_hall_followup.txt]
Re: Pellew Dining Hall

Adding to what people have said about Pellew Dining Hall. The wait figure of 12 to 18 minutes at peak matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: the furthest hall from anywhere, next to the athletics centre. Nobody tells you this at orientation.

[from dining_halden_hall_followup.txt]
Re: Halden Hall

Adding to what people have said about Halden Hall. The wait figure of rarely more than 8 minutes matches what I've seen. If you're tryingto eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: closes at 7:00pm, which catches people out. Nobody tells you this at orientation.

[from dining_halden_hall.txt]
Halden Hall

I lived here my sophomore year. Wait times: rarely more than 8 minutes, even at noon. The thing worth going for is soup rotation, and thebread is baked on site. The thing to know is that closes at 7:00pm, which catches people out.

Hours are 7:30am to 7:00pm weekdays, closed Sundays. Costs one meal swipe, or $10.00 cash.

[from dining_pellew_dining_hall.txt]
Pellew Dining Hall

Second-year here. Wait times: 12 to 18 minutes at peak, and the peak is early — 11:45 to 12:30. The thing worth going for is a dedicated allergen-free station staffed by someone who knows the menu. The thing to know is that the furthest hall from anywhere, next to the athletics centre.

Hours are 7:00am to 8:00pm daily. Costs one meal swipe, or $11.75 cash.

[from dining_north_kitchen_followup.txt]
Re: North Kitchen

Adding to what people have said about North Kitchen. The wait figure of none matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely.

Also worth saying: closed all summer and during reading week. Nobody tells you this at orientation.

---

Question: When is the best time to visit the dining hall?

Answer using only the documents above, and name the file you used.
======================================================================

To avoid the peak wait times between classes, it is recommended to go before 11:45 (`dining_pellew_dining_hall_followup.txt`, `dining_halden_hall_followup.txt`, and `dining_north_kitchen_followup.txt`).

Sources retrieved: dining_halden_hall.txt, dining_halden_hall_followup.txt, dining_north_kitchen_followup.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt

1 model calls this session, 731 tokens (668 in, 63 out)
```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->


| Question | In corpus? | Best distance |
|---|---|---|
| "When is the best time to visit the dining hall?" | Yes (Campus_Life) | 0.377 |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |
|  |  |  |

My cutoff was .6
Most of the questions fell into the .2 - .6 range of best distance for the campus life.
Most of the other OUT_OF_SCOPE questions were .8 or higher.

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it. 
     Milestone 5. -->


**1.** I asked Claude to evaluate my chunking function — I had selected a size of 800 and
an overlap of 100. Claude pointed out that the overlap was too big, and that as a result my
second chunk would largely be a copy of the first.

**2.** I asked Claude to help me debug an error I kept getting: `KeyError: '_type'`. The
diagnosis was a corrupted-cache situation, and the fix was `python -c "import store; store.reset()"`
followed by a re-index.


<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion                              | Target | Run 1 | Run 2 | Run 3 | Verdict |
|----------------------------------------|--------|-------|-------|-------|---------|
| 1. Retrieved chunk contains the answer | 4 of 5 |  4/5  |  4/5  | 4/5   |   MET   |
| 2. Every answer names a source         | 5 of 5 |  5/5  |  5/5  | 5/5   |  MET   |
| 3. Gate stops out-of-corpus questions  | 4 of 5 |  4/5  |  4/5  | 4/5   |   MET   |
| 4. No individual chunk exceeds 2,000   | 5 of 5 |  5/5  |  5/5  | 5/5   |  MET   |
| 5. Pre-AI context generation           | 4 of 5 |  0/5  |  0/5  | 0/5   |  MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion                          | Verdict | How I decided |
|---|------------------------------------|---------|---------------|
| 1. Retrieved chunk contains the answer |  MET    |4/5 on all the runs the one that failed was out of bounds|
| 2. Every answer names a source         |  MET    |5/5 All questions named a source|
| 3. Gate stops out-of-corpus questions  |  MET    |worst distance was .09 with 4/5 rejected
| 4. No individual chunk exceeds 2,000   |  MET    |5/5 for all runs|
| 5. Pre-AI context generation           |  MISSED |0/5 with no way to measure|

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

     Criterion 5 — pre-AI context generation.

     Not post-retrieval generation, but the formatting stage right before the LLM call. The search found the right documents, but the context generation script failed to inject the required metadata block—specifically the publication dates needed to verify that the information is pre-2022. The raw text chunks were dumped into the prompt payload stripped of their headers, leaving the model with no timeline anchors to evaluate age.

     The mechanism is tied to how the context builder processes chunk objects. The code extracted only the .content string of each chunk while dropping the dictionary attributes containing the publication dates. The system expected timestamped context blocks to be compiled, but the code only handed over unlabelled text snippets.

     Every test failed the exact same way: zero date metadata generated in the prompt payload across the board. Basic text queries worked fine, but any evaluation requiring temporal verification failed completely. Fixing the context assembly script to retain and prepend document headers with publication dates is what turns those zeros into passes.

## The Improvement

**What I changed:**

Two rules added to GROUNDING_INSTRUCTION in generate.py — one requiring every injected context chunk to display its publication date, one instructing the model to audit and report the temporal breakdown of sources while using all-time content. Nothing else changed: same chunker, same 94 chunks, same cutoff, same top-k.

- Every chunk injected into the prompt payload must retain its source metadata header showing the exact publication date.

- Review all retrieved sources and explicitly state the temporal breakdown (how many are pre-2022 vs. 2022 and later) while answering the prompt using all available content.

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

The diagnosis put the failure at pre-AI context generation — the right documents came back from the search, but the prompt instruction gave the model no rule to expose or track the dates — so the fix goes in the grounding instructions, which is the only thing bridging the metadata in the chunks and the final output text.

I want to be honest that this was not my first instinct. Writing a separate Python script to pre-filter or count dates upstream is on the menu, it sounds like more of a heavy engineering answer, and I had already opened up store.py to look at date-indexing filters before I re-read my own diagnosis. Filtering upstream would have restricted the model's access to all-time data and complicated the retrieval logic. Adding the tracking rule to the prompt instructions solved the evaluation check cleanly without changing the data pool.       


### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| # | Criterion                          | Verdict | How I decided |
|---|------------------------------------|---------|---------------|
| 1. Retrieved chunk contains the answer |  MET    |4/5 on all the runs the one that failed was out of bounds |
| 2. Every answer names a source         |  MET    |5/5 All questions named a source                          |
| 3. Gate stops out-of-corpus questions  |  MET    |worst distance was .09 with 4/5 rejected                  |
| 4. No individual chunk exceeds 2,000   |  MET    |5/5 for all runs                                          |
| 5. Pre-AI context generation           |  MISSED |0/5 non of the document had a publication date            |
**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

No, it made things worse, and I can say how I know: criterion 5 stayed at 0/5 and the logs confirmed that not a single chunk included a publication date. Telling the model to audit dates that weren't being sent to it didn't fix the problem; it backfired by asking the LLM to process and report on metadata that didn't exist in the prompt payload.

Two things stop me claiming more than that. A prompt rule is not a data pipeline fix. I changed the instructions and watched the score stay dead — I have not shown that prompt engineering can substitute for missing upstream metadata, which is exactly the shape of a shortcut that looks clever and fails. And forcing timeline instructions onto text that lacks timestamps has costs I didn't test. An instruction telling the model to find dates in text that lacks them just forces it to guess or hallucinate compliance. Nothing in my five criteria would catch that misdirection, which is a gap in my criteria and not a gap in the change. 

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

     Criterion 5: Pre-AI context generation (0/5)

What I'd do about it: Go back upstream to the ingestion pipeline, parse the publication date metadata during document loading, and explicitly bake the date header into the chunk's content string before it hits the vector store and gets sent in the prompt payload.

Why I stopped where I did: I ran out of time and hit the hard boundary between prompt engineering and data engineering. I tried to fix an upstream data pipeline bug with a downstream prompt instruction because it was a quicker fix, and it failed completely. Fixing it properly requires rewriting how chunks store and expose metadata, which is a separate engineering task that I didn't tackle today.

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

I would rewrite Criterion 5 ("Pre-AI context generation") to measure the payload content directly at the ingestion or assembly stage, rather than trying to evaluate it downstream through the LLM's final response or prompt rules.

As written, Criterion 5 conflated an upstream data pipeline requirement (injecting metadata into chunks) with a generation capability. Because the criterion relied on whether the model could see or process publication dates, it forced me into a confusing loop of trying to fix missing data structures with prompt instructions.

If I rewrote it, Criterion 5 would explicitly check that every chunk object in the final prompt payload contains a populated metadata dictionary or formatted header before the API call is ever made. That way, a missing date would fail an automated pre-flight assertion instantly, saving an afternoon of chasing ghost fixes in the prompt text.


# Unit 3

## The Shape

I'm taking shape A, deploy and instrument, on the local path (Path B). The Unofficial Guide already answers campus life questions end to end, but it only runs when I start it by hand, and once a question is answered nothing records what happened. I'm adding the operational layer around it: a single documented command that builds the search index if it's missing and starts `serve.py`, a structured log that writes one JSON line per `/ask` request (the question, whether it was answered or refused, the best retrieval distance, how long it took, and the input and output tokens Gemini reports), and a cost per question worked out from those logged tokens rather than guessed. The system's answering behaviour stays the same; what's new is that it can be started from a clean checkout with one command, and every request it handles leaves a record I can measure afterwards.

**Out of scope**

- **I'm not fixing the missing publication dates.** Criterion 5 from unit 2 failed because chunks don't carry their dates, and I already know the fix is in ingestion. But that's a new capability (shape C), not instrumentation, and it would change the answers I'm trying to measure.
- **I'm not hosting it.** I thought about deploying `serve.py` to a free host, since it already listens on `PORT` and `0.0.0.0`. Running locally with a committed log covers the same goals without spending the unit on accounts, secrets and a host's memory limits.
- **I'm not changing the cache or adding retries.** `generate.py` already caches answers, so a repeated question costs nothing. I'm leaving that as it is and logging when it's hit, rather than tuning it. Retrying failed Gemini calls is hardening (shape B). Either change would move the numbers before I've recorded what the system costs as it is.



## Instrumentation

Every `/ask` request writes one JSON line to `logs/requests.jsonl`. The code is
`serve.py::ask` and `serve.py::_log_request`. Each line records the question,
the HTTP status, the outcome (answered / refused / bad_request / error), the
best retrieval distance and the threshold it was compared to, the sources, how
many model calls it made, whether the answer came from the cache, the input
and output tokens Gemini reported, the cost, how long the request took, and
the error if there was one. A request that fails still gets a line. Logging is
wrapped so that a logging failure can never fail the request itself.

The full record of one real session on 2026-11-18, 16 requests against
`python serve.py` on the `campus_life` corpus, copied from
`logs/requests.jsonl` unedited:

```json
{"timestamp": "2026-11-18T01:13:59+00:00", "question": "What time does the dining hall near the library close?", "status": 200, "outcome": "answered", "best_distance": 0.3901, "threshold": 0.6, "sources": ["dining_halden_hall.txt", "dining_halden_hall_followup.txt", "dining_north_kitchen_followup.txt", "housing_morrow_house_noise.txt", "study_library_hours.txt"], "model_calls": 0, "cache_hit": true, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 142.7, "error": null}
{"timestamp": "2026-11-18T01:14:03+00:00", "question": "What is the capital of Mongolia?", "status": 200, "outcome": "refused", "best_distance": 0.8246, "threshold": 0.6, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 28.7, "error": null}
{"timestamp": "2026-11-18T01:14:06+00:00", "question": null, "status": 400, "outcome": "bad_request", "best_distance": null, "threshold": null, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 0.1, "error": null}
{"timestamp": "2026-11-18T01:14:10+00:00", "question": "What time does the dining hall near the library close?", "status": 200, "outcome": "answered", "best_distance": 0.3901, "threshold": 0.6, "sources": ["dining_halden_hall.txt", "dining_halden_hall_followup.txt", "dining_north_kitchen_followup.txt", "housing_morrow_house_noise.txt", "study_library_hours.txt"], "model_calls": 0, "cache_hit": true, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 28.1, "error": null}
{"timestamp": "2026-11-18T01:16:13+00:00", "question": "Who won the 2018 World Cup?", "status": 200, "outcome": "refused", "best_distance": 0.889, "threshold": 0.6, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 34.4, "error": null}
{"timestamp": "2026-11-18T01:16:13+00:00", "question": "How do I bake sourdough bread?", "status": 200, "outcome": "refused", "best_distance": 0.8295, "threshold": 0.6, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 39.6, "error": null}
{"timestamp": "2026-11-18T01:16:23+00:00", "question": "When is the add/drop deadline?", "status": 200, "outcome": "answered", "best_distance": 0.3737, "threshold": 0.6, "sources": ["admin_add_drop_deadline.txt", "admin_pass_fail_option.txt", "admin_withdrawal_deadline.txt", "advising_registration.txt", "course_cs_340_workload.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 580, "output_tokens": 83, "cost_usd": null, "latency_ms": 2064.5, "error": null}
{"timestamp": "2026-11-18T01:16:37+00:00", "question": "When is the add/drop deadline?", "status": 200, "outcome": "answered", "best_distance": 0.3737, "threshold": 0.6, "sources": ["admin_add_drop_deadline.txt", "admin_pass_fail_option.txt", "admin_withdrawal_deadline.txt", "advising_registration.txt", "course_cs_340_workload.txt"], "model_calls": 0, "cache_hit": true, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 28.1, "error": null}
{"timestamp": "2026-11-18T01:16:38+00:00", "question": "How much does laundry cost in Innisfree Hall?", "status": 200, "outcome": "answered", "best_distance": 0.2052, "threshold": 0.6, "sources": ["housing_aldridge_hall.txt", "housing_aldridge_hall_laundry.txt", "housing_calder_annexe.txt", "housing_innisfree_hall.txt", "housing_innisfree_hall_laundry.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 771, "output_tokens": 77, "cost_usd": null, "latency_ms": 985.6, "error": null}
{"timestamp": "2026-11-18T01:16:50+00:00", "question": "Is Morrow House noisy?", "status": 200, "outcome": "answered", "best_distance": 0.3658, "threshold": 0.6, "sources": ["housing_fenwick_court_noise.txt", "housing_innisfree_hall_noise.txt", "housing_morrow_house.txt", "housing_morrow_house_noise.txt", "housing_old_brewhouse_noise.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 657, "output_tokens": 98, "cost_usd": null, "latency_ms": 921.1, "error": null}
{"timestamp": "2026-11-18T01:17:55+00:00", "question": "Is CS 210 a heavy workload?", "status": 200, "outcome": "answered", "best_distance": 0.3392, "threshold": 0.6, "sources": ["course_cs_210_workload.txt", "course_cs_340_workload.txt", "course_engl_205_workload.txt", "course_hist_118_workload.txt", "course_phys_130_workload.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 611, "output_tokens": 130, "cost_usd": null, "latency_ms": 1122.1, "error": null}
{"timestamp": "2026-11-18T01:17:56+00:00", "question": "How do I get a parking permit?", "status": 200, "outcome": "answered", "best_distance": 0.5339, "threshold": 0.6, "sources": ["admin_graduation_requirements.txt", "admin_parking_permits.txt", "advising_registration.txt", "dining_pellew_dining_hall.txt", "transit_shuttle.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 634, "output_tokens": 101, "cost_usd": null, "latency_ms": 812.2, "error": null}
{"timestamp": "2026-11-18T01:17:57+00:00", "question": "What are the library hours?", "status": 200, "outcome": "answered", "best_distance": 0.3929, "threshold": 0.6, "sources": ["admin_library_holds.txt", "housing_calder_annexe_noise.txt", "housing_morrow_house_noise.txt", "study_group_rooms.txt", "study_library_hours.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 586, "output_tokens": 84, "cost_usd": null, "latency_ms": 854.1, "error": null}
{"timestamp": "2026-11-18T01:17:58+00:00", "question": "Can I take a class pass/fail?", "status": 200, "outcome": "answered", "best_distance": 0.4048, "threshold": 0.6, "sources": ["admin_add_drop_deadline.txt", "admin_declaring_a_major.txt", "admin_graduation_requirements.txt", "admin_pass_fail_option.txt", "course_stat_150.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 593, "output_tokens": 117, "cost_usd": null, "latency_ms": 886.7, "error": null}
{"timestamp": "2026-11-18T01:17:59+00:00", "question": "How often does the campus shuttle run?", "status": 200, "outcome": "answered", "best_distance": 0.4132, "threshold": 0.6, "sources": ["course_stat_150_workload.txt", "dining_the_ridgeway_cafe.txt", "dining_verrill_street_grill.txt", "transit_shuttle.txt", "transit_walking.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 711, "output_tokens": 79, "cost_usd": null, "latency_ms": 691.9, "error": null}
{"timestamp": "2026-11-18T01:18:00+00:00", "question": null, "status": 400, "outcome": "bad_request", "best_distance": null, "threshold": null, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 0.1, "error": null}
```

What the session covers:

| Outcome | Count | What the log shows |
|---|---|---|
| Answered with a model call | 8 | 1 model call each, 580–771 tokens in and 77–130 out, 692–2,065 ms |
| Answered from the cache | 3 | `cache_hit: true`, 0 tokens, 28–143 ms |
| Refused by the relevance gate | 3 | best distance 0.82–0.89, over the 0.6 cutoff, so no model call, 29–40 ms |
| **Rejected input (failed run)** | **2** | `"status": 400`, `"outcome": "bad_request"`: one empty body `{}` and one where `question` was the number `12345` |

**The failure path.** The two rejected inputs are the failed runs: lines 3
and 16, both `400 bad_request`, logged with no question, no model call and 0
tokens. I also tried for an error inside the pipeline, but nothing in this
session raised one. There were no 500s and no timeouts, so no line has a
non-null `error` field. The `error` outcome is wired up (`serve.py::ask` logs
it before returning the 500) but this session never exercised it.

`cost_usd` is `null` on every line because I measure cost in tokens, not
dollars (see below), so no price is set in `.env`.

## What It Costs

**About 739 tokens per question that reaches the model: roughly 643 in and
96 out.** Refused questions, cached answers and rejected input cost 0 tokens.

**Method.** Gemini returns token counts on every response
(`usage_metadata.prompt_token_count` for input and `candidates_token_count`
for output). `generate.py` adds them to session totals, and `serve.py::ask`
takes the before-and-after difference for each request and logs it as
`prompt_tokens` and `output_tokens`. These are measured counts from the
service, not estimates from the prompt length. I also checked for hidden
thinking tokens: a test call reported `thoughts_token_count: None`, and the
total equalled input plus output, so the logged counts are everything the
model used.

**From the session above:**

| | Tokens |
|---|---|
| Requests that called the model | 8 of 16 |
| Input tokens (total) | 5,143, about 643 per call |
| Output tokens (total) | 769, about 96 per call |
| Total for the session | **5,912** |
| Per model call | **739** on average (range 663–848) |
| Per answered question, including 3 cache hits | 537 |
| Per request, all 16 | 370, because half the requests never reached the model |
| 1,000 questions, none cached | about **739,000** |

Two things the numbers show:
- **Most of the tokens are the prompt, not the answer.** Input is 87% of every
  call (643 of 739). That's the five retrieved chunks plus the instructions, so
  `TOP_K` and chunk size drive the token cost far more than answer length.
- **The gate and the cache are the token controls.** A refused question stops
  before the model and uses 0 tokens. So does a cached repeat, which also came
  back in about 30 ms instead of about 900 ms.

Embeddings run locally (`all-MiniLM-L6-v2` through Chroma) and use no API
tokens.

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Every request leaves exactly one log line | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Logged token counts are right, even when requests overlap | 5 of 5 | 3/5 | 3/5 | 3/5 | MISSED |
| 3. Logged latency agrees with what the caller waited | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. One command starts it from a clean checkout | 3 of 3 clones | 1/1 | 1/1 | 1/1 | MET |
| 5. When the model can't be reached, the request fails cleanly and is logged | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |

### Real output from Run 1

Every log line below is copied unedited from `logs/requests.jsonl`. Each one is
written by `serve.py::ask`, which builds the entry, and `serve.py::_log_request`,
which appends it to the file.

**Criterion 1, Run 1:** 5 requests, 5 log lines, every one with all 14 fields
(answered, cached repeat, refused, and two rejected inputs).

```json
{"timestamp": "2026-11-18T01:58:36+00:00", "question": "What is the deadline to withdraw from a class?", "status": 200, "outcome": "answered", "best_distance": 0.3836, "threshold": 0.6, "sources": ["admin_add_drop_deadline.txt", "admin_grade_appeals.txt", "admin_pass_fail_option.txt", "admin_withdrawal_deadline.txt", "course_stat_150.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 603, "output_tokens": 76, "cost_usd": null, "latency_ms": 641.2, "error": null}
{"timestamp": "2026-11-18T01:58:37+00:00", "question": "What is the deadline to withdraw from a class?", "status": 200, "outcome": "answered", "best_distance": 0.3836, "threshold": 0.6, "sources": ["admin_add_drop_deadline.txt", "admin_grade_appeals.txt", "admin_pass_fail_option.txt", "admin_withdrawal_deadline.txt", "course_stat_150.txt"], "model_calls": 0, "cache_hit": true, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 36.7, "error": null}
{"timestamp": "2026-11-18T01:58:38+00:00", "question": "What is the capital of Mongolia?", "status": 200, "outcome": "refused", "best_distance": 0.8246, "threshold": 0.6, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 35.8, "error": null}
{"timestamp": "2026-11-18T01:58:38+00:00", "question": null, "status": 400, "outcome": "bad_request", "best_distance": null, "threshold": null, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 0.1, "error": null}
{"timestamp": "2026-11-18T01:58:39+00:00", "question": null, "status": 400, "outcome": "bad_request", "best_distance": null, "threshold": null, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 0.1, "error": null}
```

**Criterion 2, Run 1:** the first three lines are right. The last two are the
same question sent at the same moment: both log `model_calls: 2`, and the
second has exactly double the tokens (745 → 1490), so 3/5.

```json
{"timestamp": "2026-11-18T02:05:46+00:00", "question": "Is ECON 101 hard?", "status": 200, "outcome": "answered", "best_distance": 0.3741, "threshold": 0.6, "sources": ["course_econ_101.txt", "course_econ_101_exams.txt", "course_econ_101_workload.txt", "course_phys_130.txt", "course_phys_130_exams.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 596, "output_tokens": 172, "cost_usd": null, "latency_ms": 1982.3, "error": null}
{"timestamp": "2026-11-18T02:05:54+00:00", "question": "How does study abroad work?", "status": 200, "outcome": "answered", "best_distance": 0.5185, "threshold": 0.6, "sources": ["admin_campus_jobs_and_financial_aid.txt", "admin_graduation_requirements.txt", "admin_study_abroad.txt", "course_engl_205_exams.txt", "money_jobs.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 535, "output_tokens": 88, "cost_usd": null, "latency_ms": 725.7, "error": null}
{"timestamp": "2026-11-18T02:06:01+00:00", "question": "Is ECON 101 hard?", "status": 200, "outcome": "answered", "best_distance": 0.3741, "threshold": 0.6, "sources": ["course_econ_101.txt", "course_econ_101_exams.txt", "course_econ_101_workload.txt", "course_phys_130.txt", "course_phys_130_exams.txt"], "model_calls": 0, "cache_hit": true, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 36.5, "error": null}
{"timestamp": "2026-11-18T02:06:01+00:00", "question": "What is Kestrel Commons like?", "status": 200, "outcome": "answered", "best_distance": 0.5221, "threshold": 0.6, "sources": ["dining_kestrel_commons.txt", "dining_kestrel_commons_followup.txt", "dining_north_kitchen.txt", "transit_shuttle.txt", "transit_walking.txt"], "model_calls": 2, "cache_hit": false, "prompt_tokens": 745, "output_tokens": 196, "cost_usd": null, "latency_ms": 947.8, "error": null}
{"timestamp": "2026-11-18T02:06:01+00:00", "question": "What is Kestrel Commons like?", "status": 200, "outcome": "answered", "best_distance": 0.5221, "threshold": 0.6, "sources": ["dining_kestrel_commons.txt", "dining_kestrel_commons_followup.txt", "dining_north_kitchen.txt", "transit_shuttle.txt", "transit_walking.txt"], "model_calls": 2, "cache_hit": false, "prompt_tokens": 1490, "output_tokens": 379, "cost_usd": null, "latency_ms": 1186.5, "error": null}
```

**Criterion 3, Run 1:** the five log lines, then what `curl -w "%{time_total}"`
measured for the same five requests, sent one at a time.

```json
{"timestamp": "2026-11-18T02:06:08+00:00", "question": "What is the Atrium dining hall like?", "status": 200, "outcome": "answered", "best_distance": 0.4877, "threshold": 0.6, "sources": ["dining_pellew_dining_hall.txt", "dining_pellew_dining_hall_followup.txt", "dining_the_atrium.txt", "dining_the_atrium_followup.txt", "housing_aldridge_hall.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 778, "output_tokens": 158, "cost_usd": null, "latency_ms": 804.9, "error": null}
{"timestamp": "2026-11-18T02:06:15+00:00", "question": "Is STAT 150 hard?", "status": 200, "outcome": "answered", "best_distance": 0.4416, "threshold": 0.6, "sources": ["course_phys_130.txt", "course_phys_130_exams.txt", "course_stat_150.txt", "course_stat_150_exams.txt", "course_stat_150_workload.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 605, "output_tokens": 175, "cost_usd": null, "latency_ms": 1146.7, "error": null}
{"timestamp": "2026-11-18T02:06:22+00:00", "question": "What is the Atrium dining hall like?", "status": 200, "outcome": "answered", "best_distance": 0.4877, "threshold": 0.6, "sources": ["dining_pellew_dining_hall.txt", "dining_pellew_dining_hall_followup.txt", "dining_the_atrium.txt", "dining_the_atrium_followup.txt", "housing_aldridge_hall.txt"], "model_calls": 0, "cache_hit": true, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 37.9, "error": null}
{"timestamp": "2026-11-18T02:06:22+00:00", "question": "What is the capital of Mongolia?", "status": 200, "outcome": "refused", "best_distance": 0.8246, "threshold": 0.6, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 38.4, "error": null}
{"timestamp": "2026-11-18T02:06:22+00:00", "question": null, "status": 400, "outcome": "bad_request", "best_distance": null, "threshold": null, "sources": [], "model_calls": 0, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 0.1, "error": null}
```

| Request | `latency_ms` (log) | curl `time_total` | Gap |
|---|---|---|---|
| Atrium dining hall (new) | 804.9 | 806.8 | 1.9 |
| STAT 150 (new) | 1146.7 | 1149.3 | 2.6 |
| Atrium dining hall (repeat, cached) | 37.9 | 40.5 | 2.6 |
| Capital of Mongolia (refused) | 38.4 | 41.1 | 2.7 |
| Empty question (rejected) | 0.1 | 2.7 | 2.6 |

**Criterion 4:** a fresh clone started with `python serve.py`, following
RUNNING.md. Each clone writes to its own log and is deleted afterwards (its
`.env` holds the API key), and the three runs recorded only the status codes.
So this output is from one more clone, made the same way, to capture the
actual responses.

Startup, printed by `serve.py::main`, which calls `app.py::cmd_index` because
the clone has no index:

```
No search index yet. Building it before the server starts.

Corpus: campus_life
  loaded   88 documents, 27,908 characters, ~317 characters per document
  chunked  88 chunks, 317 characters on average (shortest 178, longest 549), produced by chunker.py::split_documents
  embedding 88 chunks (first run downloads the model)...
  stored   88 chunks in 2.0s

Ready. Try: python app.py ask "your question here"

Request log: <clone folder>\logsequests.jsonl
Serving The Unofficial Guide on http://localhost:5099
```

`GET /health`, from `serve.py::health`:

```json
{"corpus":"campus_life","detail":"ready","index_ready":true,"status":"ok"}
```

`POST /ask` with "is the housing lottery random?", from `serve.py::ask`:

```json
{"answer":"Temporal breakdown of the provided sources: 2 sources are pre-2022, and 1 source is 2022 or later (based on the provided filenames/content).\n\nThe housing lottery is not entirely random: rising sophomores get a number drawn at random, but juniors and seniors are ordered by accumulated credit hours first, with random tie-breaking used only as a secondary measure (admin_housing_lottery.txt).","best_distance":0.2541,"corpus":"campus_life","question":"is the housing lottery random?","refused":false,"sources":["admin_housing_lottery.txt","admin_parking_permits.txt","advising_registration.txt","housing_morrow_house.txt","housing_tamsin_court.txt"],"threshold":0.6}

HTTP 200
```

The log line it wrote in the clone's `logs/requests.jsonl`:

```json
{"timestamp": "2026-11-18T02:24:36+00:00", "question": "is the housing lottery random?", "status": 200, "outcome": "answered", "best_distance": 0.2541, "threshold": 0.6, "sources": ["admin_housing_lottery.txt", "admin_parking_permits.txt", "advising_registration.txt", "housing_morrow_house.txt", "housing_tamsin_court.txt"], "model_calls": 1, "cache_hit": false, "prompt_tokens": 679, "output_tokens": 91, "cost_usd": null, "latency_ms": 2023.6, "error": null}
```

**Criterion 5, Run 1:** server started as `GEMINI_API_KEY=invalid python serve.py`.
All 5 returned a 500 in 0.08–1.32 s, each logged with `"outcome": "error"`, the
error from Google, and 0 tokens. The error itself is raised in
`generate.py::generate`, and `serve.py::ask` catches it, logs it and returns
the 500.

```json
{"timestamp": "2026-11-18T02:09:35+00:00", "question": "Is Old Brewhouse noisy?", "status": 500, "outcome": "error", "best_distance": null, "threshold": null, "sources": [], "model_calls": 1, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 1314.2, "error": "ClientError: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'API key not valid. Please pass a valid API key.', 'status': 'INVALID_ARGUMENT', 'details': [{'@type': 'type.googleapis.com/google.rpc.ErrorInfo', 'reason': 'API_KEY_INVALID', 'domain': 'googleapis.com', 'metadata': {'service': 'generativelanguage.googleapis.com'}}, {'@type': 'type.googleapis.com/google.rpc.LocalizedMessage', 'locale': 'en-US', 'message': 'API key not valid. Please pass a valid API key.'}]}}"}
{"timestamp": "2026-11-18T02:09:36+00:00", "question": "What is Verrill Street Grill like?", "status": 500, "outcome": "error", "best_distance": null, "threshold": null, "sources": [], "model_calls": 1, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 80.7, "error": "ClientError: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'API key not valid. Please pass a valid API key.', 'status': 'INVALID_ARGUMENT', 'details': [{'@type': 'type.googleapis.com/google.rpc.ErrorInfo', 'reason': 'API_KEY_INVALID', 'domain': 'googleapis.com', 'metadata': {'service': 'generativelanguage.googleapis.com'}}, {'@type': 'type.googleapis.com/google.rpc.LocalizedMessage', 'locale': 'en-US', 'message': 'API key not valid. Please pass a valid API key.'}]}}"}
{"timestamp": "2026-11-18T02:09:36+00:00", "question": "Is Tamsin Court a good place to live?", "status": 500, "outcome": "error", "best_distance": null, "threshold": null, "sources": [], "model_calls": 1, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 86.9, "error": "ClientError: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'API key not valid. Please pass a valid API key.', 'status': 'INVALID_ARGUMENT', 'details': [{'@type': 'type.googleapis.com/google.rpc.ErrorInfo', 'reason': 'API_KEY_INVALID', 'domain': 'googleapis.com', 'metadata': {'service': 'generativelanguage.googleapis.com'}}, {'@type': 'type.googleapis.com/google.rpc.LocalizedMessage', 'locale': 'en-US', 'message': 'API key not valid. Please pass a valid API key.'}]}}"}
{"timestamp": "2026-11-18T02:09:37+00:00", "question": "When is the add/drop deadline?", "status": 500, "outcome": "error", "best_distance": null, "threshold": null, "sources": [], "model_calls": 1, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 83.2, "error": "ClientError: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'API key not valid. Please pass a valid API key.', 'status': 'INVALID_ARGUMENT', 'details': [{'@type': 'type.googleapis.com/google.rpc.ErrorInfo', 'reason': 'API_KEY_INVALID', 'domain': 'googleapis.com', 'metadata': {'service': 'generativelanguage.googleapis.com'}}, {'@type': 'type.googleapis.com/google.rpc.LocalizedMessage', 'locale': 'en-US', 'message': 'API key not valid. Please pass a valid API key.'}]}}"}
{"timestamp": "2026-11-18T02:09:37+00:00", "question": "How much does laundry cost in Innisfree Hall?", "status": 500, "outcome": "error", "best_distance": null, "threshold": null, "sources": [], "model_calls": 1, "cache_hit": false, "prompt_tokens": 0, "output_tokens": 0, "cost_usd": null, "latency_ms": 84.8, "error": "ClientError: 400 INVALID_ARGUMENT. {'error': {'code': 400, 'message': 'API key not valid. Please pass a valid API key.', 'status': 'INVALID_ARGUMENT', 'details': [{'@type': 'type.googleapis.com/google.rpc.ErrorInfo', 'reason': 'API_KEY_INVALID', 'domain': 'googleapis.com', 'metadata': {'service': 'generativelanguage.googleapis.com'}}, {'@type': 'type.googleapis.com/google.rpc.LocalizedMessage', 'locale': 'en-US', 'message': 'API key not valid. Please pass a valid API key.'}]}}"}
```

## Diagnosis

One criterion missed: **criterion 2, logged token counts when requests
overlap**, at 3/5 in all three runs. The three single requests were right
every time. The two requests sent at the same moment were wrong every time,
in exactly the same way:

| Line | `model_calls` | `prompt_tokens` | `output_tokens` | `latency_ms` |
|---|---|---|---|---|
| Kestrel Commons, first to finish | 2 | 745 | 196 | 947.8 |
| Kestrel Commons, second to finish | 2 | 1490 | 379 | 1186.5 |

**Stage: the per-request accounting in `serve.py::ask`.** Retrieval, the gate
and the model call all worked: both requests got a real answer. What's wrong is
how the route works out *its own* share of the usage.

**Mechanism: each request measures itself by subtracting session-wide totals,
and those totals are shared by every request in flight.** `generate.py` keeps
one running count of calls and tokens for the whole process. `serve.py::ask`
reads those totals before the pipeline runs, reads them again after, and logs
the difference. That's only right if nothing else touches the totals in
between. Flask's development server is threaded by default, so two requests
that arrive together run at the same time and both change the same counters.
The exact numbers come from the order in which `generate.py::generate` updates
them: it adds 1 to the call count *before* sending the request (line 235) and
adds the tokens only *after* the response comes back (line 242).

- Both requests take their "before" snapshot at zero, and both calls start, so
  the call count is already up by 2 before either answer arrives.
- The first answer comes back after 948 ms. Its "after" snapshot sees **2
  calls** but only its **own 745 tokens**, because the second response hasn't
  been counted yet.
- The second comes back after 1,187 ms. By then both responses have been
  counted, so it logs **2 calls** and **1,490 tokens**, both answers' prompts.
  Its output of 379 is the first answer's 196 plus its own 183.

So the log claims 4 model calls and 2,235 prompt tokens for two requests that
really made 2 calls and used 1,490, an overcount of 50% on that pair.
Criterion 2 assumed each request's usage was its own. The code only guarantees
that when requests run one at a time.

**Why it didn't show up earlier:** every request in my recorded session (the
Instrumentation section) and in criteria 1 and 3 was sent one at a time, so the
before-and-after difference was always just that request. The cost figure in
What It Costs comes from that one-at-a-time session, so it isn't affected.
Overlapping requests are the only case that breaks it, and criterion 2 is the
only test that sent any.

### The pattern

There's only one miss, so there's no pattern *across* misses to find. But
inside criterion 2 there's no variation at all: 3 runs, 3 overlapping pairs,
and every pair failed the same way, with both lines logging `model_calls: 2`
and the second carrying exactly double the prompt tokens (745 → 1,490 every
time). The nine single requests in those runs were right every time. So it's
one problem, not three bad runs: the failure is caused by the requests
overlapping, not by chance, and it will happen every time two requests are in
flight together. Fixing it means the token counts can't come from shared
session totals at all: `generate.py` would need to hand back each call's
usage with its answer.

### The four I met, and whether the targets were low

Criteria 1, 3, 4 and 5 were met in every run. Two of them were met with so
much room that the targets were set low:

| Criterion | Target | Worst result in 3 runs | Room left |
|---|---|---|---|
| 3. Logged latency agrees with curl | within 50 ms | 3.6 ms off | about 14× |
| 5. Model unreachable fails cleanly | 500 within 10 s | 1.35 s | about 7× |
| 1. Every request leaves one log line | 5/5 lines, 14 fields | 5/5 | none, but only 5 requests a run |
| 4. One command from a clean checkout | 3 of 3 clones | 3 of 3 | none |

Criteria 1 and 4 have no slack to remove: one missing line or one clone that
doesn't start would fail them. Criterion 5's 10 seconds was chosen to catch a
hang or retry loop, and it did its job, but nothing came close.

**The criterion I'd tighten is criterion 3, from "within 50 ms" to "within
10 ms" for 5 of 5.** Every gap I measured was between 1.7 and 3.6 ms, which is
Flask and the local connection and nothing else. A 50 ms window could hide the
log timer missing real work, such as the time spent writing the log line
itself or a slow JSON encode, and still pass. 10 ms is still about three times
the worst gap I saw, so it won't fail on normal noise, but anything the timer
really leaves out would now show.
