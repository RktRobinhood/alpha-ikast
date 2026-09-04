# Privacy and AI boundary

Status: initial framing for Wayfinder; not legal advice and not yet a complete technical evaluation.

## Self-hosting and GDPR

Self-hosting can reduce disclosures to external vendors and give a school more direct control over storage, access, and operations. It does not make student-data processing exempt from GDPR.

Denmark's Data Protection Agency states that schools' automated processing of student information is generally subject to data-protection law, that children receive particular protection, and that schools should define privacy and retention policies. The European Data Protection Board identifies schools as data controllers and requires data protection by design and by default, including purpose limitation, data minimization, storage limitation, integrity, confidentiality, and demonstrable accountability.

Primary sources:

- [Datatilsynet: Skoler og daginstitutioner](https://www.datatilsynet.dk/regler-og-vejledning/skoler-og-daginstitutioner)
- [European Data Protection Board: Privacy by design and by default](https://www.edpb.europa.eu/topics/ai-and-technology/privacy-by-design-and-by-default_en)
- [European Data Protection Board: Basic principles](https://www.edpb.europa.eu/topics/key-gdpr-concepts/basic-principles_en)

## AI architecture hypothesis

Separate the educational decision system from AI execution:

```text
curriculum + learner evidence + teacher policy
                    |
                    v
        authoritative lesson planner
                    |
          proposed bounded AI task
                    |
                    v
       replaceable AI workflow runtime
                    |
          replaceable model provider
                    |
                    v
       validated candidate or explanation
                    |
       policy checks and learner pathway
```

The project should aim for model independence and portable task boundaries, not attempt to support every AI framework equally from day one. A later research ticket should compare candidate runtimes against the actual tasks revealed by the product investigation. Routine activity recommendations should not require teacher approval; teacher oversight belongs in pathway steering, visible evidence, alerts, and intervention controls.

## Evaluation criteria for an AI workflow runtime

- Structured inputs and validated outputs
- Human approval and override support
- Durable execution, retries, and idempotency where needed
- Audit trail without unnecessary retention of student prompts or model data
- Local-model and approved hosted-model support
- Observability and cost controls
- Clear failure behavior that does not corrupt learner state
- Small operational burden for a school-hosted deployment
- License and project sustainability
