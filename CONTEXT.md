# Alpha Ikast Learning Orchestration

Language for describing the educational system and its first classroom pilot. It keeps curriculum, resources, evidence, and learner progression distinct as the project grows.

## Language

**Pilot course**:
The complete IB Mathematics: Analysis and Approaches at Standard Level (AA SL) course, the first bounded subject context used to shape and test the platform across DP1 and DP2.
_Avoid_: Math, IB Math when the exact course matters

**Curriculum destination**:
The knowledge, skills, and forms of performance students must ultimately demonstrate in the pilot course and its examinations.
_Avoid_: Content list, finish line

**Subject competency**:
A course-independent piece of subject knowledge or skill that may be shared across multiple curricula, subjects, course levels, and syllabus versions. Identical performance supplies evidence about the same competency, with the same mastery standard, regardless of the learner's current curriculum lens or the subject context in which the evidence was produced; a course does not rescale that evidence or impose a lower mastery ceiling.
_Avoid_: Course objective when the knowledge itself is not course-specific

**Curriculum lens**:
A versioned interpretation of a curriculum or syllabus that preserves its native structure, terminology, and forms of performance while selecting a traceable subset of the shared subject-competency graph. Every required syllabus expectation maps to its supporting competencies, and every competency claimed as required maps back to a syllabus expectation, preventing the lens and graph from drifting apart. A published lens version is an immutable curriculum destination for the cohorts and examination sessions to which it applies; corrections and syllabus revisions create new releases that may coexist with it. It defines that destination without duplicating subject knowledge, rescaling shared mastery, or preventing learning through connected prerequisites or beyond the course. Differences between course levels are expressed through the competencies each lens requires and how it frames them, not through different mastery standards for a shared competency.
_Avoid_: Curriculum copy, hard content boundary, course-specific knowledge graph

**Beyond-destination learning**:
Learner-chosen work on subject competencies outside the learner's current curriculum destination, available when the platform has suitable activities and the learner's enrolled-course priorities permit it. Required learning, due retrieval, and imminent assessment-readiness work take priority and must be addressed before beyond-destination learning becomes available.
_Avoid_: Extension track, off-syllabus mastery credit

**Prerequisite competency**:
A subject competency whose absence materially obstructs demonstrating a target competency, including foundations from before the IB programme. The relationship expresses a strict mathematical dependency rather than a customary teaching order. It informs diagnosis and routing but does not itself make the target competency inaccessible to a learner who is ready to attempt it.
_Avoid_: Weakness, gap when the missing capability can be named

**Prerequisite support**:
Targeted learning offered when evidence indicates that a student needs one or more prerequisite competencies for current AA SL work.
_Avoid_: Weak-student track, remedial student

**Exam preparation**:
DP2 learning activity that uses evidence about course-wide knowledge and exam performance to direct revision and practice before the final examinations.
_Avoid_: Revision when the adaptive evidence-and-routing use case is intended

**Authorized reference material**:
A source the school or teacher is entitled to access and analyze for curriculum design, such as a licensed teacher copy. Authorization to consult it does not imply permission to redistribute its contents.
_Avoid_: Free content, open content unless the license actually grants those rights

**Learning resource**:
Material that a student may use during learning and that the project is permitted to provide or link to. A learning resource exists independently of any one curriculum lens and may be reused wherever its review status, competency coverage, and observed usefulness make it suitable.
_Avoid_: Authorized reference material when students cannot lawfully receive it through the platform

**Learning activity**:
A versioned opportunity for a learner to act, practise, or demonstrate performance using one or more tools or learning resources. It maps explicitly to the subject competencies it teaches or observes and may serve multiple curriculum lenses without being copied into each one. Activity completion is not itself mastery.
_Avoid_: Curriculum competency, resource file, completion-as-mastery

**Curation-first**:
The product posture of selecting and combining suitable existing tools and learning resources before creating a new replacement.
_Avoid_: Build everything, textbook-free as an immediate pilot requirement

**Adopt, validate, then adapt**:
The delivery principle of starting from established open-source components or methods, testing them in the AA SL context, and customizing only where observed needs justify divergence.
_Avoid_: Reinvent, fork immediately

**Independent probe**:
A short competency-tagged activity attempted before feedback or hints, providing the cleanest routine observation for the mastery model.
_Avoid_: Test, because it remains low stakes and diagnostic

**Guided practice**:
A learning activity in which hints, retries, examples, or tutoring are available; completion shows supported learning but is not equivalent to independent mastery evidence.
_Avoid_: Independent probe

**Durable mastery**:
An evidence-backed judgement that a learner can demonstrate a subject competency independently across fresh and meaningfully varied work, including retrieval after a delay. It remains revisable when later evidence conflicts and is distinct from activity completion and readiness for a particular assessment.
_Avoid_: Highest score, eventual correctness, permanent mastery

**Rust**:
A visible indication that the evidence supporting a previously demonstrated competency is due for retrieval. Rust may grow with time and shrink through direct or genuinely embedded retrieval, but it does not itself assert that mastery has been lost.
_Avoid_: Skill decay, automatic mastery loss, forgetting score

**Structured reasoning task**:
A problem that captures selected meaningful intermediate mathematical steps as well as the final answer so those steps can be checked against specific competencies.
_Avoid_: Free-form AI grading

**Alpha-style experience**:
A coherent learner journey connecting goals, recommended work, evidence, visible progress, and timely teacher intervention. It does not mean copying Alpha School's schedule, branding, or institutional model.
_Avoid_: AI school, Alpha clone

**Self-hostable**:
Deployable under a school or operator's control so that it can choose the infrastructure, identity system, data location, connected services, and operating policies appropriate to its context.
_Avoid_: GDPR-free, offline-only

**Lesson plan**:
The ordered set of learning activities recommended or assigned to a student for a defined period, together with the evidence and policy that justify the selection.
_Avoid_: AI output, prompt result

**Teacher steering**:
Optional teacher input that influences the adaptive pathway, including a scheduled unit plan, an open learning horizon, priorities, timing, and assessment intentions. The learner state, prerequisite competencies, and curriculum destination drive routine next steps; teacher steering changes direction or applies professional judgement without requiring approval of each student activity.
_Avoid_: Lesson approval, manual assignment when the adaptive distinction matters

**Learning horizon**:
The teacher-shaped set of competencies that are current, upcoming, or otherwise appropriate for a student to work toward during a defined period. It may be sequenced by a unit plan or open across a broader part of the pilot course.
_Avoid_: Lesson plan, syllabus

**Open learning horizon**:
A teacher-owned learning horizon that intentionally leaves unit order and timing open, allowing the adaptive pathway to pursue mastery across its included competencies. The default open learning horizon is the full pilot-course curriculum destination; a teacher may narrow or prioritize it.
_Avoid_: No teacher control, no curriculum

**Unit plan**:
A teacher-owned description of a unit's intended competencies, teaching order, approximate timing, learning activities, and assessments.
_Avoid_: Syllabus, lesson plan

**Assessment scope**:
The competencies and expected forms of performance that an upcoming class assessment will sample.
_Avoid_: Mastery, because one assessment is evidence about mastery rather than its definition

**Assessment readiness**:
The learner's evidence-based preparedness to demonstrate the assessment scope by its scheduled date.
_Avoid_: Mastery, predicted grade

**Assessment outcome**:
A teacher-provided result from an existing class assessment, recorded against its assessment scope for teacher insight and calibration of assessment readiness. In the pilot it does not directly update the learner state.
_Avoid_: Observed learning evidence, mastery score

**Bridge phase**:
The initial operating period in which the platform supplements the school's existing AA SL teaching, unit plans, and assessments rather than replacing them.
_Avoid_: AI-first school, curriculum replacement

**Readiness uplift**:
Improvement in a learner's ability to demonstrate genuine mathematical understanding and performance on an upcoming assessment, relative to their earlier evidence.
_Avoid_: Teaching to the test when it implies memorizing answers or gaming scores

**Structured use time**:
Recurring school-supported time in which students work independently with the platform while a teacher can observe and coach. Its duration and frequency are pilot variables.
_Avoid_: Homework-only use, fixed timetable commitment

**Learner state**:
The platform's current, evidence-backed representation of what a student appears ready to do, what remains uncertain, and which prerequisites may need support. It is based on the learner's own evidence rather than assumptions about the average motivation, attainment, or ambitions of a course cohort.
_Avoid_: Ability, level when treated as a fixed trait

**Baseline exploration**:
An adaptive, low-stakes sampling of developed or adopted competencies at and below the learner's expected course level, started when a learner first signs in and repeated only when platform evidence is absent or insufficient. It samples a broad collection of available topics, then directs prerequisite support, current work, and challenge so the learner can join the teacher's current learning horizon as soon as the evidence supports it.
_Avoid_: Placement exam, complete pre-test

**Evidence confidence**:
The degree to which the available evidence supports a learner-state estimate, kept distinct from the estimated degree of mastery itself.
_Avoid_: Mastery score when the issue is uncertainty or sparse data

**Observed learning evidence**:
Student performance and interaction data produced through activities the platform presented and can interpret against known competencies. An activity may update only competencies it explicitly maps and that the learner's captured work actually exercised; success on a later competency does not automatically grant mastery of its prerequisite competencies. Evidence for a genuinely shared competency advances every curriculum lens that requires it, while retaining the activity and subject context that produced the evidence.
_Avoid_: Imported grade, teacher impression

**Solution strategy observation**:
An evidence-backed record of the mathematical method a learner used when an activity captures enough of the work to support that interpretation. It may inform feedback and future activity selection, but it is neither a fixed learner trait nor a substitute for demonstrating a required competency. A method becomes a subject competency only when the curriculum requires that method or another competency materially depends on it; otherwise it remains an observation.
_Avoid_: Learning style, preferred method inferred from a final answer alone

**Learner identity record**:
The school-facing link between a student's recognizable identity, including their name and IB candidate number, and their persistent learning history. It supports a personal application experience without requiring outside services to receive that identity.
_Avoid_: Anonymous learner, AI feedback payload

**Learner-record lifecycle**:
The period in which identifiable work, feedback, and learner state are retained to support a student through the AA SL course, examinations, results, and applicable enquiry or review period. Identifiable records are deleted when that process closes, with three years as an absolute backstop rather than a default retention period.
_Avoid_: Indefinite history, three-year default

**School professional access**:
Authenticated, attributable access through which the school's teachers and managers may view learner records when supporting students, including across ordinary class boundaries. It expresses shared professional responsibility without making records available for casual or external browsing.
_Avoid_: Assigned-teacher-only access, unrestricted employee access

**Pseudonymized AI feedback payload**:
Student learning work provided for formative AI feedback without direct learner identifiers, while the platform retains the ability to attach returned feedback to the learner identity record. Because that link remains possible, the payload is not treated as anonymous; provider training and secondary use are prohibited, zero retention is preferred, and any operational retention must be short and documented.
_Avoid_: Anonymous submission, identified AI payload, summative assessment submission

**School-controlled competency calibration**:
The school-owned interpretation of competencies, task mappings, feedback policy, and learner-state updates. External AI may return bounded formative feedback, but it does not define competencies, calibrate progression, or train on live student work.
_Avoid_: AI-owned mastery, provider-controlled calibration, skills calibration

**Mastery path**:
A visible, revisable route from the learner state through prerequisites and current course competencies toward the curriculum destination.
_Avoid_: Fixed course sequence, AI lesson plan

**Evidence-led routing**:
The default selection of a learner's next work from their learner state, prerequisite competencies, available activities, and curriculum destination. Teachers coach, steer, and intervene when their professional judgement should influence that route.
_Avoid_: Fixed class sequence, teacher approval of every activity

**Intervention**:
A deliberate teacher response to evidence that a student needs human attention, motivation, clarification, challenge, or a change in pathway.
_Avoid_: Approval, routine monitoring

**Check-in triage**:
An evidence-generated, prioritised queue of learners needing a teacher's attention or recognition. It supports coaching by surfacing actionable interventions while routine adaptive work continues without approval.
_Avoid_: Approval queue, passive analytics dashboard

**Self-directed learning**:
Learning in which a student can act on responsive next steps, understand their progress, and exercise appropriate choice without waiting for routine teacher permission.
_Avoid_: Unsupervised learning, fully autonomous learning

**Learner agency**:
The learner's ability to choose among suitable activities and make informed progress decisions within their learning horizon. It does not mean bypassing evidence-supported prerequisite support or curriculum constraints.
_Avoid_: Unbounded choice, fixed assignment

**AI workflow runtime**:
The replaceable software that coordinates model calls, tools, validation, retries, and human review for bounded AI-assisted tasks.
_Avoid_: Model, mastery engine, lesson planner
