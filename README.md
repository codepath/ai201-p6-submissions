# AI201 P6 — CineLog Calibration Submissions

Calibration submissions for **AI201 Project 6 (CineLog — Simulated Code Review)**, used to
validate the AI grader against known target scores. Forked from
[`jamjamgobambam/ai201-project6-cinelog-starter`](https://github.com/jamjamgobambam/ai201-project6-cinelog-starter).
Total points: **28** (25 required + 3 stretch).

## Structure (both monorepo browsing *and* real commit history)

Each persona is a **branch**, and on that branch the persona's full submission lives in a
**`<persona>/` subfolder** (so it browses like a monorepo) while the branch carries that persona's
**real git commit history** (which is what P6 is largely graded on — rename / dedup / test /
rebase / merge commits, conventional format, ≥4 commits).

- On each persona branch: `<persona>/` holds the submission; the other four folders are stub
  `README.txt` files pointing to their branches.
- On `main` (this branch): **all five** folders are stubs — `main` is just an index.

## Grader input

Point the grader at each persona's subfolder on its branch:

| Label | URL |
|---|---|
| Maya (Persona) | https://github.com/codepath/ai201-p6-submissions/tree/maya-commits/maya |
| Derek (Persona) | https://github.com/codepath/ai201-p6-submissions/tree/derek-commits/derek |
| Priya (Persona) | https://github.com/codepath/ai201-p6-submissions/tree/priya-commits/priya |
| Jordan (Persona) | https://github.com/codepath/ai201-p6-submissions/tree/jordan-commits/jordan |
| Tyler (Persona) | https://github.com/codepath/ai201-p6-submissions/tree/tyler-commits/tyler |

The grader reads, within each `<persona>/`: `pr-response.md` (PR Response Doc + PR description),
the persona's source (`models.py`, `services/watchlist_service.py`, `routes/watchlist/watchlist.py`,
`tests/test_watchlist.py`), and the branch's **actual commit log** (`git log` — not an embedded
screenshot). Each `<persona>/` also has a `CALIBRATION_NOTES.md` with the full per-sub-point
breakdown and determinism risks.

**Target scores are intentionally omitted here** so they don't bias grading — they live in each
persona's `CALIBRATION_NOTES.md` and in `SETUP_SUMMARY.md` (28 / 25 / 18 / 14 / 0 for
maya / derek / priya / jordan / tyler).

**Do not grade `main`** — it has no submission content, only stubs and this index.

## Starter baseline

Forked from the CineLog starter, which had `main` (post-refactor: `Film.id` is UUID) and
`feature/watchlist` (pre-refactor: `Film.id` / `WatchlistEntry.film_id` are `Integer`;
`save_to_watchlist()` not yet renamed; the deliberately messy starter commit
`added watchlist model and endpoint fixed a bug more changes`). See `SETUP_SUMMARY.md` for the
exact construction method and deviations.
