# Activity and evidence contract: throwaway logic prototype

**Retired from the investigation on 2026-09-06.** The user rejected this bespoke
simulation as the wrong starting point. Inspect and trial established upstream
workflows, map them to IB AA SL, and consider changes only after an observed gap.
The classifications below are unadopted proposals, not project requirements.

Question: can a common observation preserve grading, competency mapping, and
the context needed to distinguish independent from supported responses across
candidate mathematics engines? This experiment belongs to
[Test an activity-and-evidence contract across candidate math engines](https://github.com/RktRobinhood/alpha-ikast/issues/7).

Status: runnable semantic sketch; **teacher reaction and live engine validation
are outstanding**. No engine, backend, or mastery policy has been selected.
Python is disposable tooling authorized for this experiment.

From the repository root, run:

```powershell
python planning/activity-evidence-prototype/run.py
```

Uses only Python's standard library. Press one key then Enter. All state stays
in memory. `j` displays every field; `n` starts a fresh synthetic variant and
clears the current history; `e` changes the simulated engine and resets the demo.
Neither reset models production history retention.

## Walkthrough

| Keys | Inspect |
| --- | --- |
| `w`, `f`, `c` | The first wrong response remains independent evidence; a later correct response retains its feedback and retry context. |
| `n`, `h`, `c` | A correct first graded response after a hint is supported. |
| `n`, `u`, `c` | Missing history stays unknown, rather than implying no help. |
| `n`, `i`, `c` | Invalid syntax is retained without scoring it as mathematical failure; the first graded answer can still be an independent candidate. This policy is proposed. |
| `n`, `x`, `c` | A grader error contributes no correctness evidence. |
| `n`, `p` | Partial credit stays partial; there is no automatic conversion to a BKT observation. |
| `r` | A simulated transport replay adds no attempt or observation. This is a no-op demonstration, not a real ingestion/deduplication implementation. |
| `e` | Repeat across native, STACK-style, WeBWorK-style, and OATutor-style semantic fixtures. |

The buttons choose invented grading results; they do not accept or check typed
mathematics. The equation and fixtures were authored for this experiment without
textbook or upstream item reuse. No upstream code or student data is included.

## Proposed boundary

Keep the activity identity/version/variant and part-to-competency mapping alongside
each observation. Record event identity/time, graded-attempt ordinal, known or
unknown interaction history, help before the response, grade status/raw score,
and grader provenance. Retain the source-specific details rather than reducing
everything to a single correctness flag. The local competency identifier is an
illustration, not an adopted AA SL taxonomy.

The activity host supplies delivery history; a grade adapter supplies the grading
result; the mastery service decides how to use the observation. An activity's
independent-probe intent does not override observed help or missing history.
The provisional classifications are explanatory filters, not updates to learner
state. A wrong final answer alone cannot diagnose a particular prerequisite.

These fixtures all use our invented field names. They are not captured API
responses and do not establish interoperability. Grader revision strings are
explicitly fixture versions, not claims about deployed upstream versions.

## Source-grounded constraints

Primary sources inspected 2026-09-06:

- [STACK potential response trees](https://docs.stack-assessment.org/en/Authoring/Potential_response_trees/):
  PRT outcomes include raw score, penalty, feedback and answer note. Validation
  precedes grading, and the current input score is distinct from attempt history.
  Preserve PRT identity and author-reviewed competency mappings in a real adapter;
  do not confuse an overall penalty-adjusted mark with a fresh correctness result.
- [WeBWorK renderer README](https://github.com/openwebwork/renderer/blob/main/README.md):
  the renderer supports seeded problems and controls for displaying hints and
  solutions. Session JWTs include answer entries and an incorrect-attempt count
  that stops after success or revealing answers; answer JWTs include score and
  session state. This count cannot substitute for a complete chronological
  observation history. Display configuration alone does not establish which help
  was actually shown before an answer.
- [OATutor BKT update](https://github.com/CAHLR/OATutor/blob/main/src/models/BKT/BKT-brain.js):
  the update consumes a Boolean correctness value and model parameters.
  That function alone does not specify how hints, retries, partial credit, or
  missing context should be filtered. Its Boolean input motivates keeping a
  separate evidence-to-model policy; no code was copied.

## What remains to establish

1. Teacher reaction to the independence/retry distinction, starting with the
   first walkthrough scenario. The ticket stays open until the live exchange.
2. Actual payload extraction and field coverage against pinned engine versions,
   using newly authored items. We have not run STACK, WeBWorK, or OATutor here.
3. Part-level responses and shared hints for structured reasoning tasks; the
   current executable has one roots part only. Multiple PRTs must not create
   multiple independent mastery updates for the same response automatically.
4. Reopening the same item, cross-device continuity, out-of-order deliveries,
   grade corrections, and verified provenance. Fresh-variant reset deliberately
   does not answer these questions.
5. School-device/browser behaviour and accessibility remain untested.

After the teacher reaction and adapter investigation, capture the decision in
the ticket and remove or replace this throwaway prototype. Do not promote its
classification rules into production by accident.
