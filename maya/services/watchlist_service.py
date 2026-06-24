"""
services/watchlist_service.py — CineLog

Business logic for the watchlist feature.
"""

from app import db
from models import Film, WatchlistEntry
from services.collection_service import FilmNotFoundError


def add_to_watchlist(user_id, film_id):
    """Save a film to a user's watchlist.

    Raises FilmNotFoundError if the film_id does not exist.
    """
    film = db.session.get(Film, film_id)
    if film is None:
        raise FilmNotFoundError(f"No film found with id '{film_id}'")

    # Deduplication: don't add a film that's already on the watchlist.
    # Mirrors the existing-entry check in add_to_collection() (collection_service.py).
    existing = WatchlistEntry.query.filter_by(
        user_id=user_id, film_id=film_id
    ).first()
    if existing:
        return existing

    entry = WatchlistEntry(user_id=user_id, film_id=film_id)
    db.session.add(entry)
    db.session.commit()
    return entry


def get_watchlist(user_id):
    """Return all films on a user's watchlist (alphabetical by title)."""
    entries = (
        WatchlistEntry.query
        .filter_by(user_id=user_id)
        .join(Film)
        .order_by(Film.title.asc())
        .all()
    )

    result = []
    for entry in entries:
        film_dict = entry.film.to_dict()
        film_dict["date_added"] = entry.date_added.isoformat()
        film_dict["public"] = entry.public
        result.append(film_dict)
    return result


def remove_from_watchlist(user_id, film_id):
    """Remove a film from a user's watchlist.

    Follows the verb_to_noun naming convention and mirrors
    remove_from_collection(). Returns False (no-op) when the film is not on
    the watchlist rather than raising, so callers can treat removal as
    idempotent.
    """
    entry = WatchlistEntry.query.filter_by(
        user_id=user_id, film_id=film_id
    ).first()
    if entry is None:
        return False

    db.session.delete(entry)
    db.session.commit()
    return True
