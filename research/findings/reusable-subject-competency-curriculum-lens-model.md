# Reusable subject-competency and curriculum-lens model

Decision date: 2026-09-08. Question: [Define the reusable subject-competency and curriculum-lens model](https://github.com/RktRobinhood/alpha-ikast/issues/17).

## Decision

Represent mathematics as one shared, typed competency graph rather than separate course graphs or folders. A versioned curriculum lens preserves the native syllabus structure and selects the required competencies that form a curriculum destination. Prerequisite and beyond-destination competencies remain connected to that destination without becoming part of it.

This is a domain model, not a database, serialization format, graph technology, or complete AA SL decomposition.

## Competency identity and mastery

- A subject competency describes the same observable capability wherever it appears. AA SL, AA HL, physics, and later curricula reuse it rather than copy or rescale it.
- Identical performance supplies identical mastery evidence. Course membership and cohort-level assumptions about motivation or attainment do not bias the learner state.
- Differences between AA SL and AA HL are expressed by which competencies their lenses require, not by applying different mastery standards to a genuinely shared competency.
- Evidence from one subject may advance every curriculum lens requiring the same competency, but only when the activity explicitly maps and actually demonstrates it. Preserve the activity, subject, assistance, timing, and version provenance.
- An activity updates only the competencies it demonstrably exercises. Success on a later competency does not automatically grant mastery of every prerequisite beneath it.

## Curriculum lenses and versions

- A curriculum lens retains the syllabus's familiar headings, terminology, coverage, and forms of performance while mapping them to the shared graph.
- Mapping is traceable in both directions: every required syllabus expectation maps to supporting competencies, and every competency claimed as required maps back to a syllabus expectation.
- A published lens version is immutable for its applicable cohorts and examination sessions. Corrections and syllabus revisions produce new releases that can coexist while continuing to reuse unchanged competencies.
- A curriculum destination is a target, not a learning ceiling. Connected competencies outside it remain available under the priority rule below.

## Relationships and routing

- A prerequisite edge means that absence of one competency materially obstructs demonstrating another. Customary teaching sequence, syllabus hierarchy, useful association, application, and equivalence are different relationships and must not be represented as strict prerequisites.
- Strict prerequisite relationships guide diagnosis and the default route but are not absolute access locks. A learner may attempt appropriate target-level work; success can avoid unnecessary remediation, while failure can expose a need to investigate mapped prerequisites.
- Repeated easy work must not become a way to avoid appropriate current-course challenge.
- Beyond-destination learning becomes available only after required learning, due retrieval, and imminent assessment-readiness work are addressed. When those priorities are satisfied, a learner is not blocked from pursuing further supported study.

## Activities, resources, and methods

- Learning resources and versioned learning activities exist independently of curriculum lenses and may serve several curricula without duplication.
- Activities explicitly declare which competencies they teach or observe. Completion remains separate from mastery.
- A demonstrated solution method can be retained as a solution strategy observation. Treat a method as a separate subject competency only when a curriculum requires it or a later competency materially depends on it.
- This method/observation boundary is provisional. Revisit it if real student work shows that it misclassifies strategies, misroutes learners, or produces unhelpful feedback.

## Adoption baseline for learner progress

Do not invent a new progress formula or learner-facing graph before trial evidence exists. Preserve Open Alpha's existing concept-map and progress experience as the first surrounding baseline, connect it to the AA SL slice, and adapt only when teacher or student feedback exposes a concrete gap. The underlying learner state remains competency-based and revisable; any course view is derived from the competencies required by its lens rather than being a second mastery record.

The primary-source comparison in [Cross-curricular competency and mastery patterns](cross-curricular-competency-mastery-patterns.md) supports this direction:

- 1EdTech CASE preserves separately identified frameworks and relates items within and across them.
- Moodle separates frameworks, course selections, activity mappings, evidence, and progress views.
- Khan Academy derives course progress from revisable skill states.
- Math Academy describes a course route through a larger mathematics knowledge graph.
- OATutor maps problem steps explicitly to knowledge components and updates those mapped components.

No reviewed product establishes a complete cross-subject mastery graph that Alpha Ikast can copy unchanged. Cross-subject evidence sharing is therefore a project decision to validate through a later concrete mathematics/physics case, not a claimed upstream default.

## Deferred to evidence

- Exact AA SL competency granularity and full prerequisite graph.
- The learner-facing graph scale, navigation, coloring, aggregation, and any overall completion percentage.
- Detailed method taxonomy and qualitative-feedback policy.
- Cross-subject interface and coordination beyond a concrete shared-competency trial.
- Content approval, provenance, and versioning workflow, addressed by the following Wayfinder decision.

