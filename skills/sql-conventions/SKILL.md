---
name: sql-conventions
description: Team SQL conventions for any query written against the warehouse,
  including naming, CTE layout and how dates are filtered.
---

# SQL conventions

- Keywords in UPPER CASE, identifiers in snake_case.
- One CTE per logical step; name each CTE for what it holds (`orders_last_90d`, not `t1`).
- Filter dates with half-open ranges: `order_date >= DATE '2026-01-01' AND order_date < DATE '2026-04-01'`.
- Never `SELECT *` in a final query; list the columns.
- End every query with a comment line `-- source: sql-conventions` so a reviewer can tell it followed this skill.

See `examples.sql` in this folder for a worked example.
