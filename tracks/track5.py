# tracks/track5.py — Track 5: Plugins, Connectors, and Integrations

import streamlit as st
from utils.quiz import render_quiz
from utils.challenge import render_graded_challenge
from utils.session import is_lesson_complete, complete_lesson
from utils.grading import call_sandbox

TRACK_ID = 5

SAMPLE_CSV = """Site,Completion Rate (%),Responses,Target (%)
Meadows Health,87,214,80
Riverside Clinic,72,189,80
Valley Behavioral,91,308,80
Summit Mental Health,65,142,80
Harbor Wellness,78,267,80
Greenfield Center,58,98,80
Northside Clinic,83,176,80
Eastbridge Health,69,234,80
Lakewood Institute,94,412,80
Pinecrest Counseling,77,155,80"""

LESSONS = {
    1: {
        "concept": """
Claude's connectors are built on a secure integration layer that creates authenticated
bridges between Claude and external services. You find and enable connectors
in the Search and tools panel at the bottom left of any Claude conversation. Each connector
you add appears there as a toggle. Disable connectors not relevant to your current task
before starting — each active connector adds retrieval overhead even when unused.

**Read actions vs. write actions**

Not all connector capabilities carry the same risk. Read actions — searching emails, pulling
a Salesforce record, viewing a Slack channel — retrieve information without changing anything.
Write actions — logging notes, creating tasks, sending messages, updating records — modify
real data in live systems.

When a connector requests permission for a write action, Claude will show you what it proposes
to do and ask for confirmation. The permission prompt offers three options: allow once, allow
always, or block. Reserve "Allow always" for write actions you have tested and are confident
with. For write-capable connectors like HubSpot, Salesforce, and Monday, "Needs approval" is
the safer default until the behavior is familiar.

**Data policy applies to connectors**

Connecting a data source to Claude brings its contents into the conversation. The same rule
applies: do not connect any source that contains PHI. A Snowflake database with patient
assessment scores or any system containing identifiable patient information must not be
connected to Claude Teams. Analyze that data in tools that operate under NeuroFlow's HIPAA
agreements.
""",
        "quiz": [
            {
                "question": (
                    "NeuroFlow's patient assessment data lives in Snowflake. A data analyst wants "
                    "to use Claude to analyze behavioral health outcomes from that data. A Snowflake "
                    "connector is available in the directory. What is the right approach?"
                ),
                "options": [
                    "Connect the Snowflake connector so Claude can query the data directly",
                    "Export a de-identified summary from Snowflake and paste it into Claude Teams for analysis",
                    "Do not connect Claude Teams account to Snowflake, because the data contains PHI",
                    "Use the Data plugin, which operates under a separate HIPAA-compliant framework",
                ],
                "correct_index": 2,
                "hint": "Before connecting any data source, identify what category of information it contains.",
            },
            {
                "question": (
                    "A BD team member asks Claude to pull up recent emails from a health system "
                    "partner before a call. The Gmail connector is active. What does Claude do?"
                ),
                "options": [
                    "Tells the user to forward the relevant emails into the conversation manually",
                    "Calls the Gmail connector to retrieve the emails directly, without the user opening Gmail or pasting anything",
                    "Searches its training data for information about that health system",
                    "Asks the user to copy the email thread into the chat before proceeding",
                ],
                "correct_index": 1,
                "hint": "The connector creates a live bridge — Claude retrieves from the source directly.",
            },
            {
                "question": (
                    "After a discovery call, a BD team member wants to log call notes to the "
                    "Salesforce opportunity record and create a Monday task for the agreed "
                    "follow-up. What does each connector handle?"
                ),
                "options": [
                    "Salesforce handles both — it syncs automatically with Monday",
                    "Salesforce logs the notes and updates the deal record; the Monday connector creates the follow-up task",
                    "The Gmail connector logs the notes; Monday creates the task",
                    "One connector handles both actions since they are part of the same workflow",
                ],
                "correct_index": 1,
                "hint": "Each connector handles the service it connects to — there is no cross-service sync.",
            },
        ],
    },
    2: {
        "concept": """
Connectors extend Claude's reach — they let Claude pull information from and take actions in
the tools your team already uses. Plugins extend Claude's capabilities — they give Claude a
focused skill set and specialized tools for a specific category of work.

<p style="color:#161BAA;font-weight:600;font-size:15px;margin:16px 0;">A connector answers: where can Claude go? A plugin answers: what can Claude do once it gets there?</p>

Anthropic builds and maintains plugins. Each one adds domain-specific defaults, specialized
reasoning patterns, and execution tools that Claude does not have in a standard conversation.

**Plugins relevant to NeuroFlow roles**

The **Data plugin** lets Claude execute queries against structured data and render charts.
A data analyst producing a ranked chart from a CSV benefits from this because it provides
execution capabilities — running calculations and rendering visuals — that standard chat cannot.

The **Legal plugin** adds document review and regulatory compliance research capabilities.
A policy analyst reviewing a CMS final rule gets specialized regulatory document reasoning
applied automatically without specifying it in every prompt.

The **Sales plugin** adds deal coaching, pipeline reasoning, and outreach generation. A BD
team member drafting a five-part outreach sequence benefits from outreach structure defaults
that a standard prompt would have to specify manually.

The **Engineering plugin** adds code review patterns, architecture decision frameworks, and
incident documentation workflows for technical staff.

**When to use vs. skip a plugin**

Use a plugin when the task falls squarely within a domain category and you want those
defaults applied automatically across the session. Do not use a plugin when a well-crafted
prompt handles the task — a single outreach email drafted with a strong RTCFC prompt does
not need the Sales plugin. Plugins add token overhead. Use the simplest approach that
achieves the result.

**Using plugins across roles**

Plugins are often designed for a specific role or field, but you do not need to use the
full package. Each plugin bundles skills, connectors, and sub-agents together — but
individual skills surface as slash commands you can trigger on demand. If one or two skills
from the Sales or Legal plugin are useful to your workflow, you can use those without
engaging the rest of the plugin.

If nothing in the existing library fits your task, Plugin Create walks you through building
something from scratch, or you can start from an existing template and modify it. The
answer to "what am I trying to do" may already exist inside a plugin built for a different
role.
""",
        "quiz": [
            {
                "question": (
                    "A NeuroFlow policy analyst needs to review a 40-page CMS final rule for "
                    "compliance requirements relevant to behavioral health technology vendors. "
                    "They want Claude to apply specialized regulatory document review reasoning "
                    "automatically across the session without specifying it in every prompt. "
                    "Which plugin fits this task?"
                ),
                "options": [
                    "Operations — it handles process documentation and vendor management",
                    "Legal — it adds document review and regulatory compliance research capabilities tuned for this category of work",
                    "Productivity — it manages tasks and context across workstreams",
                    "Data — it analyzes structured datasets and renders charts",
                ],
                "correct_index": 1,
                "hint": "Match the plugin to the domain category — what type of work is this task?",
            },
        ],
    },
    3: {
        "concept": """
> 📌 **Screenshot placeholder — Tools panel**
> *Insert annotated screenshot of the Claude Teams interface showing the Search and tools panel (bottom left), with the connector list visible and one connector toggled on. Annotate: (1) where to find the panel, (2) the toggle for enabling/disabling connectors, (3) the permission prompt that appears on first write action.*


Connectors and plugins do not change the relationship between prompt quality and output quality.
A vague connector prompt produces unfocused retrieval. A vague Data plugin prompt produces
descriptive prose instead of analysis. The tools provide capability. The prompt determines
whether that capability produces something useful.

**Prompting for connectors — four required properties**

1. **Name the specific service.** "Check my email" leaves Claude to decide where to look.
   "Search my Gmail for emails from Meadows Mental Health in the last 30 days" gives Claude
   a retrievable scope in a specific system.

2. **Define a time window or retrieval scope.** Without one, Claude retrieves broadly.
   A time window — last 30 days, this week, since January 1 — focuses the retrieval.

3. **Specify the output structure.** Name sections, format, and word count before Claude
   starts generating. "Produce a five-sentence account summary with three named sections"
   produces a structured deliverable.

4. **State the purpose.** A brief for a colleague before a call reads differently than a
   Salesforce note. Telling Claude what the output is for shapes how it frames the synthesis.

**Prompting for the Data plugin**

The most common mistake is asking Claude to describe data when the goal is to analyze it.
"Describe the trends in this CSV" produces prose. "Calculate the average completion rate
per site, identify the three highest and three lowest performers, and generate a bar chart
ranked descending" produces a ranked chart with calculated values.

Name the calculation, the ranking logic, the chart type, and the sort order.

**Prompting for Monday**

Monday board items have defined fields — item name, status, assignee, due date, priority.
A prompt that names the board, defines the item, and lists the field values produces a clean
board update. A prompt that says "add this to Monday" leaves Claude to guess the board,
the item name, and every field.
""",
        "sandbox_lesson": True,
        "data_challenge": {
            "scenario": (
                "You are a program manager reviewing PHQ-9 completion rates across 10 sites. "
                "The Data plugin can run calculations and generate charts directly from the "
                "table below.\n\n"
                "Write a prompt that asks Claude to analyze this data and produce a visual "
                "output. Your prompt should request a specific calculation (e.g. an average "
                "completion rate), name a chart type (e.g. bar chart) and how to sort it "
                "(e.g. from lowest completion rate to highest), and set a threshold to flag "
                "sites that need attention (e.g. flag any site below 80%).\n\n"
                "| Site | Rate |\n"
                "| Riverside | 71% |\n"
                "| Oakland | 88% |\n"
                "| Sacramento | 64% |\n"
                "| Fresno | 82% |\n"
                "| Stockton | 56% |\n"
                "| Modesto | 79% |\n"
                "| San Jose | 91% |\n"
                "| Bakersfield | 68% |\n"
                "| Santa Rosa | 85% |\n"
                "| Redding | 73% |\n"
            ),
            "rubric": (
                "Score the prompt against three criteria (33 points each, rounded to 100):\n\n"
                "1. Asks for at least one specific calculation — average rate, highest/lowest "
                "performers, sites below a threshold, or similar numeric analysis.\n\n"
                "2. Names a specific chart type (bar chart, line chart, etc.) and a sort "
                "order (ascending, descending, alphabetical, or ranked).\n\n"
                "3. Includes a benchmark or threshold to interpret against — for example "
                "'below 80%', 'above target', or a specific numeric cutoff.\n\n"
                "If any criterion is missing, the hint must name it specifically — e.g. "
                "'Your prompt did not specify a chart type' or 'Your prompt did not include "
                "a benchmark to interpret the results against.' Never give generic feedback."
            ),
            "model_answer": (
                "Using the PHQ-9 completion rate data, calculate the average completion rate "
                "per site and identify the three highest and three lowest performers. Generate "
                "a bar chart ranked by completion rate descending. Add a one-sentence "
                "interpretation noting which sites fall below the 80% target."
            ),
            "hints": [
                "A strong prompt names a specific calculation AND a chart type with a sort order.",
                "Add a benchmark — e.g. '80% target' — so the output is self-interpreting.",
            ],
        },
    },
    4: {
        "concept": """
> 📌 **Screenshot placeholder — Plugin selector**
> *Insert annotated screenshot of the Claude Teams interface showing the plugin selection menu, with at least one plugin active. Annotate: (1) where plugins appear in the UI, (2) how to tell a plugin is active, (3) the slash command palette that shows available plugin skills.*


Plugins, connectors, and well-crafted prompts can each produce outputs that look similar on
the surface. Knowing which to reach for prevents two equally common mistakes: over-engineering
a simple task by adding tools it does not need, and under-powering a complex one by leaving
out the tool that makes it possible.

**The decision framework**

**Prompt only** — when all the information is already in the conversation and the output does
not require execution capabilities beyond generating text. This covers more ground than most
people expect. Policy briefs, outreach emails, competitive analyses, go-to-market strategies —
all are prompt-only tasks as long as source material is present and the deliverable is text.

**Connector** — when the information Claude needs lives in an external service and cannot or
should not be pasted in. The question is not whether a connector is available — it is whether
Claude needs to go somewhere to retrieve information or take an action it cannot do from within
the conversation.

**Plugin** — when the task requires execution capabilities that standard chat cannot provide
(Data plugin for calculations and charts), or when domain-specific defaults add enough value
across a repeated-task session to justify the overhead.

**Combination** — when the task needs live data from an external service AND execution
capabilities. A chart analysis session that needs files from Google Drive that are not
downloaded locally requires the Drive connector to retrieve the files and the Data plugin
to execute the analysis and render the chart.

**The simplicity principle**

Use the lightest combination that achieves the result. Every added capability layer increases
token overhead and potential points of failure. Connectors add retrieval overhead. Plugins add
domain tooling. Deep Research is the most intensive. For staff who hit usage limits frequently,
simplifying the tool stack is the first step.
""",
        "quiz": [
            {
                "question": (
                    "A NeuroFlow communications manager is writing a 300-word LinkedIn post "
                    "announcing NeuroFlow's participation in a new federal program. All relevant "
                    "details are in a PDF they have attached to the conversation. "
                    "What is the right approach?\n\n"
                    "A) Prompt only\n"
                    "B) Connector\n"
                    "C) Plugin\n"
                    "D) Combination — connector and plugin"
                ),
                "options": [
                    "A) Prompt only — all source material is attached and the deliverable is text",
                    "B) Connector — LinkedIn requires a connector to draft and post",
                    "C) Plugin — the Marketing plugin improves social content quality, but only adds value when Claude needs specialised defaults or tools not available in a standard prompt",
                    "D) Combination — the Marketing plugin plus a connector to pull program details",
                ],
                "correct_index": 0,
                "hint": "All source material is attached and the deliverable is text. The threshold for adding a plugin is when the task requires execution Claude cannot do natively — rendering charts, running calculations, or accessing live external data. A 300-word post from an attached PDF does not cross that threshold.",
            },
            {
                "question": (
                    "A NeuroFlow data analyst has six months of PHQ-9 completion data from an "
                    "exported CSV saved on their desktop. They need a bar chart showing completion "
                    "rates by site ranked highest to lowest. What is the right approach?\n\n"
                    "A) Prompt only\n"
                    "B) Connector\n"
                    "C) Plugin\n"
                    "D) Combination"
                ),
                "options": [
                    "A) Prompt only — Claude can describe the data from an attached file",
                    "B) Connector — the data needs to be retrieved before Claude can analyze it",
                    "C) Plugin — the Data plugin executes the calculation and renders the chart; the file is already available to attach",
                    "D) Combination — the Data plugin plus a connector to access the file",
                ],
                "correct_index": 2,
                "hint": "The file is already on their desktop and can be attached. What capability does rendering a chart require?",
            },
            {
                "question": (
                    "A program manager needs to analyze Q2 PHQ-9 completion data uploaded to a "
                    "shared Google Drive folder this morning. They do not have the file downloaded "
                    "locally. They need a ranked bar chart by site AND a trend comparison against "
                    "Q1, which is in the same Drive folder. What is the right approach?\n\n"
                    "A) Prompt only\n"
                    "B) Connector\n"
                    "C) Plugin\n"
                    "D) Combination"
                ),
                "options": [
                    "A) Prompt only — attach the files before starting the conversation",
                    "B) Connector — the Drive connector retrieves the files and Claude describes the trends",
                    "C) Plugin — the Data plugin handles chart generation once files are in the conversation",
                    "D) Combination — the Drive connector retrieves both files and the Data plugin executes the analysis and renders the charts",
                ],
                "correct_index": 3,
                "hint": "Two things are needed here that neither tool can provide alone — what are they?",
            },
            {
                "question": (
                    "A BD team member is drafting a detailed go-to-market brief for BHIQ targeting "
                    "ACO REACH participants. They have a product positioning document and three "
                    "case studies ready to attach. The deliverable is a structured written brief. "
                    "What is the right approach?\n\n"
                    "A) Prompt only\n"
                    "B) Connector\n"
                    "C) Plugin\n"
                    "D) Combination"
                ),
                "options": [
                    "A) Prompt only — all source material is attached and the deliverable is a text brief",
                    "B) Connector — the brief requires pulling live market data from an external source",
                    "C) Plugin — the Sales plugin improves go-to-market brief quality automatically",
                    "D) Combination — the Sales plugin plus connectors to pull competitive data",
                ],
                "correct_index": 0,
                "hint": "All source material is present and the deliverable is text. The threshold for adding a plugin is when the task requires execution Claude cannot do natively — charts, calculations, code. A 300-word post from attached material does not cross that threshold.",
            },
        ],
    },
}


def _render_data_sandbox(lesson_id: int) -> bool:
    """Lesson 5.3 sandbox — simulate Data plugin with embedded CSV."""
    state_key = f"sandbox_{TRACK_ID}_{lesson_id}"
    if state_key not in st.session_state:
        st.session_state[state_key] = {"submitted": False, "output": ""}
    ss = st.session_state[state_key]

    st.markdown("---")
    st.markdown("### Live sandbox — Data plugin simulation")
    st.markdown(
        "The table below shows a 10-row sample CSV of PHQ-9 completion rates by site. "
        "Write a prompt that produces **at least one calculated result and one chart**. "
        "Specify the chart type and sort order explicitly rather than asking Claude to describe."
    )
    st.code(SAMPLE_CSV, language="text")

    MODEL_ANSWER_53 = (
        "Using the PHQ-9 completion rate data provided, calculate the average completion "
        "rate per site. Identify the three highest and three lowest performers. Generate "
        "a bar chart ranked by completion rate descending. Add a one-sentence interpretation "
        "below the chart noting which sites are below the 80% target."
    )

    if ss["submitted"]:
        st.success("✓ Sandbox complete")
        st.markdown("**Your output:**")
        st.markdown(
            f'<div style="background:#F0FBF9;border:1px solid #2EA799;border-radius:6px;'
            f'padding:14px;font-size:13px;line-height:1.7;">{__import__("html").escape(ss["output"]).replace(chr(10), "<br>")}</div>',
            unsafe_allow_html=True,
        )
        st.markdown("**What a strong prompt includes:**")
        st.markdown(
            '- A specific calculation (e.g. average rate per site, highest/lowest performers)\n'
            '- An explicit chart type and sort order\n'
            '- A benchmark or threshold to interpret against (e.g. 80% target)\n'
            '- A one-sentence interpretation so the output is self-explanatory'
        )
        st.markdown(f"**Example prompt:**\n\n> {MODEL_ANSWER_53}")
        return True

    input_key = f"{state_key}_input"
    st.text_area(
        "Your prompt:", value="", key=input_key,
        height=140, label_visibility="collapsed",
        placeholder="Write a prompt asking Claude to calculate results and produce a chart from the data above. Specify the chart type and what you want calculated.",
    )
    col1, _ = st.columns([1, 5])
    with col1:
        if st.button("Submit →", key=f"{state_key}_submit", type="primary"):
            prompt = st.session_state.get(input_key, "").strip()
            if not prompt:
                st.warning("Enter a prompt before submitting.")
                return False
            full_prompt = (
                f"Here is a CSV of PHQ-9 completion rates by site:\n\n{SAMPLE_CSV}\n\n{prompt}"
            )
            with st.spinner("Calling Haiku…"):
                output = call_sandbox(full_prompt)
            ss["output"] = output
            ss["submitted"] = True
            complete_lesson(TRACK_ID, lesson_id)
            st.rerun()
    return False


def render_lesson(lesson_id: int) -> bool:
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        st.error(f"Lesson 5.{lesson_id} not found.")
        return False

    already_done = is_lesson_complete(TRACK_ID, lesson_id)
    # Handle inline HTML in concept
    import re as _re
    concept = lesson["concept"]
    if "<p " in concept or "<div " in concept:
        parts = _re.split(r'(<(?:p|div)\b[^>]*>.*?</(?:p|div)>)', concept, flags=_re.DOTALL)
        for part in parts:
            if not part.strip():
                continue
            if part.lstrip().startswith('<p ') or part.lstrip().startswith('<div '):
                st.markdown(part, unsafe_allow_html=True)
            else:
                st.markdown(part)
    else:
        st.markdown(concept)
    st.markdown("---")

    if already_done:
        if not (lesson.get("sandbox_lesson") or lesson.get("challenge")):
            st.success("✓ Lesson complete")
            return True

    if lesson.get("sandbox_lesson"):
        dc = lesson.get("data_challenge")
        if dc:
            return render_graded_challenge(
                track_id=TRACK_ID, lesson_id=lesson_id,
                scenario=dc["scenario"], broken_example="",
                rubric=dc["rubric"], model_answer=dc["model_answer"],
                hints=dc["hints"], input_label="Your Data plugin prompt",
                max_chars=400, single_attempt=True,
            )
        return _render_data_sandbox(lesson_id)

    if lesson.get("quiz"):
        return render_quiz(
            track_id=TRACK_ID, lesson_id=lesson_id,
            questions=lesson["quiz"], label="Knowledge check",
        )

    st.info("Content coming soon.", icon="🔜")
    return False
