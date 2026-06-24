# PR Response Doc — CineLog Watchlist Feature

## AI Usage

I used an AI assistant in two specific, bounded ways:

1. **Codebase orientation (Milestone 1).** Before reading the review comments, I pasted
   `services/collection_service.py` and asked: *"Summarize what this file is responsible for,
   what each function does, and what `add_to_collection()` returns when the film_id doesn't
   exist."* I used the summary to locate the existing deduplication pattern, then verified it
   against the actual code before relying on it.
2. **Commit-format hygiene (Milestone 4).** After my interactive rebase I pasted my
   `git log --oneline` output and asked: *"Do these messages follow the Conventional Commits
   spec, and is any single commit bundling more than one logical change?"* It flagged nothing,
   and I re-checked the spec myself before force-pushing.

For Comments 4 and 5 I wrote my own positions first, then asked the AI *"what counterargument
would a careful reviewer raise against this?"* — the public-default counterargument it raised
(privacy for new users) was one I had already addressed, so I left my reasoning as written.

## Comment 1 — Rename

**What I did:** Renamed `save_to_watchlist()` to `add_to_watchlist()` in
`services/watchlist_service.py` to match the project's `verb_to_noun` convention
(`add_to_collection`, `remove_from_collection`).

**How I verified:** I ran a project-wide find-all-references search for `save_to_watchlist`
across the repo (editor "Find All References" plus `grep -rn save_to_watchlist .`). The only
call site outside the definition was in `routes/watchlist/watchlist.py`, which I updated. After
the rename the same search returned zero remaining references to the old name, confirming no
call site was missed.

## Comment 2 — Deduplication

**What I did:** Added an existing-entry guard to `add_to_watchlist()`. Before inserting, it
queries `WatchlistEntry.query.filter_by(user_id=user_id, film_id=film_id).first()`; if a row
already exists, the function returns that existing entry and skips the insert/commit, so a film
can't appear on the same user's watchlist twice.

**How I verified:** I modeled the check on `add_to_collection()` in
`services/collection_service.py`, which performs the same `filter_by(...).first()` lookup before
inserting (it raises `AlreadyInCollectionError`; for the watchlist I return the existing entry
instead so repeated adds are idempotent). I confirmed the behavior with the duplicate-entry
test described under "Second test" below — adding the same film twice leaves exactly one row.

## Comment 3 — Missing test

**What I did:** Added `tests/test_watchlist.py` with
`test_add_to_watchlist_nonexistent_film_raises`, which asserts that adding a `film_id` that
does not exist raises `FilmNotFoundError`.

**How I verified:** I modeled it directly on `test_add_to_collection_nonexistent_film_raises`
in `tests/test_collection.py` — same `app`/`sample_user` fixtures, same
`pytest.raises(FilmNotFoundError)` structure, using a UUID that was never inserted. The test
targets the nonexistent-`film_id` case specifically (not an empty-watchlist or duplicate case).
`pytest tests/ -v` passes.

## Comment 4 — Default visibility

**My position:** Keep `public=True` as the default.

**Reasoning:** CineLog is a *community* film-tracking app — its core value is seeing what other
people are planning to watch and discovering films through them. Watchlists that default to
private would mean most users never surface their picks, which directly undercuts the discovery
loop the platform is built around. Defaulting to public optimizes for that social-discovery
behavior, which is the reason people join CineLog in the first place.

**Tradeoff acknowledged:** A private-by-default would optimize for user control and would be the
safer choice for a privacy-sensitive product. The cost is discovery: new users wouldn't
contribute to the community feed unless they opted in, and most never would. Because CineLog's
whole premise is social tracking, I think public-by-default is the right call here, with an
explicit per-entry override (see the visibility toggle below) for users who want to keep
specific films private.

## Comment 5 — Sort order

**My position:** Sort the watchlist by date added (most recent first), not alphabetically.

**Reasoning:** A watchlist isn't a reference catalog — it's a queue of "things I just heard
about and want to get to." On CineLog, users add to their watchlist reactively (after reading a
review, seeing a friend's entry), then come back to decide what to watch next. The items they
added most recently are the ones freshest in their mind, so showing newest-first matches how
people actually re-open a watchlist.

**Engagement with reviewer's point:** The maintainer wrote, *"Most users want to see what they
added recently."* I agree, and I'd add corroborating evidence: our existing `get_collection()`
already sorts `date_added.desc()` for exactly this reason, so date-added-first is consistent
with how the collection view already behaves — keeping the two list views consistent reduces
surprise. Alphabetical only wins when a list is long enough to scan by title, which a personal
watchlist rarely is. So I implemented date-added ordering rather than keeping alphabetical.

## Comment 6 — Rebase

**What conflicted:** While my PR was open, a refactor merged to `main` that migrated film IDs
from integer to UUID. My `feature/watchlist` branch still declared
`WatchlistEntry.film_id = db.Column(db.Integer, ...)` referencing the old integer `film.id`,
while `main` had changed `Film.id` (and `CollectionEntry.film_id`) to `db.Column(db.String(36))`.
The conflict was in `models.py`.

**How I resolved it:** I rebased `feature/watchlist` onto the updated `main`
(`git rebase origin/main`) and changed `WatchlistEntry.film_id` to
`db.Column(db.String(36), db.ForeignKey("film.id"), nullable=False)` so the watchlist's foreign
key matches the new UUID `Film.id` type. No other watchlist code referenced the integer type
directly. This is the `fix: update WatchlistEntry.film_id to UUID String(36) after main refactor`
commit.

**How I verified no conflict remains:** `git log --oneline origin/main..HEAD` shows a linear
history with no `Merge branch` commits, and `pytest tests/ -v` passes against the rebased tree.

## Stretch — remove_from_watchlist()

Added `remove_from_watchlist(user_id, film_id)` to `services/watchlist_service.py`, following the
`verb_to_noun` convention and mirroring `remove_from_collection()`. It looks up the entry with
`filter_by(...).first()`; **if the film is not on the watchlist it returns `False` (a no-op)**
rather than raising, so callers can treat removal as idempotent. Covered by
`test_remove_from_watchlist_not_on_list_returns_false`.

## Stretch — second test

I added `test_add_to_watchlist_duplicate_does_not_create_second_entry`. I chose the
**duplicate-entry** edge case because deduplication (Comment 2) is the watchlist's least obvious
behavior and the easiest to regress — a future change to `add_to_watchlist()` could silently
start inserting duplicates, and this test pins the "exactly one row after adding the same film
twice" guarantee.

## Stretch — visibility toggle

I added a `public` parameter to `add_to_watchlist(user_id, film_id, public=True)`. **It defaults
to `True`** (consistent with the Comment 4 decision), and a caller can pass `public=False` to
add a film privately, e.g. `add_to_watchlist(user_id, film_id, public=False)`. The value is
stored on the `WatchlistEntry.public` column and returned in `to_dict()`.

## PR Description

**What this feature does:** This PR adds a **watchlist** to CineLog — a per-user list of films a
user wants to watch later, parallel to the existing "collection" of films they've already
watched. Users can add a film to their watchlist, view their watchlist, and remove a film from
it. Adding the same film twice is a no-op (no duplicates), and each entry has a visibility flag.

**Design decisions:**
- **Default visibility = public.** CineLog is a community discovery app, so watchlists default to
  public to feed the discovery loop; a per-entry `public=False` override is available.
- **Sort order = date added (newest first).** A watchlist is a recency-driven queue, and this
  matches the existing collection view's ordering.

**How to test manually:**
```bash
# 1. Start the app
python app.py            # serves at http://127.0.0.1:5000

# 2. Create a film id to work with (use an existing seeded film, or note a UUID from /films/)
curl http://127.0.0.1:5000/films/

# 3. Add a film to a user's watchlist (replace <user_id> and <film_uuid>)
curl -X POST http://127.0.0.1:5000/watchlist/<user_id>/add \
     -H "Content-Type: application/json" \
     -d '{"film_id": "<film_uuid>"}'
# expect: 201 with the new entry JSON

# 4. Add the SAME film again — should not create a duplicate
curl -X POST http://127.0.0.1:5000/watchlist/<user_id>/add \
     -H "Content-Type: application/json" \
     -d '{"film_id": "<film_uuid>"}'

# 5. View the watchlist (newest first)
curl http://127.0.0.1:5000/watchlist/<user_id>

# 6. Add a nonexistent film — should return 404
curl -X POST http://127.0.0.1:5000/watchlist/<user_id>/add \
     -H "Content-Type: application/json" \
     -d '{"film_id": "00000000-0000-0000-0000-000000000000"}'

# 7. Run the test suite
pytest tests/ -v
```

## Commit history

```
feat: add public parameter to add_to_watchlist
test: add duplicate-entry edge case test for add_to_watchlist
feat: add remove_from_watchlist service function
fix: update WatchlistEntry.film_id to UUID String(36) after main refactor
test: add test for nonexistent film_id in add_to_watchlist
fix: add deduplication check to add_to_watchlist
fix: rename save_to_watchlist to add_to_watchlist
feat: add watchlist model and save endpoint
```
