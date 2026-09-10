# Repository guidance

Read `CONTEXT.md` before naming or changing domain concepts. This repository is in discovery: preserve decided constraints, distinguish evidence from hypotheses, and do not select implementation technology unless a ticket explicitly asks for that decision.

Do not commit student data, licensed textbook files, school secrets, credentials, or copied material without verified reuse permission and recorded provenance.

## Repository backup

After completing repository work, commit the relevant changes and push the current branch to `origin` so the artifacts are backed up online. This does not override the protected-data and reuse-permission rules above.

## Adoption before invention

Start from established projects and their existing behaviour. Inspect and trial upstream learning workflows before proposing custom mastery, hint, retry, progression, or evidence systems. The initial work is anchoring existing systems to the IB Mathematics AA SL curriculum: map competencies, prerequisites, activities, and assessment coverage using upstream structures and configuration. Preserve upstream defaults as the baseline; propose changes only after a concrete trial exposes an IB-specific gap. Do not ask the teacher to redesign mechanisms that upstream systems already provide. Synthetic replacements are not evidence that an upstream system fits. This does not override recorded reuse permissions or school-data constraints.

## Agent skills

### Issue tracker

Issues and planning artifacts live in GitHub Issues. External pull requests are not initially treated as triage requests. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the standard `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, and `wontfix` labels. See `docs/agents/triage-labels.md`.

### Domain docs

This is a single-context project using root `CONTEXT.md` and `docs/adr/`. See `docs/agents/domain.md`.
