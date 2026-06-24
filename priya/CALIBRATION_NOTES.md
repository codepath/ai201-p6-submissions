# Calibration Notes — priya-nair (borderline-pass)

**Branch:** `priya-commits`
**Target score:** 18/28 (18 required + 0 stretch = 72% of required)

## Score breakdown

| Feature | Pts | Earned / Withheld |
|---|---|---|
| F1 Rename | **1/2** | sub1 rename commit ✓ · **sub2 ✗** — Comment 1 says "renamed and updated the call site" but describes no search method / no verification that none were missed |
| F2 Dedup | **2/3** | sub1 commit ✓ · sub2 logic explained ✓ · **sub3 ✗** — never references `add_to_collection()` or any existing pattern |
| F3 Test | **2/3** | sub1 `test:` commit ✓ · sub3 nonexistent-`film_id` case confirmed ✓ · **sub2 ✗** — does not name the modeled test in `test_collection.py` |
| F4 Visibility | 3/3 | public position; CineLog community reasoning; tradeoff acknowledged |
| F5 Sort order | **2/4** | sub1 position ✓ · sub2 user-behavior reason ✓ · **sub3 ✗** (no engagement w/ maintainer's quoted line) · **sub4 ✗** (one-sentence, not substantive) |
| F6 Rebase | **2/3** | sub1 linear ✓ · sub2 `fix:` UUID commit + Integer→String diff ✓ · **sub3 ✗** — "rebased and updated film IDs to UUIDs" gives no detail on what conflicted |
| F7 Commits | 3/3 | 6 commits, all conventional, one logical change each, ≥4 |
| F8 PR desc | **3/4** | sub1 overview ✓ · sub2 both decisions + rationale ✓ · sub3 specific curl steps ✓ · **sub4 ✗** — no AI Usage section anywhere in the doc |
| F9 / F10 / F11 | 0 each | not attempted |

**Total: 1+2+2+3+2+2+3+3 = 18/28**

## Notes on the design (deviation from setup spec)

The setup spec gave priya F5 4/4 *and* F6 2/3, which sums to 19, not 18. It also routed priya's
UUID fix through a *bundled* `test:`-prefixed commit, which would simultaneously fail F7 sub2
(bundling) — making the spec's F7 2/3 unreachable alongside F6 sub2. Per "build to targets,
document deviations," priya was rebuilt with **clean, unbundled commits** (so F7 = 3/3, which is
fine — commit hygiene is mechanical and easy even for a borderline-pass student) and the 18 is
reached instead via **F5 = 2/4** (thin, non-engaging Comment 5). This is the most deterministic
distribution: every withheld sub-point is a clean structural absence, and there is no
bundled-commit ambiguity.

Every absence is unambiguous (no search method, no pattern reference, no named model test, no
conflict detail, no AI Usage section). priya's pass is earned on the strength of full F4, full F7,
and solid-but-incomplete F2/F3/F6/F8.

## Determinism risks

- **F8 sub4 (AI Usage):** the section is entirely absent (not a vague one). Grader should award 0
  on sub4 deterministically. If a grader hallucinates an AI mention, that is a grader defect to
  catch in validation.
- **F5 sub4 substantiveness** is a qualitative threshold; priya's Comment 5 is deliberately ~1
  sentence of reasoning so it falls clearly below "substantive enough for a maintainer to push
  back on." Borderline by design — a key validation watch item.
