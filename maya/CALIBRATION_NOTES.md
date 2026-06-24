# Calibration Notes — maya-chen (exemplar)

**Branch:** `maya-commits`
**Target score:** 28/28 (25 required + 3 stretch = 112% of required)

## Score breakdown (every sub-point earned)

| Feature | Pts | Evidence |
|---|---|---|
| F1 Rename | 2/2 | `fix: rename…` commit + diff; PR doc Comment 1 describes find-all-references search and confirms `watchlist.py` was the only call site |
| F2 Dedup | 3/3 | `fix: add deduplication…` commit + diff (existing-entry check, early return); PR doc explains the check and names `add_to_collection()` as the pattern |
| F3 Test | 3/3 | `test:` commit + `tests/test_watchlist.py` diff; PR doc names `test_add_to_collection_nonexistent_film_raises` as the model and confirms the nonexistent-`film_id` case |
| F4 Visibility | 3/3 | Clear `public=True` position; CineLog-specific community-discovery argument; acknowledges privacy tradeoff |
| F5 Sort order | 4/4 | Clear date-added position; CineLog recency argument; directly engages maintainer's quoted line with corroborating evidence (`get_collection` precedent); substantive |
| F6 Rebase | 3/3 | Linear history, no merge commits; `fix: update WatchlistEntry.film_id to UUID…` commit + diff (Integer→String(36)); PR doc describes integer-vs-UUID conflict and the file change |
| F7 Commits | 3/3 | All 8 commits conventional; one logical change each; ≥4 commits |
| F8 PR desc | 4/4 | Plain-language overview; both decisions named w/ rationale; step-by-step curl instructions; AI Usage section with specific prompts |
| F9 remove() | 1/1 | `feat: add remove_from_watchlist…` commit + diff + test; PR doc covers not-found (returns False) behavior and pattern alignment |
| F10 2nd test | 1/1 | `test: add duplicate-entry edge case…` commit + diff; PR doc explains the duplicate-entry choice and why |
| F11 toggle | 1/1 | `feat: add public parameter…` commit + diff (`public=True` in signature); PR doc covers behavior, default, caller usage |

**Total: 28/28**

## Construction method (deviation from setup spec)

The setup file specified branching from `feature/watchlist`, rebasing onto `main`, and rewording
the starter's messy `ec90edb` commit. Because rebasing `feature/watchlist` onto `main` produces
no automatic git conflict (the watchlist commits never touch `models.py`; `main`'s refactor
silently drops `WatchlistEntry`), this branch was instead built **linearly on top of `main`** as
a sequence of clean conventional commits — the identical end-state a successful interactive
rebase + reword produces. The grader reads commit log + diffs + PR doc, all of which are
identical to the rebase-and-reword outcome. The `fix:` UUID commit shows a clean
`Integer → String(36)` diff for the F6 cross-check.

## Determinism risks

None significant — every sub-point keys off a structural signal (commit present, function in
diff, named reference in PR doc, position taken). This is the unambiguous full-credit anchor.
