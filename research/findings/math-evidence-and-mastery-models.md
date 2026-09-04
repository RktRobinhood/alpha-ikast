# Mathematics evidence and mastery models

**Research question:** How should a self-hosted IB Mathematics AA SL pilot infer what a student knows: mark mathematical process, triangulate across short activities, or use an established statistical model?

**Bottom line:** use a hybrid. Most mastery estimates should come from repeated, skill-tagged, first-attempt observations across varied questions. Add structured step marking selectively where the route matters or where a wrong final answer is not diagnostically useful. Use an interpretable Bayesian Knowledge Tracing (BKT) service as the first longitudinal model, but keep raw observations independent of that model so it can later be recalibrated or replaced. Do not treat an LLM's reading of free-form working as authoritative mastery evidence in the pilot.

## What existing systems actually do

### OATutor: step observations feeding BKT

OATutor is the closest open-source reference for the proposed adaptive loop. Its official site describes a Creative Commons problem library, BKT-based skill mastery, and built-in experimentation; the application repository is MIT-licensed ([OATutor site](https://www.oatutor.io/), [source repository](https://github.com/CAHLR/OATutor)).

The content model decomposes problems into steps and maps each step to one or more knowledge components (KCs). Each KC has the four classic BKT parameters: prior mastery, transition/learning, slip, and guess. The next-problem heuristic is configurable; the documented default prioritizes problems with the lowest average mastery across their KCs ([OATutor repository documentation](https://github.com/CAHLR/OATutor#details-of-kc-model-description-how-it-worksformat)).

The current source is more precise than the high-level description:

- BKT receives a binary correct/incorrect observation and updates the KC probability with the standard equations ([BKT implementation](https://github.com/CAHLR/OATutor/blob/master/src/models/BKT/BKT-brain.js)).
- A KC is updated only on the first graded attempt for a step. Later attempts let the student proceed but do not repeatedly raise mastery ([problem interaction source](https://github.com/CAHLR/OATutor/blob/master/src/components/problem-layout/Problem.js#L646-L698)).
- The current code records attempt history and can treat help use as an incorrect BKT observation on the next graded submission, even if the submitted answer is correct ([problem interaction source](https://github.com/CAHLR/OATutor/blob/master/src/components/problem-layout/Problem.js#L620-L705)).
- OATutor supports textual hints and interactive scaffold steps, but its built-in answer checking is narrower than a full mathematics assessment engine: the repository documents textbox/multiple-choice steps and algebraic, numeric, and exact-string checking ([OATutor architecture](https://github.com/CAHLR/OATutor#details-of-kc-model-description-how-it-worksformat)).

**Supported conclusion:** OATutor does not infer mastery from a holistic reading of handwritten process. It creates multiple explicit, skill-labelled step observations and updates a probabilistic model from their correctness, with first-attempt/help rules to reduce false evidence.

### ASSISTments: distinguish independent success from supported completion

ASSISTments' official reporting distinguishes a correct first attempt from eventual correctness after multiple attempts, hint use, or revealing the answer. It retains attempt, hint, response, and timing information for teachers ([score-symbol definitions](https://www.assistments.org/individual-resource/what-do-the-symbols-within-the-assignment-report-e-g-green-x-red-x-red-x-with-a-yellow-background-mean), [assignment-report documentation](https://www.assistments.org/individual-resource/assignment-reports)). Practice mode permits feedback, supports, and retries with reduced credit; test mode permits one attempt and no hints or immediate feedback ([practice versus test mode](https://www.assistments.org/individual-resource/in-the-eureka-math-engage-ny-folder-there-are-two-different-folders-for-assessments-what-is-the-difference-between-formative-mode-and-test-mode)). Free-form reasoning is supported, but the documented workflow has a teacher score it on a four-point scale rather than automatic process grading ([open-response scoring](https://www.assistments.org/individual-resource/how-to-score-open-response-questions-that-are-not-graded-automatically-in-assistments)).

**Supported conclusion:** established classroom software treats “got there independently” and “completed with support” as different evidence. It also keeps learning-time support separate from cleaner assessment observations.

### STACK: robust mathematical answer properties and limited line-by-line reasoning

STACK is GPL-licensed and uses the Maxima computer algebra system to evaluate mathematical properties rather than relying only on literal answer matching. Its answer tests cover algebraic equivalence, required form, numerical precision, units, calculus, sets, logic, and other properties ([official answer-test reference](https://docs.stack-assessment.org/en/Authoring/Answer_Tests/)). Potential Response Trees combine those tests into a directed decision graph that can assign scores, penalties, targeted feedback, and an answer-note path for reporting ([official PRT documentation](https://docs.stack-assessment.org/en/Authoring/Potential_response_trees/)).

STACK can accept multiple inputs, multipart questions, proofs assembled from steps, and line-by-line algebra. However, its equivalence-reasoning documentation explicitly says that checking a list of equivalent expressions does **not** determine whether step size or working order is sensible ([equivalence-reasoning assessment](https://docs.stack-assessment.org/en/Specialist_tools/Equivalence_reasoning/Equivalence_assessment/)). Its free-text extractor documentation describes extracting named results from written working as a “pragmatic middle ground,” while still using explicit answer fields ([free-text extractors](https://docs.stack-assessment.org/en/Specialist_tools/Free_text_input/Extractors/)).

**Supported conclusion:** deterministic process marking is feasible when “process” is represented as authored steps or testable mathematical properties. General judgement of arbitrary written reasoning remains a different and harder problem.

### CTAT: genuine process tracing, with authoring cost

Carnegie Mellon’s Cognitive Tutor Authoring Tools (CTAT) model explicit solution paths. An author demonstrates correct and alternative routes, common incorrect actions, ordering constraints, hints, feedback, and skill labels. At runtime, the tutor matches each student action against the allowed graph ([official example-tracing tutorial](https://cdn.ctat.cs.cmu.edu/CMUCTAT/CTAT/docs/tutorial-example-tracing.html), [CTAT repository](https://github.com/CMUCTAT/CTAT)).

This is stronger process evidence than final-answer checking, but the source also reveals the cost: alternative correct strategies and common misconceptions must be demonstrated/generalised and annotated for each problem family. An unrecorded alternative correct solution is initially treated as unrecognised until the author adds or generalises that path ([official tutorial, “Test Alternative Solution”](https://cdn.ctat.cs.cmu.edu/CMUCTAT/CTAT/docs/tutorial-example-tracing.html)).

**Supported conclusion:** full model tracing can mark process, but broad AA SL coverage would require substantial knowledge engineering. It is better reserved for a small number of high-value problem types during the pilot.

### WeBWorK: a reusable problem engine, not a mastery model

WeBWorK provides a self-hostable open-source homework system, a large community problem library, randomised variants, answer checking, hints, attempts, and immediate feedback ([project repositories](https://github.com/openwebwork), [Open Problem Library](https://github.com/openwebwork/webwork-open-problem-library)). Its standalone renderer can be run in Docker and returns submitted answer text/LaTeX, incorrect-attempt counts, problem state, and scores through JWT-wrapped APIs ([renderer documentation](https://github.com/openwebwork/renderer)).

**Supported conclusion:** WeBWorK is useful as a content and deterministic grading engine. Its documented renderer does not itself supply a longitudinal KC mastery model, so a pilot would need to map problems to competencies and send interaction events to a separate learner-model service.

## What the statistical models contribute

### Bayesian Knowledge Tracing

Classic BKT is a two-state hidden Markov model: for each skill it maintains a probability of mastery and updates it after sequential correct/incorrect observations using prior-mastery, learning/transition, guess, and slip parameters. The original model is Corbett and Anderson’s *Knowledge Tracing: Modeling the Acquisition of Procedural Knowledge* ([DOI record](https://doi.org/10.1007/BF01099821)). The open-source [pyBKT](https://github.com/CAHLR/pyBKT) library can fit and evaluate standard BKT plus extensions for different guess/slip, learning, forgetting, and student/item classes; it expects ordered student, skill, and correctness observations.

BKT’s value here is not that it “understands” mathematics. It is an interpretable accumulator of uncertain, sequential evidence after content authors have defined the KCs and item-to-KC mappings. OATutor’s own documentation notes that its BKT parameters are normally determined empirically and can be A/B tested ([OATutor BKT parameters](https://github.com/CAHLR/OATutor#bkt-parameters)).

**Implication:** BKT is suitable for an early mastery service, but initial probabilities are provisional until local interaction data can fit and validate them. A displayed “82% mastery” must not be presented as a calibrated fact during that phase.

### Item Response Theory

IRT models the probability of success as a function of a learner’s latent proficiency and item properties such as difficulty and, in richer models, discrimination and guessing. It can put learners and items from different test forms on a common scale when they are linked by common items or learners. It also has assumptions that must be statistically checked and requires specialist calibration work ([UK Standards and Testing Agency handbook](https://www.gov.uk/government/publications/national-curriculum-test-development-handbook/test-development-handbook-2023), [ETS introduction](https://www.ets.org/research/policy_research_reports/publications/report/2020/kbxx.html)).

**Implication:** IRT is a better conceptual fit for broad diagnostic placement and choosing items of appropriate difficulty than for tracking learning step by step. It becomes attractive after the pilot has a stable item bank and enough responses to calibrate item parameters. It should not be the launch dependency.

### The models are complementary, not competing answer graders

BKT and IRT consume scored observations; neither decides whether an algebraic transformation, graph, proof, or explanation is mathematically valid. That scoring must come from deterministic answer tests, authored step models, human review, or a separately validated automated rater. The learner model should therefore be downstream of the mathematics grading engine.

## Recommendation for the IB Mathematics AA SL pilot

The following is a **design recommendation/inference**, not a claim that one cited product already implements the complete design.

### 1. Use three evidence modes

| Mode | Student experience | Mastery treatment |
|---|---|---|
| Independent probe | One attempt before feedback; no hints; short and low stakes | Strongest BKT observation |
| Guided practice | Retries, hints, worked examples, AI coaching, and scaffold steps | Evidence of learning/activity; supported success is not independent mastery evidence |
| Structured reasoning task | Several meaningful intermediate inputs plus final answer; occasionally an uploaded/free response | Each validated step informs its KC; free-form work is retained for teacher review or experimental AI feedback, not authoritative mastery |

This preserves a supportive learning experience without allowing a hint-revealed answer to masquerade as mastery. After guided practice, schedule a new, isomorphic independent probe rather than repeatedly grading the same item.

### 2. Triangulate by design

Do not declare a competency mastered from one correct answer or one long solution. Update continuously, but require evidence diversity before using a high-confidence label:

- more than one independently answered item;
- different surface forms and contexts;
- observations separated in time, including retrieval after a delay;
- at least one item near the expected AA SL demand when claiming AA SL readiness;
- prerequisite KCs tagged separately from the target KC.

The exact counts and thresholds should be treated as pilot policy and tested, not disguised as properties of BKT. The UI should show both estimated mastery and evidence sufficiency (for example, *emerging—2 recent observations*) rather than a naked percentage.

### 3. Thin-slice most content; model process selectively

For broad syllabus and prerequisite coverage, author short items whose response cleanly tests one or a small number of KCs. Use STACK-style CAS/property tests for algebraic equivalence, required form, numerical accuracy, graph features, and units. Use multipart questions when a mistake at one stage would otherwise hide what the student knows.

Invest in CTAT/STACK-style process models only for recurring, high-value AA SL forms—for example solving equations, constructing a calculus argument, interpreting a statistical result, or moving from context to model—where teachers can name the meaningful steps and common misconceptions. This gets most of the diagnostic benefit without having to encode every possible handwritten route through the entire course.

### 4. Start with an interpretable mastery backend

Build the learner model behind a small, versioned interface:

```text
observation event
  = learner pseudonym + item/version + KC(s) + correctness
    + first-attempt flag + help level + attempt count + timestamp
    + response/answer-note + grader/version

mastery service
  observation stream -> BKT state per learner/KC

lesson selector
  unit-plan horizon + assessment scope + prerequisite graph
  + BKT state + evidence sufficiency -> next activity candidates
```

Keep the append-only observation events as the source of truth and treat BKT state as a reproducible projection. This permits parameter refitting, model comparison, audits, and deletion/retention enforcement without losing the provenance of a recommendation. The event vocabulary can later map to the 1EdTech Caliper Assessment profile, which defines structured assessment-item events and responses ([Caliper 1.2 specification](https://www.imsglobal.org/spec/caliper/v1p2/)).

Begin with standard BKT/pyBKT and transparent problem-selection rules. Use conservative seed parameters, label estimates as provisional, and validate predictions against later independent probes and school assessments. Add simple IRT/Rasch calibration later for the diagnostic item bank, once response volume and item stability justify it.

### 5. Keep AI outside the authoritative scoring path at first

AI can choose among already eligible activities, explain feedback, generate hint variants, summarise patterns for teachers, and propose KC tags or new items for review. Deterministic code should enforce the teacher’s unit-plan horizon, upcoming assessment scope, prerequisite rules, item exposure, and evidence requirements.

For photographed or free-form working, an AI model may offer formative feedback and propose a process classification, but the pilot should store that as a separate, lower-trust signal. Promote it into mastery evidence only after a local validation set shows acceptable agreement with teacher judgements across diverse correct methods and common errors. This keeps the system model- and harness-agnostic while the hard educational state remains stable.

## Direct answer to the design question

Yes, process can be marked—but only reliably when the process is made machine-readable through explicit intermediate answers, testable mathematical properties, or authored solution paths. Full free-form process marking across AA SL is not the right first dependency.

The best pilot is therefore **thin-sliced activity triangulation as the default, selective structured process marking for diagnostically important problems, and BKT as the initial longitudinal estimator**. Treat hint use, retries, timing, and AI interaction as context about the observation rather than simplistic positive or negative mastery points. Later, use IRT to improve diagnostic routing and item difficulty calibration, not as a replacement for the competency model.

