# sage-test-skills-public

Test fixtures for Domino Sage's Project skills and custom tools (issues #619–#625).

- `skills/` — three skills. `chart-captions` deliberately spells its file `skill.md` in lower case;
  `sql-conventions` carries a binary `logo.png` that Sage should skip and report.
- `tools/` — `fx_rate.ts` (TypeScript), `margin.py` (Python, read-only, errors on a negative cost),
  `write_note.py` (Python, writes a file, not read-only).

This README is outside every skill folder, so Sage should ignore it.
