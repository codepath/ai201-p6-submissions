# AI201 P6 — CineLog Calibration Submissions

Calibration submissions for **AI201 Project 6 (CineLog — Simulated Code Review)**, used to
validate the AI grader against known target scores. Forked from
[`jamjamgobambam/ai201-project6-cinelog-starter`](https://github.com/jamjamgobambam/ai201-project6-cinelog-starter).

Total points: **28** (25 required + 3 stretch).

| Persona | Branch | Tier | Target Score | % of Required |
|---------|--------|------|-------------|---------------|
| maya-chen | `maya-commits` | exemplar | 28/28 | 112% |
| derek-okafor | `derek-commits` | strong | 25/28 | 100% |
| priya-nair | `priya-commits` | borderline-pass | 18/28 | 72% |
| jordan-rivera | `jordan-commits` | borderline-fail | 14/28 | 56% |
| tyler-walsh | `tyler-commits` | minimal | 0/28 | 0% |

## How to run the grader

P6 is graded largely off the **real git commit history** of the submission branch (rename / dedup
/ test / rebase / merge commits, conventional format, ≥4 commits). **Point the grader at each
individual persona branch** — e.g. branch `maya-commits` of `codepath/ai201-p6-submissions`. Each
branch is a self-contained submission: the watchlist source, `tests/`, `pr-response.md`, and the
branch's own commit history. The grader reads:

- `pr-response.md` (PR Response Doc + PR description, committed at repo root)
- the branch's actual commit log (`git log` on that branch) — **not** an embedded screenshot
- the changed watchlist source (`models.py`, `services/watchlist_service.py`,
  `routes/watchlist/watchlist.py`, `tests/test_watchlist.py`)

Each branch also carries a `CALIBRATION_NOTES.md` with the full per-sub-point score breakdown and
any determinism risks.

**Do not grade `main`.** `main` holds only this index, `SETUP_SUMMARY.md`, and the original
starter (`feature/watchlist` plus the post-refactor `main` state). The persona submissions live on
their own branches; review them by checking out each branch, not from `main`.

## Branch baseline

- `main` — post-refactor starter state: `Film.id` is `String(36)` UUID; no watchlist.
- `feature/watchlist` — pre-refactor starter state: `Film.id` / `WatchlistEntry.film_id` are
  `Integer`; `save_to_watchlist()` not yet renamed; contains the deliberately messy starter commit
  `added watchlist model and endpoint fixed a bug more changes`.

Each persona branch is the starter plus that persona's targeted work; see `SETUP_SUMMARY.md` for
the exact construction method and deviations from the setup spec.
