# Planning

## Wayfinder status

The source material has been organized, but the Wayfinder map has not yet been created. The Wayfinder process first requires a precise destination; that destination determines what belongs on the map and what is out of scope.

The issue tracker is GitHub. Repository and tracker setup are in progress.

## First decision

The effort covers the complete **IB Mathematics: Analysis and Approaches SL** course and works backward from its examination destination into prerequisite knowledge. It is intended for DP2 exam preparation, DP1 prerequisite support, and eventually routine use by every AA SL student.

The working delivery posture is curation-first: evaluate and combine existing open-source components and lawfully reusable content before building replacements. The pilot should initially stay close to the teacher's existing sequence and treatment, using licensed Haese Mathematics teacher materials and other authorized current publications as references. A textbook-independent model is a later direction, not an initial constraint. Whole-course scope does not require a single all-at-once release; small classroom-usable slices should accumulate toward it.

The first-release workflow will not be selected until the available open-source systems, reusable content, and integration effort have been investigated. The experiment is to reproduce useful parts of the Alpha-style learner experience inside an established, non-AI-first school; it is not a commitment to reorganize the school around AI.

The product must be self-hostable so each adopting school can control its infrastructure and student-data flows. The working architecture keeps model providers replaceable and AI workflow tasks portable across runtimes, while selecting one concrete runtime when implementation begins. The AI runtime is not the authoritative learner-state or lesson-planning system.

Students receive adaptive next steps without routine teacher approval. Teachers operate as coaches who monitor progress, intervene where needed, and steer the system through ordered unit plans: intended competencies, approximate timing, and assessment scope. The platform remains responsive to the individual student's evidence while maintaining a path toward upcoming class assessments.

The first deployment is a bridge phase: it supplements conventional AA SL teaching and assessments. Its immediate outcome is improved genuine readiness for the teacher's existing tests while also repairing prerequisites. Whether Alpha School itself uses traditional tests remains an open research question, not an assumption for this project.

Students should receive structured school time to use the platform independently, with the teacher present as coach. Exact scheduling remains a pilot variable. The experience must help students understand their current learner state and the path toward assessment readiness and mastery.

With insufficient prior data, learner-state bootstrapping uses adaptive baseline exploration across varied competencies at and below the student's expected course level. The system follows uncertain or weak evidence into prerequisite chains and stops when confidence is sufficient for a useful initial path; ongoing work then updates the estimate.

Learner-state estimates use only evidence produced through platform-observed activities, not imported aggregate grades or teacher judgments. Conventional assessments remain important as targets and external evaluation signals, but do not directly initialize mastery.

## Known fog beyond that decision

- Release order between DP2 exam preparation and DP1 prerequisite support
- Meaning and operational boundary of “in house”
- Representation of teacher steering and learning horizons
- Student choice within an adaptive pathway
- Policy for balancing prerequisite recovery and assessment readiness
- Placement of supplementary learning within the existing timetable
- Initial diagnosis and learner-state bootstrapping
- Evidence types, confidence thresholds, and stopping rules for baseline exploration
- Representation and interpretation of mathematical working, hints, attempts, and final answers

## Evidence-model research criteria

The investigation of existing mathematics tools and statistical mastery models should compare:

- diagnostic value of final-answer, step-level, and extended-response evidence;
- whether multiple thin-sliced items can identify a competency reliably;
- how hints, retries, timing, and item difficulty affect an estimate;
- support for prerequisite graphs and uncertainty-aware selection;
- alignment between short competency evidence and AA SL exam-style reasoning;
- content-authoring and tagging burden for teachers;
- explainability to students and teachers;
- self-hosting, licensing, and integration fit;
- risks of automated marking, especially for handwritten or open mathematical work.

## Confirmed evidence direction

The primary-source comparison in [Mathematics evidence and mastery models](../research/findings/math-evidence-and-mastery-models.md) recommends:

- thin-sliced, competency-tagged, first-attempt observations as the default evidence;
- triangulation across varied questions and time rather than mastery from one answer;
- selective structured step/process marking for high-value AA SL problem forms;
- interpretable Bayesian Knowledge Tracing (BKT) as the initial longitudinal model;
- Item Response Theory (IRT) later, after a stable item bank and enough response data exist for calibration;
- AI feedback on free-form working as formative, non-authoritative evidence until locally validated;
- append-only raw observation events as the source of truth, independent of any replaceable mastery model.

This is accepted as the starting architecture under an **adopt, validate, then adapt** principle. Component selection and local validation remain Wayfinder investigations; the project will not implement a new mastery model or mathematics grading engine before evaluating the existing options.

## Implementation boundary

The user experience must be web-hosted for compatibility across common device types and operating systems. Backend architecture, framework, AI runtime, and deployment topology remain deliberately undecided until the investigations establish what should be adopted.
- Alpha School's actual assessment and mastery practices
- AI workflow runtime and portability boundary
- Examination sessions and classroom constraints
- Student, teacher, leadership, and possibly parent needs
- Pedagogical model for progression and mastery
- Initial activity and evidence types
- Curriculum representation and subject-extension seams
- Build-versus-integrate choices
- Data protection, safeguarding, security, and governance
- Evaluation design and success criteria
- Open-source governance and contribution model

## Content acquisition boundary

Research may catalog and analyze openly licensed materials, public specifications, and resources the school is authorized to use. The project will not treat appearance on an unofficial document-sharing site as a license to bulk-download, extract, or redistribute copyrighted books.
