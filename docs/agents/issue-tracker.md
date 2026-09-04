# Issue tracker: GitHub

Issues and planning artifacts for this repository live in GitHub Issues. Use the `gh` CLI for operations and infer the repository from the configured Git remote.

## Common operations

- Create: `gh issue create --title "..." --body "..."`
- Read: `gh issue view <number> --comments`
- List: `gh issue list --state open --json number,title,body,labels,assignees`
- Comment: `gh issue comment <number> --body "..."`
- Label: `gh issue edit <number> --add-label "..."`
- Close: `gh issue close <number> --comment "..."`

## Pull requests as a triage surface

External pull requests are **not** treated as feature requests by the triage workflow initially. Contributions may still be accepted and reviewed normally. Revisit this when contribution and implementation conventions exist.

## Wayfinding operations

- The map is one issue labelled `wayfinder:map`.
- Each investigation is a child issue labelled `wayfinder:research`, `wayfinder:prototype`, `wayfinder:grilling`, or `wayfinder:task`.
- Use GitHub sub-issues where available. Otherwise, list children as tasks in the map and place `Part of #<map>` in each child.
- Use GitHub's native issue dependencies where available. Otherwise, place `Blocked by: #<number>` at the top of the blocked issue.
- The frontier consists of open, unassigned child issues with no open blockers.
- Claim a frontier issue before work with `gh issue edit <number> --add-assignee @me`.
- Resolve by posting the answer as a comment, closing the issue, and adding one linked gist to the map's `Decisions so far` section.

