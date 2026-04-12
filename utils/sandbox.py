# utils/sandbox.py
# Live sandbox component — lets learners submit a prompt to Haiku and see the output.
# Lesson 3.1 uses a comparison sandbox (weak vs improved, side by side).
# Other sandbox lessons use a standard single-input sandbox.

import streamlit as st
from html import escape
from utils.session import complete_lesson, is_lesson_complete
from utils.grading import call_sandbox


def _fmt(text: str) -> str:
    """Escape HTML and convert newlines for safe injection into a div."""
    return escape(text).replace("\n", "<br>")


def render_comparison_sandbox(
    track_id: int,
    lesson_id: int,
    weak_prompt: str,
    instruction: str,
) -> bool:
    """
    Lesson 3.1 pattern: show weak prompt, learner improves it,
    both run and outputs appear side by side.
    Returns True after submission (lesson always passes).
    """
    state_key = f"sandbox_cmp_{track_id}_{lesson_id}"

    if state_key not in st.session_state:
        st.session_state[state_key] = {
            "submitted": False,
            "weak_output": "",
            "improved_output": "",
        }

    ss = st.session_state[state_key]

    st.markdown("---")
    st.markdown("### Live sandbox")
    st.markdown(instruction)

    if ss["submitted"]:
        # Show completed comparison
        st.success("✓ Sandbox complete")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Weak prompt output:**")
            st.markdown(
                f'<div style="background:#FFF3F3;border:1px solid #F16061;border-radius:6px;'
                f'padding:12px;font-size:13px;line-height:1.6;">{_fmt(ss["weak_output"])}</div>',
                unsafe_allow_html=True,
            )
        with col2:
            st.markdown("**Your improved prompt output:**")
            st.markdown(
                f'<div style="background:#F0FBF9;border:1px solid #2EA799;border-radius:6px;'
                f'padding:12px;font-size:13px;line-height:1.6;">{_fmt(ss["improved_output"])}</div>',
                unsafe_allow_html=True,
            )
        return True

    # Show weak prompt (read-only)
    st.markdown("**Starting prompt (weak):**")
    st.code(weak_prompt, language=None)

    # Learner's improved version
    improved_key = f"{state_key}_input"
    st.markdown("**Your improved prompt:**")
    st.text_area(
        "Improve the prompt using RTCFC:",
        key=improved_key,
        height=160,
        placeholder="Rewrite the prompt adding Role, Context, Format, and Constraints…",
        label_visibility="collapsed",
    )

    col1, _ = st.columns([1, 5])
    with col1:
        if st.button("Run both →", key=f"{state_key}_submit", type="primary"):
            improved = st.session_state.get(improved_key, "").strip()
            if not improved:
                st.warning("Write your improved prompt before running.")
                return False

            with st.spinner("Running both prompts…"):
                weak_out = call_sandbox(weak_prompt)
                improved_out = call_sandbox(improved)

            ss["weak_output"] = weak_out
            ss["improved_output"] = improved_out
            ss["submitted"] = True
            complete_lesson(track_id, lesson_id)
            st.rerun()

    return False


def render_sandbox(
    track_id: int,
    lesson_id: int,
    starter_prompt: str,
    instruction: str,
    system_prompt: str = None,
) -> bool:
    """
    Standard sandbox: learner edits a starter prompt, submits to Haiku, sees output.
    Returns True after first submission.
    """
    state_key = f"sandbox_{track_id}_{lesson_id}"

    if state_key not in st.session_state:
        st.session_state[state_key] = {
            "submitted": False,
            "output": "",
        }

    ss = st.session_state[state_key]

    st.markdown("---")
    st.markdown("### Live sandbox")
    st.markdown(instruction)

    if ss["submitted"]:
        st.success("✓ Sandbox complete")
        st.markdown("**Output:**")
        st.markdown(
            f'<div style="background:#F0FBF9;border:1px solid #2EA799;border-radius:6px;'
            f'padding:14px;font-size:13px;line-height:1.7;">{_fmt(ss["output"])}</div>',
            unsafe_allow_html=True,
        )
        return True

    input_key = f"{state_key}_input"
    st.text_area(
        "Your prompt:",
        value=starter_prompt,
        key=input_key,
        height=180,
        label_visibility="collapsed",
    )

    col1, _ = st.columns([1, 5])
    with col1:
        if st.button("Submit →", key=f"{state_key}_submit", type="primary"):
            user_prompt = st.session_state.get(input_key, "").strip()
            if not user_prompt:
                st.warning("Enter a prompt before submitting.")
                return False

            with st.spinner("Calling Haiku…"):
                output = call_sandbox(user_prompt, system_prompt=system_prompt)

            ss["output"] = output
            ss["submitted"] = True
            complete_lesson(track_id, lesson_id)
            st.rerun()

    return False
