# Calibration Notes — derek-okafor (strong)

**Branch:** `derek-commits`
**Target score:** 25/28 (24 required + 1 stretch = 100% of required)

## Score breakdown

| Feature | Pts | Notes |
|---|---|---|
| F1 Rename | 2/2 | rename commit + diff; PR doc describes project-wide search, confirms sole call site |
| F2 Dedup | 3/3 | dedup commit + diff; logic explained; names `add_to_collection()` pattern |
| F3 Test | 3/3 | `test:` commit + diff; names modeled test; confirms nonexistent-`film_id` case |
| F4 Visibility | 3/3 | clear **private** position; CineLog onboarding-specific reasoning; tradeoff acknowledged (choice differs from maya; F4 grades reasoning, not the choice) |
| **F5 Sort order** | **3/4** | sub1 position ✓, sub2 user-behavior argument ✓, **sub3 ✗**, sub4 substantive ✓ |
| F6 Rebase | 3/3 | linear; `fix:` UUID commit + Integer→String(36) diff; conflict described |
| F7 Commits | 3/3 | 6 commits, all conventional, one logical change each, ≥4 |
| F8 PR desc | 4/4 | overview; both decisions w/ rationale; specific curl steps; AI Usage section |
| F9 remove() | 1/1 | `feat:` commit + diff + test; PR doc covers not-found (False) behavior + pattern |
| F10 2nd test | 0/1 | not attempted — no second `test:` commit, no extra test, no PR-doc entry |
| F11 toggle | 0/1 | not attempted — no `public` parameter, no commit, no PR-doc entry |

**Total: 25/28**

## The one withheld point (F5 sub3) — deliberate, structural

Derek's Comment 5 takes a clear date-added position (sub1), argues from user behavior — "a
watchlist functions as a queue… people act on the most recent additions first" (sub2), and is a
real, multi-sentence argument a maintainer could push back on (sub4). What it **does not do** is
engage the maintainer's *specific* stated point — the line *"Most users want to see what they
added recently."* Derek never quotes or addresses that sentence; he argues recency in the
abstract. That is the single, clean miss → **sub3 not earned**.

This is the chosen withhold to land derek at 25 (the setup spec's prose described all four F5
sub-points as earned, which would total 26; engagement is the most structural sub-point to
withhold — quote-present vs. quote-absent — so it is the most deterministic choice). Contrast with
maya, who explicitly quotes the maintainer and adds the `get_collection` precedent (F5 4/4).

## Construction method

Built linearly on `main` (see maya's notes for why a literal rebase produces no git conflict). End
state — commit log, diffs, PR doc — is identical to a clean rebase-and-reword. `pytest` passes.

## Determinism risks

- **F5 sub3 vs sub4 boundary:** a lenient grader could read derek's recency argument as implicitly
  engaging the maintainer (the maintainer *also* argued recency) and award sub3 → 26/28. The
  submission is written so derek argues recency for a *different* reason (queue consumption) and
  never references the maintainer's sentence, to keep the miss clean. Watch this in validation.
