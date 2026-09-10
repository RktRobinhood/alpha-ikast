# Mastery-path UI prototype

> THROWAWAY PROTOTYPE — do not treat this as production architecture or approved policy.

Three variants of one AA SL learning session, switchable with `?variant=A`,
`?variant=B`, or `?variant=C` on the same prototype route.

The prototype asks: **What should students and teachers see and do so that a
responsive mastery path is understandable, steerable, and coachable without
requiring approval of every activity?**

All names and evidence are synthetic. The learner-state values and intervention
signals are illustrative, not a resolved mastery policy.

## Run

From the repository root:

```powershell
python -m http.server 4187 --bind 127.0.0.1 --directory planning/mastery-path-ui-prototype
```

Then open <http://127.0.0.1:4187/?variant=A>.
