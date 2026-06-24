# PR Response Doc — CineLog Watchlist Feature

## AI Usage

I used AI tools in two specific ways during this project:

1. **Codebase orientation.** I gave the assistant `services/collection_service.py` and asked it
   to summarize each function and explain what `add_to_collection()` returns when the `film_id`
   doesn't exist. I used that to find the existing deduplication pattern, then read the code
   myself to confirm before reusing it.
2. **Conventional-commit check.** Before force-pushing, I pasted my `git log --oneline` and asked
   whether the messages followed Conventional Commits and whether any commit bundled more than one
   change. I then verified against the spec myself.

## Comment 1 — Rename

**What I did:** Renamed `save_to_watchlist()` to `add_to_watchlist()` to match the project's
`verb_to_noun` convention.

**How I verified:** I used a project-wide search (`grep -rn save_to_watchlist .` plus my editor's
Find All References) to locate every call site. The only one outside the definition was in
`routes/watchlist/watchlist.py`, which I updated. Re-running the search afterward returned no
remaining references to the old name, so I'm confident none were missed.

## Comment 2 — Deduplication

**What I did:** Added an existing-entry check to `add_to_watchlist()`. It queries
`WatchlistEntry.query.filter_by(user_id=user_id, film_id=film_id).first()` before inserting and,
if a row already exists, returns it without adding a second one.

**How I verified:** I modeled the check on `add_to_collection()` in
`services/collection_service.py`, which does the same `filter_by(...).first()` lookup before
inserting. I confirmed adding the same film twice leaves a single row.

## Comment 3 — Missing test

**What I did:** Added `tests/test_watchlist.py` with
`test_add_to_watchlist_nonexistent_film_raises`, asserting `FilmNotFoundError` is raised for a
`film_id` that doesn't exist.

**How I verified:** I modeled it on `test_add_to_collection_nonexistent_film_raises` in
`tests/test_collection.py` — same fixtures and `pytest.raises(FilmNotFoundError)` structure. It
targets the nonexistent-`film_id` case specifically. `pytest tests/ -v` passes.

## Comment 4 — Default visibility

**My position:** Default watchlists to **private** (`public=False`).

**Reasoning:** CineLog onboards a lot of new users who are just starting to build their lists. A
private default protects people during that early period when they're experimenting and may not
realize their picks are visible to the whole community. Optimizing for that onboarding experience
— letting users build confidence before sharing — is more important than maximizing the feed on
day one, and users who want to share can flip an entry to public deliberately.

**Tradeoff acknowledged:** A public default would optimize for discovery — more watchlists in the
community feed, more films surfaced to other users. That's a real benefit for a social app. But I
think the cost (surprising new users by exposing lists they assumed were private) outweighs it for
CineLog specifically, where the audience skews toward newer users still finding their footing.

## Comment 5 — Sort order

**My position:** Sort the watchlist by date added, newest first.

**Reasoning:** A watchlist functions as a queue of films a user recently decided they want to
watch. People tend to act on the most recent additions first — they add something after hearing
about it and come back soon after to watch it — so surfacing the newest entries at the top matches
how the list actually gets used. Alphabetical ordering treats the watchlist like a reference index,
which isn't really what it is. This is a deliberate change from the current alphabetical sort, and
it keeps the watchlist consistent with how a personal queue is normally consumed.

## Comment 6 — Rebase

**What conflicted:** A refactor merged to `main` migrated film IDs from integer to UUID. My branch
still declared `WatchlistEntry.film_id = db.Column(db.Integer, ...)`, while `main` had moved
`Film.id` and `CollectionEntry.film_id` to `db.Column(db.String(36))`. The conflict was in
`models.py`.

**How I resolved it:** I rebased onto the updated `main` and changed `WatchlistEntry.film_id` to
`db.Column(db.String(36), db.ForeignKey("film.id"), nullable=False)` so the foreign key matches the
new UUID `Film.id`. That's the `fix: update WatchlistEntry.film_id to UUID String(36) after rebase`
commit.

**How I verified no conflict remains:** `git log --oneline origin/main..HEAD` is linear with no
`Merge branch` commits, and `pytest tests/ -v` passes.

## Stretch — remove_from_watchlist()

Added `remove_from_watchlist(user_id, film_id)`, following `verb_to_noun` naming and mirroring
`remove_from_collection()`. **If the film isn't on the watchlist it returns `False` (a no-op)**
instead of raising, so removal is idempotent. Covered by
`test_remove_from_watchlist_not_on_list_returns_false`.

## PR Description

**What this feature does:** Adds a per-user **watchlist** to CineLog — films a user wants to watch
later, alongside the existing collection of films they've already watched. Users can add a film to
their watchlist, view it, and remove a film. Adding the same film twice does not create a duplicate.

**Design decisions:**
- **Default visibility = private.** Protects new users while they build their lists; they can make
  an entry public deliberately.
- **Sort order = date added (newest first).** A watchlist is a recency-driven queue.

**How to test manually:**
```bash
python app.py                      # http://127.0.0.1:5000

# add a film (replace ids)
curl -X POST http://127.0.0.1:5000/watchlist/<user_id>/add \
     -H "Content-Type: application/json" -d '{"film_id": "<film_uuid>"}'
# add the same film again -> no duplicate
curl -X POST http://127.0.0.1:5000/watchlist/<user_id>/add \
     -H "Content-Type: application/json" -d '{"film_id": "<film_uuid>"}'
# view the watchlist
curl http://127.0.0.1:5000/watchlist/<user_id>
# nonexistent film -> 404
curl -X POST http://127.0.0.1:5000/watchlist/<user_id>/add \
     -H "Content-Type: application/json" -d '{"film_id": "00000000-0000-0000-0000-000000000000"}'
# run tests
pytest tests/ -v
```

## Commit history

```
feat: add remove_from_watchlist service function
fix: update WatchlistEntry.film_id to UUID String(36) after rebase
test: add test for nonexistent film_id in add_to_watchlist
fix: add deduplication check to add_to_watchlist
fix: rename save_to_watchlist to add_to_watchlist
feat: add watchlist model and save endpoint
```
