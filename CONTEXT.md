# Alpha Ikast Learning Orchestration

Language for describing the educational system and its first classroom pilot. It keeps curriculum, resources, evidence, and learner progression distinct as the project grows.

## Language

**Pilot course**:
The complete IB Mathematics: Analysis and Approaches at Standard Level (AA SL) course, the first bounded subject context used to shape and test the platform across DP1 and DP2.
_Avoid_: Math, IB Math when the exact course matters

**Curriculum destination**:
The knowledge, skills, and forms of performance students must ultimately demonstrate in the pilot course and its examinations.
_Avoid_: Content list, finish line

**Prerequisite competency**:
A specific piece of knowledge or skill a learner needs before a target competency, including foundations from before the IB programme.
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
Material or an activity that a student may use during learning and that the project is permitted to provide or link to.
_Avoid_: Authorized reference material when students cannot lawfully receive it through the platform

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
The ordered units, timing, priorities, and assessment intentions a teacher places on the adaptive pathway, without approving each student activity.
_Avoid_: Lesson approval, manual assignment when the adaptive distinction matters

**Learning horizon**:
The teacher-shaped set of competencies that are current, upcoming, or otherwise appropriate for a student to work toward during a defined period.
_Avoid_: Lesson plan, syllabus

**Unit plan**:
A teacher-owned description of a unit's intended competencies, teaching order, approximate timing, learning activities, and assessments.
_Avoid_: Syllabus, lesson plan

**Assessment scope**:
The competencies and expected forms of performance that an upcoming class assessment will sample.
_Avoid_: Mastery, because one assessment is evidence about mastery rather than its definition

**Assessment readiness**:
The learner's evidence-based preparedness to demonstrate the assessment scope by its scheduled date.
_Avoid_: Mastery, predicted grade

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
The platform's current, evidence-backed representation of what a student appears ready to do, what remains uncertain, and which prerequisites may need support.
_Avoid_: Ability, level when treated as a fixed trait

**Baseline exploration**:
An adaptive, low-stakes sampling of competencies at and below the learner's expected course level, used when prior evidence is absent or insufficient.
_Avoid_: Placement exam, complete pre-test

**Evidence confidence**:
The degree to which the available evidence supports a learner-state estimate, kept distinct from the estimated degree of mastery itself.
_Avoid_: Mastery score when the issue is uncertainty or sparse data

**Observed learning evidence**:
Student performance and interaction data produced through activities the platform presented and can interpret against known competencies.
_Avoid_: Imported grade, teacher impression

**Mastery path**:
A visible, revisable route from the learner state through prerequisites and current course competencies toward the curriculum destination.
_Avoid_: Fixed course sequence, AI lesson plan

**Intervention**:
A deliberate teacher response to evidence that a student needs human attention, motivation, clarification, challenge, or a change in pathway.
_Avoid_: Approval, routine monitoring

**Self-directed learning**:
Learning in which a student can act on responsive next steps, understand their progress, and exercise appropriate choice without waiting for routine teacher permission.
_Avoid_: Unsupervised learning, fully autonomous learning

**AI workflow runtime**:
The replaceable software that coordinates model calls, tools, validation, retries, and human review for bounded AI-assisted tasks.
_Avoid_: Model, mastery engine, lesson planner
