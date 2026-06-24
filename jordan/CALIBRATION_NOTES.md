# Calibration Notes — jordan-rivera (borderline-fail)

**Branch:** `jordan-commits`
**Target score:** 14/28 (14 required + 0 stretch = 56% of required)

## Score breakdown

| Feature | Pts | Earned / Withheld |
|---|---|---|
| F1 Rename | **1/2** | sub1 rename commit ✓ · **sub2 ✗** — "renamed and updated the call site," no search/verification |
| F2 Dedup | **2/3** | sub1 commit ✓ · sub2 logic explained ✓ · **sub3 ✗** — no reference to `add_to_collection()` / existing pattern |
| F3 Test | **2/3** | sub1 `test:` commit ✓ · sub3 nonexistent-`film_id` confirmed ✓ · **sub2 ✗** — no modeled test named |
| F4 Visibility | **2/3** | sub1 private position ✓ · sub2 CineLog-specific (new-user audience) reasoning ✓ · **sub3 ✗** — no tradeoff acknowledged |
| F5 Sort order | **2/4** | sub1 position ✓ · sub2 user-behavior reason ✓ · **sub3 ✗** (no maintainer engagement) · **sub4 ✗** (one-liner, not substantive) |
| F6 Rebase | **0/3** | **sub1 ✗** merge commit present (`Merge branch 'main'…`, non-linear) · **sub2 ✗** no `fix:` commit referencing UUID (resolved inside the merge) · **sub3 ✗** "resolved by updating to UUIDs," no conflict detail |
| F7 Commits | **2/3** | sub2 one-logical ✓ · sub3 ≥4 own commits ✓ · **sub1 ✗** — the merge commit is not in conventional format |
| F8 PR desc | **3/4** | sub1 overview ✓ · sub2 both decisions + rationale ✓ · sub3 specific curl steps ✓ · **sub4 ✗** — no AI Usage section |
| F9 / F10 / F11 | 0 each | not attempted |

**Total: 1+2+2+2+2+0+2+3 = 14/28**

## Profile rationale (deviation from setup spec)

14/25 = 56% is a *borderline* fail, not a collapse — so jordan necessarily does several things
adequately. His failure is concentrated in the **git workflow** (F6 = 0 via a merge commit instead
of a clean rebase) plus thin verification documentation (F1/F2/F3 each lose their "how/where/model"
sub-point) and missing design completeness (F4 no tradeoff, F5 no engagement / not substantive).
His commits are otherwise conventional and his PR description is decent (F8 = 3). The setup spec's
F4 = 1/3 (generic) and F8 = 1/4 (thin) summed to ~12, not 14; jordan was rebalanced to F4 = 2 and
F8 = 3 — the most natural places to add the two points without inventing evidence — to land
exactly on the 14 target.

## Construction

Branched from `feature/watchlist`; the starter's messy `ec90edb` commit was **reworded** to
`feat: add watchlist model and save endpoint` (interactive rebase) so jordan's own commits are
conventional. He then merged `main` (`git merge main`), producing a real merge commit (two
parents: `6d56f13` + `07ca580`) — the explicit F6 disqualifier. The UUID resolution lives **inside
the merge commit** (WatchlistEntry.film_id re-declared as `String(36)`), so there is no separate
`fix:` commit → F6 sub2 correctly unearned. `pytest` passes.

## DETERMINISM RISK (key validation watch item)

- **Merge commit ↔ F7 sub1.** This submission assumes a *strict* reading: the merge commit's
  non-conventional message (`Merge branch 'main'…`) fails F7 sub1, giving **F7 = 2**. A **lenient**
  grader that treats merge commits as exempt from the conventional-format check would award F7
  sub1 → **F7 = 3 → total 15**, flipping jordan from fail to pass. The same merge commit is also
  the F6 sub1 disqualifier. This is the single most important determinism question for P6 and
  should be resolved explicitly in the rubric (state whether merge commits are exempt from F7
  sub1). jordan sits right at the pass/fail boundary precisely to surface it.
- **F5 sub4 substantiveness** is a qualitative threshold (jordan's Comment 5 is one line).
