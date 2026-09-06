# Privacy requirements for the self-hosted AA SL pilot

Research date: 2026-09-06. Resolves the investigation [Define privacy requirements for a self-hosted classroom pilot](https://github.com/RktRobinhood/alpha-ikast/issues/6).

Status: planning requirements and proposed acceptance criteria, not school authorization. No student records, school contracts, infrastructure, or institutional policies were inspected. School-specific legal basis, retention periods, and approvals remain unverified. No implementation technology is selected.

## Evidence-backed requirements

The GDPR requires lawful, purpose-limited, proportionate processing; safeguards by design; appropriate security; processor contracts; and mechanisms for data-subject rights. Pseudonymized records remain personal data when re-identification is possible. A DPIA is required for processing likely to create high risk, with prior supervisory consultation where unmitigated high risk remains. Solely automated decisions with legal or similarly significant effects require separate Article 22 assessment. Breaches must be documented; notification to the authority is normally required within 72 hours of awareness unless unlikely to risk rights and freedoms, and affected people must be informed where high risk warrants it. These obligations survive self-hosting. [GDPR, Articles 4–6, 12–22, 25, 28, 30, 32–36](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng).

Datatilsynet's school guidance requires particular attention to children, intelligible notices, and retention justified by purpose. There is no universal school-record retention period in GDPR. The institution's legal status and purpose matter to lawful basis: public authorities cannot use legitimate interests for processing in performance of their tasks. Do not infer the gymnasium's legal basis from guidance about municipal primary schools or assume parental consent authorizes everything. [Datatilsynet: schools](https://www.datatilsynet.dk/regler-og-vejledning/skoler-og-daginstitutioner).

Deletion must remove practical access, not merely hide a record. Delete from backups where technically possible; otherwise ensure deleted records are removed again on restoration. Define and verify deletion procedures. [Datatilsynet: deletion](https://www.datatilsynet.dk/regler-og-vejledning/behandlingssikkerhed/sletning). Backup design should follow risk assessment and include recovery procedures. [Datatilsynet: backup](https://www.datatilsynet.dk/regler-og-vejledning/behandlingssikkerhed/katalog-over-foranstaltninger/backup).

Hosting location alone does not settle international transfers: review actual processing, onward transfers, suppliers, and the effective transfer mechanism. [Datatilsynet: cloud](https://www.datatilsynet.dk/regler-og-vejledning/cloud).

## Proposed pilot acceptance criteria

The following are project recommendations translating the requirements above into reviewable criteria. They are not claims that legislation mandates these precise designs.

| Area | Proposed criterion before real learner evidence is processed | Required evidence or owner |
| --- | --- | --- |
| Purpose and responsibility | Separate learning support, assessment-readiness calibration, security, and product research. Identify the legal controller and accountable school sponsor; document legal basis for each purpose. | School-approved purpose register; DPO or privacy contact advice. |
| Data inventory | Inventory identity mappings, course membership, responses, hints/retries, learner state, assessment outcomes, interventions, logs, exports, backups, and provider payloads. Record purpose, access, recipients, and deletion rule for each. | Field-level inventory and data-flow diagram. |
| Identity | Use a stable internal learner identifier; keep name/account mapping within the school-approved identity boundary. Request only required identity attributes. Avoid CPR numbers and birth dates unless a separately justified need emerges. | Example synthetic account and identity-field review. |
| Minimization | Start with tagged responses and selected mathematical steps. Exclude ambient audio/video, browsing surveillance, diagnoses, and unrestricted teacher notes from the first slice. | Synthetic observation examples; rejected-field examples. |
| Access | Learners see their own evidence; teachers see assigned learners; administrative access is limited, attributable, and revocable. Explicitly decide substitute-teacher and support access. | Role matrix; cross-student and cross-class denial checks; leaver-account check. |
| Retention | Set different purpose-based periods and triggers for raw responses, derived state, assessment outcomes, identity, operational logs, and backups. Include withdrawal and course completion. Do not default to indefinite retention for model improvement. | School-owned retention schedule with rationale and review dates. |
| Deletion and correction | Cover live records, derived learner state, caches, exports, processors, and restored backups. Decide how corrected evidence affects estimates without retaining the original indefinitely. | Synthetic deletion/correction exercise and restore exercise. |
| Audit and security | Log privileged access, role changes, exports, policy/model versions, and interventions without copying full answers into logs. Protect transport, storage and secrets; require stronger authentication for privileged users; assign patching and incident ownership. | Risk assessment, access review, sanitized audit sample, response runbook. |
| Backups | Name the operator, location, access, expiry, restore target, and deletion-replay procedure. Include identity mappings and keys in recovery planning. | Documented and tested recovery procedure. |
| Processors | Inventory hosting, identity, email, analytics, error reporting, remote support, content embeds and AI vendors. Review contracts, subprocessors, retention, independent purposes, and transfers. | Approved supplier register; contracts and evidence held privately. |
| AI providers | Default to no real learner records in external models until the exact task and payload are approved. Disable provider training or other reuse unless separately justified and authorized. Stripping names alone is insufficient. | Synthetic payload inspection, documented provider settings and terms. |
| Transparency and rights | Explain baseline exploration, estimated learner state, uncertainty, routing, recipients, retention and contact routes in student-readable language. Decide parent access in light of age and rights, rather than granting it automatically. | Notice reviewed with students; access/correction/objection/deletion request procedure. |
| Teacher oversight | Keep estimates revisable and explainable through evidence; permit intervention. Assess actual consequences of routing, including repeated prerequisite detours, rather than treating a nominal teacher override as proof of meaningful oversight. | Scenario review; route challenge and intervention mechanism. |

## Impact assessment and AI classification

Recommendation: plan on conducting a DPIA, with the school's privacy lead confirming scope. The combination of longitudinal evaluation, learners including children, and adaptive technology warrants explicit assessment rather than assuming a small pilot is exempt. Record necessity, alternatives, risks, mitigation, and residual risk. This is a project inference from the assessment criteria, not a completed legal determination. [Datatilsynet: DPIA guidance](https://www.datatilsynet.dk/Media/2/6/Konsekvensanalyse.pdf).

AI classification must cover the complete educational function, not just whether a language model writes text. Annex III includes AI evaluating learning outcomes, including outcomes used to steer learning. Article 6 provides limited exceptions, but profiling affects that analysis. School emotion recognition is prohibited subject to narrow medical/safety exceptions. Examine provider/deployer roles and, where applicable, human oversight, logging, conformity, registration and fundamental-rights assessment obligations. Deterministic probes do not alone establish that the overall learner-model/routing system falls outside the Act. [AI Act, Articles 3–6, 26–27 and Annex III, consolidated 27 July 2026](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727).

The Commission's current guidance reports Annex III high-risk rules applying from **2 December 2027**, following the July 2026 amendment; the original 2 August 2026 date must not be copied as the current deadline. Prohibitions and AI-literacy obligations already apply. Recheck the applicable text and launch date when selecting components. [European Commission: navigating the AI Act](https://digital-strategy.ec.europa.eu/en/faqs/navigating-ai-act).

## School decisions still needed

One follow-up discussion can establish the planning boundary: identify the accountable school owner and privacy contact; decide permitted identity/data fields and recipients; settle the external-service boundary; assign retention-policy ownership; and agree what evidence the school requires before classroom use. Exact supplier contracts, completed DPIA, incident procedures and deployment tests belong to subsequent delivery and school authorization, not a claim that this research has approved the pilot.

The architecture and classroom-operating-model decisions should consume that boundary. Until it is settled, prototypes can use synthetic learners. A route to implementation must name the later approval gates and responsible roles, without requiring production deployment inside this planning map.

## Verification and limits

All linked primary sources were accessed on the research date. The report contains original synthesis and recommendations, with no copied school or student material. Review checked coverage against every topic in the investigation question. The assessment does not establish the gymnasium's statutory basis, approve a vendor, determine an exact AI classification, or complete a DPIA. Those depend on institutional facts and the eventual processing design.
