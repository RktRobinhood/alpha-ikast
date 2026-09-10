# Cross-curricular competency and mastery patterns

Research date: 2026-09-08. Question: how do established standards and learning systems represent competencies, relationships, curriculum alignment, overlapping courses or subjects, learner evidence, and visible progress?

## Conclusion

Established systems do not treat a curriculum as a folder of duplicated skills. The strongest reusable pattern is a set of separately identifiable layers:

1. **Competency definitions and relationships** describe what can be known or done.
2. **Curriculum or course selections** identify which competencies form a learner's destination.
3. **Activities and resources** map to the competencies they teach or observe.
4. **Learner evidence and state** record what a particular learner has demonstrated for those competencies.
5. **Progress views** project that learner state through a chosen course, unit, learning plan, or review horizon.

This is a synthesis, not the documented architecture of one product. CASE supplies the exchange and alignment layer but no mastery algorithm. Moodle supplies frameworks, plans, activity mappings, ratings, and progress views, mostly in trees. Khan Academy and Math Academy show learner-facing course progress and revisable skill/topic state. OATutor shows the most inspectable fine-grained mapping from problem steps to knowledge components and a statistical update per component.

For Alpha Ikast, this evidence supports treating the IB syllabus as a traceable destination through a larger graph, not as a separate copy of mathematics. It also supports a learner-facing map rather than a folder metaphor. The exact node boundaries, cross-subject evidence rules, and progress calculation still require trials against real AA SL material and later against another subject.

## Evidence boundary

- **Documented behavior** below is stated in an official specification, official product documentation, first-party source code, or first-party research.
- **Project inference** is a proposed interpretation for Alpha Ikast. It is clearly labeled and should be tested rather than treated as established fact.
- No student data, licensed IB material, private product behavior, or copied textbook content was inspected. Public OpenStax/OATutor structure is described without reproducing learning material.

## What established systems do

| System | Competency / relationship model | Course or curriculum alignment | Learner state and progress | Boundary relevant to Alpha Ikast |
| --- | --- | --- | --- | --- |
| **1EdTech CASE 1.1** | A framework document contains uniquely identified competency items. Associations can connect items within or across framework documents using relations including `isChildOf`, `isPartOf`, `exactMatchOf`, `precedes`, `isRelatedTo`, and `replacedBy`; the association vocabulary is extensible. | Frameworks and items can be aligned to other frameworks and items. Stable identifiers allow resources, activities, and assessment results to refer to the same definitions across systems. Documents carry version and status metadata. | CASE enables consistent references for reporting, but it does not define how evidence becomes mastery or how progress is calculated. | Strong precedent for preserving an authoritative syllabus structure while aligning it to other competency definitions. Its `precedes` relation means order, not necessarily a strict learning prerequisite. |
| **Moodle competencies** | Competencies live in version-distinguishable frameworks arranged as trees; related links and parent-completion rules are also available. Frameworks have configurable rating scales. | Courses and learning-plan templates select competencies from frameworks. Activities can map to one or more course competencies. | Students see current ratings and progress in courses and learning plans. Activities may attach evidence, request review, or automatically complete a competency; prior-learning evidence can be linked to one or more competencies and reviewed. | Clear separation of framework, course/plan, activity mapping, evidence, rating, and progress. The documented tree and completion rules are administrative affordances, not a prerequisite knowledge graph or a validated mastery model. |
| **Khan Academy Mastery** | Learner state is maintained for individual skills with visible levels from Not started through Mastered; later performance can move a skill up or down. | Skills are grouped into units and courses. | The current Course Mastery percentage is the share of course skills at Proficient or Mastered. Exercises, quizzes, unit tests, course challenges, and personalized Mastery Challenges can update skill levels. | Strong precedent for calculating a familiar course view from underlying skill states, while keeping the state revisable. The public documentation does not describe cross-course or cross-subject identity rules for skills. |
| **Math Academy** | A graph contains mathematical topics and relationships including prerequisites. A learner's answers are overlaid on it as an individual knowledge profile; spaced repetitions add a visible stability dimension. | Diagnostics are tailored to a course but also inspect lower-course foundations. Task selection can repair foundations while continuing course work whose prerequisites are available. | The knowledge frontier shows what the learner is ready to learn. Topic nodes become visually darker as spaced-repetition evidence becomes more stable; diagnostics report course progress and foundational gaps. | Closest public example of “a destination inside a larger mathematics graph.” Its exact graph, learner model, and routing algorithms are proprietary, and it does not establish a cross-subject model. |
| **OATutor / OpenStax-derived content** | A centralized skill model maps each problem step to one or more knowledge components (KCs). BKT parameters and learner mastery are maintained per KC. | Course plans group lessons, while the skill model separately maps steps to KCs. Content sources can be versioned and loaded separately. OpenStax-derived problems retain source and licence attribution. | The pinned source updates mapped KCs from the first graded attempt and uses KC mastery for adaptive problem selection. | Inspectable precedent for separating course organization from activity-to-competency mapping and updating only mapped KCs. Its optional taxonomy is ordering metadata, not a developed cross-curriculum graph. |

### 1EdTech CASE: preserve native frameworks and connect them

CASE is the clearest primary-source answer to “what do others do when standards overlap?” It represents the source framework as a digital document containing individually identified items, while associations relate items or whole documents to other frameworks. `exactMatchOf` can state equivalence, `replacedBy` can connect versions, and broader relations can preserve hierarchy, part-whole structure, order, or looser relatedness. The official CASE overview also describes tagging learning resources and activities with competency identifiers so outcomes can be reported consistently across platforms.

CASE therefore supports many-to-many alignment without forcing all frameworks into one hierarchy. It also warns against overloading one edge: its normative definition of `precedes` is temporal or presentation order, whereas Alpha Ikast's **prerequisite competency** is a stricter claim that absence materially obstructs the target.

**Project inference:** retain the IB lens's own headings and statements as an authoritative, versioned structure; align each required statement to one or more subject competencies; and audit in both directions so neither the syllabus nor the competency graph silently drifts. Use different relationship meanings for hierarchy, strict prerequisite, curricular order, equivalence, and merely related concepts.

### Moodle: a destination selects competencies; evidence remains attached to competencies

Moodle's documentation distinguishes a competency framework from a course, a learning-plan template, an activity, evidence, and a learner rating. A course can list the competencies it teaches, a learning plan selects a set for a learner or cohort, and an activity may be associated with multiple competencies. Students see progress through the course or plan rather than having to browse the complete framework.

Moodle also demonstrates a caution. It can automatically mark a parent complete when children are complete or mark a competency complete from activity completion. Those are configurable administrative rules, not evidence that completion equals durable mastery. Alpha Ikast has already decided to preserve activity completion separately from mastery.

**Project inference:** a curriculum destination can behave like a learning-plan selection over shared competencies while its learner-facing progress is calculated from the learner state. A separately editable “syllabus completion score” would risk contradicting the competency evidence unless it represents something genuinely different, such as teacher-reported coverage.

### Khan Academy: course progress is a projection over revisable skill states

Khan Academy's current documentation says each skill has a visible state, later work can move it up or down, and Course Mastery is calculated as the percentage of course skills currently at Proficient or Mastered. Unit and course activities can update several skills, and Mastery Challenges revisit three previously practised skills after a delay.

This is a useful behavior pattern, not a transferable formula. Khan's public rule does not express Alpha Ikast's separate evidence-confidence, rust, or curriculum-weighting requirements, and it does not say how the same capability is identified across courses.

**Project inference:** “all of the syllabus coloured in” is best understood as a curriculum view over competency state. It can show current position, recent growth, uncertain or rusty areas, and remaining requirements without creating a second mastery record for the same mathematics.

### Math Academy: a course is a route through a larger mathematics graph

Math Academy explicitly describes thousands of linked topics across mathematics, with prerequisites between topics, a learner-specific knowledge profile overlaid on that graph, and a knowledge frontier separating what the learner knows from what they are ready to learn. Its course-specific diagnostic also probes lower-course foundations, and its routing can address those foundations while allowing progress elsewhere in the selected course. Spaced-repetition status is visible on topic nodes as a stability signal.

**Project inference:** this closely matches the desired shape for AA SL: the fixed IB destination is a highlighted region and trajectory through a larger subject graph, not a hard wall. Prerequisites below it and optional mathematics beyond it remain connected. This source does not justify copying Math Academy's unknown algorithms or assuming that a mathematics-only graph solves cross-subject overlap.

### OATutor: activities provide evidence only for mapped knowledge components

OATutor's first-party documentation and pinned source separate course plans from a centralized skill model. Problem steps map to arrays of KCs, each KC has BKT parameters, and the learner state is updated for those mapped KCs. Its content tooling records both source attribution and KC tags for OpenStax-derived material.

**Project inference:** resources from different lawful sources can support the same subject competency without being copied into each curriculum. A task should update only the competencies that it explicitly maps and actually exercises. Reusing a resource does not by itself prove that its mapping or difficulty is suitable for IB; curation and classroom evidence remain necessary.

## Cross-subject overlap: supported direction and unresolved policy

No reviewed learning product publicly documents the complete behavior needed for a single learner graph spanning mathematics, physics, and other school subjects. CASE does explicitly support associations across framework documents; Moodle can place framework competencies into courses and plans; the adaptive products reviewed here are principally course- or mathematics-centered.

The following is therefore **project synthesis**:

- Keep a shared mathematical competency once when the observable capability and mastery standard are genuinely identical.
- Let AA SL, AA HL, physics, and later curricula each select or align to that competency while preserving their own native syllabus structures.
- Keep subject-specific applications distinct. “Use a mathematical model to analyse kinematics” is not automatically identical to “differentiate a function,” even if the physics activity exercises differentiation.
- Allow evidence from a physics activity to inform a mathematical competency only when the activity mapping and captured work actually demonstrate that mathematics. Mere topical proximity or a curriculum-level “related to” link is insufficient.
- Expose the overlap to teachers as a connection, with provenance: which subject activity supplied which evidence, under what conditions, and for which competency. Do not let evidence silently migrate between subjects.

For the teacher's example, the useful view is not two folders called calculus and kinematics. It is connected nodes: a physics-specific kinematics capability can depend on or apply shared mathematical nodes, while each curriculum lens highlights the nodes it requires. This permits a physics teacher to see whether relevant mathematics has been demonstrated without treating performance in either subject as interchangeable by default.

## Concrete interpretation of “quadratics and transformations”

The phrase is too broad to be one trustworthy mastery node. A provisional diagnostic decomposition might include nodes for recognising equivalent quadratic forms, identifying roots or a vertex from an appropriate form, relating parameter changes to graph transformations, converting between forms, and using those capabilities in unfamiliar problems. Some nodes may have strict prerequisites; others may only be commonly taught in sequence.

This example is illustrative, not a decided AA SL graph. The correct boundaries should be derived backward from the authorized syllabus and assessment expectations, checked against established upstream content structures, and tried with real tasks. The learner-facing interface can still group these nodes under the familiar IB heading “quadratics” while revealing connections and prerequisites when useful.

## What to carry into the design, without selecting technology

1. Treat the full structure as a typed graph, not a folder tree. A tree may remain one useful syllabus or navigation view.
2. Give curriculum statements and subject competencies stable identities and explicit version provenance.
3. Preserve distinct relationship meanings: syllabus hierarchy, competency decomposition, strict prerequisite, curricular sequence, equivalence, application, and loose relationship.
4. Make each curriculum destination a traceable selection/alignment over competencies, while preserving the curriculum's native organization.
5. Attach activities and evidence to competencies explicitly; retain activity, subject, assistance, timing, and version provenance.
6. Maintain one learner state per genuinely shared competency, then calculate course, unit, review, and cross-subject views from it.
7. Show students both position and motion: required nodes mastered, nodes in progress or uncertain, due retrieval/rust, recent gains, and the next justified steps toward the destination.
8. Validate the model first with a complete AA SL slice. Add physics only after the math graph and evidence mappings expose a concrete cross-subject case to trial.

## Open questions for trials

- Which AA SL syllabus statements decompose into several observable competencies, and which apparently separate statements rely on the same competency?
- Which relations are truly strict prerequisites rather than teacher sequence or useful association?
- How should a syllabus area's progress aggregate required competencies without hiding a single important gap?
- When does work in physics genuinely demonstrate a mathematical competency, and what captured reasoning is necessary before sharing that evidence?
- Which learner-facing map is understandable at useful scale: full graph, local neighbourhood, syllabus outline with expandable connections, or a combination?
- Does showing cross-subject evidence help teachers coordinate, or create misleading confidence without enough task-level provenance?

## Primary sources

- 1EdTech Consortium, [CASE standards overview](https://www.1edtech.org/standards/case) and [CASE 1.1 information model](https://www.imsglobal.org/sites/default/files/spec/case/v1p1/information_model/caseservicev1p1_infomodelv1p0.html), final release dated 2025-01-24. Accessed 2026-09-08.
- 1EdTech Consortium, [CASE 1.1 Best Practice and Implementation Guide](https://www.imsglobal.org/spec/CASE/v1p1/impl). Accessed 2026-09-08.
- Moodle, [Competency frameworks](https://docs.moodle.org/500/en/Competency_frameworks), [Competencies](https://docs.moodle.org/500/en/Competencies), and [Learning plans](https://docs.moodle.org/500/en/admin/tool/lp/learningplans). Accessed 2026-09-08.
- Khan Academy, [What are Course and Unit Mastery?](https://support.khanacademy.org/hc/en-us/articles/115002552631-What-are-Course-and-Unit-Mastery) and [What are Mastery Challenges?](https://support.khanacademy.org/hc/en-us/articles/360037494231-What-are-Mastery-Challenges). Accessed 2026-09-08.
- Math Academy, [How It Works](https://mathacademy.com/how-it-works) and [How Our AI Works](https://mathacademy.com/how-our-ai-works). Accessed 2026-09-08.
- CAHLR, [OATutor repository at the pinned revision](https://github.com/CAHLR/OATutor/tree/6de5ada333f02ac18752aac48e38b9462a7882bd), including its documented content-source, course-plan, skill-model, BKT, and problem-selection structure. Accessed 2026-09-08.
- Pardos et al., [“OATutor: An Open-source Adaptive Tutoring System and Curated Content Library for Learning Sciences Research”](https://doi.org/10.1145/3544548.3581574), CHI 2023. Accessed 2026-09-08.
- CAHLR, [OATutor Tooling](https://github.com/CAHLR/OATutor-Tooling), documenting OpenStax source attribution, lesson organization, and step/KC tagging. Accessed 2026-09-08.
