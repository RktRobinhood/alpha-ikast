# Start with existing learning workflows

2026-09-06. Direction corrected by the user: adopt existing systems, anchor them
to IB Mathematics AA SL, and defer behavioural changes until trials expose a need.
The synthetic Python evidence prototype is retired from the investigation.

## Existing starting points

| Project | Existing behaviour to start from | Initial IB mapping work |
| --- | --- | --- |
| OATutor | Step-based problems, hints and scaffolds, knowledge-component mappings, BKT, configurable adaptive problem selection. Its interaction code already gates mastery updates by first-attempt state and tracks pending help treatment. | Map existing step/skill identifiers to AA SL competencies and prerequisite competencies; assemble a bounded lesson using upstream content/configuration structures. Keep upstream help and retry behaviour for the baseline trial. |
| Numbas | Topic/prerequisite graph; built-in DIAGNOSYS and Mastery algorithms. Mastery queues incorrect questions again and removes correct ones. | Map AA SL competencies to topics, group learning objectives, and assign permission-cleared questions. Trial a built-in algorithm before considering custom routing. |
| Open Alpha | Existing concept-path experience and quiz progression. The current quiz endpoint keeps the highest score and uses 80 as its completion threshold. | Inspect how AA SL concepts and prerequisite edges fit the existing curriculum structure. Preserve its role as the intended foundation; record actual integration gaps before designing replacements. |

These are distinct upstream approaches, not a decision to combine all of them or
select a production architecture. Numbas's diagnostic documentation retains a
dated development caveat; it establishes available behaviour, not classroom
validation. Open Alpha's reuse permission remains a separate existing ticket.

## Concrete investigation

Start with an unchanged upstream learning sequence for quadratic equations.
Record the upstream revision/configuration, actual learner interactions, existing
skill/content identifiers, and which AA SL competencies they cover. Identify what
can be accomplished through content mapping and configuration. Any proposed code
change must identify the observed IB requirement the baseline cannot satisfy.

Do not require a new generic observation contract, separate mastery service, or
new retry policy before this trial. Earlier agent recommendations to build these
are hypotheses, not prerequisites. Teacher input should address curriculum fit
and an actual student experience rather than invented technical fixtures.

## Evidence and corrections

- [OATutor README](https://github.com/CAHLR/OATutor): inspected 2026-09-06; documents
  step-to-KC mappings, hint/scaffold structures, configurable problem selection,
  lesson controls and optional Firebase logging. It also explicitly states
  CC BY 4.0 for content with per-asset attribution. Earlier local findings that
  inferred no reuse permission solely from missing repository licence metadata
  are insufficient; consult this statement and the individual assets' provenance.
- [OATutor interaction implementation](https://github.com/CAHLR/OATutor/blob/main/src/components/problem-layout/Problem.js):
  inspected 2026-09-06; includes firstAttempts and helpPenaltyPendingByStep and
  gates the BKT update. These existing mechanisms should be traced and exercised,
  not reimplemented from the standalone BKT equation. A pinned trial remains needed.
- [Numbas diagnostic algorithms](https://docs.numbas.org.uk/en/latest/exam/diagnostic.html):
  inspected 2026-09-06; documents the graph, built-in algorithms and their rules.
- [Open Alpha quiz submission](https://github.com/lamira-the-human/open-alpha/blob/main/api/tutor/quiz/submit.ts):
  inspected 2026-09-06; confirms highest-score retention and threshold behaviour.

## Live upstream trial

Trialled 2026-09-07 against pinned upstream revisions:

| Project | Revision | What was exercised |
| --- | --- | --- |
| OATutor | `6de5ada333f02ac18752aac48e38b9462a7882bd` | Source plus the hosted OpenStax Intermediate Algebra quadratic-formula lesson. |
| OATutor Content | `2f27a597268ae5d1826f69083ad91cf8864a0c05` | Repository metadata and hosted attributed content. A native Windows checkout failed on an upstream filename containing `|`. |
| Numbas | `0f0ea3337196cb8e98d4edf04f1afaedc8cf8df5` | A locally compiled, original five-topic AA SL configuration using the unchanged DIAGNOSYS algorithm. |
| Open Alpha | `965f8a096cd1f10e15cdefb5ee466b5098ed1332` | Source and the public demo path through Grade 9 Algebra 1 to Solving Quadratics by Factoring. |

### OATutor

The hosted lesson supplied a coherent step-based experience without login:
three-part questions, progressively unlocked authored hints, immediate
deterministic feedback, retries, visible lesson mastery, source attribution, and
an optional AI tutor separated from mastery. A correct retry advanced the step
without increasing displayed mastery. The visible content sequence covers
factorisation, completing the square, the quadratic formula, applications,
graphs, transformations, and inequalities, giving the AA SL slice a substantial
existing content and interaction baseline.

One concrete inconsistency needs clarification before classroom use: after two
hints, a correct first submission changed displayed lesson mastery from 12% to
13%, while nearby interface copy said that using hints would not increase
mastery credit. The source contains first-attempt and pending-help controls, so
the first response should be to trace and explain the upstream behaviour rather
than replace it.

The hosted content visibly attributed OpenStax and CC BY 4.0. The content
repository's current tree cannot be checked out natively on Windows because at
least one filename contains a character Windows forbids. That is an authoring
and deployment workflow gap, not an educational-model rejection; WSL/Linux or
an upstream filename correction can preserve the baseline.

### Numbas DIAGNOSYS

The configuration mapped algebraic equivalence, factorising, solving a
factorable quadratic, evaluating a discriminant, and interpreting roots into a
prerequisite graph without custom routing or marking code. DIAGNOSYS began at a
mid-chain target, gave deterministic feedback, offered a same-topic retry, and
on moving on routed backward after inferring a downstream topic failed. Passing
factorisation inferred its expansion prerequisite passed without asking it. The
five-topic diagnostic ended after three presented questions with a 60% total
and a broad recommendation to work more on the AA SL objective.

This proves that existing configuration can express and traverse the slice. It
also exposes why DIAGNOSYS should not define the pilot's learner state by itself:
a single response can infer several competencies, the random entry point does
not reflect a teacher-shaped learning horizon, and the final message is too
coarse to provide a mastery path. Numbas remains a strong candidate for
deterministic probes and a contained baseline-exploration component; its input,
checking, accessibility, and whole-class capacity are evaluated separately.

### Open Alpha

The public demo exposed a plausible surrounding journey: choose a level and
subject, then select from Algebra 1 concepts including factoring trinomials,
quadratic functions, solving by factoring, completing the square, and the
quadratic formula. Selecting a concept led to an AI-tutor conversation rather
than a deterministic activity. No message was sent to the external service.
The public page's GitHub link currently names a repository that does not resolve;
the pinned inspected source remains `lamira-the-human/open-alpha`.

## Decision

Use **OATutor as the first learning-workflow baseline** for the quadratic slice.
Its existing problem, step, hint, scaffold, retry, knowledge-component, BKT, and
adaptive-selection structures are the best fit observed in the live teacher
review. Start by mapping and configuring them, preserving upstream behaviour;
adapt only the hint/mastery inconsistency, Windows content workflow, or another
gap demonstrated by a concrete trial.

Use Open Alpha as the surrounding learner journey and mastery-path foundation,
not as the primary deterministic activity engine. Keep Numbas available as a
focused deterministic assessment and diagnostic component, without forcing it
to replace OATutor's stronger guided-practice experience.

The IB Mathematics AA SL fit belongs in a versioned **curriculum lens** over
shared **subject competencies**. OATutor knowledge components and activities map
to course-independent subject competencies; the AA SL lens selects and frames
the required coverage, depth, terminology, and forms of performance. AA HL and
other curricula can reuse overlapping competencies without copying them, and a
learner may explore beyond the curriculum destination. This preserves the
useful upstream learning mechanics while making syllabus updates and adjacent
courses configuration and mapping work rather than wholesale content forks.

Teacher reaction was positive: the OATutor experience and base structure looked
promising, with the central challenge correctly identified as fitting strong
education-agnostic or non-IB material to the IB course without hard-coding the
subject knowledge to one syllabus.
