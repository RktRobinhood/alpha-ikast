# Structured mathematics input and whole-class feedback capacity

**Research date:** 2026-09-08  
**Question:** [Validate structured math input and whole-class feedback capacity](https://github.com/RktRobinhood/alpha-ikast/issues/16)  
**Status:** primary-source comparison and test definition. No production infrastructure is selected, no editor or grader was built, and no student data was used.

## Decision recommendation

Keep the unchanged **Numbas** input-and-marking experience as the first AA SL baseline and test its browser-side path on the school's actual devices. It already accepts algebraic expressions, previews their interpretation, checks value equivalence and required form, and returns immediate authored feedback in the learner's browser. That is the smallest established path from the resolved quadratic-workflow investigation, and it avoids making a shared checking service the bottleneck for ordinary class practice.

Treat **MathLive as an optional input component, not an assessment engine**. It is a strong candidate if the Numbas trial demonstrates that plain JME entry is a concrete usability or notation barrier, but its LaTeX/MathJSON output is not Numbas JME and its Compute Engine comparisons are not a drop-in replacement for an authored assessment policy. Do not add a translation layer speculatively.

Keep **STACK's stateless API** as the first server-side comparison for AA SL responses that need CAS-backed validation, form-sensitive answer tests, multipart reasoning, or response-specific feedback beyond the verified Numbas baseline. Keep the **WeBWorK standalone renderer** as a second server-side comparison where an existing PG problem or its rendering contract has a specific advantage. Both must pass the synthetic whole-class test below on a school-controlled test host before either is relied on for live feedback.

Use **Open Alpha only as the surrounding learner journey**. At the inspected revision it presents multiple-choice quizzes, compares option letters in the browser, and accepts a client-computed aggregate score; it has no structured mathematics input or deterministic algebra checker. Its optional AI tutor and generated quiz path must remain outside authoritative checking. Its missing repository licence still prevents code reuse without permission.

## Evidence status and limits

This report distinguishes three kinds of statements:

- **Verified upstream fact** means the cited upstream documentation or pinned source says or implements it.
- **Observed fact** means the earlier local trial recorded in [Start with existing learning workflows](upstream-first-learning-loop.md) exercised it. That trial demonstrated behaviour, not load capacity.
- **Hypothesis / proposed test condition** means it still needs a controlled trial. One exploratory MathLive Compute Engine microbenchmark was run on the discovery workstation, but no comparable Numbas, STACK, WeBWorK, Open Alpha, browser-device, or production-like latency, throughput, CPU, or memory benchmark was run. Upstream configuration examples and qualitative performance advice are not measurements of this school's workload.

The conclusion is therefore a **validation order**, not a claim that any server-side engine already supports a whole class on unspecified hardware.

## Pinned upstream revisions and reuse boundary

Revisions were read from each upstream repository's default branch on 2026-09-08.

| Component | Pinned revision | Verified code licence | Reuse boundary |
| --- | --- | --- | --- |
| [Numbas runtime](https://github.com/numbas/Numbas/tree/0f0ea3337196cb8e98d4edf04f1afaedc8cf8df5) | `0f0ea3337196cb8e98d4edf04f1afaedc8cf8df5` | [Apache-2.0](https://github.com/numbas/Numbas/blob/0f0ea3337196cb8e98d4edf04f1afaedc8cf8df5/LICENSE) | Runtime licence does not license third-party questions or media. Keep item-level provenance.
| [MathLive and Compute Engine](https://github.com/arnog/mathlive/tree/c952a2048049673891afd2b7b3714cd63855a9f0) | `c952a2048049673891afd2b7b3714cd63855a9f0` | [MIT](https://github.com/arnog/mathlive/blob/c952a2048049673891afd2b7b3714cd63855a9f0/LICENSE.txt) | Library licence does not decide the licence of authored tasks or expected answers.
| [STACK](https://github.com/maths/moodle-qtype_stack/tree/6df3a710a4665594056b686ddc133eb7635cfd87) | `6df3a710a4665594056b686ddc133eb7635cfd87` | [GPL-3.0](https://github.com/maths/moodle-qtype_stack/blob/6df3a710a4665594056b686ddc133eb7635cfd87/COPYING.txt) | Software, documentation, and bundled/sample question material have distinct terms; preserve question provenance.
| [WeBWorK webwork2](https://github.com/openwebwork/webwork2/tree/e47434b00318c509f8774aca8f05503463f53ce8) | `e47434b00318c509f8774aca8f05503463f53ce8` | [GPL-2-or-later **or** Artistic-1.0](https://github.com/openwebwork/webwork2/blob/e47434b00318c509f8774aca8f05503463f53ce8/LICENSE) | The application licence does not automatically cover OPL content.
| [WeBWorK standalone renderer](https://github.com/openwebwork/renderer/tree/1134ffbbf5e656148e579f424f70bcd9f1d15936) | `1134ffbbf5e656148e579f424f70bcd9f1d15936`; PG submodule `4b3e564cf4e5a36807ca5a341734f8d604e8b77d` | [GPL-3.0](https://github.com/openwebwork/renderer/blob/1134ffbbf5e656148e579f424f70bcd9f1d15936/LICENSE.md) | Mount only original or permission-cleared PG content; OPL's default content terms are a separate decision.
| [Open Alpha](https://github.com/lamira-the-human/open-alpha/tree/965f8a096cd1f10e15cdefb5ee466b5098ed1332) | `965f8a096cd1f10e15cdefb5ee466b5098ed1332` | **No repository licence found** | Public source is inspectable but not reusable without permission.

## Capability comparison

| Capability | Numbas | MathLive | STACK | WeBWorK renderer / webwork2 | Open Alpha |
| --- | --- | --- | --- | --- | --- |
| Structured input | Text JME expression with interpreted mathematical preview; separate number, matrix, gap-fill and other part types. | Rich `<math-field>` web component; physical/virtual keyboard; emits LaTeX and MathJSON and supports named editable prompts. | Algebraic, numerical, matrix, multiline, multiple-choice and other input types; validation shows the interpreted answer before grading. | PG answer blanks and answer evaluators support numerical, formula and other authored response types; renderer returns interactive HTML or JSON. | Multiple-choice option strings only in the current quiz component.
| Deterministic checking | Browser-side JME marking; samples values for expression equivalence and can impose form patterns or custom authored marking. | Browser-side structural, arithmetic, and identity comparisons; arithmetic/identity comparisons can be undetermined and identity may use sampling. This is a toolkit, not an AA SL marking policy. | Server-side Maxima plus explicit answer tests and Potential Response Trees (PRTs); can distinguish equivalence, form and other properties. | Server-side PG answer evaluators; problem source defines checking and feedback. | Browser compares the selected option letter with `correctAnswer`; the server accepts the browser's aggregate score. This is deterministic only for MCQ presentation, not trustworthy algebra evidence.
| Feedback, hints, retries | Immediate marking feedback, warnings, alternative answers, adaptive marking, advice/reveal settings and authored steps; the prior trial observed retries and hints. | Provides parse diagnostics and UI states for correct/incorrect prompts; hint and retry policy belongs to the host application. | Input validation, answer-test outcomes and PRT branches provide response-specific feedback; Moodle behaviour controls attempts, penalties and hints. | Preview/check buttons and PG problem feedback; hints/solutions and attempt policy depend on problem and host configuration. | Shows one explanation after each MCQ choice and allows a new quiz later; AI chat may provide hints, but is separate and non-deterministic.
| Embedding seam | Self-contained static/SCORM package or a `<numbas-exam>` custom element; optional LTI provider for launches and stored attempts. | npm/ES module, UMD script, or web component inside any host page. | Moodle/ILIAS plugin, LTI route, or Docker-oriented stateless JSON API with `/render`, `/validate`, and `/grade`. | Docker/local renderer with a POST `/render-api`; `formURL` can point through a host. Full webwork2 is a course/homework application. | Route-level React/Vercel application; no established maths-engine adapter in the inspected source.
| Where checking load runs | Learner browser for ordinary Numbas runtime marking. | Learner browser when used as documented. | Shared server and Maxima service. | Shared renderer/webwork2 server and PG process. | MCQ comparison in browser; database writes and uncached AI generation on shared external services.
| Accessibility evidence | Upstream runtime ACR says the default v7.1 theme satisfies WCAG 2.1 AA; author content, extensions, LTI and editor are out of scope. | Keyboard navigation, screen-reader MathML/speakable output and accessible menu are documented, but no upstream conformance report was found in this review. | Upstream guidance covers keyboard/screen-reader use and author responsibilities; equation input remains linear syntax unless a separate input widget is added. No product-wide conformance claim should be inferred. | Current guide documents labelled answer blanks, accessible navigation and MathJax 4, while identifying inaccessible PDFs and author-dependent problem gaps. | No upstream accessibility statement or conformance report was found; the quiz source alone is not evidence of accessibility.
| Self-hosting | Static files can be school-hosted; editor and LTI provider are separately self-hostable. | Package files can be served with the host; no service is required for input or Compute Engine checks. | Moodle/ILIAS or the standalone API plus a Maxima service can be school-hosted; greater operational surface. | Docker or local renderer is documented; full webwork2 is also self-hostable. | README describes local development but production around Vercel, Turso and ATXP; code reuse is blocked by missing licence.
| Whole-class responsiveness | **Strong hypothesis for ordinary feedback** because checks run per browser; shared static delivery and persistence still require measurement. | **Strong hypothesis for input responsiveness** because parsing/checking is local; must measure on representative low-spec devices. | **Unproven** and question-dependent. CAS sessions, number of inputs/PRTs, randomisation and deployment choices affect latency. | **Unproven** and problem-dependent. Every render/check request reaches shared PG infrastructure. | Stored MCQs should be relatively light, but uncached AI generation is explicitly described upstream as 15–30 seconds; neither path is a structured-math solution.

## What the primary sources establish

### Numbas: complete baseline with browser-local marking

Numbas mathematical-expression parts accept JME syntax, show a rendered preview of how an answer was interpreted, compare expected and submitted expressions over sampled variable values, and can enforce a required form with pattern restrictions. The author controls checking tolerance, sample range/points, penalties and feedback. These are established activity behaviours, not a new grader design ([mathematical-expression documentation](https://docs.numbas.org.uk/en/latest/question/parts/mathematical-expression.html), [question-part and custom-marking reference](https://docs.numbas.org.uk/en/latest/question/parts/reference.html)).

The runtime can be embedded as a `<numbas-exam>` custom element loaded from a self-contained exam package. The upstream page warns that multiple embedded exams must not compete for one SCORM API, which is a concrete integration constraint if Open Alpha hosts more than one activity on a page ([embedding guide](https://docs.numbas.org.uk/en/latest/embedding.html)). The runtime's security model deliberately performs marking in the browser, so answers should not be treated as secure high-stakes assessment evidence; that trade-off is acceptable for the ticket's low-stakes independent probes and guided practice but must remain explicit ([security guide](https://docs.numbas.org.uk/en/latest/security.html)).

The upstream accessibility conformance report covers the default runtime theme, not authored content, extensions, the editor or LTI provider. It reports WCAG 2.1 AA conformance for runtime v7.1 and records the browsers and assistive technology used in its September 2023 evaluation ([Numbas ACR](https://docs.numbas.org.uk/en/latest/accessibility/exam-vpat.html)). AA SL items still need keyboard, screen-reader, zoom/reflow and mathematical-language review because authoring can reintroduce barriers.

### MathLive: high-quality structured entry, intentionally separable from policy

MathLive exposes a `<math-field>` element, touch virtual keyboard, keyboard commands and value formats including LaTeX and MathJSON. Named prompts provide multipart fill-in-the-blank fields, while the Compute Engine can parse the result and emit diagnostics ([integration guide](https://mathlive.io/mathfield/guides/integration/), [fill-in-the-blank guide](https://mathlive.io/mathfield/guides/fill-in-the-blank/), [Compute Engine API](https://mathlive.io/compute-engine/api/)). It can be packaged locally rather than loaded from a CDN.

The Compute Engine distinguishes syntactic sameness, arithmetic equality and identity. Arithmetic and identity comparisons can be undetermined, and identity checking can use pseudo-random sampling; exact, approximate and form-sensitive AA SL outcomes therefore need authored policy and test cases rather than a blanket `isEqual()` call ([comparison semantics](https://mathlive.io/compute-engine/guides/symbolic-computing/), [core identity semantics](https://mathlive.io/compute-engine/reference/core/)). MathLive is consequently a plausible accessible input seam, not evidence that a new browser grader should replace Numbas or STACK.

An exploratory local microbenchmark used `@cortex-js/compute-engine` 0.126.2 on Node 24.14.0. Across 5,000 repeated comparisons drawn from five quadratic-equivalence pairs, module import plus engine initialization took 291 ms; comparison p50 was 0.335 ms, p95 1.421 ms, and p99 2.937 ms; process RSS grew by about 139 MiB over the run. These figures describe one warm desktop process, not a browser, school device, shared service, or production capacity test. More importantly, `isEqual()` returned `undefined` for four of five representative equivalences; `isIdenticallyEqual()` returned true for all five. Malformed LaTeX produced a structured expression containing error nodes rather than a thrown error. A real integration would therefore need explicit parse-error handling, three-valued result handling, a policy for sampling, and regression cases for false positives and false negatives. The result supports MathLive as an input candidate, not as an authoritative checker.

### STACK: deepest response-specific algebra checking, with a real service boundary

STACK separates input validation from assessment and uses explicit answer tests and Potential Response Trees to assign marks and feedback based on mathematical properties. This supports algebraic equivalence, required form and multipart reasoning more directly than a generic equality check ([input overview](https://docs.stack-assessment.org/en/Authoring/Inputs/), [answer tests](https://docs.stack-assessment.org/en/Authoring/Answer_Tests/), [Potential Response Trees](https://docs.stack-assessment.org/en/Authoring/Potential_response_trees/)). Moodle supplies attempt, penalty and hint behaviour when STACK is used as its question type.

The repository's standalone API is not hypothetical: it documents stateless JSON `/render`, `/validate`, `/grade`, `/test`, `/download` and `/diff` routes, with Docker deployment and a separate HTTP Maxima service. Its example sets `GOEMAXIMA_QUEUE_LEN` to 32, but that is a configuration example—not proof that 32 simultaneous classroom requests meet a latency target ([STACK API README at the pinned revision](https://github.com/maths/moodle-qtype_stack/blob/6df3a710a4665594056b686ddc133eb7635cfd87/api/README.md)).

Upstream performance guidance says deployed variants improve caching, randomisation loops can produce unpredictable runtimes and timeouts, input count increases CAS sessions, and older versions incurred a CAS session per PRT. The installation guide says optimized Maxima images are required for production and points to pooling to smooth startup overhead ([performance notes](https://docs.stack-assessment.org/en/STACK_question_admin/Notes_about_performance/), [optimising Maxima](https://docs.stack-assessment.org/en/Installation/Optimising_Maxima/)). This makes item shape part of the load-test fixture; a trivial one-input question cannot stand in for a structured reasoning task.

### WeBWorK: mature PG checking and a smaller renderer seam

The standalone renderer accepts problem source/path plus a deterministic seed through POST `/render-api`, can return HTML or JSON, and exposes preview/check controls. Its `formURL` may be redirected through a surrounding application, giving Open Alpha an integration seam without adopting all of webwork2 ([renderer API README at the pinned revision](https://github.com/openwebwork/renderer/blob/1134ffbbf5e656148e579f424f70bcd9f1d15936/README.md)). The renderer pins the PG engine at revision `4b3e564cf4e5a36807ca5a341734f8d604e8b77d`; both engine and exact problem revision belong in every result record.

The current WeBWorK accessibility guide usefully separates the web application, PG renderer and authored problem. It documents labelled answer blanks, keyboard-oriented navigation and MathJax 4, but warns that PDFs and individual/legacy problem content may be inaccessible ([WeBWorK accessibility guide](https://github.com/openwebwork/webwork2/blob/e47434b00318c509f8774aca8f05503463f53ce8/doc/AccessibilityGuide.md)). A renderer embedded in another application does not inherit the full webwork2 course shell's accessibility automatically.

### Open Alpha: orchestration shell, not the checker

At the pinned revision, Open Alpha's quiz component renders four option buttons, compares the chosen letter with a supplied `correctAnswer`, reveals an explanation, and computes the aggregate score in React. Its submit endpoint trusts the client-provided score, retains the highest score and calls 80% complete ([quiz component](https://github.com/lamira-the-human/open-alpha/blob/965f8a096cd1f10e15cdefb5ee466b5098ed1332/frontend/src/components/Quiz.tsx), [submission route](https://github.com/lamira-the-human/open-alpha/blob/965f8a096cd1f10e15cdefb5ee466b5098ed1332/api/tutor/quiz/submit.ts)). The quiz endpoint returns five stored questions when available; otherwise it asks an external LLM to generate them ([quiz route](https://github.com/lamira-the-human/open-alpha/blob/965f8a096cd1f10e15cdefb5ee466b5098ed1332/api/tutor/quiz.ts)). The README reports 15–30 seconds for first-time generated lesson content, but that is upstream-reported rather than locally measured ([Open Alpha README](https://github.com/lamira-the-human/open-alpha/blob/965f8a096cd1f10e15cdefb5ee466b5098ed1332/README.md)).

These facts identify the clean seam: Open Alpha may launch or embed a permission-cleared deterministic activity and consume its bounded result. AI chat can explain or offer formative help, but it must not decide correctness, define subject competencies, or update school-controlled calibration.

## Representative synthetic whole-class test

The test should compare **unchanged upstream paths** before any adapter or production design is selected. Use only original AA SL fixtures and synthetic learner IDs.

### Cohort and workload

Use 32 virtual learners, representing one full class, plus one teacher dashboard reader. Run the same three permission-cleared quadratic fixtures in every engine:

1. one expression-equivalence input, such as an expanded quadratic;
2. one required-form input, such as factorised form, including a valid but wrong-form response; and
3. one two-input structured reasoning task, such as discriminant followed by root interpretation.

Each learner performs this ten-minute sequence with a fixed random seed: load/render; enter malformed input and request validation/preview; submit a mathematically wrong answer; reveal one authored hint where the engine supports it; retry correctly; load the next variant. Start all learners over a ten-second ramp, then synchronize one validation burst and one submission burst of 32 requests. Repeat with warm caches, cold application processes, and one deliberately expensive but author-approved fixture. Do not call an LLM.

For Numbas and MathLive, run real headless browsers under a representative low-spec school-device CPU/network profile and measure both browser work and the static/persistence endpoints. For STACK and WeBWorK, drive the documented HTTP routes while browsers exercise the rendered controls. Keep fixture semantics and response sequence equivalent; do not force byte-identical protocols.

### Measurements to record

| Layer | Required measurement |
| --- | --- |
| Browser | package bytes transferred (cold/warm), time to usable input, input-event duration, parse/preview/check p50/p95/p99, long tasks, peak JS heap, and whether the page stays keyboard/screen-reader operable under load |
| Shared service | request rate, queue depth, p50/p95/p99 for render/validate/grade/persist, response bytes, CPU, resident memory, process count, cache state and saturation point |
| Correctness | normalized outcome, partial-credit/feedback branch, seed, engine revision, item revision, and zero cross-learner state leakage |
| Reliability | HTTP/error rate, timeout count, malformed-input behaviour, worker crash/restart behaviour, duplicate-submit behaviour and recovery time |
| School network | client-observed latency and transfer volume with the test host reached through the same network path intended for the pilot |

Store raw, timestamped machine-readable results beside the test plan only when the benchmark is actually run. Record host CPU/RAM/OS, container/process limits, browser version, network shaping, cache state, worker/pool configuration and exact commands. Without that context, a latency number is not reusable evidence.

### Provisional acceptance questions, not adopted requirements

The teacher and operator should confirm the acceptable feedback delay and failure budget before the trial. A useful first hypothesis to test is that ordinary validation and checking should feel immediate (provisionally p95 at or below one second and p99 below three seconds during both 32-request bursts), with no mathematically incorrect result, no lost accepted submission and no cross-learner leakage. These are **proposed trial thresholds**, not measured facts or a production service-level objective.

The failure drill should stop one checking worker during the synchronized burst. A safe result is an explicit retryable failure with no fabricated grade, followed by recovery without duplicate evidence. Browser-local engines should also be tested with persistence unavailable: they may continue formative checking, but the UI must not imply that the observation was saved.

## AA SL gaps that remain after this research

- Validate the actual notation set for the first AA SL slice: equations versus expressions, factorised/expanded form, inequalities, sets of roots, exact radicals, intervals, function notation and multipart reasoning. “Symbolic input” alone does not prove these marking policies.
- Trial Numbas's current JME entry with keyboard-only, screen-reader, touch and Danish keyboard users before adding MathLive. If a barrier is observed, compare a MathLive front end against STACK's and WeBWorK's native input syntax using the same tasks.
- Run the synthetic class test. Whole-class capacity for STACK and WeBWorK, and low-spec browser responsiveness for Numbas/MathLive, remain hypotheses.
- Decide how a launched/embedded activity reports first response, hint exposure, retries and deterministic outcome to Open Alpha's surrounding journey without making the external engine the learner-state authority. This is an integration mapping, not permission to invent a new grading system.
- Obtain an explicit Open Alpha reuse licence before adapting its source.

## Decision boundary

This evidence is enough to avoid a premature combination. Start with Numbas as already selected for deterministic probes and keep its native input. Add MathLive only after an observed input/accessibility gap. Escalate specific items to a short STACK API trial when their checking or feedback cannot be expressed cleanly in Numbas. Trial WeBWorK renderer only when a permission-cleared PG activity provides a concrete advantage. The synthetic load test—not a technology preference—decides whether any shared checking path is responsive enough for one class.
