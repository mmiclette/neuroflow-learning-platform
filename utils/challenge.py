# utils/challenge.py
# Graded challenge component used across tracks.
# Handles standard challenge (3 attempts, model answer on 3rd fail),
# and the single-attempt Lesson 3.2 variant.

import streamlit as st
from utils.session import complete_lesson
from utils.grading import grade_challenge


def _strengths_callout(text: str) -> None:
    st.markdown(
        f'<div style="background:#EAF3DE;border-left:3px solid #3B6D11;'
        f'border-radius:4px;padding:10px 14px;margin:8px 0;">'
        f'<span style="color:#3B6D11;font-weight:500;">What worked:</span> '
        f'<span style="color:#212121;">{text}</span></div>',
        unsafe_allow_html=True,
    )



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
    mark_complete: bool = True,
    pass_threshold: int = 70,
) -> bool:
    """
    Render a graded short-input challenge.

    single_attempt=True: submit once, always advance, show explanation.
    mark_complete=False: do not call complete_lesson on pass — let the
      caller (e.g. a following quiz) own the completion signal.
    pass_threshold: minimum score to count as a pass (default 70). Lets an
      individual challenge demand a stricter bar (for example, 75 when full
      credit requires every one of four criteria).

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
                explanation = result.get('explanation', '')
                score = result.get('score', 0)
                if score >= 95:
                    st.success(f"✓ All criteria met.")
                    if result.get('strengths'):
                        _strengths_callout(result['strengths'])
                    with st.expander("Compare with full-credit example"):
                        st.markdown(model_answer)
                else:
                    st.info(f"**Submitted.** {explanation}")
                    if result.get('hint'):
                        st.markdown(
                            f'<div style="background:#EBF3FA;border-left:3px solid #478FCC;'
                            f'border-radius:4px;padding:10px 14px;margin:8px 0;">'
                            f'<span style="color:#478FCC;font-weight:500;">What was missing:</span> '
                            f'<span style="color:#212121;">{result["hint"]}</span></div>',
                            unsafe_allow_html=True,
                        )
                    st.markdown(
                        f'<div style="background:#EBF3FA;border-left:3px solid #478FCC;'
                        f'border-radius:4px;padding:10px 14px;margin:8px 0 4px;">'
                        f'<span style="color:#478FCC;font-weight:500;">Full-credit example:</span></div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(model_answer)
            else:
                local_pass = result.get("_passed_local", result.get("pass"))
                if local_pass:
                    attempt_word = "attempt" if cs["attempts"] == 1 else "attempts"
                    st.success(
                        f"✓ Passed — score {result['score']}/100 "
                        f"({cs['attempts']} {attempt_word})"
                    )
                    if result.get("strengths"):
                        _strengths_callout(result["strengths"])
                    # Always show the improvement callout on a partial-credit
                    # pass so the learner sees which criterion they missed,
                    # even when they are above the pass threshold. The
                    # grader returns a hint whenever score < 100.
                    if result.get("hint") and result["score"] < 100:
                        st.markdown(
                            f'<div style="background:#FEF6E7;border-left:3px solid #D97706;'
                            f'border-radius:4px;padding:10px 14px;margin:8px 0;">'
                            f'<span style="color:#B45309;font-weight:500;">What could be improved:</span> '
                            f'<span style="color:#212121;">{result["hint"]}</span></div>',
                            unsafe_allow_html=True,
                        )
                    st.markdown(
                        f'<div style="background:#EBF3FA;border-left:3px solid #478FCC;'
                        f'border-radius:4px;padding:10px 14px;margin:8px 0 4px;">'
                        f'<span style="color:#478FCC;font-weight:500;">Full-credit example:</span></div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(model_answer)
                else:
                    st.info(
                        "Attempts used. Review what was missed below and study the "
                        "full-credit example carefully before moving on."
                    )
                    if result.get("hint"):
                        st.markdown(
                            f'<div style="background:#EBF3FA;border-left:3px solid #478FCC;'
                            f'border-radius:4px;padding:10px 14px;margin:8px 0;">'
                            f'<span style="color:#478FCC;font-weight:500;">What was missing:</span> '
                            f'<span style="color:#212121;">{result["hint"]}</span></div>',
                            unsafe_allow_html=True,
                        )
                    st.markdown(
                        f'<div style="background:#EBF3FA;border-left:3px solid #478FCC;'
                        f'border-radius:4px;padding:10px 14px;margin:8px 0 4px;">'
                        f'<span style="color:#478FCC;font-weight:500;">Full-credit example:</span></div>',
                        unsafe_allow_html=True,
                    )
                    st.markdown(model_answer)
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

    # Show current hint if a previous attempt failed. Prefer the grader's
    # tailored "hint" (which targets the specific criterion missed on this
    # attempt) over the generic static hints list, since dynamic feedback is
    # more useful than pre-authored hints tied only to attempt number.
    last = cs.get("last_result")
    last_passed = bool(last and last.get("_passed_local", last.get("pass")))
    if last and not last_passed and not single_attempt:
        dynamic_hint = last.get("hint")
        hint_text = dynamic_hint
        if not hint_text:
            hint_idx = min(attempts_so_far - 1, len(hints) - 1)
            if hint_idx >= 0 and hints:
                hint_text = hints[hint_idx]
        if hint_text:
            label = "What was missing" if dynamic_hint else "Hint"
            st.markdown(
                f'<div style="background:#EBF3FA;border-left:3px solid #478FCC;'
                f'border-radius:4px;padding:10px 14px;margin:8px 0;">'
                f'<span style="color:#478FCC;font-weight:500;">{label}:</span> '
                f'<span style="color:#212121;">{hint_text}</span></div>',
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

    # Show the character limit inline so a learner whose paste gets silently
    # blocked by max_chars can see why. Streamlit's text_area refuses pastes
    # that would exceed max_chars without surfacing an error.
    used = len(user_input or "")
    near_limit = used >= int(max_chars * 0.85)
    color = "#C0392B" if near_limit else "#757575"
    st.markdown(
        f'<p style="font-size:12px;color:{color};margin:-4px 0 10px 0;'
        f'text-align:right;">{used} / {max_chars} characters</p>',
        unsafe_allow_html=True,
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

        # Apply the challenge-specific pass threshold. This supersedes the
        # grader's own pass/fail flag, which uses a fixed 70 baseline.
        score_val = int(result.get("score", 0) or 0)
        result["_passed_local"] = score_val >= pass_threshold
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
            if mark_complete:
                complete_lesson(track_id, lesson_id)
            st.rerun()

        elif result["_passed_local"]:
            cs["passed"] = True
            cs["completed"] = True
            if mark_complete:
                complete_lesson(track_id, lesson_id)
            st.rerun()

        elif cs["attempts"] >= 3:
            # 3rd failure — reveal model answer and advance
            cs["show_model_answer"] = True
            cs["completed"] = True
            if mark_complete:
                complete_lesson(track_id, lesson_id)
            st.rerun()

        else:
            st.rerun()

    return False
