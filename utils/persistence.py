# utils/persistence.py
# Supabase-backed persistence for per-user learning progress.
#
# Stores one row per learner in the `progress` table, keyed on their work
# email address. The full navigation/progress state is serialized as a JSON
# object in the `state` column so that adding new progress fields in the
# future does not require a schema migration.
#
# Expected Supabase table schema:
#   create table progress (
#     user_id    text primary key,
#     state      jsonb not null,
#     updated_at timestamptz not null default now()
#   );

from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

import streamlit as st


_TABLE = "progress"


def get_supabase_client(*, silent: bool = False):
    """Return a cached Supabase client.

    Reads SUPABASE_URL and SUPABASE_KEY from st.secrets. The client is cached
    on st.session_state so we do not rebuild it on every rerun.

    When `silent=True`, suppress all user-facing error messages and return
    None on any failure. Used by load_user_progress during the initial
    restore attempt so a fresh user or a temporary Supabase outage never
    greets the learner with red error banners.
    """
    cached = st.session_state.get("_supabase_client")
    if cached is not None:
        return cached
    try:
        from supabase import create_client
    except ImportError:
        if not silent:
            st.error(
                "The `supabase` Python package is not installed. "
                "Add `supabase` to requirements.txt and redeploy."
            )
        return None
    try:
        url = st.secrets["SUPABASE_URL"]
        key = st.secrets["SUPABASE_KEY"]
    except Exception as exc:
        if not silent:
            st.error(
                f"Supabase credentials are missing from st.secrets: {exc}. "
                "Configure SUPABASE_URL and SUPABASE_KEY."
            )
        return None
    try:
        client = create_client(url, key)
    except Exception as exc:
        if not silent:
            st.error(f"Could not initialize Supabase client: {exc}")
        return None
    st.session_state._supabase_client = client
    return client


def _serialize_progress(progress: dict | None) -> dict:
    """Convert the progress dict to a JSON-safe structure.

    st.session_state.progress uses integer track/lesson keys. JSON only
    supports string keys, so we coerce keys to strings for transport and
    coerce them back in `_deserialize_progress`.
    """
    if not progress:
        return {}
    out: dict[str, dict[str, bool]] = {}
    for track_id, lessons in progress.items():
        out[str(track_id)] = {str(l_id): bool(v) for l_id, v in (lessons or {}).items()}
    return out


def _deserialize_progress(raw: dict | None) -> dict:
    """Inverse of `_serialize_progress`."""
    if not raw:
        return {}
    out: dict[int, dict[int, bool]] = {}
    for track_id, lessons in raw.items():
        try:
            tid = int(track_id)
        except (TypeError, ValueError):
            continue
        inner: dict[int, bool] = {}
        for l_id, v in (lessons or {}).items():
            try:
                inner[int(l_id)] = bool(v)
            except (TypeError, ValueError):
                continue
        out[tid] = inner
    return out


def _serialize_certificate_names(names: dict | None) -> dict:
    if not names:
        return {}
    return {str(track_id): str(n) for track_id, n in names.items()}


def _deserialize_certificate_names(raw: dict | None) -> dict:
    if not raw:
        return {}
    out: dict[int, str] = {}
    for track_id, name in raw.items():
        try:
            out[int(track_id)] = str(name)
        except (TypeError, ValueError):
            continue
    return out


def load_user_progress(email: str) -> Optional[dict]:
    """Fetch a learner's stored state from Supabase.

    Returns the parsed `state` JSON dict if a row exists for the given
    email, or None if no row exists or the lookup failed. Always silent:
    no st.warning / st.error / st.info / print on any code path, because a
    first-time learner should not see an error banner just because no row
    has been created yet, and a transient Supabase failure at load time
    should not block the learner from starting a fresh session.
    """
    if not email:
        return None
    try:
        client = get_supabase_client(silent=True)
        if client is None:
            return None
        response = (
            client.table(_TABLE)
            .select("state")
            .eq("user_id", email)
            .limit(1)
            .execute()
        )
        rows = getattr(response, "data", None) or []
        if not rows:
            return None
        state = rows[0].get("state")
        if not isinstance(state, dict):
            return None
        return state
    except Exception:
        return None


def save_user_progress(email: str) -> bool:
    """Upsert the current session state to Supabase.

    Reads the five tracked variables out of st.session_state and writes
    them back under the learner's email. Always silent: no st.warning /
    st.error / st.info / st.success on any code path. Returns True on a
    confirmed write, False on any failure (missing email, missing client,
    network error, Supabase rejection).
    """
    if not email:
        return False
    try:
        client = get_supabase_client(silent=True)
        if client is None:
            return False
        state_payload = {
            "view": st.session_state.get("view", "home"),
            "current_track": st.session_state.get("current_track"),
            "current_lesson": st.session_state.get("current_lesson"),
            "progress": _serialize_progress(st.session_state.get("progress")),
            "certificate_names": _serialize_certificate_names(
                st.session_state.get("certificate_names")
            ),
        }
        row = {
            "user_id": email,
            "state": state_payload,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
        client.table(_TABLE).upsert(row, on_conflict="user_id").execute()
        return True
    except Exception:
        return False


def reset_user_progress(email: str) -> bool:
    """Delete the row for this learner.

    Always silent: no st.warning / st.error / st.info / st.success on any
    code path. Returns True on a confirmed delete, False on any failure.
    """
    if not email:
        return False
    try:
        client = get_supabase_client(silent=True)
        if client is None:
            return False
        client.table(_TABLE).delete().eq("user_id", email).execute()
        return True
    except Exception:
        return False


def diagnose(email: str) -> dict:
    """Run an end-to-end health check on the persistence layer.

    Returns a dict with named, user-readable statuses for each step:
      - secrets_present: bool
      - package_installed: bool
      - client_initialized: bool
      - read_ok: bool
      - read_error: str | None
      - row_exists: bool
      - write_ok: bool
      - write_error: str | None

    Safe to call at any time; never raises. Surfaces problems that
    save_user_progress/load_user_progress hide. Lets the home screen tell
    the learner exactly where the persistence chain is breaking so the
    operator can fix the real cause (most often RLS policies or missing
    table) rather than guessing.
    """
    out = {
        "secrets_present": False,
        "package_installed": False,
        "client_initialized": False,
        "read_ok": False,
        "read_error": None,
        "row_exists": False,
        "write_ok": False,
        "write_error": None,
    }
    try:
        try:
            _ = st.secrets["SUPABASE_URL"]
            _ = st.secrets["SUPABASE_KEY"]
            out["secrets_present"] = True
        except Exception:
            return out
        try:
            import supabase  # noqa: F401
            out["package_installed"] = True
        except ImportError:
            return out
        client = get_supabase_client(silent=True)
        if client is None:
            return out
        out["client_initialized"] = True

        if not email:
            # Without an email we cannot exercise read/write paths.
            return out

        # Read probe.
        try:
            resp = (
                client.table(_TABLE)
                .select("state")
                .eq("user_id", email)
                .limit(1)
                .execute()
            )
            rows = getattr(resp, "data", None) or []
            out["read_ok"] = True
            out["row_exists"] = bool(rows)
        except Exception as exc:
            out["read_error"] = str(exc)[:300]
            return out

        # Write probe: upsert whatever state we have now. Writes a real row
        # using live session values so the learner's next login restores
        # correctly. Idempotent and safe to run repeatedly.
        try:
            state_payload = {
                "view": st.session_state.get("view", "home"),
                "current_track": st.session_state.get("current_track"),
                "current_lesson": st.session_state.get("current_lesson"),
                "progress": _serialize_progress(st.session_state.get("progress")),
                "certificate_names": _serialize_certificate_names(
                    st.session_state.get("certificate_names")
                ),
            }
            row = {
                "user_id": email,
                "state": state_payload,
                "updated_at": datetime.now(timezone.utc).isoformat(),
            }
            client.table(_TABLE).upsert(row, on_conflict="user_id").execute()
            out["write_ok"] = True
        except Exception as exc:
            out["write_error"] = str(exc)[:300]
    except Exception as exc:
        # Defensive: never let a diagnostic call raise into the UI.
        out["write_error"] = (out.get("write_error") or "") + f" [outer: {exc}]"
    return out


def apply_loaded_state(state: dict) -> None:
    """Populate st.session_state from a previously loaded `state` dict.

    Called once during init after a successful load_user_progress. Keeps
    the restore logic in one place so init_session_state stays readable.
    """
    st.session_state.view = state.get("view", "home")
    st.session_state.current_track = state.get("current_track")
    st.session_state.current_lesson = state.get("current_lesson")
    st.session_state.progress = _deserialize_progress(state.get("progress"))
    st.session_state.certificate_names = _deserialize_certificate_names(
        state.get("certificate_names")
    )
