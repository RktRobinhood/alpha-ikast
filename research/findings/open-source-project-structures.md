# Open-source project structures relevant to an AA SL adaptive-learning pilot

**Research date:** 2026-09-04  
**Scope:** Repository structure, deployable boundaries, content and learner-model layers, extension seams, licensing, and self-hosting. This is an architecture survey, not a backend selection.

## Executive finding

No reviewed project is a complete, ready-to-adopt version of the intended product. The strongest path is compositional:

- use **OATutor and pyBKT** as the clearest starting point for skill-tagged evidence and probabilistic mastery;
- evaluate **STACK and the WeBWorK renderer** as independently hosted mathematical response engines;
- curate openly licensed content from **OATutor Content, STACK's sample library, and selected WeBWorK OPL material**, preserving item-level attribution and license metadata;
- learn from **Open TutorAI CE** for model/provider isolation and self-hosted AI/RAG services;
- keep **Open edX and Kolibri** as possible host/integration platforms, not assumed foundations;
- treat **Open Alpha, tutornew/OpenTutor, and Studyield** primarily as product/architecture references until their maturity, licensing, and learner-model fit are resolved.

Only a browser-based, cross-device delivery surface is decided. Nothing in this review justifies choosing a backend yet.

## Comparison at a glance

| Exact project | What is actually deployable | Educational data/model | Main extension seam | License state | Realistic use here |
|---|---|---|---|---|---|
| [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | Static React application; optional Firebase logging; separate Express LTI middleware | Step-level problems, KC mappings, BKT parameters, configurable selection heuristics | Replaceable content-source folders, problem-selection functions, optional LTI layer | MIT code; content is separately CC BY 4.0 | Adopt and adapt the mastery/content concepts; prototype with its content; do not assume its whole UI/data design |
| [lamira-the-human/open-alpha](https://github.com/lamira-the-human/open-alpha) | React/Vite UI plus Vercel functions, Turso, and ATXP-hosted LLM access | JSON prerequisite graph; five-question quiz; maximum score at or above 80% marks completion | Curriculum JSON/schema and route-level APIs | **No repository license found** | Reference the learner/parent experience and simple graph flow only |
| [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | FastAPI/SvelteKit application; Docker Compose with local Ollama; Kubernetes assets | Users, chats, files, RAG, “supports,” governance; no demonstrated longitudinal KC mastery layer | Domain services/repositories, HTTP adapters, explicit AI-provider interface | BSD-3-Clause | Reuse or learn from provider/RAG boundaries; evaluate as a service donor, not the learning core |
| [tutornew/OpenTutor](https://github.com/tutornew/OpenTutor) | JS monorepo plus Python LiveKit agents; multi-service Docker development stack | Lesson/session runtime, modular activities, agent prompts; no established statistical mastery engine found | Manifest-driven learning modules and shared TS packages | **No repository license found** | Reference lesson orchestration, modular activity UI, and session ideas only |
| [studyield/studyield](https://github.com/studyield/studyield) | React/NestJS system with PostgreSQL, Redis, Qdrant, ClickHouse, and Docker Compose | Generated paths, quizzes, RAG, knowledge graph, analytics; current progress is mostly completion and aggregate score | NestJS feature modules | **AGPL-3.0 in LICENSE; README badge/text says Apache-2.0** | Reference feature decomposition; do not treat it as an established mastery model or copy code until license discrepancy is resolved |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | LMS + Studio modular monolith, supported by IDAs and React MFEs; deployed through Tutor | Mature course/content, enrolment, grading, learner records and analytics infrastructure | LTI, XBlocks, REST APIs, Django app plugins, hooks, frontend slots | AGPL-3.0 | Possible institutional host/integration target; likely too much platform for the first learning-loop experiment |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | Offline-first Django/Vue server reached by browsers on laptops/tablets/phones | Content channels, auth, facilities/classes, assignments and event logs; not a BKT/IRT mastery engine | First-class Django/plugin and frontend hook system | MIT | Strong reference or host if offline/LAN delivery matters; otherwise mine its content, logging, and coach patterns |
| [maths/moodle-qtype_stack](https://github.com/maths/moodle-qtype_stack) | Moodle/ILIAS question type; Maxima may run separately; repository also exposes a standalone API | Authored inputs, CAS validation, answer tests, multipart work, potential-response logic | Moodle plugin, question XML/library, standalone API | GPL-3.0 code; docs and bundled sample material CC BY-SA 4.0 | High-value candidate for deterministic mathematics assessment as a separate service or existing LMS integration |
| [openwebwork/webwork2](https://github.com/openwebwork/webwork2), [renderer](https://github.com/openwebwork/renderer), [OPL](https://github.com/openwebwork/webwork-open-problem-library) | Full homework/course application or a smaller Dockerized PG rendering service | Randomized PG problems, answer checking, attempts and scores; no longitudinal KC model in renderer | Renderer HTTP/JWT contract and separable problem library | Renderer GPL-3.0; OPL defaults to CC BY-NC-SA 3.0 with possible per-contribution alternatives | Trial the renderer behind an adapter; curate only license-compatible, AA-SL-mapped problems |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | Python library, not an application | Fits/predicts BKT and variants from ordered learner-skill-response data; includes a roster/state API | DataFrame/CSV mappings and Python API | MIT | Best candidate to adopt as an independent learner-model experiment, behind our own contract |

## Project-by-project findings

### 1. OATutor: the clearest reusable learning loop

OATutor is unusually separable for an adaptive tutor. The browser application can be built as static assets and deployed without a backend. Firebase is optional for persistent logging, while a separate Express middleware supports LTI. Its repository divides the learning system into a React interaction layer, BKT update logic, configurable item-selection heuristics, and versioned content sources ([repository documentation](https://github.com/CAHLR/OATutor#project-structure)).

Its external [OATutor-Content repository](https://github.com/CAHLR/OATutor-Content) makes the content contract concrete:

- a problem pool with explicit steps and hint pathways;
- `skillModel.json` for problem-to-knowledge-component mappings;
- `bkt-params` for prior, learn, slip, and guess parameters;
- `coursePlans.json` for grouping content into lessons/courses.

The application repository explicitly makes its content source a Git submodule, so code and curriculum can evolve independently ([`.gitmodules`](https://github.com/CAHLR/OATutor/blob/main/.gitmodules)). The application code is [MIT-licensed](https://github.com/CAHLR/OATutor/blob/main/LICENSE); the content repository states CC BY 4.0 and includes per-item attribution ([content README](https://github.com/CAHLR/OATutor-Content#licenseatribution)).

**Adopt:** its evidence vocabulary, content/KC separation, BKT implementation ideas, selection-policy seam, and suitable openly licensed prerequisite content.  
**Adapt:** AA SL competency identifiers, prerequisite graph, teacher unit horizon, assessment-readiness policy, event schema, and problem-selection rules.  
**Do not assume:** that a static/local-browser learner state, basic algebraic checking, Firebase logging, or its existing UI is sufficient for a school-wide system.

### 2. Open Alpha: a relevant product sketch, not a legal code base yet

The exact repository is `lamira-the-human/open-alpha`. It contains `frontend`, `backend`, Vercel `api` functions, JSON `curriculum`, and documentation. Its curriculum schema represents concepts with prerequisite IDs, relative levels, lesson material, guided practice, a mastery check, and remediation metadata ([curriculum schema](https://github.com/lamira-the-human/open-alpha/blob/main/curriculum/schema.json)).

The apparent mastery model is deterministic rather than statistical: the quiz endpoint retains a learner's maximum percentage and marks the concept complete at 80%; the next-concept endpoint selects an incomplete node whose prerequisites are complete ([quiz submission](https://github.com/lamira-the-human/open-alpha/blob/main/api/tutor/quiz/submit.ts), [next concept](https://github.com/lamira-the-human/open-alpha/blob/main/api/tutor/next/%5Bsubject%5D.ts)). Lessons can be pre-authored JSON or generated and cached. The LLM client uses an OpenAI-compatible SDK but a hard-coded ATXP gateway URL, while production is described around Turso and Vercel ([LLM integration](https://github.com/lamira-the-human/open-alpha/blob/main/api/_lib/llm.ts), [README architecture](https://github.com/lamira-the-human/open-alpha#technical-details)).

Although the README calls it open source and says it can be run independently, the repository has no `LICENSE` file and GitHub reports no detected license. Source visibility alone does not grant permission to copy, modify, or redistribute it.

**Reference:** the lightweight student path, concept-graph JSON, cached generated lessons, and progress visibility.  
**Do not adopt:** code or content unless the owner adds a suitable license. Its threshold score should not be mistaken for the desired evidence-based mastery model, and its documented managed-service dependencies are not the intended in-house deployment boundary.

### 3. Open TutorAI Community Edition: useful AI infrastructure, limited learning model

This is the distinct repository `Open-TutorAi/open-tutor-ai-CE`. Its current layout is a domain-oriented FastAPI backend (`accounts`, `learning`, `ai`, `content`, `governance`, `system`), transport layer (`gateway`), persistence layer (`data`), and a SvelteKit UI. The repository documents a router → service → repository boundary and keeps provider adapters under `ai/providers` ([architecture and domain map](https://github.com/Open-TutorAi/open-tutor-ai-CE/blob/main/AGENTS.md)).

The provider seam is real in source: an abstract provider interface and registries/adapters separate provider configuration from higher-level services ([provider base](https://github.com/Open-TutorAi/open-tutor-ai-CE/blob/main/ai/providers/base.py), [provider package](https://github.com/Open-TutorAi/open-tutor-ai-CE/tree/main/ai/providers)). The default Compose stack runs the application beside Ollama and persists application/vector data locally, while other Compose overlays and Helm assets cover larger deployments ([Compose file](https://github.com/Open-TutorAi/open-tutor-ai-CE/blob/main/devops/docker/docker-compose.yaml), [devops tree](https://github.com/Open-TutorAi/open-tutor-ai-CE/tree/main/devops)). It is [BSD-3-Clause licensed](https://github.com/Open-TutorAi/open-tutor-ai-CE/blob/main/LICENSE).

However, its “learning supports” model stores objectives, subject, level, duration, dates, files and a linked chat; course packages are currently thin, and no competency graph or longitudinal BKT/IRT layer is evident in the documented domain map ([support model](https://github.com/Open-TutorAi/open-tutor-ai-CE/blob/main/data/models/support.py), [learning tree](https://github.com/Open-TutorAi/open-tutor-ai-CE/tree/main/learning)).

**Adopt/evaluate:** provider abstraction, local-model deployment pattern, file/RAG services, access control, and clean service boundaries.  
**Do not use as proof:** that adaptive curriculum, mastery, or teacher coaching workflows are solved.

### 4. tutornew/OpenTutor: modular agentic lesson experimentation

This is unrelated to Open TutorAI CE. It is a JavaScript workspaces monorepo containing a Next.js lesson application, a Vite/Express visual workspace, mini-apps, shared TypeScript packages, and Python LiveKit agent services ([repository README](https://github.com/tutornew/OpenTutor#project-structure)). The visual workspace has a module registry and modules split into manifest, runtime, server, and UI files, including lesson, exercise-sheet, mental-math, and evaluation components ([module tree](https://github.com/tutornew/OpenTutor/tree/main/apps/opentutor/modules/src/modules)). This is a useful example of activities as composable modules rather than one universal chat screen.

Its Docker Compose documentation is explicitly a lightweight local **development** stack. It runs several web apps, agents, and LiveKit, stores user data in a mounted directory, and still requires a Gemini/Google API key for Gemini-backed features ([deployment guide](https://github.com/tutornew/OpenTutor/blob/main/DEPLOYMENT.md)). There is no license file in the repository and no GitHub-detected license.

**Reference:** modular activity manifests, lesson runtime/session design, and the split between lesson UI and agent services.  
**Do not adopt yet:** code, because permission is not established; nor the whole multi-service/real-time stack before a classroom need establishes that complexity.

### 5. Studyield: broad feature coverage, but not the claimed statistical foundation

Studyield is a React frontend plus a NestJS backend organized into many feature modules: content, knowledge base, learning paths, quiz, exam clone, teach-back, problem-solver agents, analytics, research, storage, and infrastructure adapters ([backend module tree](https://github.com/studyield/studyield/tree/main/backend/src/modules)). Its Compose topology adds PostgreSQL, Redis, Qdrant and ClickHouse, making self-hosting possible but operationally much larger than a simple pilot ([Docker Compose](https://github.com/studyield/studyield/blob/main/docker-compose.yml)).

The current learning-path service asks an LLM to generate ordered steps and computes progress as the percentage of steps marked complete. Analytics reports counts, streaks and average quiz score. The AI service is currently centered on OpenRouter with direct OpenAI fallback ([learning-path service](https://github.com/studyield/studyield/blob/main/backend/src/modules/learning-paths/learning-paths.service.ts), [analytics service](https://github.com/studyield/studyield/blob/main/backend/src/modules/analytics/analytics.service.ts), [AI service](https://github.com/studyield/studyield/blob/main/backend/src/modules/ai/ai.service.ts)). No BKT, IRT, knowledge tracing, or comparable learner-state algorithm was found in these primary source paths. “Adaptive” and “mastery” should therefore be treated as product claims, not an established statistical layer.

There is also a material license inconsistency: the current [`LICENSE`](https://github.com/studyield/studyield/blob/main/LICENSE) is GNU AGPL v3, while the [README](https://github.com/studyield/studyield#studyield) displays and describes Apache-2.0. The license file and GitHub metadata should govern any preliminary risk assessment, but this should be clarified with the maintainers before reuse.

**Reference:** feature/module decomposition, knowledge-base flow, teach-back experience, and exam-oriented UI ideas.  
**Do not adopt wholesale:** before operational scope and AGPL obligations are deliberately accepted; do not use its completion percentage as the learner model.

### 6. Open edX: mature host platform, high operational gravity

The central `openedx-platform` repository is a Django/Python modular monolith containing two main services: Studio (CMS authoring) and the LMS. The wider platform includes independently deployed applications and React micro-frontends ([platform repository documentation](https://docs.openedx.org/projects/edx-platform/en/latest/references/docs/README.html), [architecture overview](https://docs.openedx.org/en/latest/developers/references/developer_guide/architecture.html)). The repository is [AGPL-3.0](https://github.com/openedx/openedx-platform/blob/master/LICENSE).

Its strength is its mature set of seams. Official documentation lists REST integration, LTI, XBlocks, Django app plugins, hooks, design/theming mechanisms, and frontend plugin slots. It recommends LTI when a learning tool should work across more than one LMS ([extension options](https://docs.openedx.org/projects/edx-platform/en/latest/concepts/extension_points.html)). Production self-management is possible, but the project explicitly says installation is not simple and recommends the community-supported Docker distribution Tutor ([platform README](https://docs.openedx.org/projects/edx-platform/en/latest/references/docs/README.html)).

**Potentially adopt later:** institutional course/identity/authoring infrastructure, LTI integration, or XBlocks if the school's context points there.  
**Do not assume now:** that its course-oriented data model is the right shell for a responsive, cross-unit mastery path. The operational cost and upgrade surface are large relative to proving one AA SL learning loop.

### 7. Kolibri: strong offline/content/coach architecture

Kolibri is an MIT-licensed, offline-first learning platform. A server can be installed on several operating systems and accessed by ordinary browsers on Windows, macOS, Linux, Android and iOS over a local network ([repository](https://github.com/learningequality/kolibri), [server/client guide](https://kolibri.readthedocs.io/en/latest/access/access_lan.html)).

Its backend deliberately separates core services—authentication, content, logging, tasks and device management—from optional plugins such as Learn, Coach and Facility. Plugins are Django apps loaded through a defined `kolibri_plugin` module and hooks; frontend applications are also plugin-based Vue single-page applications ([plugin architecture](https://kolibri-dev.readthedocs.io/en/latest/backend_architecture/plugins.html), [single-page application architecture](https://kolibri-dev.readthedocs.io/en/develop/frontend_architecture/single_page_apps.html)). This is a mature example of keeping durable platform capabilities separate from workflows.

One constraint matters for integration: Kolibri explicitly warns that most endpoints are internal and unstable; only `/public/` APIs carry backward-compatibility expectations ([backend API stability notice](https://kolibri-dev.readthedocs.io/en/latest/backend_architecture/index.html)).

**Adopt/reference:** offline-capable delivery, content-channel concepts, activity logging, coach workflows, and plugin boundaries.  
**Use as host only if justified:** by offline/LAN or content-distribution needs. It does not remove the need for an AA SL competency/mastery service.

### 8. STACK: mature mathematics checking as a bounded service

STACK is a long-running automatic mathematics assessment system. Its main form is a Moodle question type, with an ILIAS integration and a stated API for standalone third-party use. The repository contains answer/input logic, Potential Response Trees, libraries, authoring/admin tooling, tests, and Moodle integration surfaces ([repository README](https://github.com/maths/moodle-qtype_stack)). It uses Maxima for mathematical properties and can run Maxima separately through GoeMaxima/MaximaPool; official installation guidance targets Linux and documents supported Moodle versions ([installation guide](https://github.com/maths/moodle-qtype_stack/blob/master/doc/en/Installation/index.md)).

The pedagogically useful layer is deeper than final-answer equality: typed mathematical expressions, validation separate from assessment, structured randomization, multipart items, units, line-by-line inputs, and authored response logic. The bundled library currently advertises more than 4,200 tested questions, including algebra refresher material ([official documentation](https://github.com/maths/moodle-qtype_stack/blob/master/doc/en/index.md), [question library](https://github.com/maths/moodle-qtype_stack/blob/master/doc/en/STACK_question_admin/Library/index.md)).

Code is GPL-3.0; documentation and bundled sample questions/materials are CC BY-SA 4.0 ([license statement](https://github.com/maths/moodle-qtype_stack#license)).

**Trial first:** wrap its standalone API or an existing Moodle instance behind a small “render/check response” contract.  
**Adopt selectively:** AA SL item templates and deterministic feedback patterns with correct attribution/share-alike handling.  
**Avoid:** coupling the learner model directly to Moodle/STACK internals; mastery belongs in a separate layer.

### 9. WeBWorK: separate the renderer from the course-management system

“WeBWorK” refers to several repositories, not one component:

- `webwork2` is the full course-management/homework application;
- `renderer` is a smaller Mojolicious/Perl service derived from WeBWorK2;
- `webwork-open-problem-library` is the independently mounted content collection.

The renderer has a Docker recipe and accepts raw PG, a library path, or a problem URL plus a seed. It can return HTML or JSON and wraps problem/session/answer state in JWTs, including submitted answer text/LaTeX, attempts and score ([renderer README and API](https://github.com/openwebwork/renderer#renderer-api)). This is a credible integration seam because it is explicitly user-agnostic and expects another system to own the learner/problem identity and persistence.

The OPL separates `Contrib`, `Pending`, and the editorial `OpenProblemLibrary` ([OPL README](https://github.com/openwebwork/webwork-open-problem-library)). Its default content license is CC BY-NC-SA 3.0, but individual contributions may specify alternatives, so a blanket “open content” assumption is unsafe ([OPL license](https://github.com/openwebwork/webwork-open-problem-library/blob/main/OPL_LICENSE)).

**Trial:** the standalone renderer as a deterministic, randomized item engine.  
**Curate:** only individually reviewed, license-compatible, AA-SL-relevant OPL items, with a provenance manifest.  
**Do not adopt automatically:** the full WeBWorK course application or assume renderer scores constitute mastery.

### 10. pyBKT: a focused learner-model component

pyBKT is an MIT-licensed Python library rather than a platform. It consumes ordered student, skill, item/resource and correct/incorrect observations from DataFrames or CSV/TSV; it fits and predicts classic BKT and variants for per-student priors, item-specific guess/slip, learning, forgetting, and resource classes. Its `Roster` API can retain the current state for a cohort ([repository and usage documentation](https://github.com/CAHLR/pyBKT)).

This narrowness is an advantage: it can sit behind a technology-neutral learner-state contract while the web application, event store, item engine, and teacher dashboard remain independent.

**Adopt for experiments:** batch calibration and/or online state prototypes once AA SL competency tags and response events exist.  
**Do not confuse with intelligence:** it will only be as meaningful as the skill map, item tagging, parameter estimation, and evidence rules supplied to it.

## Cross-project structure worth preserving

The reusable pattern across the strongest projects is not a particular framework. It is a set of boundaries:

```text
browser experience
      |
learning-session / next-activity contract
      |
+-----+--------------------+---------------------+
| curriculum graph         | learner state       | teacher steering
| units, KCs, prerequisites| evidence + mastery  | order, dates, tests
+--------------------------+---------------------+
      |
activity adapter contract
      |
+----------------+----------------+----------------+
| native thin    | STACK         | WeBWorK PG     |
| slice items    | response API  | renderer       |
+----------------+----------------+----------------+
      |
optional AI task contract (explain, hint, draft, classify)
      |
replaceable local or remote model/provider
```

This lets the project learn from OATutor without inheriting its storage choices; use STACK/WeBWorK without making either the student system of record; and use an AI provider layer without giving an LLM authority over mastery.

## Recommended adoption sequence—not an implementation commitment

1. **Create a license/provenance catalogue before copying content.** Record source repository, exact file/item, upstream revision, author/attribution, license, modification state, and AA SL competency mapping. Keep authorized commercial textbook PDFs outside the public repository and outside any general-purpose corpus.
2. **Prototype one shared item/evidence contract.** It should accommodate a native short item, a STACK response, and a WeBWorK response without choosing the application backend.
3. **Run a small content-and-grading bake-off.** Map the same narrow AA SL/prerequisite slice across OATutor content, STACK, WeBWorK, and teacher-authored examples; compare coverage, authoring effort, feedback quality, mobile/browser behavior, and licensing.
4. **Prototype mastery independently.** Replay the resulting event data through OATutor-style BKT and pyBKT. Keep “assessment readiness” and scheduled unit scope outside the mastery probability.
5. **Evaluate host shells only after the learning loop is credible.** Compare a thin custom web shell with Open edX/Kolibri integration using the same contracts. The existence of a mature LMS is not evidence that it should own adaptive sequencing.
6. **Evaluate AI as replaceable tasks.** Open TutorAI CE offers a useful provider boundary; Open Alpha, tutornew/OpenTutor and Studyield offer interaction ideas. None establishes that an agent should be the authoritative lesson scheduler.

## Identity and license cautions

- **Open TutorAI CE** (`Open-TutorAi/open-tutor-ai-CE`) and **OpenTutor/tutor.new** (`tutornew/OpenTutor`) are unrelated. A third current repository, [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor), also uses the OpenTutor name. Always record owner/repository, not display name alone.
- **Open Alpha** in this report means `lamira-the-human/open-alpha`; unrelated repositories share similar names.
- **WeBWorK** must be cited at component level (`webwork2`, `renderer`, or OPL).
- **Open Alpha and tutornew/OpenTutor have public source but no detected license.** They are not safe reuse sources unless permission/license is added.
- **Studyield's README says Apache-2.0 while its LICENSE and GitHub metadata say AGPL-3.0.** Treat it as unresolved, provisionally AGPL, rather than choosing the more permissive label.
- Content licenses and software licenses are separate. OATutor, STACK, and WeBWorK each require content-level provenance even when the executing software's license is clear.

## Bottom line for Wayfinder

The next investigation should not select a web framework or database. It should prove that a small AA SL slice can be represented as a prerequisite/KC graph, served through interchangeable activity engines, converted into trustworthy evidence, and updated into an interpretable learner state. The repository survey gives us credible building blocks for each of those pieces without requiring an early commitment to a monolithic platform.
