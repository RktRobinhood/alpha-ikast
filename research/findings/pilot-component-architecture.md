# Component architecture for the AA SL pilot

**Research date:** 2026-09-10  
**Question:** [Choose the component architecture for the pilot](https://github.com/RktRobinhood/alpha-ikast/issues/11)  
**Status:** decision support from pinned upstream source, official documentation, and the repository's completed upstream trials. This selects logical responsibilities and adoption boundaries, not a backend, framework, database, deployment topology, or network protocol.

## Recommendation

Build the pilot as a **school-controlled learning-orchestration core with activity adapters and reproducible learner-state projections**. The boundaries below are semantic contracts: they say who owns each fact and the minimum meaning that must cross a boundary. They do not require microservices, HTTP, events, a particular programming language, or separate deployments. The first implementation may keep the owned capabilities together while preserving these seams in code and tests.

Use **OATutor at pinned revision `6de5ada333f02ac18752aac48e38b9462a7882bd` as the first guided-practice runtime and operational BKT baseline**. Preserve its problem/step/hint/scaffold, first-graded-attempt, help-penalty, KC-mapping, BKT, and problem-selection behaviour for the first mapped AA SL slice. Its documented architecture already separates content sources, course plans, step-to-KC mappings, BKT parameters, and configurable selection; it can build as static assets and makes Firebase logging optional ([OATutor pinned README](https://github.com/CAHLR/OATutor/tree/6de5ada333f02ac18752aac48e38b9462a7882bd#oatutor), [pinned interaction source](https://github.com/CAHLR/OATutor/blob/6de5ada333f02ac18752aac48e38b9462a7882bd/src/components/problem-layout/Problem.js), [MIT licence](https://github.com/CAHLR/OATutor/blob/6de5ada333f02ac18752aac48e38b9462a7882bd/LICENSE)). This is adoption of an established learning workflow, not permission to let OATutor's browser state or optional Firebase become the school record. Add the narrowest possible observation egress beside its existing persistence; do not first extract or redesign its internally coupled BKT and selection loop as a new service.

Integrate **Numbas at pinned revision `0f0ea3337196cb8e98d4edf04f1afaedc8cf8df5` as a deterministic mathematics activity engine**, initially for fresh independent probes and bounded diagnostics. Keep its authored input, marking, feedback, and attempt behaviour inside the engine; map its real attempt data into the common observation meaning outside it. Numbas officially supports embedding an exam with a `<numbas-exam>` element and can use SCORM for stored attempts; its LTI provider exposes question/part scores, completion, variables, and an action timeline ([embedding guide](https://docs.numbas.org.uk/en/latest/embedding.html), [LTI attempt-data documentation](https://docs.numbas.org.uk/lti/en/v3.0/instructor/resources.html#attempts), [Apache-2.0 runtime licence](https://github.com/numbas/Numbas/blob/0f0ea3337196cb8e98d4edf04f1afaedc8cf8df5/LICENSE)). Browser-side marking is intentionally inspectable and therefore unsuitable as secure high-stakes evidence, but it fits the pilot's low-stakes practice/probe role ([security guide](https://docs.numbas.org.uk/en/latest/security.html)). The runtime licence does not establish permission for any particular activity content, which remains item-level provenance.

Treat **Open Alpha at pinned revision `965f8a096cd1f10e15cdefb5ee466b5098ed1332` as the product-shell reference, not the pilot's current reusable code base or educational record**. Its prerequisite graph and learner journey remain the right reference for the mastery-path experience, and the teacher-approved prototype already selected a focused session, optional competency map, and check-in timeline. But the pinned repository contains no licence grant, so its code cannot be copied, modified, or deployed without permission ([pinned repository tree](https://github.com/lamira-the-human/open-alpha/tree/965f8a096cd1f10e15cdefb5ee466b5098ed1332), [repository tree API](https://api.github.com/repos/lamira-the-human/open-alpha/git/trees/965f8a096cd1f10e15cdefb5ee466b5098ed1332?recursive=1)). Even if permission arrives, its client-submitted highest score and fixed 80% completion rule must not become learner state, and its grade-level next-concept rule must not replace curriculum lenses, evidence confidence, or teacher steering ([quiz submission](https://github.com/lamira-the-human/open-alpha/blob/965f8a096cd1f10e15cdefb5ee466b5098ed1332/api/tutor/quiz/submit.ts), [next-concept route](https://github.com/lamira-the-human/open-alpha/blob/965f8a096cd1f10e15cdefb5ee466b5098ed1332/api/tutor/next/%5Bsubject%5D.ts)).

The resulting shape is compositional but deliberately small:

```text
versioned curriculum + teacher steering
                 |
                 v
      school-owned orchestration core
       |          |               |
       v          v               v
 activity catalog/adapter   observation record   learner-state projection
       |
       +-- OATutor guided practice
       +-- Numbas deterministic probes
       +-- optional AI task, never authoritative
```

The arrows show responsibility and information flow, not deployment units.

## Adopt, integrate, adapt, or reject

| Candidate or behaviour | Decision for the pilot | Boundary and reason |
| --- | --- | --- |
| OATutor problem, step, hint, scaffold, retry, first-graded-attempt and KC/BKT loop | **Adopt unchanged for the first mapped slice** | This was the strongest workflow in the completed upstream trial, and the pinned source already implements help-aware, once-per-step BKT updates. Trial it before changing it. |
| OATutor content-source, `coursePlans`, `skillModel`, and versioned BKT-parameter separation | **Adopt as the initial authoring/configuration shape; adapt mappings** | Map upstream KCs and activities to shared subject competencies and the AA SL curriculum lens. Do not copy licensed or unattributed content without item-level provenance. OATutor documents separately versioned content sources and item-level CC BY 4.0 attribution in its content repository ([content structure and licence](https://github.com/CAHLR/OATutor/tree/6de5ada333f02ac18752aac48e38b9462a7882bd#content-sources)). |
| OATutor browser/local state and optional Firebase logging as the authoritative learner record | **Reject** | OATutor documents a static deployment with browser storage and optional Firebase. The school needs a lifecycle-controlled, auditable record independent of the runtime; no storage technology is selected here. |
| Numbas expression entry, deterministic marking, feedback, compiled activity package, and actual attempt data | **Integrate behind the activity/observation boundary** | Preserve the upstream runtime. Translate only the semantic facts needed by the school record; retain source-specific provenance for review and remarking. |
| Numbas DIAGNOSYS or Mastery queue as persistent cross-activity learner state | **Reject for that role; retain as activity-local behaviour** | The completed trial found one-pass prerequisite propagation too coarse for durable mastery. The official diagnostic documentation describes bounded graph algorithms, not a longitudinal evidence model ([diagnostic algorithms](https://docs.numbas.org.uk/en/latest/exam/diagnostic.html)). |
| Open Alpha learner journey, concept-map orientation, and graph validation ideas | **Adapt as a product pattern; code adoption is blocked** | Recreate only from project requirements and teacher-validated prototype evidence unless explicit reuse permission is obtained. If licensed later, reassess a source-level adaptation from the pinned revision. |
| Open Alpha quiz/mastery, grade-level routing, current database/API/AI deployment choices | **Reject** | These couple progression to a client-supplied best score and a grade ladder and carry unvalidated Vercel, Turso, and external-LLM assumptions. They conflict with the decided evidence, curriculum-lens, privacy, and self-hosting boundaries. |
| Standard BKT with OATutor's pinned online update behaviour | **Adopt as the initial learner-state projection** | Keep parameters and model version explicit and estimates provisional. Raw observations remain independent so the projection can be replayed or replaced. pyBKT is a later fitting/validation tool, not a launch dependency ([pyBKT official README](https://github.com/CAHLR/pyBKT/blob/master/README.md)). |
| AI tutoring, hinting, tagging, or generation | **Optional integration after the deterministic loop works** | AI may return bounded formative proposals through a school-controlled task boundary. It may not grade authoritative evidence, define competencies, mutate learner state, or route around teacher policy. |
| The retired synthetic activity/evidence prototype | **Reject as architecture evidence** | Its fixtures and field names were invented and never validated against live adapters or teacher reaction. It remains a discarded semantic sketch, explicitly marked non-authoritative in the [prototype README](../../planning/activity-evidence-prototype/README.md). Real OATutor and Numbas payloads and behaviour must ground implementation. |

## Stable semantic contracts

These contracts specify **minimum responsibilities and data meaning**, not transport schemas. A contract can be an in-process interface, a persisted record, a file/configuration boundary, or a network adapter. Field names, serialization, endpoints, transaction design, and storage layout belong to later implementation tickets.

### 1. Curriculum contract

**Owns:** immutable curriculum-lens releases; shared subject-competency identities and descriptions; strict prerequisite relations; bidirectional mapping between syllabus expectations and competencies; expected forms of performance; review and source provenance.

**Must provide:** a resolved curriculum destination for a learner/cohort; competency and prerequisite references at a named version; evidence that every required syllabus expectation is covered in both mapping directions.

**Must not own:** activities, learner performance, mastery estimates, teacher timing, or generated explanations. Open Alpha's schema establishes that a prerequisite graph is practical, but its grade-like `level`, bundled lesson material, and fixed mastery check must be separated from the curriculum destination ([pinned schema](https://github.com/lamira-the-human/open-alpha/blob/965f8a096cd1f10e15cdefb5ee466b5098ed1332/curriculum/schema.json)).

### 2. Activity contract

**Owns:** versioned activity identity; engine and engine revision; reviewed content/resource provenance and reuse status; mode or intended evidence role; parts/steps and their explicit competency mappings; launch/configuration reference; authored feedback and help policy.

**Must provide:** enough information to present or launch the exact reviewed activity version and to interpret which competencies a captured part actually exercised. Engine-specific configuration remains available for audit rather than being flattened away.

**Must not own:** the learner's durable state, curriculum membership, or a claim that completion equals mastery. OATutor's separate course plans, step mappings, hints, and BKT parameters and Numbas's compiled packages are upstream precedents for retaining activity-local meaning without making an engine the curriculum authority ([OATutor content-source structure](https://github.com/CAHLR/OATutor/tree/6de5ada333f02ac18752aac48e38b9462a7882bd#content-source-directory-structure), [Numbas embedding guide](https://docs.numbas.org.uk/en/latest/embedding.html)).

### 3. Observation contract

**Owns:** the durable account of what the learner did and what the activity/grader returned, including correction or supersession history.

**Must preserve at minimum:** stable event identity for deduplication; local learner reference; occurrence and receipt order/time; exact activity, version, variant/seed, part/step, engine and grader revision; the reviewed competency-mapping version; submitted-response reference or permitted retained representation; validation status; score/outcome and scale; attempt ordinal; whether prior interaction history is known; help, feedback, scaffold, or answer reveal before the response; activity mode; source payload/provenance sufficient for audit and remarking.

**Must not do:** infer a missing prerequisite from one wrong answer, convert every engine score to a Boolean prematurely, overwrite an earlier independent response with eventual correctness, or update learner state itself. Numbas's official storage surface records part answers, question submissions, advice display and answer reveal as distinct operations, which supports preserving interaction context rather than only a final percentage ([SCORM storage API](https://docs.numbas.org.uk/runtime_api/en/latest/Numbas.storage.SCORMStorage.html)). OATutor's pinned source separately tracks first attempts, help pending by step, and attempt history before updating BKT ([interaction source](https://github.com/CAHLR/OATutor/blob/6de5ada333f02ac18752aac48e38b9462a7882bd/src/components/problem-layout/Problem.js)).

### 4. Learner-state contract

**Owns:** a reproducible, versioned projection from eligible ordered observations to the current estimate for each subject competency; evidence confidence; retention/rust status; contested-state signals; model and parameter provenance.

**Must provide:** state at a named projection/model version; the supporting observation references; a reason an observation was included or excluded; enough provenance to replay the result after parameter or policy changes.

**Must not own:** raw observations, curriculum requirements, activity completion, assessment outcomes, or teacher priorities. The initial projector uses standard BKT and OATutor's pinned update eligibility. Assessment readiness is a separate projection over learner state, evidence, assessment scope, date, and expected conditions.

### 5. Teacher-steering contract

**Owns:** attributable, versioned teacher intent: learning horizon, ordered or open unit plan, competency priorities/exclusions, approximate timing, assessment scope/date/conditions, explicit intervention, and the reason and duration of an override.

**Must provide:** the currently applicable steering for a learner/class and a history sufficient to explain why a recommendation changed.

**Must not do:** rewrite observations, directly award mastery, silently alter the curriculum lens, or require approval for each routine activity. The orchestration policy combines steering with learner state, prerequisites, curriculum destination, and available activities to produce eligible next activities and an inspectable rationale.

This capability is project-owned because none of the three inspected upstreams supplies it: OATutor course plans configure tutor lessons, Numbas objectives and topics configure an exam, and Open Alpha's next-concept logic uses completed prerequisites plus grade level. Those are adapter inputs, not a learning horizon or attributable teacher intent.

### 6. Optional-AI contract

**Owns:** one bounded task invocation and its provenance, not educational authority.

**Must preserve at minimum:** task purpose and version; allowed input categories; a pseudonymous/local correlation reference rather than direct learner identity; approved context/resource versions; requested output constraints; provider, model and AI workflow runtime/version; validation outcome; latency/error; retention/secondary-use conditions; reviewer status when content could later reach learners.

**May return:** a formative explanation or hint, a proposed tag, a candidate activity/resource, or a teacher summary.

**Must not do:** define a competency, decide deterministic correctness, mutate observations or learner state, bypass teacher steering, or publish generated content without review. A deterministic fallback or graceful absence is required for every pilot-critical path.

### Cross-cutting school boundary

The local learner identity record, authorization, audit, and learner-record lifecycle apply across all six contracts. External engines and AI receive only the identifiers and data required for their bounded role. This is an invariant of the architecture, not evidence that a particular identity system or database has been selected.

## Ordered tracer-bullet implementation slices

Each slice should exercise a useful end-to-end path through real upstream behaviour. Tickets should pin revisions, use synthetic learners until the school data boundary is approved, and carry content provenance.

1. **OATutor guided-practice tracer.** Map one permission-cleared quadratic OATutor lesson and its actual KCs to the versioned AA SL lens; run the pinned activity unchanged; capture its real first response, help, retry, and step result; reproduce the pinned BKT update; show the learner the next suitable activity and the evidence behind that suggestion. Acceptance requires parity with upstream behaviour and a documented mismatch list, not a redesigned tutor.
2. **Fresh Numbas independent-probe tracer.** Launch one newly authored quadratic probe in the pinned Numbas runtime; retain its real package/seed, part result, attempt context, reveal/advice state, and grader revision; map only the reviewed competencies; project the new observation into the same learner state used by the OATutor tracer. Acceptance requires deduplication/replay, invalid/ungraded handling, and a comparison against the source attempt record.
3. **Teacher-steered route tracer.** Let a teacher narrow an open learning horizon, add one assessment scope/date, and prioritize one competency; route the same synthetic learner again; show the teacher and learner why the recommendation changed without an approval queue. Acceptance requires attributable steering history and proof that no mastery observation was rewritten.
4. **Evidence and intervention tracer.** Show the teacher the real chronological attempts, help context, current projection, confidence/rust, and one actionable check-in signal; record a teacher intervention separately from learner evidence. Acceptance requires a contested or sparse-evidence case and a fresh probe route, not a dense analytics dashboard.
5. **Lifecycle and access tracer.** Exercise local identity linkage, professional access, export/correction, projection replay, and deletion against synthetic records across the earlier slices. Acceptance requires that deleting or correcting eligible observations invalidates and rebuilds the projection without retaining forbidden copies in adapter or AI logs.
6. **Optional AI formative tracer.** Only after the deterministic path works and provider conditions are approved, request one pseudonymized explanation or hint through the optional-AI contract; validate and display it as formative assistance; retain provenance and prove that timeout, rejection, or provider removal leaves activity delivery, grading, state, and routing operational.

These are tracer bullets rather than horizontal subsystem builds: each should produce one observable learner/teacher outcome while hardening only the contracts it crosses.

## Explicit non-decisions and re-evaluation triggers

| Not decided now | Revisit only when | Evidence required |
| --- | --- | --- |
| Backend language/framework, database, modular monolith versus services, queues, and deployment topology | The first two tracers establish real data shape, concurrency, lifecycle, and adapter constraints | Measured school-device/class workload, failure/recovery needs, operational ownership, and a comparison against the smallest self-hostable options |
| A universal transport schema or standards stack | A real second host/engine cannot map cleanly through the semantic contracts | Captured upstream payloads, a concrete interoperability consumer, and proof that LTI, SCORM, Caliper, or another standard covers the needed meaning without loss |
| Open Alpha fork or source reuse | The copyright holder supplies explicit reusable terms | Written licence/permission, pinned permitted revision, dependency and content provenance, and a gap analysis against the project-owned shell |
| Changes to OATutor hint, retry, BKT, or selection behaviour | The unchanged AA SL tracer exposes a reproducible educational or operational gap | Real interaction traces, teacher/student review, later fresh-probe comparison, and a bounded change that can preferably be contributed upstream |
| pyBKT or another separate runtime mastery service | Offline fitting, cross-validation, or scale makes OATutor's small online update insufficient | Stable mappings, sufficient ordered observations, held-out prediction/calibration evidence, and replay parity with the selected model |
| Numbas DIAGNOSYS as persistent learner state | A real AA SL diagnostic agrees with later independent evidence and avoids false prerequisite/downstream inferences | Prospective comparison with the BKT projection and teacher-reviewed error cases |
| STACK, WeBWorK, MathLive, or a new native checker | A permission-cleared AA SL item cannot be expressed accessibly or graded adequately in the adopted OATutor/Numbas path | A concrete failed item/accessibility trial and a same-task comparison of semantics, latency, capacity, licensing, and adapter cost |
| AI provider or AI workflow runtime | A bounded formative use case, privacy conditions, and deterministic fallback are approved | Provider contract/retention review, local evaluation set, failure-mode test, cost/latency measurement, and proof that no authoritative state depends on it |
| AI grading or AI-authored progression | A later local validation demonstrates reliable agreement across diverse correct methods and errors and governance explicitly permits it | Teacher-labelled AA SL validation set, subgroup/error analysis, appeal/audit path, and a new consequential decision record |
| Production use of student data | The school's accountable owner approves the privacy, access, retention, processor, and DPIA boundary | Recorded governance decisions and production readiness evidence; until then all tracers use synthetic learners |

## Why this architecture is the smallest credible choice

No inspected upstream project owns all of the pilot's curriculum, teacher intent, deterministic mathematics interaction, longitudinal evidence, school record, and optional AI boundaries. Selecting one as the whole backend would either inherit an unlicensed and weak mastery path (Open Alpha), force an activity runtime to become the school record (OATutor or Numbas), or replace proven workflows with an invented platform.

The recommended seams preserve what the upstream systems already do well: OATutor teaches and updates KCs; Numbas presents and marks structured mathematical work; Open Alpha informs the surrounding journey if and when reuse is lawful. The school-owned core adds only the responsibilities that no adopted runtime can authoritatively hold: the AA SL curriculum lens, durable observations, replayable learner state, teacher steering, lifecycle control, and inspectable routing. That is enough architecture to write implementation tickets while keeping the backend genuinely undecided.

## Sources and evidence limits

Primary sources inspected on 2026-09-10:

- CAHLR, [OATutor at pinned revision `6de5ada333f02ac18752aac48e38b9462a7882bd`](https://github.com/CAHLR/OATutor/tree/6de5ada333f02ac18752aac48e38b9462a7882bd), especially the project/content structure, interaction source, BKT implementation, and MIT licence.
- Numbas, [runtime at pinned revision `0f0ea3337196cb8e98d4edf04f1afaedc8cf8df5`](https://github.com/numbas/Numbas/tree/0f0ea3337196cb8e98d4edf04f1afaedc8cf8df5), [embedding](https://docs.numbas.org.uk/en/latest/embedding.html), [security](https://docs.numbas.org.uk/en/latest/security.html), [SCORM storage API](https://docs.numbas.org.uk/runtime_api/en/latest/Numbas.storage.SCORMStorage.html), and [LTI attempt data](https://docs.numbas.org.uk/lti/en/v3.0/instructor/resources.html#attempts).
- Lamira the Human, [Open Alpha at pinned revision `965f8a096cd1f10e15cdefb5ee466b5098ed1332`](https://github.com/lamira-the-human/open-alpha/tree/965f8a096cd1f10e15cdefb5ee466b5098ed1332), especially its curriculum schema, quiz submission, next-concept route, and pinned tree's missing licence file.
- CAHLR, [pyBKT official repository](https://github.com/CAHLR/pyBKT), used only to bound a later fitting/validation option.

The live workflow conclusions come from the repository's completed [upstream-first learning-loop trial](upstream-first-learning-loop.md), not a new classroom trial. No student data, licensed IB or textbook content, production deployment, whole-class load test, accessibility trial on school devices, or external AI call was used. Upstream documentation establishes available behaviour and interfaces; it does not establish fitness for Ikast-Brande Gymnasium until the ordered tracers exercise them locally.
