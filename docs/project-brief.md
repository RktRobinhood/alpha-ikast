# Project brief

## Working vision

Create an open-source, school-controlled learning orchestration platform that helps each student and their teachers answer:

1. What does the student currently know?
2. What should the student work on next?
3. Which available activity is appropriate for that next step?
4. What evidence would demonstrate progress or mastery?
5. Where is human support needed?

The product may integrate existing learning tools and resources rather than attempting to author or deliver every lesson itself.

## Starting point

Use the complete **IB Mathematics: Analysis and Approaches SL (AA SL)** course as the first proving ground. Mathematics is narrow enough to prototype explicit prerequisites, structured practice, assessment, and mastery estimates. The surrounding model should not assume that every future subject uses math-like questions or mastery evidence.

The published AA SL curriculum and examination destination will define the forward learning target. The model must also extend backward through prerequisite competencies so that a student can be routed to missing foundations below the nominal IB level.

For the pilot, the representation should remain close to the teacher's established teaching practice. Licensed Haese Mathematics teacher materials are the primary reference for the sequence and treatment currently used with students, supplemented by the other current curriculum publications available to the teacher. A later phase may move toward a more textbook-independent experience after the initial model has been tested.

The intended AA SL coverage includes both cohorts:

- **DP2:** course-wide diagnosis and targeted exam preparation;
- **DP1:** prerequisite support for students who need foundations beneath their current topic;
- **later adoption:** a useful pathway and progress layer for every AA SL student.

This is the full product boundary, not a requirement to release every part simultaneously. Delivery can proceed through small vertical slices that produce classroom value while accumulating toward whole-course coverage.

## Long-term scope

The eventual framework may support all IB subjects taught at Ikast-Brande Gymnasium, including subjects with substantial variation in:

- lesson and activity types;
- individual versus collaborative work;
- quantitative, written, oral, practical, and project evidence;
- formative versus summative assessment;
- progression and prerequisite structure;
- teacher judgment and moderation.

## Product hypothesis

The most reusable part of Alpha School's reported model is not a single AI tutor. It is the orchestration layer that joins placement, curriculum structure, activity selection, learning evidence, progress, goals, and adult intervention into one student experience.

The project adopts a **curation-first** posture: combine existing open-source software, interoperable tools, and lawfully reusable learning resources wherever they fit. Build new components only where the pilot exposes a genuine gap.

The implementation principle is **adopt, validate, then adapt**. Begin with established open-source components and statistical approaches, test them against real AA SL needs, and customize or replace them only when evidence exposes a gap.

The project is also an experiment in whether selected parts of the reported Alpha experience can create value inside an established school that is not organized around an “AI-first” model. AI is a replaceable capability within the platform, not a prerequisite for every learning interaction or a substitute for the school's teachers.

The core product must be self-hostable by Ikast-Brande Gymnasium and by other adopting schools. Self-hosting is intended to support local governance and reduce unnecessary disclosure to third parties; it does not remove the school's responsibilities as a controller of student data.

The working AI architecture is **model-agnostic and harness-portable**. Educational capabilities should expose stable, inspectable task contracts so a chosen AI workflow runtime can later be replaced. The project should still choose one runtime for implementation rather than building a universal meta-framework in advance.

Lesson planning should remain an authoritative application capability grounded in curriculum structure, learner evidence, deterministic constraints, and teacher policy. AI may propose, tag, explain, or generate candidates, but should not be the sole source of consequential progression decisions.

Students should receive responsive next steps without waiting for a teacher to approve each lesson or activity. Teachers act as coaches: they see progress and evidence, receive useful intervention signals, and can change direction when professional judgment calls for it.

Teacher authority is primarily expressed through **steering**. A teacher provides ordered unit plans with approximate timing, intended competencies, and assessment scope. This gives the system a view of where the class is going. Within that direction, the platform adapts activities to each student's current learner state and supports meaningful student choice.

Upcoming unit assessments create time-bounded readiness goals. The pathway should distinguish long-term mastery from readiness for a particular assessment, use assessment results as further evidence, and keep recommended work aligned with what the teacher actually intends to test.

The initial deployment is a **bridge phase** inside a conventional school. Existing classroom teaching, unit plans, and assessments continue; the platform supplements them. Its near-term purpose is to raise each student's genuine mathematical level and readiness for those assessments, not to replace the course or optimize superficial test-taking tricks.

The school should provide recurring structured time for students to use the platform independently with a teacher available as coach. The pilot will determine the appropriate duration and frequency. During this time, students should build a clearer evidence-based picture of their learner state and see a comprehensible path toward readiness and mastery.

When prior evidence is absent, the platform should conduct a **baseline exploration**: sample varied competencies at and below the student's expected course level, adapt the next probes to the answers, and progressively narrow uncertainty. It should descend into prerequisite chains where evidence is weak and stop testing once it has enough confidence to recommend a useful path. This is not a one-time label; later learning and assessment evidence continually revises the learner state.

The learner-state model should be derived from **observed learning evidence** generated inside activities the platform presented and understood. It should not be initialized from imported aggregate grades or teacher judgments, whose meaning and consistency may differ. Existing classroom assessments define readiness targets and provide an external measure of impact, but do not directly seed the platform's mastery estimates.

The chosen initial evidence architecture is hybrid:

- repeated, competency-tagged independent probes provide the default evidence;
- evidence is triangulated across varied questions and time;
- structured process marking is reserved initially for high-value AA SL problem forms;
- an interpretable BKT model accumulates longitudinal competency evidence;
- IRT is a later option for diagnostic item calibration when sufficient stable response data exists;
- AI assessment of free-form working remains formative until locally validated;
- raw observation events remain independent of the replaceable mastery model.

A first conceptual loop is:

```text
curriculum model
    -> current learner state
    -> recommended activity
    -> student work
    -> learning evidence
    -> updated learner state
    -> student/teacher action
```

## Candidate capabilities—not commitments

- Curriculum and competency mapping
- Learner profiles and evidence histories
- Recommendations for next learning activities
- Native assessments and external-tool integrations
- Student goals, progress, pacing, and reflection
- Teacher overview, intervention queues, and overrides
- Auditable content-generation and analytics workflows
- Replaceable local or hosted AI models

## Decided implementation constraints

- The student and teacher experience is web-hosted so it can work across common device types and operating systems.
- The product is self-hostable by a school or another operator.
- Student records and the core educational model are not coupled to one AI vendor.

The backend architecture, application framework, AI workflow runtime, deployment topology, and specific open-source base remain undecided. Those choices should follow the product and component investigations.

## Guardrails suggested by the research

- Teachers retain authority over curriculum interpretation, consequential decisions, and interventions.
- Mastery estimates must be explainable through underlying evidence.
- AI output is not, by itself, proof of student mastery.
- The core educational record should not be locked to one model vendor or content provider.
- Subject-specific pedagogy must be able to vary behind a shared platform shell.
- Student data protection, safeguarding, accessibility, and academic integrity are design inputs, not later add-ons.
- Content ingestion must respect copyright, licensing, attribution, and the school's legitimate access rights. Public availability is not treated as permission to copy or redistribute.

## Decisions deliberately left open

- Who the first product is primarily for: student, teacher, or both
- Which of the DP2 exam-preparation and DP1 prerequisite-support workflows should become usable first; this should follow an investigation of reusable tools and content rather than be chosen in isolation
- What “in house” must mean for hosting, data custody, maintenance, and reliance on external services
- How teachers express learning horizons, priorities, exclusions, and urgent overrides
- How much choice students receive among equally suitable next activities
- How the pathway balances missing prerequisites against an approaching unit assessment
- Exact duration and frequency of structured use time
- Which evidence types and stopping rules make baseline exploration reliable without becoming exhausting
- Which existing tools should supply the item engine, deterministic mathematics grading, learner model, and user experience
- Which AI workflow runtime best fits the selected open-source base and lesson-planning tasks
- Whether the first milestone is a decision-ready specification, a classroom prototype, or a deployable pilot
- What “mastery” should mean in an IB context
- Which activities and evidence types the first vertical slice must support
- Where existing tools and resources leave gaps that justify native activities
- Which data may be processed locally or by external services
- What evidence would justify expanding from mathematics to another subject
