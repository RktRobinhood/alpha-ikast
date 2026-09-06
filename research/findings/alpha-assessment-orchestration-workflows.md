# Alpha School assessment and orchestration workflows

Research date: 2026-09-06. Question: GitHub issue #5. Status: bounded primary-source investigation; product and policy decisions remain open.

## Result and evidence boundary

Public operational documentation supports a multi-stage orchestration model: subject-specific placement, assigned learning, separate progression assessments, visible workload and progress, and human support. The transferable idea is a coherent learning loop, not a requirement to reproduce Alpha's school timetable, incentives, thresholds, or product stack.

This report distinguishes **documented mechanics** (support instructions and API contracts), **vendor descriptions** (Alpha's own promotional explanations), **unknowns** (not established by the reviewed evidence), and **recommendations** (our interpretation for the bridge phase). Documentation establishes what the vendor describes, not independent classroom effectiveness or deployment at every campus. No private dashboard or student record was accessed. Existing [claim inventory](../synthesis/alpha-school-model.md) and [supplied notes](../raw/2026-09-04-alpha-school-notes.md) were reviewed; this report supersedes their unverified claims only where explicitly addressed below.

## 1. Placement is a workflow with subject-specific exceptions

**Documented mechanics.** Home-page placement assignments normally use MAP RIT information to select a starting test independently for each subject. Without MAP, configured starts are kindergarten for students in Grade 5 or below and Grade 3 for older students. Vocabulary/writing start at Grade 3; science has separate eligibility conditions. A first-attempt score of at least 90% advances testing; a failure moves testing down until a pass establishes a foundation. Saved failures then determine subsequent coursework. For most subjects, 60–89% leads to targeted courses and below 60% to a full course. Mathematics explicitly differs: any failed placement test leads to the full base course for that grade after passing the preceding grade. The left-panel placement entry follows a different fixed-start, upward-testing flow and stops at the first failure. [Placement support guide](https://support.alpha.school/article/133839-quick-start-guide-placement-tests-in-timeback)

**Unknowns.** Public instructions do not expose the MAP-to-starting-test conversion table, its calibration, accommodation rules, or the exact stopping logic in every edge case.

**Bridge-phase recommendation.** Preserve the already-decided baseline exploration: broad, low-stakes competency sampling that lets the student join the teacher's learning horizon promptly. Do not adopt a grade-ladder placement exam or the mathematics full-course rule without local evidence. Those are materially different from the prerequisite support defined in [CONTEXT.md](../../CONTEXT.md).

## 2. Four assessment functions must remain distinct

| Function | What public primary sources establish | Limit |
|---|---|---|
| Initial placement | The branching subject workflow above establishes a starting course. | A starting level is not a complete competency model. |
| Routine application learning | Alpha's FAQ describes 90% concept mastery before advancement. | This broad vendor statement does not identify one common evidence algorithm across every app. |
| Course/grade progression | Support tells learners to complete ordered lessons, take an assigned standardized test, and repeat learning and testing after failure. Some tests may be taken early; failed results can produce targeted lessons or next-grade lessons while learning continues. | Progression policy cannot be reconstructed as one universal hard lock from this page. |
| External benchmarking | Alpha describes MAP as its K–8 accountability measure, with three administrations annually in its presentation; SAT/AP serve high-school accountability. The presentation separately describes grade-mastery tests varying by location, naming Texas and Florida examples. | The presentation is a historical vendor account, not proof of current test administration, licensed forms, or comparable validity across campuses. |

Sources: [FAQ](https://alpha.school/faq/), [grade progression instructions](https://support.alpha.school/article/31841-advancing-to-the-next-grade-level-aiming-for-mastery), [Alpha presentation transcript](https://alpha.school/resources/how-do-alpha-school-workshops-develop-personalized-learning-and-ai-tutoring/).

**Documented test experience.** AlphaTest assignments show test identity, subject, grade and base XP. Learners launch from TimeBack, authenticate, review instructions, attempt and submit; interrupted tests can resume. An overdue assessment can block a course. Scores usually arrive promptly, but writing is manually graded and may take 24 hours. Students can inspect previous scores, but wrong-answer solutions are withheld. Sub-90% results lead to further coursework or a lower placement test. [AlphaTest instructions](https://support.alpha.school/article/128994-how-to-take-tests-in-alphatest)

**Interpretation.** Claims that this model eliminates tests or all human grading are unsupported. Equally, neither a percentage threshold nor a course completion count is equivalent to our evidence-backed learner state. Traditional teacher-set AA SL class assessments are a different category: the repository has already decided their outcomes inform teacher insight and readiness calibration without directly updating learner state. This research provides no reason to reverse that boundary.

## 3. Student choice, daily work and motivation

**Vendor description.** A current Alpha video transcript describes a guide-led launch, choosing the first subject from TimeBack, short focus cycles with breaks, guide coaching, and a dashboard showing completed work and next steps to students, guides and parents. It supports choice of subject order; it does not establish unrestricted choice of activities or permission to skip required learning. [Two-hour day transcript](https://alpha.school/resources/how-alpha-two-hour-school-day-works/)

**Vendor description.** An October 2025 article describes 25-minute sessions, progress rings, personal targets, privileges, internal currency and collective rewards. It also promotes computer-vision-based engagement feedback. These are descriptions of incentive and monitoring practices, not evidence that the incentives cause better understanding or suit AA SL students. References to 90% assessment mastery and 80–85% practice accuracy concern different activities; neither establishes a single probabilistic mastery rule. [Gamification article](https://alpha.school/blog/how-ai-and-gamification-transform-learning-at-alpha-school/)

**Documented mechanics.** The published XP guide lists many subject apps and a separate standardized-test XP scheme. Test XP depends on a base value and performance tiers. A reading scheme restricts credit to attempts above the highest mastered grade. Thus XP is a configured cross-app reward measure, not automatically a count of independently demonstrated competencies. [Academics XP guide](https://cms.academics.alpha.school/2hrlearning-xp-guide)

**Unknowns.** The exact authority for changing a student's daily goal, recalculation schedule, student choice within a subject, guide override permissions, and campus-specific rewards are not established here. An advertised personal target and a report's built-in pacing target should not silently be treated as the same field.

**Bridge-phase recommendation.** Prototype suitable activity choice within the learning horizon and a clear recommended next action. Make daily success about a feasible learning intention and evidence of progress. XP, public competition, cash-like incentives and restricted access to other school activities require separate justification; they are not prerequisites for an Alpha-style experience.

## 4. Progress and pacing have different meanings

**Documented mechanics.** `Reports > My Learning Report` exposes earned XP, remaining XP, completion percentage and weeks at the daily goal. Completion percentage can come directly from an app or be estimated from XP. The support page explicitly distinguishes completing content from demonstrating mastery on the subsequent assessment. Failure can lead to further targeted learning and reassessment. Its deadline calculation divides remaining XP by remaining school days; this estimates workload, not the probability of being ready for a particular assessment. [Course completion and pacing guide](https://support.alpha.school/article/133259-understanding-course-completion-in-timeback-to-plan-student-pacing)

Older support documentation also directs learners to Daily Activity, subject-filtered leaderboards and a My MAP Report analysis tab. This establishes that several views have existed, not that all are the current navigation. [Progress evaluation guide](https://support.alpha.school/article/31716-how-to-evaluate-your-learning-progress)

**Bridge-phase recommendation.** Keep completion, learner state, evidence confidence and assessment readiness legible as different concepts. A route toward the curriculum destination can coexist with a time-bounded goal. Avoid presenting an activity-count forecast as a mastery or exam-readiness promise.

## 5. Guide visibility and intervention

**Documented mechanics.** Guides join or create classes to populate Home summaries and Learning Metrics with a roster. The support screenshots are described as containing a Student XP Summary and class actions. Visibility is campus-scoped; missing learners or classes can be an access/setup issue rather than absent learning. [Guide onboarding instructions](https://support.alpha.school/article/130167-how-can-guides-join-a-class-and-start-monitoring-student-metrics-in-timeback-dash)

**Unknowns.** This establishes a metrics dashboard, not a complete verified check-in triage queue. Public instructions reviewed here do not establish an intervention priority algorithm, workload capacity, resolution states, false-alert rates, or a complete teacher override audit trail. Vendor descriptions of coaching establish intent, not reliable intervention effectiveness.

**Bridge-phase recommendation.** Use the existing check-in triage concept: present a reason, supporting evidence, its recency and uncertainty, and a useful teacher action. Distinguish a learning need from a technical synchronization problem. Preserve teacher steering without requiring approval for routine adaptive work.

## 6. Data flow is heterogeneous and can be delayed

**Documented mechanics.** Alpha support says TimeBack obtains learning data through app-specific integrations and that many are not real time. AlphaNumbers can show more XP than TimeBack while an update is pending; guides/support should investigate if the mismatch persists after a full day. This directly limits broad marketing language about live progress. [XP synchronization support](https://support.alpha.school/article/129734-why-is-the-xp-in-alphanumbers-different-from-the-xp-in-timeback)

**Documented platform capability.** TimeBack's current integration documentation describes progressively richer integrations, including structured Caliper learning events for question responses and mastery-related reporting. This supports a standards-oriented integration surface; it does not establish that each app in Alpha's catalog implements every level. [Platform introduction](https://docs.platform.timeback.com/), [Caliper integration](https://docs.platform.timeback.com/integration/level-3-caliper-events)

TimeBack's Insights API also documents coaching views derived from those events, including session and trend data. Some documented insight types use webcam, screen, client, DOM, network, app-event, or related detection sources. This is evidence of a possible vendor capability, not a reason to collect that data in the pilot; the data-necessity, safeguarding, and governance decision belongs in the privacy investigation. The API also says that an empty result immediately after a session begins can mean that asynchronous ingestion has not materialized the session yet. [Insights API](https://docs.platform.timeback.com/integration/level-4-insights-api)

**Reconstructed conceptual loop (inference, not a verified implementation diagram):**

```text
initial assessment -> subject placement / assigned learning
                  -> activity in a connected application
                  -> app-specific evidence and progress updates
                  -> reporting, pacing and subsequent assignments
                  -> separate progression assessment when required
                  -> additional learning / advancement + human intervention
```

**Bridge-phase recommendation.** Retain provenance and freshness for evidence. Missing, delayed or contradictory data should remain uncertainty, not become an inferred failure or mastered competency. An activity/evidence contract should describe meaning as well as transport: independent response versus guided practice, mapping to competencies, timestamps, attempts and correction handling. No protocol or implementation technology is selected here.

## 7. Adjacent design reference: Open Alpha

The public [Open Alpha repository](https://github.com/lamira-the-human/open-alpha) is a small, currently active, community-oriented project inspired by Alpha School. It is **not** Alpha School or TimeBack, and its source code is not a pilot component candidate: the repository has no declared licence, its stated Vercel/Turso/ATXP deployment is outside the project's self-hosting constraint, and its K–12, parent-facing scope does not fit the AA SL bridge phase.

**Ideas worth carrying forward.** Its curriculum files separate concept metadata from the interface, express prerequisite links explicitly, and include a validator for dangling links, cycles, duplicate identifiers, level consistency, and incomplete content bundles. Its roadmap also treats contributor-friendly curriculum files, review, and versioning as product work rather than incidental administration. These are useful patterns for the map's still-unspecified authoring, review, provenance, and versioning workflow. See its [curriculum schema](https://github.com/lamira-the-human/open-alpha/blob/main/curriculum/schema.json), [graph validator](https://github.com/lamira-the-human/open-alpha/blob/main/curriculum/validate.js), and [roadmap](https://github.com/lamira-the-human/open-alpha/blob/main/ROADMAP.md).

**Ideas that do not transfer yet.** The current recommendation logic assumes grade-level prerequisites without observed evidence on a learner's first visit. A five-question quiz at 80% sets a concept as mastered, and later results can only preserve or increase that score. This conflicts with the pilot's evidence confidence, prerequisite support, independent probes, triangulation over time, and interpretable BKT direction. Its on-demand AI-generated lessons and community/agent review queue also require a permissions, curriculum review, safeguarding, and provenance model before they could be used with students. See [next-concept logic](https://github.com/lamira-the-human/open-alpha/blob/main/api/tutor/next/%5Bsubject%5D.ts), [quiz submission](https://github.com/lamira-the-human/open-alpha/blob/main/api/tutor/quiz/submit.ts), and [review endpoint](https://github.com/lamira-the-human/open-alpha/blob/main/api/quality/review.ts).

The resulting direction is to adopt the *shape* of a validated, versioned curriculum graph and to investigate its appropriate AA SL authoring governance; it is not to copy Open Alpha's code, content, mastery threshold, infrastructure, or AI-first teaching approach.

## 8. What this investigation does and does not settle

The primary sources support the existence of placement, ordered work, assessment gates, cross-app reporting, incentives and human coaching. They also expose important exceptions that the earlier supplied model omitted. They do not independently validate accelerated-learning claims, reveal a universal mastery engine, or prove transfer to an IB classroom. Promotional outcomes should remain vendor claims; neither API completeness nor benchmark scores alone establish causality.

The following questions belong in existing follow-up work rather than duplicate research tickets:

1. **Mastery/readiness policy:** What independent evidence, retention checks and uncertainty should justify route changes? How should contradictory class assessment outcomes prompt review without directly changing learner state?
2. **Student/teacher prototype:** How much suitable choice should a student see, and how will completion, confidence, readiness and delayed evidence be understood?
3. **Classroom operating model:** What achievable daily intention fits structured use time, and which check-in reasons deserve teacher attention first?
4. **Activity/evidence contract:** Which connected activities can provide interpretable competency evidence, and which provide only completion or engagement signals?
5. **Privacy boundary:** Which data is actually necessary for coaching? Publicly described monitoring features are not a requirement for the pilot.

A private vendor walkthrough would resolve exact current screens and configuration permissions, but is not necessary to begin those bridge-phase decisions. No student data, proprietary test items, screenshots containing student records, or licensed learning content were copied into this report.
