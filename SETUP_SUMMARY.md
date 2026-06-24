# AI201 P6 (CineLog) — Calibration Setup Summary

**Date:** 2026-06-23
**Session:** Claude Code (AI-grading workflow, step 1 — show-file hygiene + calibration submissions)
**Repo:** `codepath/ai201-p6-submissions` (fork of `jamjamgobambam/ai201-project6-cinelog-starter`)

---

## STRUCTURE UPDATE (2026-06-24) — subfolder layout + preserved history

To give graders/humans the familiar monorepo browsing layout **without losing the real
per-branch commit history** P6 is graded on, each persona branch was rewritten with
`git filter-repo --to-subdirectory-filter <persona>`: the branch's entire real history now lives
under a **`<persona>/` subfolder**, and a tip commit adds stub `README.txt` folders for the other
four personas plus a branch-level pointer README. `main` was rebuilt as a pure index: top-level
`README.md` + this file + five stub folders (root starter removed; it remains on `feature/watchlist`).

- Grader input is now **`tree/<persona>-commits/<persona>`** (e.g. `…/tree/maya-commits/maya`).
- `git log -- <persona>` on each branch returns exactly that persona's real history (the
  stub/index tip commit touches only sibling paths, so it does not appear in the subfolder log).
- Branch history rewrite means the persona-branch commit hashes changed and were force-pushed; the
  commit *messages/topology* (what F1/F2/F3/F6/F7 grade) are identical to the originals, now under
  the subfolder. jordan's and tyler's merge commits survived the move.

---

## Starter repo baseline

Confirmed two branches in the starter, both carried into this fork:

- **`main`** — post-refactor: `Film.id` and `CollectionEntry.film_id` are `db.String(36)` UUID;
  `WatchlistEntry` does **not** exist on `main` (the watchlist is the feature under review).
  Commits: `feat: initial CineLog API…` → `refactor: migrate film IDs from integer to UUID`.
- **`feature/watchlist`** — pre-refactor: `Film.id` and `WatchlistEntry.film_id` are `Integer`;
  `save_to_watchlist()` not yet renamed. Commits: `feat: initial…` → `added watchlist model and
  endpoint fixed a bug more changes` (the deliberately messy commit) → `fix: update film retrieval
  method to use db.session.get…`.

Files provided: `app.py`, `models.py` (User/Film/CollectionEntry[/WatchlistEntry on feature]),
`services/collection_service.py`, `services/watchlist_service.py` (feature branch),
`routes/{films,collection,watchlist/watchlist}.py`, `tests/test_collection.py`,
`CONTRIBUTING.md` (conventional-commit rules), `README.md`, `requirements.txt`.

Key finding that shaped construction: the watchlist commits on `feature/watchlist` never modify
`models.py` (the `WatchlistEntry` model lives in the shared base commit), and `main`'s refactor
*removed* `WatchlistEntry`. So a literal `git rebase feature/watchlist onto main` produces **no
automatic git conflict** and silently drops `WatchlistEntry`. The UUID "conflict" is therefore
reconstructed as an explicit model edit (Integer → String(36)) in each persona's history.

---

## Task 1 — Show-file hygiene (`ai201/show/show_6.md`)

**No changes needed — clean on both checks. No PR opened.**

- **Dedup:** No duplicated blocks. The Features list, the per-milestone steps, and the "Submitting"
  recap cover the same features at different altitudes (intended scaffolding), not repeated copy.
- **Grader-language:** No banned terms. The only two "grader" mentions ("graders who read many of
  these submissions," "a grader who hasn't seen the codebase") are the acceptable generic form per
  the validation rubric §5.

## Quick gate (validation rubric §1–5) against `ai_grading_6.md` — PASS

- §1 Artifacts: `grading_raw.yaml`, `ai_grading_6.md`, `grading/grading_6.md`, `pages/grading.md`
  all present; every criterion has grader instructions.
- §2 Sync: feature titles / criterion text / point values consistent; totals 25 + 3 = 28 match
  `pages/grading.md`. **Advisory:** `grading_raw.yaml`'s `legacy_grading_instructions` still say
  "the commit history screenshot includes…" while the structured `grader_instructions` correctly
  redirect to the actual commit log. Functionally equivalent (both award on a rename/dedup/test
  commit existing); the structured side is what the AI uses. Not blocking.
- §3 Readable channel: every commit-history criterion redirects the unreadable `git log`
  screenshot to "the actual commit log on `feature/watchlist`"; PR description is also committed to
  `pr-response.md` so it is readable. Sound — **provided submissions carry real git history**
  (they do; see below).
- §4 Determinism: binary stretch features are binary ("No partial credit"); partial criteria have
  explicit sub-points.
- §5 Student fairness: all six comments + commit-history + PR-description + AI-usage requirements
  are disclosed in `show_6.md`; no grading-mechanism language.

§6/§7 advisory: see determinism risks below.

---

## Task 2 — Calibration submissions

One branch per persona (real, independent git history), because the majority of P6 criteria
(F1, F2, F3, F6, F7, F9, F10, F11) are scored off the actual commit log. Subfolders on a shared
branch cannot carry five divergent histories.

| Persona | Branch | Tier | Target | Per-feature (F1..F8 + F9/F10/F11) |
|---|---|---|---|---|
| maya-chen | `maya-commits` | exemplar | **28/28** | 2,3,3,3,4,3,3,4 + 1,1,1 |
| derek-okafor | `derek-commits` | strong | **25/28** | 2,3,3,3,3,3,3,4 + 1,0,0 |
| priya-nair | `priya-commits` | borderline-pass | **18/28** | 1,2,2,3,2,2,3,3 + 0,0,0 |
| jordan-rivera | `jordan-commits` | borderline-fail | **14/28** | 1,2,2,2,2,0,2,3 + 0,0,0 |
| tyler-walsh | `tyler-commits` | minimal | **0/28** | 0,0,0,0,0,0,0,0 + 0,0,0 |

### Branch verification (`git log main..<branch>`)

- `maya-commits`: 9 commits, 0 merges, all conventional, linear. `pytest` passes.
- `derek-commits`: 7 commits, 0 merges, all conventional, linear. `pytest` passes.
- `priya-commits`: 6 commits, 0 merges, all conventional, linear. `pytest` passes.
- `jordan-commits`: 7 commits incl. **1 merge commit** (`Merge branch 'main'…`); own commits
  conventional. `pytest` passes.
- `tyler-commits`: 5 commits incl. **1 merge commit**; messy/freeform messages; `save_to_watchlist`
  un-renamed; no dedup/test. (Code intentionally broken — 0 credit.)

Every persona folder/branch was built from the starter baseline (not from scratch): personas
branched from `main` (maya/derek/priya, built the watchlist feature as clean conventional commits
— equivalent end-state to a rebase-and-reword) or from `feature/watchlist` (jordan/tyler, to
produce a real merge commit; jordan's messy starter commit was reworded, tyler's was kept).

---

## Deviations from the setup spec (all to hit the headline targets — pre-approved approach)

1. **No "merge all personas into `main` as subfolders."** The spec's subfolder model is incoherent
   with the branch-per-persona structure (personas are whole-repo variants at the same paths;
   merging them yields conflicts, not folders). `main` is instead a clean index (`README.md` +
   `SETUP_SUMMARY.md`); review each persona by checking out its branch.
2. **Passing personas built linearly on `main`** rather than via a literal rebase + reword of the
   messy commit, because that rebase produces no git conflict and drops `WatchlistEntry` (see
   baseline finding). End-state (commit log, diffs, PR doc) is identical to a clean
   rebase-and-reword; the `fix:` UUID commit shows a clean `Integer → String(36)` diff.
3. **Sub-point reconciliations** (spec's per-sub-point prose didn't sum to the stated targets):
   - **derek F5 = 3/4** (spec prose implied 4/4 → would total 26). Withheld **sub3** (engagement):
     derek argues recency for his own reason and never addresses the maintainer's quoted line.
   - **priya = 18** via **F5 = 2/4** + **F7 = 3/3** (spec's F5 4/4 + F6 2/3 summed to 19 and required
     a bundled commit that would itself fail F7 sub2). Rebuilt with clean unbundled commits.
   - **jordan = 14** via **F4 = 2/3** and **F8 = 3/4** (spec's F4 1/3 + F8 1/4 summed to ~12). 56%
     is a borderline fail, so jordan necessarily does several things adequately; failure is
     concentrated in F6 (merge commit) + thin verification docs + missing tradeoff/engagement.
4. **All passing personas' histories are fully conventional** (the spec's "keep the messy `ec90edb`
   commit" would have failed F7 sub1/sub2 for every passing persona). maya/derek/priya never carry
   it; jordan's was reworded; only tyler keeps it.

---

## Grading-file ambiguities & DETERMINISM RISKS (first items for the validation step)

1. **Merge commit ↔ F7 sub1 (jordan, highest priority).** jordan is engineered to sit on the
   pass/fail line. A **strict** grader counts the merge commit's non-conventional message as
   failing F7 sub1 → F7 = 2 → **jordan = 14 (fail)**. A **lenient** grader exempting merge commits
   → F7 sub1 earned → F7 = 3 → **jordan = 15 (pass)**. The rubric should state explicitly whether
   merge commits are exempt from the conventional-format check. Same merge commit is the F6 sub1
   disqualifier.
2. **F7 sub3 "≥4 commits reflecting the distinct changes made" (tyler).** Raw-commit-count reading
   could award sub3 to tyler (junk + merge + docs commits) → tyler = 1/28. Intended reading keys
   off *meaningful* distinct changes (rename/dedup/test/rebase), none of which exist → 0. Confirm
   the grader uses the qualifier, not a raw count.
3. **F5 sub3 vs sub4 boundary (derek, priya).** "Directly engages the maintainer's quoted point"
   (sub3) vs "substantive enough to push back on" (sub4) are adjacent qualitative thresholds. derek
   is written to pass sub4 but miss sub3 (argues recency for a different reason, never cites the
   maintainer's line); priya misses both (one-line Comment 5). A grader could blur these.
4. **F8 sub4 AI-Usage absence (priya, jordan, tyler).** The section is entirely absent in these
   submissions (not a vague mention). Grader must award 0 deterministically; a hallucinated AI
   mention would be a grader defect.
5. **F6 sub2 reliance on a `fix:`-prefixed UUID commit.** maya/derek/priya earn it via an explicit
   `fix:` commit whose diff shows `Integer → String(36)`. jordan/tyler resolve UUID inside the
   merge (no `fix:` commit) → sub2 correctly unearned.

---

## Open question carried from the setup spec

- **PASS-THRESHOLD-UNKNOWN:** No numeric pass threshold for P6 is documented in `ai_grading_6.md`,
  `grading_6.md`, or `pages/grading.md`. The borderline-pass (priya 18) vs borderline-fail
  (jordan 14) labels assume ~72% as the de facto pass line. Confirm the correct threshold before
  finalizing pass/fail interpretation.

---

## Handoff

**Ready for grader validation.** Next step: run each persona through the web-UI grader **pointed at
the persona's subfolder on its branch** — `tree/maya-commits/maya`, `tree/derek-commits/derek`,
`tree/priya-commits/priya`, `tree/jordan-commits/jordan`, `tree/tyler-commits/tyler` — and paste
the output into the validation prompt. Compare against the targets above and the per-sub-point
breakdowns in each `<persona>/CALIBRATION_NOTES.md`; the five determinism risks above are the first
things to check.
