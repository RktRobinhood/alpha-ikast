# Supplied Alpha School research dump

> Preserved verbatim from the user's attachment on 2026-09-04. Claims and links have not yet been independently verified.

+Alpha School does not appear to use one magical “AI teacher.” Its current setup is closer to an adaptive-learning operating system sitting on top of a collection of specialist EdTech apps.

The central piece is TimeBack, Alpha’s proprietary platform. Students log into it each morning and see what they need to work on, their progress toward mastery, daily goals, XP, and their individual learning pathway. TimeBack uses assessment data—including NWEA MAP RIT scores—to place students at different levels by subject and then routes them into appropriate learning apps.

What they actually use
Area	Examples currently documented by Alpha
Math	Math Academy, Zearn, AlphaNumbers, Happy Numbers, AlphaMath, Math Quest, Math Cakes, Edia, TimeBack Learn
Reading	AlphaRead, AlphaPhonics, Alpha Reading Fluency, MobyMax, Literably, ReadTheory, CommonLit
Language/grammar	eGUMPP, Lalilo, Freckle, MobyMax
Vocabulary/writing	Membean, AlphaWrite, VocabLoco, Vocabulon
Science	MobyMax, Edmentum, Nice Academy, AlphaScience
Social studies	TimeBack Scroll
AI/creative skills	Teach Tales, Twin Pics
Speaking	Orai
Early reading	ChatABC
External assessment	NWEA MAP

That isn't reconstructed from press articles: Alpha's own current academic support documentation exposes much of the app ecosystem.

Interestingly, in May 2026 Alpha's co-founder explicitly published a list of 10 tools they use:

Math Academy — adaptive/mastery mathematics
Teach Tales — their AI-generated personalized reading/story platform
Twin Pics — AI prompting/prompt-engineering game
Numbio — arithmetic fluency
ChatABC — AI oral-reading tutor
Khan Academy
Membean — adaptive vocabulary/spaced repetition
eGUMPP — grammar, usage and mechanics
MobyMax — adaptive K–8 curriculum/diagnostics
Orai — automated public-speaking feedback.

The architecture is therefore approximately:

MAP/placement data → TimeBack → individualized learning pathway → specialist adaptive app → mastery data back to TimeBack → XP/progress/goals → Guide intervention when needed.

That's considerably more interesting than the marketing phrase “AI tutor.” Alpha itself says TimeBack is the proprietary layer, while much of the underlying content comes from third-party applications. Its system integrates the data from those applications so that, for example, XP earned in AlphaNumbers or Zearn is fed back into TimeBack.

And there is a major pedagogical detail: the software isn't supposed to provide six hours of digital school. Alpha says students normally spend about two hours on academics, while the adults—called Guides rather than teachers—concentrate on motivation, coaching and relationships. The rest of the day is workshops, projects, entrepreneurship, public speaking, physical activity, etc.

For what you're interested in as a teacher, I think TimeBack is actually the part worth dissecting, rather than the individual apps. The potentially replicable idea is essentially a student-facing learning dashboard that knows the curriculum, diagnoses gaps, assigns the next activity, records mastery and gives students visible progress toward freeing up their time. Most of the actual instruction can then be relatively ordinary EdTech.

I can dig further into exactly how TimeBack works—screens, mastery thresholds, XP, pacing, incentives, tests, and what Guides see—and reverse-engineer a version of the model that would make sense in an IB classroom.

Yesterday 5:47 AM
Are there videos of it

Yes. There are now some videos that show substantially more of the actual system rather than just Alpha’s marketing pitch.

The one I’d start with is “What a Two-Hour School Day Actually Looks Like.” It explicitly shows/describes students opening the TimeBack dashboard, choosing subjects, working through individualized levels, taking focus breaks, and seeing real-time progress. Alpha says the same progress view is available to students, Guides, and parents.
Watch it on Alpha’s site

Then watch “Alpha Core Skills.” Alpha has multiple versions aimed at different age groups, and these are more useful for seeing what students are physically doing during the two-hour block.

The longer explanation is this one:

That is older—July 2024, before the branding switched to TimeBack—but it explains the underlying architecture and philosophy in much more detail.

Alpha also now has an entire video library with a “timeback” filter, plus categories for “AI Apps,” “2X Learning,” and “The Model.”
Alpha School video library

There is also a TimeBack support video intended for students/parents in Alpha’s support documentation, which is potentially even more interesting because it is instructional rather than promotional.

The thing I haven’t yet found publicly is a proper 15–30 minute screen-recorded walkthrough of TimeBack Dash showing the entire student workflow: login → goals → XP → assigned app → mastery → data coming back → Guide dashboard.

That’s the video I suspect you actually want. I can specifically hunt for UI footage/screenshots of TimeBack and reconstruct how the system works screen-by-screen, rather than looking at general Alpha videos.

Is there any open source initiatives trying to bring this type of edtech to everyone that's kind of a free option I'm also curious on the side to some AI frameworks like swamp club or something else could be used to make this parking system using AI for development

Yes. The open-source ecosystem is considerably closer to an “Alpha School for everyone” than I expected. The pieces exist; what is largely missing is the TimeBack-style orchestration layer that joins them into one coherent student experience.

The projects I would actually investigate
Project	How close to Alpha?	Maturity	Why it matters
Open Alpha	★★★★★	Early	Literally describes itself as inspired by Alpha School’s 2-hour model
OATutor	★★★★☆	Strong/research-proven	Real adaptive mastery engine using Bayesian Knowledge Tracing
Open TutorAI	★★★★☆	Developing	Full self-hosted classroom AI platform: students, teachers, parents
OpenTutor / tutor.new	★★★☆☆	Very new	Agentic AI teachers and tutoring orchestration
Studyield	★★★☆☆	Developing	Knowledge graphs, learning paths, adaptive assessment, multi-agent solving
Open edX	★★★☆☆	Very mature	Excellent open platform underneath everything, but needs an adaptive layer
Kolibri	★★☆☆☆	Very mature	Excellent free/offline learning infrastructure, less Alpha-like

The remarkable one is Open Alpha. It isn't merely similar; its repository explicitly says it is an “open source AI-powered education platform inspired by Alpha School's 2-hour learning model.” Students choose Math, Reading or Science, work with an AI tutor, take short mastery quizzes, and unlock subsequent concepts after scoring at least 80%. Parents get a separate dashboard and AI coach. The current stack is React/Vite + Turso + an LLM gateway.

Open Alpha on GitHub

I would not, however, build your project directly around Open Alpha yet. It's useful as a reference implementation, but it is relatively young.

OATutor is potentially the important bit

OATutor is much more academically interesting. UC Berkeley researchers developed it specifically because most serious adaptive-tutoring technology was proprietary. It has been classroom field-tested and includes:

Bayesian Knowledge Tracing → skill mastery estimates → adaptive problem selection → mastery progression.

It also includes LTI integration, A/B testing, open algebra content and an MIT-licensed codebase. The underlying system was published at CHI 2023 after three years of iterative development and classroom trials.

That is much closer to the actual intelligence underneath TimeBack than merely attaching ChatGPT to an LMS.

For example:

Student answers quadratic question incorrectly.

A weak AI system says:

“Here is an explanation of quadratics.”

An OATutor-style system updates something closer to:

Student
│
├── Linear equations          0.96 mastery
├── Factorisation             0.82
├── Expanding brackets        0.91
├── Zero-product property     0.48  ← problem
└── Quadratic modelling       0.37

The system can therefore make a defensible decision about what comes next.

OATutor already implements that sort of selection using Bayesian Knowledge Tracing and configurable problem-selection heuristics.

OATutor

Then there is Open TutorAI

This one may be the most convenient starting point for actually deploying something.

Open TutorAI Community Edition is self-hostable, BSD-3-Clause licensed and explicitly provides student, teacher and parent experiences. Their Docker deployment supports Ollama as well as OpenAI-compatible APIs, which means you can run the AI locally rather than necessarily paying an API provider.

Open TutorAI

There's also another unrelated project called OpenTutor / tutor.new, which describes itself as an open platform for orchestrating and automating AI-powered teachers, including Python agent services. It is interesting architecturally but extremely young.

And Studyield has gone surprisingly far in another direction: AI-generated learning paths, knowledge graphs, adaptive assessments, teach-back evaluation, RAG and multi-agent problem solving, all self-hostable.

And yes: Swamp Club

You remembered the name correctly.

Swamp Club is an open-source AI-oriented automation framework. Its central abstractions are typed Models, YAML-defined workflows, secrets vaults and immutable/versioned data. The interesting feature is that it has explicitly been designed so AI coding agents can operate the framework rather than requiring a human to manually configure everything.

Swamp Club

But I would make an important distinction:

I would use Swamp to build and maintain the educational system. I would not use Swamp as the educational system itself.

For example, Swamp could be extremely useful for:

IB curriculum PDF
        ↓
AI extracts syllabus concepts
        ↓
AI proposes competency graph
        ↓
AI generates question candidates
        ↓
AI verifies answers
        ↓
AI checks difficulty / prerequisites
        ↓
teacher approves
        ↓
questions enter item bank
        ↓
nightly analytics inspect student results
        ↓
flag suspicious/bad questions

Those are exactly the kinds of repeatable, versioned, auditable workflows Swamp is designed around.

That's a good place for agents.

I wouldn't let an LLM decide:

"Matt understands differentiation now."

Instead:

Student evidence
      ↓
deterministic mastery model
      ↓
mastery probability
      ↓
prerequisite graph
      ↓
next activity

Then let AI operate around that deterministic core.

An open-source TimeBack

If we were designing this from scratch now, I would actually make it something like this:

                         OPEN TIMEBACK
┌────────────────────────────────────────────────────────────┐
│                    STUDENT DASHBOARD                       │
│                                                            │
│   TODAY                                                    │
│   Mathematics  ███████░░  72%     Continue →              │
│   Psychology   █████████  91%     Mastered ✓              │
│   TOK          █████░░░░  54%     Continue →              │
│                                                            │
│   Focus: 1 h 14 min       XP: 840        Streak: 6 days   │
└───────────────┬────────────────────────────────────────────┘
                │
                ▼
┌────────────────────────────────────────────────────────────┐
│                    MASTERY ENGINE                          │
│                                                            │
│              Competency knowledge graph                    │
│                         +                                  │
│           Bayesian Knowledge Tracing                       │
│                         +                                  │
│                 spaced retrieval                           │
│                                                            │
│             "What should Matt do next?"                    │
└───────────────┬────────────────────────────────────────────┘
                │
       ┌────────┼──────────┬───────────────┐
       ▼        ▼          ▼               ▼
   AI Tutor   Quiz      Simulation     External tool
              Engine                    via LTI
       │        │          │               │
       └────────┴──────────┴───────────────┘
                         │
                         ▼
                  LEARNING EVENTS
                         │
                         ▼
                mastery recalculated

There is actually a standards-based way to do almost all of this.

QTI can represent the assessment/question bank. LTI can connect external applications and return results. Caliper Analytics can normalize events coming from different learning tools. 1EdTech explicitly describes Caliper as enabling consolidated learning activity data and even real-time curriculum personalization.

So you don't have to invent proprietary equivalents of Alpha's integrations.

The AI framework I would choose

I wouldn't use an elaborate “society of 15 autonomous agents.”

For this application I currently favour:

PydanticAI + PostgreSQL + a deterministic mastery engine.

PydanticAI now supports durable agent execution through Temporal, DBOS, Prefect and Restate, including long-lived workflows and human-in-the-loop execution.

Alternatively LangGraph is a solid choice if we want explicit graph-based agent workflows; it supports persistence, streaming and debugging.

And if reliability became critical, Temporal could sit underneath everything. It's specifically built so long-running workflows survive failures and resume from where they stopped.

So my stack would roughly be:

React / Next.js
       │
       ▼
FastAPI
       │
 ┌─────┴────────────┐
 │                  │
 ▼                  ▼
PydanticAI      Mastery Engine
AI tutor         BKT / IRT
 │                  │
 └──────┬───────────┘
        ▼
   PostgreSQL
        │
        ├── students
        ├── competencies
        ├── evidence
        ├── mastery
        ├── activities
        └── learning events

Local AI:
Ollama / vLLM
        │
        ▼
Qwen / Gemma / Llama etc.

Development automation:
Swamp Club

And the AI model can be replaceable. The core educational data isn't trapped inside Claude, GPT or Gemini.

Where this gets particularly interesting for you

I don't think the killer open-source project is “free Khanmigo.”

I think it's:

An open-source TimeBack.

The system doesn't need to own all the teaching material.

It needs to know:

what the student knows → what they should learn next → what evidence would demonstrate mastery → which available resource is best for obtaining that evidence.

That means it could orchestrate existing resources rather than replacing them.

For Math, for example:

Functions
   │
   ├── notation ✓
   ├── domain/range ✓
   ├── inverse functions 67%
   │       │
   │       └── recommend BTC task 4
   │
   └── transformations 31%
           │
           ├── watch explanation
           ├── interactive graph
           └── mastery check

And this is much more achievable now than building an LMS from scratch. OATutor has already solved a large chunk of the adaptive-learning mathematics; Open TutorAI has already solved substantial portions of the AI classroom infrastructure; Open edX has solved LMS interoperability; the 1EdTech standards solve much of the integration problem; and Swamp/PydanticAI/LangGraph give us mature tools for AI-assisted development and orchestration.

The missing product is essentially the beautiful, student-friendly pacing/mastery layer joining them together.

I think that is a legitimately interesting open-source project rather than just another AI-teacher wrapper.

