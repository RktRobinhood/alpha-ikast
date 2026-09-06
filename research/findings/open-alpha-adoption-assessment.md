# Open Alpha adoption assessment

Research date: 2026-09-06. Question: [Evaluate Open Alpha as an adopt-and-adapt pilot foundation](https://github.com/RktRobinhood/alpha-ikast/issues/13).

## Recommendation

Make [Open Alpha](https://github.com/lamira-the-human/open-alpha) a major **adopt-and-adapt foundation** for the AA SL bridge-phase pilot, once its copyright holder grants an explicit reuse licence and provenance is recorded. Its learner-facing web experience, curriculum-graph shape, curriculum validation, pre-authored-content preference, and contribution/review direction offer a useful base. It must not be deployed unchanged or treated as the authoritative learner-state, content-governance, teacher-steering, or production-data solution.

The first pilot should preserve the Open Alpha experience where it helps a learner see a path and start work, while replacing or adapting the educational record behind it. This gives the project a real starting point without inheriting a K–12 grade ladder as an AA SL learning model.

## Verified reuse boundary

The repository calls itself open source, but GitHub currently reports no declared repository licence: its [licence endpoint](https://api.github.com/repos/lamira-the-human/open-alpha/license) returns `404`, its [community profile](https://api.github.com/repos/lamira-the-human/open-alpha/community/profile) has `license: null`, and its tree contains no `LICENSE` file. That means its public visibility and stated intent do not yet grant the project permission to copy, modify, or deploy its code or curriculum. This is a provenance issue, not a rejection of the project.

Before forking or reusing material, record a licence selected by the copyright holder, the approved source revision, and the provenance of every retained dependency and curriculum contribution. This follows the repository's existing [discovery licensing strategy](../synthesis/licensing-strategy.md) and the definition of **authorized reference material** in `CONTEXT.md`.

## What to adopt

| Open Alpha capability | AA SL pilot role | Evidence |
| --- | --- | --- |
| React learner experience, concept map, progress view, tutor conversation, and activity navigation | A concrete starting surface for the first learning loop and later student mastery path prototype. | [Repository structure](https://github.com/lamira-the-human/open-alpha), [frontend](https://github.com/lamira-the-human/open-alpha/tree/main/frontend) |
| Subject JSON with explicit prerequisite edges | Starting shape for an AA SL competency and prerequisite graph. Replace grade levels with pilot-course and prerequisite competencies. | [Schema](https://github.com/lamira-the-human/open-alpha/blob/main/curriculum/schema.json) |
| Graph validation for dangling prerequisites, cycles, duplicate identifiers, and incomplete bundles | A reusable quality gate for the AA SL curriculum graph. Extend it with curriculum-source provenance, reviewer approval, competency tags, and activity/evidence validation. | [Validator](https://github.com/lamira-the-human/open-alpha/blob/main/curriculum/validate.js) |
| Pre-authored content preferred over generated/cached lessons | Keep this precedence: approved, permission-cleared learning resources should be selected before optional AI-assisted explanations. | [Lesson resolver](https://github.com/lamira-the-human/open-alpha/blob/main/api/curriculum/lesson.ts) |
| Contribution and review workflow direction | A useful starting point for a teacher/expert review queue after it gains authenticated roles, provenance, and an AA SL release process. | [Contribution endpoint](https://github.com/lamira-the-human/open-alpha/blob/main/api/contribute/lesson.ts), [review endpoint](https://github.com/lamira-the-human/open-alpha/blob/main/api/quality/review.ts) |

## Required adaptations before students use it

### Evidence-led learner state

Open Alpha's [quiz submission route](https://github.com/lamira-the-human/open-alpha/blob/main/api/tutor/quiz/submit.ts) accepts a client-provided aggregate score, preserves the highest result forever, and treats 80% as mastery. Its [next-concept route](https://github.com/lamira-the-human/open-alpha/blob/main/api/tutor/next/%5Bsubject%5D.ts) assumes lower-grade prerequisites for a new learner. These rules do not provide the pilot's observed learning evidence, baseline exploration, independent-probe distinction, evidence confidence, retention, or interpretable BKT direction.

Adapt the activity boundary so that deterministic, competency-tagged independent probes create immutable observations. Let the learner state interpret those observations; do not let the browser assert mastery. Guided practice and tutor conversation remain useful learning activity, but their completion does not equal independent mastery.

### Curriculum and content governance

The [lesson route](https://github.com/lamira-the-human/open-alpha/blob/main/api/curriculum/lesson.ts) can generate and immediately cache content for later learners. The contribution and review routes accept a caller-supplied contributor or reviewer identity; the review route imports authentication but does not enforce it. The published workflow has no source-rights record, approved-release version, or school-owned reviewer role.

For AA SL, generated explanations, items, and hints must remain candidates until an authorized reviewer approves a version with its source and reuse status. Permission-cleared native items and linkable learning resources need separate provenance from the licensed teacher materials used only as authorized reference material.

### Teacher steering and bridge-phase operations

The data model currently defines student and parent roles, while the project needs teacher steering, learning horizons, assessment scopes, check-in triage, and interventions. It also stores tutor/coach messages, learner interests, learning-event payloads, and guest-session IP hashes. The repository's Vercel configuration, Turso client, ATXP gateway, and unrestricted CORS in the legacy Express server are implementation choices to replace or validate against the pilot's self-hosting, data-governance, and safeguarding requirements. See [database model](https://github.com/lamira-the-human/open-alpha/blob/main/api/_lib/db.ts), [LLM client](https://github.com/lamira-the-human/open-alpha/blob/main/api/_lib/llm.ts), [Vercel configuration](https://github.com/lamira-the-human/open-alpha/blob/main/vercel.json), and [legacy server](https://github.com/lamira-the-human/open-alpha/blob/main/backend/src/server.ts).

## Adoption sequence

1. Obtain and record explicit Open Alpha reuse permission and the exact source revision.
2. Create a school-controlled fork only after that permission is in place; retain the learner experience, concept-map shell, graph schema, and validator as the starting baseline.
3. Replace client-reported quiz scores with the activity-and-evidence contract under investigation. Preserve raw observations independently of the mastery model.
4. Add AA SL curriculum, prerequisite competencies, authorized-resource provenance, review roles, and versioned release records.
5. Add teacher steering, assessment scope, check-in triage, and a self-hostable deployment/data boundary before classroom use.
6. Keep AI tutoring and generation behind inspectable task contracts. Start with approved content and deterministic mathematics checks; allow AI-assisted material only after its review and evaluation path is defined.

This route makes Open Alpha a large and visible part of the pilot without treating the current implementation as educationally or operationally complete.
