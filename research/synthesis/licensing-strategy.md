# Licensing strategy during discovery

Status: operational research rule, not legal advice and not a final project-license decision.

## Decision deferred

The final licenses for Alpha Ikast software, documentation, and educational content will be selected after the component and content investigations reveal what the project actually needs to combine and distribute.

## Rules that cannot be deferred

### Inspect broadly

Public repositories, papers, products, and learning materials may be studied as sources of ideas, architecture patterns, comparison, and research evidence.

### Copy only with permission

Code or content enters a prototype or the public repository only when an applicable license or direct permission allows that use. GitHub explains that a public repository without a license remains under default copyright: others may view and fork it through GitHub, but do not receive general permission to reproduce, distribute, or create derivative works.

### Record provenance immediately

Every adopted component or content item should record its source, exact version/revision, copyright holder or author when available, license, attribution requirements, modifications, and where it is distributed.

### Keep kinds of work separate

Software, educational content, documentation, model weights, and datasets can carry different licenses. A final repository may legitimately contain separately licensed parts; one “strictest” license does not automatically replace every upstream license.

### Check compatibility before combination

Copyleft strength is not a universal ordering. Two licenses are compatible only when the planned combination and distribution can satisfy both. Separate services or adapters may sometimes avoid forming one combined derivative work, but that conclusion depends on the licenses and integration and must be checked deliberately.

## Practical discovery categories

| Category | Discovery use | Copy into project? |
|---|---|---|
| Permissively licensed code | Inspect, run, compare | Yes, with notices and conditions |
| Compatible copyleft code | Inspect, run, compare | Potentially; review combination and distribution obligations first |
| Openly licensed content | Inspect and map | Potentially; retain attribution and content-specific terms |
| NonCommercial content | Inspect and test internally where permitted | Keep isolated until intended distribution and use are confirmed compatible |
| Public source with no license | Inspect and reference ideas | No copying, modification, or redistribution without permission |
| Licensed school/teacher materials | Use as authorized curriculum references | Do not place in the public repository or redistribute unless the license permits it |

## Primary guidance

- [GitHub: Licensing a repository](https://docs.github.com/en/enterprise-cloud@latest/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository)
- [GNU Project: Frequently Asked Questions about GNU licenses](https://www.gnu.org/licenses/gpl-faq.html.en)
- [Creative Commons: Compatible licenses](https://creativecommons.org/compatible-licenses/)
- [Creative Commons: Frequently Asked Questions](https://creativecommons.org/faq/)

