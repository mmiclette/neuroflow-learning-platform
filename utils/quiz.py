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
            "last_wrong_index": None,
        }

    qs = st.session_state[state_key]

    # Defensive: validate question data at render time so bad data is caught early
    # instead of silently producing wrong counts or index errors.
    if not isinstance(questions, list) or len(questions) == 0:
        st.error("Quiz has no questions configured.")
        return False
    for i, q in enumerate(questions):
        opts = q.get("options") if isinstance(q, dict) else None
        ci = q.get("correct_index") if isinstance(q, dict) else None
        if (not isinstance(opts, list) or len(opts) == 0
                or not isinstance(ci, int) or not (0 <= ci < len(opts))):
            st.error(f"Quiz data error on question {i + 1}. Please report this.")
            return False

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
    total = len(questions)

    # Prominent progress header: counter + progress bar so learners can see the
    # number advance after each correct answer.
    progress_pct = int(round((q_idx / total) * 100))
    st.markdown(
        f'<div style="display:flex;justify-content:space-between;align-items:center;'
        f'margin:4px 0 6px 0;">'
        f'<span style="font-size:14px;font-weight:600;color:#161BAA;">'
        f'Question {q_idx + 1} of {total}</span>'
        f'<span style="font-size:12px;color:#757575;">{progress_pct}% complete</span>'
        f'</div>'
        f'<div style="background:#E5E7EB;border-radius:4px;height:6px;overflow:hidden;'
        f'margin-bottom:14px;">'
        f'<div style="background:#2EA799;height:100%;width:{progress_pct}%;'
        f'transition:width 0.3s ease;"></div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # Wrong-answer counter badge
    if wrong_count > 0:
        st.markdown(
            f'<p style="font-size:12px;color:#F16061;margin:0 0 8px 0;">'
            f"Wrong answers this lesson: {wrong_count} of 3</p>",
            unsafe_allow_html=True,
        )

    # Render the question as bold HTML so bolding spans multiple paragraphs and
    # so inline tags like <u> render correctly. Preserves line breaks from the
    # source string by converting them to <br>.
    q_html = q["question"].replace("\n\n", "<br><br>").replace("\n", "<br>")
    st.markdown(
        f'<div style="font-weight:600;font-size:15px;color:#212121;'
        f'margin:0 0 12px 0;line-height:1.55;">{q_html}</div>',
        unsafe_allow_html=True,
    )

    radio_key = f"{state_key}_q{q_idx}_radio"
    selected = st.radio(
        "Select your answer:",
        q["options"],
        key=radio_key,
        label_visibility="collapsed",
        index=None,
    )

    # Show feedback from previous attempt. If the question defines an
    # "option_hints" dict mapping a wrong option's index to a tailored hint,
    # prefer that over the generic "hint" field. This lets an author give
    # answer-specific feedback while falling back to the default when the
    # selected option has no dedicated explanation.
    if qs["last_wrong"]:
        msg = "Incorrect — try again."
        hint_text = None
        last_wrong_idx = qs.get("last_wrong_index")
        opt_hints = q.get("option_hints")
        if isinstance(opt_hints, dict) and last_wrong_idx is not None:
            hint_text = opt_hints.get(last_wrong_idx) or opt_hints.get(str(last_wrong_idx))
        if not hint_text:
            hint_text = q.get("hint")
        if hint_text:
            msg += f" Hint: {hint_text}"
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
            qs["last_wrong_index"] = None
            qs["current_q"] += 1
            if qs["current_q"] >= len(questions):
                qs["completed"] = True
                if mark_complete:
                    complete_lesson(track_id, lesson_id)
            st.rerun()
        else:
            qs["wrong_count"] += 1
            qs["last_wrong"] = True
            try:
                qs["last_wrong_index"] = q["options"].index(selected)
            except ValueError:
                qs["last_wrong_index"] = None
            st.rerun()

    return False
