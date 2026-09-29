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
