# utils/quiz.py
# Reusable quiz component. Enforces the 3-wrong-answer restart rule.
# Returns True when all questions answered correctly; False otherwise.

import streamlit as st
from utils.session import complete_lesson, reset_quiz


def render_quiz(
    track_id: int,
    lesson_id: int,
    questions: list[dict],
    label: str = "Knowledge check",
    mark_complete: bool = True,
) -> bool:
    """
    Render a multiple-choice quiz with the platform restart rule.

    Each question dict must contain:
      - "question": str
      - "options": list[str]   (display text, no ✓ markers)
      - "correct_index": int   (0-based index of correct option)
      - "hint": str | None     (optional — shown after wrong answer before restart)

    Returns True when all questions answered correctly.
    """
    state_key = f"quiz_{track_id}_{lesson_id}"

    # Initialise per-lesson quiz state
    if state_key not in st.session_state:
        st.session_state[state_key] = {
            "current_q": 0,
            "wrong_count": 0,
            "completed": False,
            "last_wrong": False,
        }

    qs = st.session_state[state_key]

    st.markdown(f"### {label}")

    # -----------------------------------------------------------------------
    # Forced restart state
    # -----------------------------------------------------------------------
    if qs["wrong_count"] >= 3:
        st.markdown(
            """
            <div style="background:#FEE2E2;border:1.5px solid #F16061;border-radius:8px;
                        padding:16px 20px;margin:16px 0;">
              <strong style="color:#C0392B;">Lesson restart required</strong><br>
              <span style="color:#212121;">You have exceeded the wrong answer limit for this lesson.
              Please restart the lesson from the beginning to continue.</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("↺  Restart lesson", key=f"restart_{state_key}"):
            reset_quiz(track_id, lesson_id)
            st.rerun()
        return False

    # -----------------------------------------------------------------------
    # Already completed
    # -----------------------------------------------------------------------
    if qs["completed"]:
        st.success("✓  All questions answered correctly")
        return True

    # -----------------------------------------------------------------------
    # Current question
    # -----------------------------------------------------------------------
    q_idx = qs["current_q"]
    if q_idx >= len(questions):
        qs["completed"] = True
        if mark_complete:
            complete_lesson(track_id, lesson_id)
        st.rerun()
        return True

    q = questions[q_idx]
    wrong_count = qs["wrong_count"]

    # Wrong-answer counter badge
    if wrong_count > 0:
        st.markdown(
            f'<p style="font-size:12px;color:#F16061;margin:0 0 8px 0;">'
            f"Wrong answers this lesson: {wrong_count} of 3</p>",
            unsafe_allow_html=True,
        )

    st.markdown(
        f'<p style="font-size:13px;color:#757575;margin:0 0 4px 0;">'
        f"Question {q_idx + 1} of {len(questions)}</p>",
        unsafe_allow_html=True,
    )
    st.markdown(f"**{q['question']}**")

    radio_key = f"{state_key}_q{q_idx}_radio"
    selected = st.radio(
        "Select your answer:",
        q["options"],
        key=radio_key,
        label_visibility="collapsed",
        index=None,
    )

    # Show feedback from previous attempt
    if qs["last_wrong"]:
        msg = "Incorrect — try again."
        if q.get("hint"):
            msg += f" Hint: {q['hint']}"
        st.markdown(
            f'<p style="color:#F16061;font-size:13px;margin:4px 0 8px 0;">{msg}</p>',
            unsafe_allow_html=True,
        )

    col1, _ = st.columns([1, 5])
    with col1:
        submit_pressed = st.button(
            "Submit", key=f"{state_key}_q{q_idx}_submit", type="primary"
        )

    if submit_pressed:
        if selected is None:
            st.warning("Please select an answer before submitting.")
            return False

        correct_option = q["options"][q["correct_index"]]
        if selected == correct_option:
            qs["last_wrong"] = False
            qs["current_q"] += 1
            if qs["current_q"] >= len(questions):
                qs["completed"] = True
                if mark_complete:
                    complete_lesson(track_id, lesson_id)
            st.rerun()
        else:
            qs["wrong_count"] += 1
            qs["last_wrong"] = True
            st.rerun()

    return False
