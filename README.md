# NeuroFlow AI Learning Platform

Internal self-paced learning platform for NeuroFlow staff. Eight tracks covering AI fundamentals through agents and MCP. Built with Streamlit. All 43 lessons are complete.

## Quick deploy

### 1. Clone and install

```bash
git clone <your-repo-url>
cd neuroflow-ai-learning
pip install -r requirements.txt
```

### 2. Configure API key

Create `.streamlit/secrets.toml` (gitignored):

```toml
ANTHROPIC_API_KEY = "sk-ant-..."
```

### 3. Run locally

```bash
streamlit run app.py
```

### 4. Deploy to Streamlit Cloud

1. Push repo to GitHub (public or private)
2. Go to [share.streamlit.io](https://share.streamlit.io) → New app
3. Select repo, branch `main`, entry point `app.py`
4. Settings → Secrets → paste your `secrets.toml` content
5. Deploy

---

## Curriculum

| Track | Title | Level | Lessons |
|---|---|---|---|
| 1 | AI fundamentals | Foundation | 3 |
| 2 | Claude fundamentals | Foundation | 5 |
| 3 | Prompt engineering | Foundation | 8 |
| 4 | Claude.ai skills and projects | Intermediate | 7 |
| 5 | Plugins, connectors, and integrations | Intermediate | 4 |
| 6 | Cowork and desktop automation | Intermediate | 6 |
| 7 | Claude Code | Advanced | 5 |
| 8 | Agents and MCP | Advanced | 5 |

**43 lessons · 75 quiz questions · 13 graded challenges · 4 sandboxes · 5 diagrams · 2 video lessons · 8 certificates**

Tracks 1–3 are for all staff. Tracks 7–8 are for engineers and technical staff.

---

## Key mechanics

**Quiz failure rule:** Three wrong answers on any quiz lesson forces a lesson restart. No continuation until the learner confirms restart. Counter is per-lesson, not per-question.

**Graded challenge flow:** Single text submission → Haiku scores against a rubric → score returned with explanation → model answer revealed after the third failure. Passing threshold: 70/100.

**Lesson 3.2 single-attempt:** Submit once, always advance regardless of score. Haiku returns an explanation of what was and wasn't covered.

**Session-only state:** No database. No user accounts. No saved progress across browser sessions. A warning banner on every lesson page reminds learners of this.

**Certificates:** Learner enters their name on the certificate page after completing all lessons in a track. Certificate renders as a printable HTML view with NeuroFlow branding.

---

## Project structure

```
app.py                     # Entry point — routing, page renders, global CSS
requirements.txt
data/
  curriculum.py            # All track and lesson metadata (source of truth)
utils/
  session.py               # Session state, navigation helpers, progress tracking
  quiz.py                  # Quiz component — 3-wrong-answer restart rule
  challenge.py             # Graded challenge component — 3-attempt model answer reveal
  grading.py               # Anthropic API calls (Haiku grading + sandbox)
  sandbox.py               # Live and comparison sandbox renderers
  certificate.py           # Certificate HTML generator and print view
components/
  diagrams.py              # Five SVG diagrams as Python string constants
tracks/
  track1.py                # AI fundamentals (3 lessons)
  track2.py                # Claude fundamentals (5 lessons)
  track3.py                # Prompt engineering (8 lessons)
  track4.py                # Claude.ai skills and projects (7 lessons)
  track5.py                # Plugins, connectors, and integrations (4 lessons)
  track6.py                # Cowork and desktop automation (6 lessons)
  track7.py                # Claude Code (5 lessons)
  track8.py                # Agents and MCP (5 lessons)
```

---

## Adding or editing lesson content

Each track file exports:
- `LESSONS: dict` — lesson content keyed by `lesson_id` (integer)
- `render_lesson(lesson_id: int) -> bool` — renders the lesson, returns `True` when passed

Minimal lesson entry:

```python
LESSONS = {
    1: {
        "concept": "Markdown rendered above the quiz.",
        "quiz": [
            {
                "question": "Question text",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "correct_index": 1,   # 0-based
                "hint": "Shown after a wrong answer.",
            }
        ],
    }
}
```

For graded challenges, call `utils/challenge.render_graded_challenge()`.
For live sandboxes, call `utils/grading.call_sandbox()` or `call_sandbox_with_search()`.

---

## Diagrams

Five SVG diagrams stored as string constants in `components/diagrams.py`:

| ID | Lesson | Description |
|---|---|---|
| `context_window` | 2.1 | Tokens, context window boundary, what falls outside |
| `rtcfc` | 3.1 | Five RTCFC prompt components with labels |
| `connector_ecosystem` | 5.3 | NeuroFlow MCP services and relationships |
| `project_structure` | 7.3 | `.claude/` directory structure with annotations |
| `agent_loop` | 8.1 | Agentic loop flowchart |

SVG uses hardcoded hex values only — no CSS custom properties. Dark mode via `prefers-color-scheme: dark` inside a `<style>` block within the SVG.

---

## API usage

All Haiku calls go through `utils/grading.py`. The API key is read from `st.secrets["ANTHROPIC_API_KEY"]` (Streamlit Cloud) or `ANTHROPIC_API_KEY` environment variable (local). The key is never exposed client-side.

**Model:** `claude-haiku-4-5-20251001`

**API-calling lessons:** 2.4, 3.1, 3.2, 3.4, 3.8, 4.2, 4.3, 4.6, 5.3, 6.2, 7.3, 7.4, 7.5, 8.4, 8.5
