# Calibration Notes — tyler-walsh (minimal / zero anchor)

**Branch:** `tyler-commits`
**Target score:** 0/28 (0% of required)

## Score breakdown — every feature scores 0

| Feature | Pts | Why 0 |
|---|---|---|
| F1 Rename | 0/2 | No rename commit; `save_to_watchlist()` is still named that in the service; no Comment 1 entry |
| F2 Dedup | 0/3 | No dedup commit; no existing-entry check in the watchlist source; no Comment 2 entry |
| F3 Test | 0/3 | No `test:` commit; no `tests/test_watchlist.py`; no Comment 3 entry |
| F4 Visibility | 0/3 | Pure deferral — "I think either could work, whatever you prefer." No position, no reasoning |
| F5 Sort order | 0/4 | Pure deferral — "Whichever sort order you think is best." No position, no reasoning, no engagement |
| F6 Rebase | 0/3 | Merge commit present (`Merge branch 'main' into tyler-commits`, non-linear); no `fix:` UUID commit; no Comment 6 entry |
| F7 Commits | 0/3 | Freeform messages ("did the stuff", the messy starter commit "added watchlist model and endpoint fixed a bug more changes"); not conventional; no commits reflecting the project's distinct changes |
| F8 PR desc | 0/4 | One-sentence overview only ("This PR adds a watchlist feature."); no design decisions; no testing steps; no AI Usage section |
| F9 / F10 / F11 | 0 each | not attempted |

**Total: 0/28**

## Construction

Branched from `feature/watchlist` (the messy starter commit `ec90edb` is **kept, not reworded** —
tyler did no history cleanup). One freeform `did the stuff` commit (a trivial README touch, no
watchlist work). Then `git merge main` → merge commit (two parents `a0d6cf4` + `07ca580`), the
explicit F6 disqualifier; the UUID refactor was not deliberately resolved. `save_to_watchlist()`
is left un-renamed. No dedup, no test file. The PR doc takes no positions.

## DETERMINISM RISK (validation watch item)

- **F7 sub3 (≥4 commits "reflecting the distinct changes made").** `git log main..HEAD` shows
  several raw commits (the messy starter commit, `did the stuff`, the merge, the docs commit). A
  grader counting *raw commits* could award sub3 (→ F7 = 1, tyler = 1/28). The intended reading is
  the criterion's qualifier — "reflecting the distinct changes made across the project (rename,
  dedup, test, rebase update)" — **none** of which exist here, so sub3 = 0 and F7 = 0. Worth
  confirming the grader keys off *meaningful* distinct changes, not a raw count. Even under the
  lenient reading tyler scores 1/28 and remains the clear zero-anchor.
