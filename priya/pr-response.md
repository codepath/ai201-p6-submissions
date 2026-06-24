# PR Response Doc — CineLog Watchlist Feature

## Comment 1 — Rename

**What I did:** I renamed the function `save_to_watchlist()` to `add_to_watchlist()` and updated
the call site so everything still works.

## Comment 2 — Deduplication

**What I did:** I added a deduplication check to `add_to_watchlist()`. Before it adds a film, it
looks up whether a `WatchlistEntry` for that `user_id` and `film_id` already exists. If one does,
the function returns the existing entry and does not add a second one, so the same film can't end
up on a watchlist twice.

## Comment 3 — Missing test

**What I did:** I wrote a test for the missing `film_id` case in `tests/test_watchlist.py`. The
test adds a `film_id` that doesn't exist in the database and asserts that the function raises
`FilmNotFoundError` instead of failing some other way.

## Comment 4 — Default visibility

**My position:** I think `public=True` should stay the default.

**Reasoning:** CineLog is a community app — the whole point is seeing what other people are
planning to watch and finding films that way. If watchlists were private by default, most users
would never share their picks, and the community/discovery side of the app would basically stop
working. Defaulting to public keeps that discovery flowing, which is the main reason people use
CineLog.

**Tradeoff acknowledged:** A private default would optimize for user control and privacy, which is
a fair thing to want. But for CineLog specifically, where the value is in the shared community
feed, I think public is the right default, and anyone who wants a film kept private can set that
on the individual entry.

## Comment 5 — Sort order

**My position:** Sort by date added, newest first. Users usually come back for the films they
just added, so showing those at the top fits how the list gets used.

## Comment 6 — Rebase

**What I did:** I rebased my branch and updated the film IDs to use UUIDs so my watchlist code
matched `main`. After the rebase the branch history is linear with no merge commits.

## PR Description

**What this feature does:** This PR adds a watchlist to CineLog — a list of films a user wants to
watch later, separate from their collection of films they've already watched. Users can add a film
to their watchlist, view their watchlist, and the same film can't be added twice.

**Design decisions:**
- **Default visibility = public**, because CineLog is a community discovery app.
- **Sort order = date added (newest first)**, because a watchlist is a recency-driven queue.

**How to test manually:**
```bash
python app.py     # http://127.0.0.1:5000

# add a film to a watchlist (replace ids)
curl -X POST http://127.0.0.1:5000/watchlist/<user_id>/add \
     -H "Content-Type: application/json" -d '{"film_id": "<film_uuid>"}'

# view the watchlist
curl http://127.0.0.1:5000/watchlist/<user_id>

# add a nonexistent film -> 404
curl -X POST http://127.0.0.1:5000/watchlist/<user_id>/add \
     -H "Content-Type: application/json" -d '{"film_id": "00000000-0000-0000-0000-000000000000"}'

# run tests
pytest tests/ -v
```

## Commit history

```
fix: update film_id to UUID String(36) after rebase
test: add test for nonexistent film_id in add_to_watchlist
fix: add deduplication check to add_to_watchlist
fix: rename save_to_watchlist to add_to_watchlist
feat: add watchlist model and save endpoint
```
