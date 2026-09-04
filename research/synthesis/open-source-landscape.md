# Open-source landscape: leads to investigate

Status: lead inventory from supplied research; project claims, licenses, and maturity are not yet independently verified.

## Product and platform references

| Candidate | Reported relevance | Key investigation |
|---|---|---|
| Open Alpha | Directly inspired by Alpha School's two-hour model | Is the architecture reusable, active, licensed appropriately, and suitable beyond its current subjects? |
| OATutor | Adaptive tutoring and Bayesian Knowledge Tracing | Can its mastery and problem-selection components support an IB Mathematics pilot? |
| Open TutorAI Community Edition | Self-hosted student, teacher, and parent experiences | Is it a viable platform base or mainly a reference implementation? |
| OpenTutor / tutor.new | Agentic tutor orchestration | Does it offer stable components beyond a young proof of concept? |
| Studyield | Knowledge graphs, adaptive assessment, and learning paths | Which concepts or modules are reusable and evidence-backed? |
| Open edX | Mature learning platform and integrations | Would adapting it reduce infrastructure work or create excessive platform complexity? |
| Kolibri | Mature offline learning infrastructure | Does offline-first delivery matter for the intended school context? |

## Interoperability standards

| Standard | Possible role |
|---|---|
| QTI | Portable assessment items and tests |
| LTI | Launch and exchange with external learning tools |
| Caliper Analytics | Normalized learning activity events |

These standards should be evaluated against actual pilot workflows before they become architectural requirements.

## AI and workflow infrastructure

| Candidate | Possible role | Caution |
|---|---|---|
| PydanticAI | Typed AI application and agent workflows | AI workflow layer, not the learner model |
| LangGraph | Explicit persistent graph workflows | Added orchestration complexity must earn its place |
| Temporal, DBOS, Prefect, Restate | Durable background execution | Likely premature until long-running workflows are known |
| Ollama, vLLM | Local model serving | Hardware, model quality, operations, and data policy need evaluation |
| Swamp Club | Versioned automation for curriculum/content operations | Development/content operations tool, not the education platform itself |

## Architectural hypothesis to test

The system may be strongest if it separates:

1. an inspectable curriculum and learner-state core;
2. subject-specific activity and evidence adapters;
3. student and teacher experiences;
4. optional AI assistance around—not in place of—consequential educational decisions.

No candidate stack has been selected.

