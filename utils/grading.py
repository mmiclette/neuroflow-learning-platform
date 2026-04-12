# utils/grading.py
# All Anthropic API calls. API key is read from st.secrets.
# Model: claude-haiku-4-5-20251001 for all graded tasks.

import json
import streamlit as st

HAIKU_MODEL = "claude-haiku-4-5-20251001"

GRADING_SYSTEM_PROMPT = """You are a grading assistant for the NeuroFlow AI Learning Platform.
Score the learner's response against the rubric below.
Return a JSON object with exactly three fields:
  "score": integer 0-100
  "pass": boolean (true if score >= 70)
  "hint": string — one sentence targeting the lowest-scoring criterion. If pass is true, set hint to null. Never reveal the model answer in the hint.

Rubric:
{rubric}

Model answer (your reference only — do not share):
{model_answer}

Grade strictly but fairly. Award partial credit where criteria are partially met.
Short responses can earn full marks — judge on content, not length."""


def _get_client():
    try:
        import anthropic
        return anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
    except Exception as e:
        st.error(f"API configuration error: {e}. Check your Streamlit secrets.")
        return None


def grade_challenge(
    learner_response: str,
    rubric: str,
    model_answer: str,
) -> dict:
    """
    Submit a learner response to Haiku for grading.
    Returns {"score": int, "pass": bool, "hint": str | None}
    """
    client = _get_client()
    if not client:
        return {"score": 0, "pass": False, "hint": "API unavailable — check configuration."}

    system = GRADING_SYSTEM_PROMPT.format(rubric=rubric, model_answer=model_answer)

    try:
        message = client.messages.create(
            model=HAIKU_MODEL,
            max_tokens=512,
            system=system,
            messages=[{"role": "user", "content": learner_response}],
        )
        raw = message.content[0].text.strip()
        # Strip markdown code fences if present
        if raw.startswith("```"):
            raw = raw.split("```")[1]
            if raw.startswith("json"):
                raw = raw[4:]
        result = json.loads(raw)
        return {
            "score": int(result.get("score", 0)),
            "pass": bool(result.get("pass", False)),
            "hint": result.get("hint"),
        }
    except json.JSONDecodeError:
        return {"score": 0, "pass": False, "hint": "Grading response could not be parsed. Try again."}
    except Exception as e:
        return {"score": 0, "pass": False, "hint": f"Grading error: {str(e)[:120]}"}


def call_sandbox_with_search(prompt: str) -> tuple[str, bool]:
    """
    Send a prompt to Haiku with web search enabled.
    Returns (response_text, search_was_used).
    search_was_used is True if Claude actually called the web_search tool.
    """
    client = _get_client()
    if not client:
        return ("API unavailable — check your Streamlit secrets configuration.", False)

    try:
        message = client.messages.create(
            model=HAIKU_MODEL,
            max_tokens=1024,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            messages=[{"role": "user", "content": prompt}],
        )
        search_used = any(
            getattr(block, "type", None) == "tool_use"
            for block in message.content
        )
        text_parts = [
            block.text
            for block in message.content
            if getattr(block, "type", None) == "text"
        ]
        return ("\n".join(text_parts) or "(No text output)", search_used)
    except Exception as e:
        return (f"Error calling model: {str(e)[:200]}", False)


def call_sandbox(prompt: str, system_prompt: str = None) -> str:
    """
    Send a prompt to Haiku for live sandbox lessons.
    Returns the model response text.
    """
    client = _get_client()
    if not client:
        return "API unavailable — check your Streamlit secrets configuration."

    messages = [{"role": "user", "content": prompt}]
    kwargs = {
        "model": HAIKU_MODEL,
        "max_tokens": 1024,
        "messages": messages,
    }
    if system_prompt:
        kwargs["system"] = system_prompt

    try:
        message = client.messages.create(**kwargs)
        return message.content[0].text
    except Exception as e:
        return f"Error calling model: {str(e)[:200]}"
