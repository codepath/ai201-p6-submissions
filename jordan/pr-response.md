# PR Response Doc — CineLog Watchlist Feature

## Comment 1 — Rename

**What I did:** I renamed `save_to_watchlist` to `add_to_watchlist` and updated the call site.

## Comment 2 — Deduplication

**What I did:** I added a deduplication check to `add_to_watchlist`. It checks whether a
`WatchlistEntry` with the same `user_id` and `film_id` already exists, and if it does, the
function returns that existing entry and does not add the film again. So a film can only be on a
user's watchlist once.

## Comment 3 — Missing test

**What I did:** I added a test in `tests/test_watchlist.py` for the case where the `film_id`
doesn't exist in the database. It asserts that `add_to_watchlist` raises `FilmNotFoundError` for a
`film_id` that was never added.

## Comment 4 — Default visibility

**My position:** Keep the default private.

**Reasoning:** CineLog has a lot of users who are just getting started and building out their
watchlists. A private default means those new users aren't accidentally broadcasting half-finished
lists to the whole community while they're still figuring things out, which fits CineLog's
new-user-heavy audience better than exposing everything by default.

## Comment 5 — Sort order

**My position:** Date added, newest first — users mostly come back for the stuff they just added,
so it makes sense to put recent additions on top.

## Comment 6 — Rebase

**What I did:** I resolved the conflict by updating the film IDs to use UUIDs so my branch lined up
with `main`.

## PR Description

**What this feature does:** This PR adds a watchlist to CineLog. A watchlist is a list of films a
user wants to watch later, separate from the collection of films they've already watched. Users
can add a film to their watchlist and view it, and a film can't be added to the same watchlist
twice.

**Design decisions:**
- **Default visibility = private**, to protect new users while they build their lists.
- **Sort order = date added (newest first)**, because users return for recent additions.

**How to test manually:**
```bash
python app.py     # http://127.0.0.1:5000

# add a film (replace ids)
curl -X POST http://127.0.0.1:5000/watchlist/<user_id>/add \
     -H "Content-Type: application/json" -d '{"film_id": "<film_uuid>"}'

# view the watchlist
curl http://127.0.0.1:5000/watchlist/<user_id>

# nonexistent film -> 404
curl -X POST http://127.0.0.1:5000/watchlist/<user_id>/add \
     -H "Content-Type: application/json" -d '{"film_id": "00000000-0000-0000-0000-000000000000"}'

# run the tests
pytest tests/ -v
```

## Commit history

```
Merge branch 'main' into jordan-commits
test: add test for nonexistent film_id in add_to_watchlist
fix: add deduplication check to add_to_watchlist
fix: rename save_to_watchlist to add_to_watchlist
fix: update film retrieval method to use db.session.get in collection and watchlist services
feat: add watchlist model and save endpoint
```
