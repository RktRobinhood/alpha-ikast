# Mastery policy from established learning systems

Research date: 2026-09-07. Question: [Set the mastery and assessment-readiness policy](https://github.com/RktRobinhood/alpha-ikast/issues/9).

## Conclusion

The pilot should not invent a universal score or treat a corrected answer as if it were an independent success. It should begin with OATutor's actual learning workflow and preserve the distinction that established systems repeatedly make:

- feedback, hints, retries, explanations and corrective work are how learning happens;
- the first response before help is the cleanest routine observation of what the learner can currently do;
- success after support is valuable evidence that the support worked, but it does not erase the earlier observation or by itself establish mastery;
- mastery becomes more credible when it survives a fresh problem, mixed practice and delayed retrieval;
- performance for an upcoming assessment is a separate, scope- and date-specific question that also depends on format, timing and freshness.

This is a synthesis of public behavior, not a claim that Alpha School, TimeBack, Math Academy, OATutor, Khan Academy and ASSISTments share one algorithm. They do not. Their numerical rules differ substantially, and the most sophisticated algorithms are proprietary. The convergence is in the shape of the learning cycle, not in one threshold.

## Model decision

**Select competency-level standard BKT as the pilot's longitudinal mastery measure, using OATutor's pinned first-attempt observation and update behavior as the operational baseline.** Use the BKT probability to route learning, not as a self-validating declaration of durable mastery. Put the evidence-confidence and retention requirements described later around that estimate.

This selects a model family and observable behavior, not an implementation technology. OATutor already performs the small online update needed for its learning loop. [pyBKT](https://github.com/CAHLR/pyBKT) is the compatible open-source tool for offline fitting, cross-validation and later comparison of BKT variants; its official documentation accepts ordered learner/skill/correctness records, fits standard BKT, supports item-specific guess/slip, learning and forgetting variants, and evaluates predictions with RMSE, AUC, accuracy or custom metrics ([pyBKT README](https://github.com/CAHLR/pyBKT/blob/master/README.md)). It should not become a launch dependency or be used to fit parameters from a tiny pilot sample.

The measure is therefore:

```text
learner state for a subject competency
  = standard BKT P(learned), updated from eligible ordered KC observations
  + a separate evidence-confidence label
  + retention status from later independent retrieval
```

Assessment readiness remains a different projection over the assessment scope and expected conditions. No single scalar is selected to combine mastery, confidence and readiness.

### Comparative decision matrix

| Candidate | What it measures / does | Fit for this pilot | Decision now | Why |
| --- | --- | --- | --- | --- |
| **OATutor standard BKT** | Sequential probability of a two-state learned/not-learned KC, with explicit prior, learn/transition, slip and guess parameters | Direct match to the adopted step/KC workflow; interpretable; online; first-attempt and help rules are inspectable | **Selected as the initial longitudinal mastery measure** | It is already part of the adopted upstream behavior and is the smallest established statistical model that can accumulate uncertain evidence across activities. Its assumptions and parameters can be audited. |
| **pyBKT standard model** | Fits and evaluates the same BKT family from ordered correctness data | Strong for offline calibration and reproducible model comparison | **Selected later as the fitting/validation reference, not as a required runtime** | It can cross-validate the basic model and exposes parameters. The pilot first needs stable competency mappings and enough independent observations. |
| **pyBKT item/student/forgetting variants** | Adds different priors, learn rates, item guess/slip, resource effects and optional forgetting | Potentially improves prediction when items and learners differ | **Defer** | Extra parameters can overfit sparse pilot data and become hard to explain. Add only when held-out prediction shows a material, stable gain and the sample supports it. |
| **Numbas DIAGNOSYS** | One-pass rule-based diagnosis over a topic dependency graph; passes propagate to prerequisites and failures to downstream topics | Useful for a short baseline exploration and deterministic activity selection | **Use only for its bounded diagnostic/activity role, not as persistent learner state** | Each topic is tested at most once and inferred graph propagation is coarse. Numbas itself says diagnostic mode remained in active development and had not been used with real students as of its documentation note ([diagnostic algorithms](https://docs.numbas.org.uk/en/latest/exam/diagnostic.html)). |
| **Numbas Mastery algorithm** | Ordered per-topic question queue; correct questions leave the queue, incorrect ones move to the end, and all questions must eventually be correct | Clear local practice loop with deterministic completion | **Available as an activity-local algorithm; not selected as the longitudinal measure** | It records eventual queue completion, not uncertainty, help provenance, retention or evidence across activities. It is useful learning behavior but cannot answer the learner-state question alone ([Numbas Mastery algorithm](https://docs.numbas.org.uk/en/latest/exam/diagnostic.html#mastery)). |
| **Fixed percentage or streak** (Alpha progression, Khan, ASSISTments) | Transparent categorical gate over a bounded activity | Easy to explain; useful inside an assessment or practice set | **Use only where the adopted activity already defines it; do not make it the cross-activity model** | The established products use incompatible rules: 90%, staged 70/100/mixed evidence, or three in a row. A threshold is policy, not a transferable estimate of latent knowledge. |
| **Math Academy knowledge profile / FIRe** | Proprietary graph-based weighting of answers, speed and spaced explicit/implicit repetitions | Closest behavioral target for long-term mathematics learning and a real tool in Alpha's catalog | **Adopt its public principles, not its unavailable algorithm** | Its formulas, parameters and validation data are not public. Reimplementing an inferred version would violate adoption-before-invention and could not be shown equivalent. |
| **IRT / Rasch** | Estimates learner proficiency relative to calibrated item difficulty; richer IRT models can add discrimination and guessing | Strong future fit for baseline exploration, item-bank calibration and comparable forms | **Do not use for the initial longitudinal learner state** | It is oriented to measurement across items/forms rather than learning transitions. It requires stable items, linked responses, sufficient sample size and model-fit checking. The [UK test-development handbook](https://www.gov.uk/government/publications/national-curriculum-test-development-handbook/test-development-handbook-2023) and [ETS introduction](https://www.ets.org/research/policy_research_reports/publications/report/2020/kbxx.html) describe those calibration and assumption demands. |
| **Open Alpha highest-score / 80% completion rule** | Retains the highest client-reported quiz percentage and completes a concept at 80% | Relevant only to the surrounding Open Alpha product shell | **Not selected** | It cannot decrease, distinguish support from independence, represent uncertainty, or test retention. It is weaker than the OATutor baseline already adopted ([quiz source](https://github.com/lamira-the-human/open-alpha/blob/main/api/tutor/quiz/submit.ts)). |

The decision favors interpretability and adoption fit over theoretical sophistication. It also keeps the raw observation history model-independent, so later evidence can displace BKT without rewriting what students did.

## Evidence boundary

The report distinguishes three kinds of statements:

- **Documented behavior** is what official product documentation or source code says the system does.
- **Empirical evidence** is a reported study of learner outcomes. It may support a learning practice without validating every product rule or threshold.
- **Pilot recommendation** is the proposed interpretation for Alpha Ikast. It is not attributed to a source as though the source had designed this pilot.

Public vendor documentation establishes described behavior, not universal deployment at every Alpha campus or causal effectiveness. No private Alpha or TimeBack dashboard, proprietary algorithm, student data or licensed assessment item was inspected.

## What Alpha and TimeBack actually establish

Alpha publicly lists Math Academy among its mathematics applications in its [Academics XP Guide](https://cms.academics.alpha.school/2hrlearning-xp-guide), and Alpha has separately described Math Academy as one of the tools it uses in an [official product article](https://alpha.school/blog/10-ai-tools-we-use-at-alpha-and-you-should-too/). That supports studying Math Academy as one real Alpha learning workflow. It does not establish that every Alpha student uses it, that TimeBack reproduces its learner model, or that all connected applications obey one mastery rule.

TimeBack's own support documentation makes the orchestration boundary explicit. A course-completion percentage may come from the learning app or be estimated from XP; reaching 100% completion is not the same as mastery. Course completion is followed by a separate end-of-course assessment. A pass progresses the learner, while a failure can lead to targeted remediation and another attempt ([course completion and pacing](https://support.alpha.school/article/133259-understanding-course-completion-in-timeback-to-plan-student-pacing)). The documented progression flow likewise separates assigned lessons, a standardized assessment, targeted work after failure, and reassessment ([grade progression](https://support.alpha.school/article/31841-advancing-to-the-next-grade-level-aiming-for-mastery)).

Alpha's placement workflow uses a 90% pass rule, moves a learner down through grade-level assessments after a first failure, and later assigns learning before reassessment. Mathematics is a special case: any failed mathematics placement assessment leads to the full base course at that grade after the preceding grade is passed, rather than the 60–89% “hole-filling” path used by most other subjects ([placement guide](https://support.alpha.school/article/133839-quick-start-guide-placement-tests-in-timeback)). This is a coarse grade-placement and progression policy, not evidence of a universal item-level mastery algorithm.

TimeBack's public integration documentation reinforces the same separation. A provider determines when a learner is ready for a mastery assessment; an assessment vendor reports item results; TimeBack aggregates the result against a pass threshold and issues a mastery credential only after a pass. Failed assessments can be retried ([Competency Track](https://docs.platform.timeback.com/integration/competency-track)). Connected learning apps can also report their own mastery events ([Caliper Events Reference](https://docs.platform.timeback.com/event-reference/caliper-events)). These interfaces transport assertions and results; they do not reveal one TimeBack algorithm for hints, retries, retention or confidence.

**Supported conclusion:** the Alpha precedent is not “90% of every activity means mastery.” It is that learning activity, XP/completion, assessment and progression are distinct. Alpha Ikast should preserve that distinction.

## Math Academy: the most relevant documented Alpha math workflow

Math Academy describes a knowledge graph, a learner knowledge profile and adaptive task selection. Its initial diagnostic samples course content and lower-course foundations. During lessons, a worked example is followed by up to five practice problems; two consecutive correct responses allow progression to the next knowledge point. Every problem has an explanation. A timed quiz becomes available roughly every 150 XP, prevents reference to lesson material, mixes recent topics, and sends missed topics into immediate review before an optional retake ([How It Works](https://mathacademy.com/how-it-works)).

Its long-term model is not a one-time mastery flag. Math Academy says the knowledge profile measures appropriately spaced successful repetitions. Overdue reviews can move a learner backwards. Practice of advanced topics can give discounted, fractional repetition credit to simpler skills actually encompassed by that work, rather than automatically crediting every prerequisite. Its diagnostic also weights conflicting evidence, discounts a correct answer that takes excessively long, and can mark a borderline topic “conditionally completed” so later struggle causes the route to fall back ([How Our AI Works](https://mathacademy.com/how-our-ai-works)). The exact formulas and calibration are not public.

Math Academy also explicitly distinguishes course mastery from test preparation. Its official test-preparation guide says content mastery is necessary but insufficient for test performance; readiness additionally requires practice under the target test's timing, wording, format and multi-skill demands. It recommends multiple different authentic practice tests, targeted same-day correction, later unassisted retrieval and spaced review ([standardized-test guidance](https://www.mathacademy.com/how-to-maximize-performance-on-a-standardized-math-test)).

**Supported conclusion:** the closest documented Alpha mathematics model combines granular prerequisites, short mastery checks, mixed quizzes, time/automaticity, corrective review and continued spaced retrieval. It does not reduce durable mastery to a single percentage.

## OATutor: the adopted activity-workflow baseline

At the pinned upstream revision [`6de5ada`](https://github.com/CAHLR/OATutor/tree/6de5ada333f02ac18752aac48e38b9462a7882bd), OATutor decomposes problems into steps and maps each step to one or more knowledge components (KCs). Each KC has the standard Bayesian Knowledge Tracing parameters for current mastery, transition/learning, slip and guess. Its default selection strategy prioritizes problems with the lowest average KC mastery, while lessons can configure a target mastery and completion behavior ([repository documentation](https://github.com/CAHLR/OATutor/tree/6de5ada333f02ac18752aac48e38b9462a7882bd)).

The source is more important than a generic BKT description:

- [`BKT-brain.js`](https://github.com/CAHLR/OATutor/blob/6de5ada333f02ac18752aac48e38b9462a7882bd/src/models/BKT/BKT-brain.js) performs the binary correct/incorrect Bayesian update and then applies the transition probability.
- [`Problem.js`](https://github.com/CAHLR/OATutor/blob/6de5ada333f02ac18752aac48e38b9462a7882bd/src/components/problem-layout/Problem.js) updates each tagged KC only on the first graded attempt for a step. A correct later retry lets the learner progress but does not repeatedly increase the KC estimate.
- The same source defers a help penalty until the next graded response: the interface can show that response as correct so the learner can proceed, while BKT receives an incorrect observation.
- [`helpPenaltyMode.js`](https://github.com/CAHLR/OATutor/blob/6de5ada333f02ac18752aac48e38b9462a7882bd/src/util/helpPenaltyMode.js) makes this configurable. The pinned default treats opening an authored hint as help and therefore gives no mastery credit on the next submission; AI-chat help defaults to no penalty. Other modes can wait for answer reveal or never penalize help.

OATutor's parameters and mappings are content configuration, and its documentation says BKT parameters are normally empirically determined and can be tested. A BKT probability is an estimate under those parameters; it is not a confidence interval and should not be presented as a calibrated certainty before validation.

**Supported conclusion:** the baseline already answers the immediate retry question. Keep the retry as supported learning and forward movement, but do not turn it into a second positive BKT observation. Preserve the upstream help behavior for the baseline trial, including the visible promise that authored hints will not increase mastery credit, and record whether the treatment causes an observed IB-specific problem before changing it.

## Khan Academy: proficiency first, then mixed confirmation

Khan Academy uses explicit states rather than a naked probability. An exercise below 70% produces Attempted; 70–99% can produce Familiar; 100% can produce Proficient. Mastered requires a learner who is already Proficient to answer correctly on a mixed-skill assessment. Later misses can lower the state ([mastery levels](https://support.khanacademy.org/hc/en-us/articles/5548760867853--How-do-Khan-Academy-s-Mastery-levels-work)).

Its Mastery Challenges add a time and mixing dimension. They unlock no more than once per 12 hours, contain six randomized questions covering three skills, and use two questions per skill: two correct raises the level, two incorrect lowers it, and a split result leaves it unchanged ([Mastery Challenges](https://support.khanacademy.org/hc/en-us/articles/360037494231-What-are-Mastery-Challenges)). Course and unit percentages aggregate skill-level mastery points and can move up or down ([course and unit mastery](https://support.khanacademy.org/hc/en-us/articles/115002552631-What-are-Course-and-Unit-Mastery)).

**Supported conclusion:** even a system with fixed percentage rules distinguishes same-skill practice from mastery confirmed in mixed work, and it treats mastery as revisable rather than permanent.

## ASSISTments: supported practice, first-attempt reporting and reassessment

ASSISTments makes help and attempts visible rather than collapsing them into final correctness. Its practice report distinguishes correct on the first try, correct eventually after an error or Support, incorrect, and answer reveal; teachers can inspect attempts, hints and timing ([assignment reports](https://www.assistments.org/individual-resource/assignment-reports)). In Practice Mode, hints and multiple attempts support learning. Test Mode removes immediate feedback, hints and multiple attempts to observe independent performance ([Practice versus Test Mode](https://www.assistments.org/individual-resource/enabling-test-mode)). A hint reduces practice credit; showing an explanation or answer produces zero credit ([Student Supports](https://www.assistments.org/individual-resource/student-supports)).

ASSISTments Skill Builders operationalize a different mastery rule from Alpha, OATutor and Khan: three consecutive correct answers on randomized same-skill problems. If that is not achieved within ten questions, more problems become available the next day ([Skill Builders](https://www.assistments.org/individual-resource/what-are-skill-builders-and-how-are-they-different-from-the-other-content-within-assistments)). Its Automatic Reassessment and Relearning System (ARRS) research used later reassessment and assigned relearning when performance was not retained; the reported randomized study found better later performance on reassessed/relearned skills, with the strongest benefit for learners with low pretest performance ([ARRS research summary and linked paper](https://www.assistments.org/blog-posts/our-research-reassessing-and-relearning)).

This product-level evidence is compatible with broader ASSISTments evidence, but it must not be overstated. A large randomized field trial of 2,850 seventh-grade students in 43 schools found higher end-of-year mathematics assessment performance when ASSISTments' timely feedback/hints and teacher reports were used with teacher training than under the existing homework condition ([SRI report](https://www.sri.com/publication/education-learning-pubs/online-mathematics-homework-increases-student-achievement/)). That supports feedback-rich formative work as part of a classroom system; it does not validate “three correct” as a universal mastery threshold or isolate which component caused the gain.

## What converges, and what does not

| Question | Convergence in established systems | Material differences / unknowns |
| --- | --- | --- |
| Does corrected work matter? | Yes. Correction, explanation, remediation and retry are part of learning. | Credit ranges from no mastery update (OATutor) to reduced practice credit (ASSISTments) to proprietary task scoring (Math Academy). |
| Is eventual correctness the same as independent success? | No. OATutor updates only once; ASSISTments reports “correct eventually” separately; Math Academy and ASSISTments provide separate no-help assessment modes. | No universal penalty for every kind of help exists. OATutor itself configures authored hints and AI chat differently. |
| Is one threshold universal? | No. | Public rules include OATutor's configurable BKT target, Alpha's 90% progression/placement assessment, Math Academy's two-in-a-row lesson rule, Khan's staged 70/100/mixed rules and ASSISTments' three-in-a-row rule. |
| Must mastery persist? | Mature workflows revisit prior learning. | Khan uses a 12-hour-gated mixed challenge; Math Academy uses a proprietary spaced schedule; ASSISTments has published expanding reassessment work; Alpha documents reassessment after failed progression tests but not a fine-grained retention schedule. |
| Is completion mastery? | No in TimeBack; other systems also distinguish work/XP from stronger evidence. | Some connected apps can send their own mastery assertion, whose internal basis remains app-specific. |
| Is mastery assessment readiness? | No. | Math Academy explicitly requires format- and timing-specific preparation beyond curriculum mastery. TimeBack separately gates completion with an assessment. |
| Do the systems expose evidence confidence? | They expose related signals: BKT probability, staged states, conditional completion, attempts, help, timing and recency. | None of the reviewed public documentation provides a portable, calibrated confidence label that Alpha Ikast can copy unchanged. |

The classic mastery-learning premise is also a learning cycle rather than a magic percentage. Bloom's original formulation treats time needed as variable and asks instruction to provide the conditions under which learners can attain a defined level ([*Learning for Mastery*, ERIC record and full text](https://eric.ed.gov/?id=ED053419)). The product evidence above makes that cycle concrete: assess, give corrective support, reassess, and continue reviewing. It does not justify importing Bloom's reported outcomes, Alpha's marketing claims or any vendor's threshold as a guaranteed effect in IB Mathematics AA SL.

## Recommended pilot policy

This section is a recommendation synthesized from the documented systems. It deliberately starts from the adopted OATutor workflow and adds only the boundaries needed to interpret it honestly.

### 1. Preserve observations before interpreting them

For every graded step or item, retain enough context to replay and audit the learner state: activity and item version, mapped subject competency/KC, timestamp, response order, scored result, whether it was the first submission, help channel and help depth, answer reveal, mode (guided practice or independent), response time when meaningful, and grader/version. Preserve completion and XP as activity facts, not mastery evidence.

This is not a new scoring formula. It preserves the distinctions already surfaced by OATutor, ASSISTments, Math Academy and TimeBack so a later calibration does not have to reconstruct them from a final score.

### 2. Use the pinned OATutor update rule for the baseline trial

For an OATutor step, update each mapped KC once, on the first graded submission, using the pinned upstream BKT equations and that lesson's versioned BKT parameters. Do not allow repeated attempts on the same step to create repeated positive updates.

Use the pinned hint behavior unchanged in the first trial: if the configured help mode marks the step as helped, the next graded response supplies no positive mastery credit even when the interface correctly allows the learner to proceed. Keep AI-chat treatment as configured by the upstream lesson rather than silently treating all AI interaction as equivalent to an answer reveal.

Do not adopt 80%, 90%, “two in a row” or “three in a row” as a replacement OATutor threshold merely because another system uses it. Record the OATutor target and parameters with the content version. Those values remain provisional until their predictions can be compared with later independent work in the AA SL setting.

### 3. Classify evidence without devaluing supported learning

- **Independent observation:** the first graded response to a fresh item before hints, explanations, answer reveal or tutoring. Correct and incorrect responses both inform learner state.
- **Supported learning:** all feedback, hints, scaffold use, explanation review and subsequent attempts. Eventual success shows that the learner completed the supported learning cycle; it does not overwrite the independent observation or create another positive update for the same item.
- **Independent confirmation:** a correct response on a fresh, unassisted item that exercises the same competency in a different surface form or mixed context.
- **Retention confirmation:** independent confirmation after a meaningful delay.

A learner should receive feedback and be able to advance within guided practice after a corrected response. “No additional mastery credit” must never mean “the learning did not count”; it means that the next mastery claim should use a fresh observation.

### 4. Add evidence-confidence labels, not a second hidden mastery algorithm

Show estimated mastery and evidence confidence separately. The following labels are a pilot recommendation, not copied vendor labels:

- **Insufficient evidence:** no eligible independent observation, or only completion/supported activity is available.
- **Provisional:** independent evidence exists but is narrow, same-session or not yet corroborated.
- **Corroborated:** fresh independent evidence spans more than one item form or a mixed context.
- **Rusty:** earlier evidence was strong enough to route forward, but the competency is due for retrieval because its retention evidence is aging. Rust is not evidence that mastery has been lost.
- **Contested:** recent independent evidence conflicts materially with the current estimate or an assessment outcome, requiring another probe or teacher review.

Do not display BKT probability as evidence confidence. Mastery probability answers a model-dependent “how likely learned?” question; confidence answers “how much suitable evidence supports that estimate?” During the pilot, label confidence from provenance, independence, diversity and recency rather than pretending to have a statistically calibrated interval.

### 5. Show rust without inventing mastery loss

Add **rust** as a visible maintenance layer on the mastery bar. The mastery estimate continues to show what the latest eligible observations support; rust shows how overdue that competency is for retrieval. Elapsed time can increase rust and make review more urgent, but it must not reduce the BKT estimate by itself. A failed retrieval is new evidence and may then lower or contest the learner state.

Rust need not create a machine of repetitive single-skill reviews. A fresh independent probe can clear it directly, while a new, mixed or advanced task can reduce rust for several older competencies through **implicit retrieval**. This transfer requires an explicit activity-to-competency mapping showing that the task actually exercises each older competency. Prerequisite adjacency or topical similarity alone earns no credit. Implicit retrieval should receive discounted credit when coverage is partial, too early, supported by help, or weaker than a direct probe.

This adopts the public behavior of Math Academy's Fractional Implicit Repetition at the level of principle, without reconstructing its proprietary formula. Math Academy distinguishes prerequisite topics from genuinely “encompassed” component skills, discounts implicit repetitions, and compresses several due reviews into a smaller set of advanced tasks that actually exercise them ([How Our AI Works](https://mathacademy.com/how-our-ai-works)).

On successful retrieval, reduce or clear rust and extend the next review interval. On unsuccessful retrieval, preserve the learner's earlier evidence, update the state from the new response, and route focused corrective practice followed by another fresh confirmation. Do not reset the learner to the beginning of the original path. The retained history may support faster reconfirmation, but the pilot should measure that rather than assume a universal relearning rate.

### 6. Require fresh, varied and delayed evidence for durable mastery

Allow the native OATutor estimate to route practice, but reserve the learner-facing claim **durable mastery** for a competency that has:

1. reached its versioned OATutor target from eligible independent observations;
2. been confirmed on at least one fresh item rather than a repeat of a revealed/corrected item;
3. appeared in at least one mixed or meaningfully different context; and
4. survived a delayed independent retrieval opportunity.

Use an expanding review schedule as the starting retention pattern. If the pilot needs a concrete public default, trial the ASSISTments ARRS cadence described in the [primary study](https://files.eric.ed.gov/fulltext/ED558215.pdf) (approximately 7, 14, 28 and 56 days), while allowing ordinary Math Academy-style “implicit” or mixed practice to satisfy a due review only when the item genuinely exercises the mapped competency. Treat this cadence as a trialable configuration, not a universal law.

Failed independent reassessment must be able to lower or contest the learner state and route corrective practice. That matches OATutor's negative BKT updates, Khan's level-down behavior, Math Academy's backward movement and ASSISTments' reassessment/relearning cycle. A highest-ever score must not make mastery permanent.

### 7. Keep assessment readiness as a separate projection

Assessment readiness should answer: “Given this assessment scope and scheduled date, how prepared is the learner to demonstrate the required forms of performance under the expected conditions?” It should draw on, but not redefine, durable mastery.

Readiness evidence should therefore be filtered by the assessment scope and should emphasize recent, independent work at the expected AA SL demand, including mixed multi-competency problems, unfamiliar wording, appropriate calculator/no-calculator conditions, time constraints where relevant, and human-scored structured reasoning where the assessment requires it. Supported practice remains the route to improvement but is not the readiness check itself.

Continue to respect the repository's decided bridge-phase boundary: a teacher-provided class assessment outcome informs teacher insight and calibration of readiness but does not directly update the learner state. A contradiction should create a **contested** signal and a fresh independent probe or mapping review, not silently rewrite mastery.

## What the first trial should decide from evidence

The first OATutor AA SL slice should preserve the pinned defaults and collect enough non-sensitive interaction data to answer concrete questions:

1. Do the existing KC mappings make first-attempt updates diagnostically meaningful for the mapped subject competencies?
2. Does the default authored-hint penalty discourage productive hint use or correctly prevent false mastery credit?
3. Do later fresh probes agree with the OATutor estimate well enough to use its target for routing?
4. Which item variations genuinely supply diverse evidence rather than cosmetic variants of the same procedure?
5. Does the proposed review cadence maintain performance without crowding out current work?
6. Does readiness computed from recent assessment-scope probes correspond usefully with existing class assessments, without turning those outcomes into learner-state updates?

Change an upstream behavior only after one of these trials exposes a specific AA SL gap. That follows the repository's “adopt, validate, then adapt” constraint while still giving issue #9 an operational policy: preserve support, protect independent evidence, confirm mastery over varied and delayed retrieval, and keep upcoming-assessment readiness separate.

## Alternatives not selected and re-evaluation triggers

| Alternative not selected now | Revisit when | Evidence required before changing course |
| --- | --- | --- |
| A single fixed streak or percentage as the persistent mastery measure | BKT predictions are no better than a simpler rule, or the statistical state is consistently misunderstood by learners and teachers | Pre-registered comparison on held-out fresh probes and later retention observations; teacher usability evidence; analysis by competency rather than aggregate accuracy alone |
| pyBKT item-specific guess/slip or learning-rate variants | The same competency shows stable, material item-difficulty or resource effects and the dataset has repeated responses per item/KC | Cross-validation against standard BKT with a predefined improvement criterion; parameter stability across cohorts/time; no degradation for sparse competencies |
| BKT with explicit forgetting | The baseline systematically overpredicts delayed independent performance and scheduled retention checks reveal time-dependent decay | Held-out delayed-probe data; comparison of calibration and error with/without forgetting; evidence that the added parameter is identifiable rather than absorbing mapping errors |
| Automatically clearing rust from prerequisite links or topic similarity | Authored activity mappings prove too costly and graph relations reliably predict which older competencies a task actually exercises | Held-out retrieval evidence showing the inferred implicit-practice links predict later performance without systematically masking rusty prerequisites |
| IRT/Rasch for baseline exploration | The item bank and AA SL mappings are stable, several linked forms exist, and response volume supports calibration | Specialist model-fit review, item characteristic and differential-item-functioning checks, uncertainty estimates, and validation that adaptive placement shortens the baseline without misrouting prerequisite support |
| Numbas DIAGNOSYS as the persistent learner model | A real AA SL trial shows that one-pass prerequisite propagation agrees with later independent observations and its coarse states are sufficient for routing | Comparison against BKT and teacher-reviewed cases, including false prerequisite passes and false downstream failures; updated evidence of real-student use from Numbas maintainers |
| Numbas Mastery queue as the cross-activity model | The pilot intentionally chooses deterministic topic completion over probabilistic learner state | Evidence that queue completion predicts fresh and delayed performance, plus an explicit policy for hints, repeat variants and state reversal |
| A Math Academy-like graph/spaced-repetition model | Math Academy exposes a licensable integration/model, or repeated trials demonstrate a specific gap that BKT plus retention scheduling cannot handle | Official algorithm/integration documentation or a bounded gap report; independent validation; no reconstruction from marketing descriptions alone |
| Deep knowledge tracing or another opaque/high-capacity model | The pilot has a much larger, representative sequence dataset and an interpretable model demonstrably fails | Strict learner-level temporal holdout, calibration and subgroup error analysis, comparison with standard/extended BKT, explanation and audit plan, and proof that predictive gain changes useful decisions |
| Self-reported confidence as mastery credit | A validated AA SL study shows it improves prediction beyond scored independent performance | Prospective validation against later independent tasks; safeguards against confidence bias. Until then, use self-confidence only to prompt review, as Math Academy's test-preparation guidance does. |
| Class assessment outcomes directly updating learner state | A later governance decision changes the bridge-phase boundary and assessment mappings/rubrics are sufficiently consistent | Teacher-approved calibration study, versioned assessment-scope mappings, handling of accommodations and missingness, and an audit trail. Until then, use outcomes to contest readiness and request a probe. |

The first formal review of the selected model should occur after the bounded OATutor AA SL trial has produced fresh and delayed independent observations—not after an arbitrary calendar date. The review should compare predictions, not merely whether students eventually completed practice.
