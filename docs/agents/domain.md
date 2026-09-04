# Domain documentation

Alpha Ikast currently uses a single domain context.

## Before exploring or changing the project

- Read `CONTEXT.md` at the repository root.
- Read relevant decisions under `docs/adr/` if that directory exists.
- Use the glossary's canonical vocabulary and avoid terms it explicitly rejects.

If a new domain concept is necessary, use the domain-modeling process to define it. Create an ADR only for a consequential, hard-to-reverse decision arising from a genuine trade-off.

## Layout

```text
/
├── CONTEXT.md
├── docs/
│   ├── agents/
│   └── adr/        # created lazily when the first ADR is warranted
└── ...
```

