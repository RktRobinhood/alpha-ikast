# First AA SL learning-loop slice: quadratic equations

**Research question:** Which narrow but representative AA SL topic and prerequisite chain offers the best first learning-loop experiment when reusable content and mathematics engines are compared for coverage, deterministic grading, authoring effort, browser behaviour, and assessment relevance?

**Status:** decision support based on the supplied local teaching plan and primary project documentation inspected on 2026-09-05. It is not permission to copy any problem, and it does not choose the production architecture.

## Recommendation

Run the first loop on **solving quadratic equations**, starting with factorable equations and then sampling the discriminant and quadratic formula. Treat it as a compact competency set rather than a single undifferentiated topic:

1. preserve equivalence while expanding, collecting terms, and factorising;
2. solve a factorable quadratic through the zero-product property;
3. select and apply the discriminant or quadratic formula for a non-factorable quadratic; and
4. interpret roots against the graph of the quadratic when that representation is supplied.

The prerequisite chain is explicit enough to make routing useful while remaining small enough to test: signed-number and fractional arithmetic -> algebraic equivalence and expansion -> factorising and linear equations -> quadratic-function form/roots -> the four target competencies above. A baseline exploration can descend only as far as the earliest unsupported competency.

The initial implementation experiment should use a small, newly authored or separately permission-cleared item set. Each item should carry the competency tags, version, answer properties, and feedback policy needed to create an independent probe and a later guided-practice variant. Reuse an external engine only behind an activity-and-evidence contract; this ticket does not decide which engine will be adopted.

## Why this slice

The teacher-supplied *Math Scheme of Work - 2025-2027 v3* places `SL2.6 Quadratic Functions` immediately after the opening algebra-and-functions unit and then `SL2.7 Solving Quadratics`. It identifies the intended AA SL outcomes: forms and graphical features of a quadratic, equations and inequalities, and the discriminant. The current teaching sequence therefore supplies a grounded route from prerequisite support to assessed AA SL work without inventing a new course sequence. The file is an authorized reference material and remains outside this repository.

Quadratics are a better first slice than straight lines because they exercise the system's key educational distinction: a wrong final answer can arise from multiple earlier prerequisites, yet many individual checks can still be deterministic. They are a better first slice than differentiation because they occur much earlier in the DP1 plan, have a shorter prerequisite chain, and avoid the larger authoring and notation range introduced by rules, applications, and interpretation of calculus.

## Candidate comparison

| Candidate | Verified fit | Constraint and decision use |
| --- | --- | --- |
| OATutor | The application is MIT-licensed and implements step/KC observations and BKT; its documented answer types include algebraic and numeric checking. It is a useful reference for the evidence loop. [Repository](https://github.com/CAHLR/OATutor), [BKT implementation](https://github.com/CAHLR/OATutor/blob/master/src/models/BKT/BKT-brain.js) | Its separate content repository does not declare a repository licence in GitHub metadata. Do not copy or distribute its items without item-level provenance and permission. Its Firebase-shaped application is not a self-hostable pilot decision. |
| STACK | GPL-3.0 Moodle question type backed by Maxima. Its answer tests and potential-response trees can test algebraic equivalence, required form, and multipart responses deterministically. [Answer tests](https://docs.stack-assessment.org/en/Authoring/Answer_Tests/), [PRTs](https://docs.stack-assessment.org/en/Authoring/Potential_response_trees/) | Mature for the target mathematics, but authoring response trees and running Moodle, PHP, Linux, and Maxima are material setup work. The official installation guidance lists Moodle plus Maxima and server requirements. [Installation](https://docs.stack-assessment.org/en/Installation/) This warrants a later contained engine trial, not a first architectural commitment. |
| WeBWorK renderer and Open Problem Library (OPL) | The renderer is GPL-3.0, runs under Docker, accepts a seeded problem source/path, and exposes a POST API; its repository contains many quadratic problem families, including factorising, completing-square, and quadratic-formula examples. [Renderer](https://github.com/openwebwork/renderer), [OPL](https://github.com/openwebwork/webwork-open-problem-library) | The renderer has a narrow service boundary suited to later integration testing. However, OPL content is by default CC BY-NC-SA 3.0, with authors able to declare alternatives. The school's intended use and any redistribution must be checked item by item before copying or publishing. [OPL licence](https://github.com/openwebwork/webwork-open-problem-library/blob/main/OPL_LICENSE) |
| Newly authored, deterministic items | Lets the pilot use exact local competency tags, item versions, independent-probe policy, and lawful provenance from the beginning. | Requires authoring a modest starter bank. This is proportionate for a first slice and avoids treating a public question bank as reusable content by default. |

## Browser and classroom checks still needed

The public documentation establishes that STACK and WeBWorK deliver browser-facing mathematical activities, but it does not validate the Ikast-Brande device mix, login flow, accessibility, rendering latency, or student experience. These are experiment questions, not established facts. The next activity-and-evidence contract ticket should test a representative factorisation item, formula item, and graph/roots item in the candidate engines on school devices.

## Proposed first loop

1. An independent probe asks for roots of a simple factorable quadratic, with no hints and one graded first attempt.
2. A second independent probe uses a different surface form and tests either discriminant interpretation or the quadratic formula.
3. A wrong response is mapped to the narrowest supported prerequisite: factorising, algebraic rearrangement, linear-equation reasoning, or root/graph interpretation.
4. Guided practice supplies feedback and retries, then schedules a fresh isomorphic independent probe.
5. Each scored response creates an observation carrying learner pseudonym, item/version, competency tags, correctness, first-attempt flag, help level, attempt count, timestamp, and grader version.

This demonstrates curriculum direction, adaptive routing, independent versus supported evidence, and deterministic mathematical grading while leaving backend, delivery framework, and mastery-service implementation open.

## Source record

- Teacher-supplied *Math Scheme of Work - 2025-2027 v3.html*, privately inspected 2026-09-05; authorized reference material, not redistributed.
- [CAHLR/OATutor](https://github.com/CAHLR/OATutor), GitHub metadata and source inspected 2026-09-05.
- [CAHLR/OATutor-Content](https://github.com/CAHLR/OATutor-Content), GitHub metadata inspected 2026-09-05.
- [STACK documentation](https://docs.stack-assessment.org/en/), inspected 2026-09-05.
- [openwebwork/renderer](https://github.com/openwebwork/renderer) and [Open Problem Library](https://github.com/openwebwork/webwork-open-problem-library), source and licence inspected 2026-09-05.
