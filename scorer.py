def judge(question: str, expects: str, answer: str, results) -> bool:
    
    if not expects:
        return False
    return expects.strip().lower() in (answer or "").lower()


def retrieval_hit(expects: str, results) -> bool:
    
    if not expects:
        return False
    needle = expects.strip().lower()
    return any(needle in (r.text or "").lower() for r in results)
