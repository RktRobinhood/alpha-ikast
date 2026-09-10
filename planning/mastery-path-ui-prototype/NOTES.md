# Prototype reaction notes

Question: What should students and teachers see and do in one rough end-to-end
AA SL learning session?

Status: hybrid direction confirmed by the teacher on 2026-09-06. This is a design
record for a throwaway prototype, not an approved product specification.

## Teacher reaction captured on 2026-09-06

- Keep a clean, focused aesthetic; the interface could otherwise become cluttered.
- Use the school identity and official logo. The teacher confirmed on 2026-09-06
  that this school initiative has permission to use it. The prototype references
  the authoritative SVG served by `https://www.ikast-gym.dk/Files/Templates/
  Designs/espresso-v4/_assets/img/IBG_logo_RGB.svg`; no copy is committed.
- Do not imply that free-form algebra steps can be assessed instantly by AI.
  Local deterministic feedback, AI-assisted feedback, latency, and whole-class
  concurrency must be evaluated separately.
- Integrate Alpha's 25-minute Pomodoro-style focus blocks and breaks, adapted to
  the bridge phase rather than copying its whole-school schedule.
- Adopt an established structured mathematics input rather than expecting plain
  text entry for exponents, fractions, roots, and other notation.
- The competency map is promising. Start from the official IB mathematics mind
  map and the Open Alpha concept-map shell, then add AA SL prerequisite detail
  only where the curriculum mapping requires it.
- Design the primary structured-use experience for larger screens, while keeping
  a deliberate mobile subset for orientation, short practice, progress, and
  teacher/student check-ins on the go.
- Begin from existing open-source work, preserve upstream behavior as the
  baseline, and contribute validated improvements back under a suitable licence.

## Confirmed synthesis

Use a hybrid rather than a single winning mockup:

1. **Focused session is the default student surface** — one mathematical move,
   one visible 25-minute block, and little surrounding chrome.
2. **Competency map is the orientation surface** — available on demand, not
   permanently surrounding every question.
3. **Check-in timeline is the teacher surface** — actionable evidence and the
   student's recent attempts, not an approval queue or dense analytics dashboard.
4. **Guided workspace becomes secondary** — useful for choosing between equally
   suitable activities and explaining why, but not the always-visible shell.

## Upstream anchors found

- Alpha School publicly describes four 25-minute Pomodoro learning blocks and
  short focus cycles with breaks.
- Open Alpha contains a learner concept-map shell and curriculum prerequisite
  graph, but no timer implementation was found in its current repository tree.
- The official IB mathematics mind map is a curriculum-orientation source, not
  yet a prerequisite graph.
- Numbas provides open-source mathematical-expression input and deterministic
  marking; MathLive provides a structured math field, virtual keyboard, and
  MathJSON serialization. These are candidates for trial, not selections.
