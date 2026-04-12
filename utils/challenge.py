# utils/challenge.py
# Graded challenge component used across tracks.
# Handles standard challenge (3 attempts, model answer on 3rd fail),
# and the single-attempt Lesson 3.2 variant.

import streamlit as st
from utils.session import complete_lesson
from utils.grading import grade_challenge


def render_graded_challenge(
    track_id: int,
    lesson_id: int,
    scenario: str,
    broken_example: str,
    rubric: str,
    model_answer: str,
    hints: list[str],
    input_label: str = "Your response",
    max_chars: int = 500,
    single_attempt: bool = False,
) -> bool:
    """
    Render a graded short-input challenge.

    single_attempt=True: Lesson 3.2 mode — submit once, always advance,
    show explanation only (no score number displayed).

    Returns True when the lesson is passed or auto-advanced.
    """
    state_key = f"challenge_{track_id}_{lesson_id}"

    if state_key not in st.session_state:
        st.session_state[state_key] = {
            "attempts": 0,
            "passed": False,
            "completed": False,
            "last_result": None,
            "show_model_answer": False,
        }

    cs = st.session_state[state_key]

    st.markdown("---")
    st.markdown("### Challenge")

    # -----------------------------------------------------------------------
    # Already passed
    # -----------------------------------------------------------------------
    if cs["passed"] or cs["completed"]:
        if cs["last_result"]:
            result = cs["last_result"]
            if single_attempt:
                st.info(f"**Submitted.** {result.get('explanation', '')}")
            else:
                if result.get("pass"):
                    attempt_word = "attempt" if cs["attempts"] == 1 else "attempts"
                    st.success(
                        f"✓ Passed — score {result['score']}/100 "
                        f"({cs['attempts']} {attempt_word})"
                    )
                else:
                    st.info("Model answer revealed. Lesson complete — move to next lesson.")
                    st.markdown(f"**Model answer:**\n\n{model_answer}")
        return True

    # -----------------------------------------------------------------------
    # Show scenario and broken example
    # -----------------------------------------------------------------------
    st.markdown(scenario)

    if broken_example:
        st.markdown("**Starting point:**")
        st.code(broken_example, language=None)

    # Attempt counter
    attempts_so_far = cs["attempts"]
    if attempts_so_far > 0 and not single_attempt:
        attempt_word = "attempt" if attempts_so_far == 1 else "attempts"
        st.caption(f"{attempts_so_far} of 3 {attempt_word} used")

    # Show current hint if a previous attempt failed
    if cs["last_result"] and not cs["last_result"].get("pass") and not single_attempt:
        hint_idx = min(attempts_so_far - 1, len(hints) - 1)
        if hint_idx >= 0 and hints:
            st.markdown(
                f'<div style="background:#EBF3FA;border-left:3px solid #478FCC;'
                f'border-radius:4px;padding:10px 14px;margin:8px 0;">'
                f'<span style="color:#478FCC;font-weight:500;">Hint:</span> '
                f'<span style="color:#212121;">{hints[hint_idx]}</span></div>',
                unsafe_allow_html=True,
            )

    # -----------------------------------------------------------------------
    # Input field
    # -----------------------------------------------------------------------
    response_key = f"{state_key}_response"
    user_input = st.text_area(
        input_label,
        key=response_key,
        max_chars=max_chars,
        height=120,
        placeholder="Write your response here…",
    )

    col1, _ = st.columns([1, 5])
    with col1:
        submit = st.button("Submit", key=f"{state_key}_submit", type="primary")

    if submit:
        if not user_input or not user_input.strip():
            st.warning("Please write a response before submitting.")
            return False

        with st.spinner("Grading…"):
            result = grade_challenge(user_input.strip(), rubric, model_answer)

        cs["attempts"] += 1
        cs["last_result"] = result

        if single_attempt:
            # Lesson 3.2 mode: always advance; show what was met/missed, no score number.
            if result.get("pass") and result.get("score", 0) >= 95:
                explanation = "All criteria met — your prompt covered every required component."
            elif result.get("hint"):
                explanation = (
                    "Here is what a full-credit response would have included: "
                    + result["hint"]
                )
            else:
                explanation = (
                    "Most criteria met. Review the model answer below to see a "
                    "full-credit example."
                )
            cs["last_result"]["explanation"] = explanation
            cs["passed"] = True
            cs["completed"] = True
            complete_lesson(track_id, lesson_id)
            st.rerun()

        elif result["pass"]:
            cs["passed"] = True
            cs["completed"] = True
            complete_lesson(track_id, lesson_id)
            st.rerun()

        elif cs["attempts"] >= 3:
            # 3rd failure — reveal model answer and advance
            cs["show_model_answer"] = True
            cs["completed"] = True
            complete_lesson(track_id, lesson_id)
            st.rerun()

        else:
            st.rerun()

    return False
