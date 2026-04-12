# utils/session.py
import streamlit as st
from data.curriculum import TRACKS, get_lesson_count


def init_session_state():
    """Initialize all session state on first load."""
    if st.session_state.get("_initialized"):
        return

    st.session_state._initialized = True
    st.session_state.view = "home"
    st.session_state.current_track = None
    st.session_state.current_lesson = None

    # Progress: {track_id: {lesson_id: True/False}}
    st.session_state.progress = {
        t_id: {l_id: False for l_id in track["lessons"]}
        for t_id, track in TRACKS.items()
    }

    # Quiz wrong-answer counters: {(track_id, lesson_id): int}
    st.session_state.quiz_wrong_counts = {}

    # Challenge attempt counters: {(track_id, lesson_id): int}
    st.session_state.challenge_attempts = {}

    # Learner names for certificates: {track_id: str}
    st.session_state.certificate_names = {}


# ---------------------------------------------------------------------------
# Navigation helpers
# ---------------------------------------------------------------------------

def navigate(view: str, track_id: int = None, lesson_id: int = None):
    """Update view and rerun. Always call st.rerun() after this."""
    st.session_state.view = view
    if track_id is not None:
        st.session_state.current_track = track_id
    if lesson_id is not None:
        st.session_state.current_lesson = lesson_id
    st.rerun()


def go_home():
    navigate("home")


def go_track(track_id: int):
    navigate("track", track_id=track_id)


def go_lesson(track_id: int, lesson_id: int):
    navigate("lesson", track_id=track_id, lesson_id=lesson_id)


def go_certificate(track_id: int):
    navigate("certificate", track_id=track_id)


def go_reference():
    navigate("reference")


# ---------------------------------------------------------------------------
# Progress helpers
# ---------------------------------------------------------------------------

def complete_lesson(track_id: int, lesson_id: int):
    """Mark a lesson as complete."""
    st.session_state.progress[track_id][lesson_id] = True


def is_lesson_complete(track_id: int, lesson_id: int) -> bool:
    return st.session_state.progress.get(track_id, {}).get(lesson_id, False)


def is_track_complete(track_id: int) -> bool:
    lessons = st.session_state.progress.get(track_id, {})
    return all(lessons.values()) if lessons else False


def get_track_completion_count(track_id: int) -> tuple[int, int]:
    """Returns (completed_count, total_count)."""
    lessons = st.session_state.progress.get(track_id, {})
    total = len(lessons)
    done = sum(1 for v in lessons.values() if v)
    return done, total


def get_first_incomplete_lesson(track_id: int) -> int:
    """Returns the lesson_id of the first incomplete lesson, or 1 if all complete."""
    lessons = st.session_state.progress.get(track_id, {})
    for lesson_id in sorted(lessons.keys()):
        if not lessons[lesson_id]:
            return lesson_id
    return 1


# ---------------------------------------------------------------------------
# Quiz helpers
# ---------------------------------------------------------------------------

def get_quiz_wrong_count(track_id: int, lesson_id: int) -> int:
    return st.session_state.quiz_wrong_counts.get((track_id, lesson_id), 0)


def increment_quiz_wrong(track_id: int, lesson_id: int):
    key = (track_id, lesson_id)
    st.session_state.quiz_wrong_counts[key] = (
        st.session_state.quiz_wrong_counts.get(key, 0) + 1
    )


def reset_quiz(track_id: int, lesson_id: int):
    st.session_state.quiz_wrong_counts.pop((track_id, lesson_id), None)
    # Clear all widget state for this quiz
    prefix = f"quiz_{track_id}_{lesson_id}"
    for key in list(st.session_state.keys()):
        if key.startswith(prefix):
            del st.session_state[key]


# ---------------------------------------------------------------------------
# Challenge helpers
# ---------------------------------------------------------------------------

def get_challenge_attempts(track_id: int, lesson_id: int) -> int:
    return st.session_state.challenge_attempts.get((track_id, lesson_id), 0)


def increment_challenge_attempt(track_id: int, lesson_id: int):
    key = (track_id, lesson_id)
    st.session_state.challenge_attempts[key] = (
        st.session_state.challenge_attempts.get(key, 0) + 1
    )
