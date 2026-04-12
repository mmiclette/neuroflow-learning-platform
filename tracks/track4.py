# tracks/track4.py — Track 4: Claude.ai Skills and Projects, 7 lessons

import streamlit as st
from utils.quiz import render_quiz
from utils.challenge import render_graded_challenge
from utils.session import is_lesson_complete, complete_lesson
from utils.grading import call_sandbox_with_search

TRACK_ID = 4

LESSONS = {
    1: {
        "concept": """
A Claude Project is a persistent workspace that holds three things: instructions,
knowledge files, and conversation history. Understanding when to use one — and how
to set it up effectively — is the most high-leverage skill for NeuroFlow team workflows.

**Instructions** apply to every conversation inside the Project. Write them once and
every team member who opens the Project works from the same baseline without re-explaining
context. This is the single biggest efficiency gain Projects offer.

**Knowledge files** are documents Claude references in every Project conversation. Upload
product positioning docs, policy frameworks, clinical guidelines, partner briefs — and
Claude draws on them when answering questions inside the Project, without you needing to
paste the content each time.

**Conversation history** is visible to all Project members. This prevents duplicate work
and surfaces useful prior outputs across the team.

**Projects are shared across teams**

A Project admin creates the Project once, writes the instructions, uploads the knowledge
files, and shares it with the team. Every member who opens that Project works from the same
baseline — the same instructions, the same knowledge files, the same conversation history.
No one needs to rebuild context independently.

To share a Project, the admin invites team members directly from Project Settings. Shared
Projects appear in each member's Project list. Conversation history from all members is
visible inside the Project.

**Maintaining a Project over time**

Projects decay without maintenance. NeuroFlow's products and positioning change. A Project
built in January that no one updates by April is working from stale context. The cadence
that works: weekly (five minutes) — skim recent conversations, add any corrections to the
instructions that you re-prompted twice. Monthly (fifteen minutes) — re-read the full
instruction set and knowledge file list, remove anything no longer true.

The practical test: if you find yourself typing the same background paragraph at the start
of new conversations, that background belongs in a Project.
""",
        "quiz": [
            {
                "question": "What is the primary advantage of Project instructions over typing context at the start of each conversation?",
                "options": [
                    "Project instructions use a more powerful model",
                    "Project instructions are shared with Anthropic for model improvement",
                    "Project instructions enable web search in conversations",
                    "Project instructions apply automatically to every conversation in the Project without re-entry",
                ],
                "correct_index": 3,
                "hint": "The key word is 'automatically' — once written, they apply to every conversation in the Project.",
            },
            {
                "question": (
                    "A BD team member opens the Value Proposition Navigator Project and asks for "
                    "a value proposition for a Medicare Advantage plan. What happens automatically?"
                ),
                "options": [
                    "Claude asks them to re-explain NeuroFlow's products before proceeding",
                    "Claude applies the Project instructions and knowledge files to their request without any additional setup",
                    "Claude needs the team member to upload the relevant product positioning document",
                    "Claude generates a generic value proposition since it cannot access company documents",
                ],
                "correct_index": 2,
                "hint": "Everything a Project admin set up — instructions and knowledge files — is already applied before the conversation starts.",
            },
            {
                "question": (
                    "Your team is building a Project for federal procurement work. The primary "
                    "reference document is a 100-page VA program guide. Pages 1–20 contain the "
                    "program overview your team needs. The remaining 80 pages cover clinical "
                    "protocols that are not relevant. What should you do?"
                ),
                "options": [
                    "Upload the full 100-page document — Claude will focus on the relevant sections",
                    "Screenshot pages 1–20 and upload the images as knowledge files",
                    "Use Adobe Acrobat or a similar tool to extract pages 1–20 and upload only those",
                    "Paste the document into a standard chat, ask for a summary, and add that summary to the Project",
                ],
                "correct_index": 2,
                "hint": "Uploading irrelevant content forces Claude to treat it as potentially relevant context on every query — upload only what the Project needs.",
            },
        ],
    },
    2: {
        "concept": """
A Skill is a self-contained package of instructions that teaches Claude a specific domain
of expertise and a set of workflows. When a skill is active, Claude does not need you to
explain the process, establish the context, or specify the format. It already knows. The
skill loaded that knowledge before the conversation began.

**What a skill is**

A skill is a folder containing a single required file — `SKILL.md` — and optional supporting
files: scripts, reference documents, templates, and assets. The `SKILL.md` file holds two
things: a short metadata block (frontmatter) that tells Claude when to use the skill, and
the full instructions that define what Claude should do when it does.

The frontmatter looks like this:

```
---
name: neuroflow-federal-procurement
description: Monitors and analyzes federal procurement opportunities for NeuroFlow.
  Use when the user asks about SAM.gov solicitations, federal contract opportunities,
  behavioral health RFPs, or phrases like "procurement alert", "new federal opportunity",
  or "check SAM".
---
```

The description field is critical. Claude reads it to decide whether this skill applies
to the current task. Vague descriptions — "helps with federal work" — trigger the skill
at the wrong times. Precise descriptions with trigger phrases ensure it activates exactly
when it should.

**Three persistent capability layers at NeuroFlow**

Understanding where skills fit relative to Projects and plugins prevents confusion:

- **Projects** hold persistent context — instructions, knowledge files, and conversation history scoped to a team workflow
- **Skills** hold persistent expertise — domain knowledge and workflow instructions that Claude loads as capabilities  
- **Plugins** hold persistent tools — specialized reasoning patterns and execution capabilities (Data plugin, Legal plugin, etc.)

Skills are the right layer when you have a recurring workflow that needs domain expertise
and process consistency. A `neuroflow-policy-comments` skill ensures every policy team
member drafting a federal comment letter works from the same regulatory expertise and
letter structure, without re-establishing that expertise in every conversation.

**How to deploy a skill**

You write the `SKILL.md`, upload the folder to Skills in the Claude Teams admin panel,
and the skill becomes available to all team members. When someone's conversation matches
the description trigger phrases, Claude loads the skill's instructions automatically.
""",
        "challenge": {
            "scenario": (
                "NeuroFlow's policy team drafts public comment letters responding to CMS "
                "proposed rules, SAMHSA guidance, congressional RFIs, and policy position "
                "statements. The team currently re-establishes this context in every Claude "
                "conversation from scratch.\n\n"
                "You want Claude to draft a `neuroflow-policy-comments` skill. "
                "**Task:** Write the prompt you would send to Claude to draft this skill. "
                "Your prompt must give Claude the domain expertise to assign, the task types "
                "to include, the audience and output structure to follow, and at least one "
                "explicit constraint on what the skill should prohibit."
            ),
            "broken_example": "",
            "rubric": (
                "Score the prompt against five criteria (20 points each):\n\n"
                "1. Domain and purpose described clearly enough for Claude to write an accurate "
                "description field and role — names the regulatory context and agencies involved, "
                "not just 'policy team'.\n\n"
                "2. Task types specified with at least two concrete examples (public comment "
                "letters, RFI responses, congressional submissions, or similar).\n\n"
                "3. Output structure named — letter sections or format requirements — so Claude "
                "knows what consistency to enforce across users.\n\n"
                "4. Audience or context provided — who the letters go to and what they need "
                "to achieve (CMS, SAMHSA, VA/DoD, congressional staff, or similar).\n\n"
                "5. At least one explicit 'do not' constraint named — the most consequential "
                "prohibition for federal policy submissions."
            ),
            "model_answer": (
                "Draft a Claude skill called neuroflow-policy-comments for NeuroFlow's policy "
                "team. The skill should assign the role of a senior federal health policy analyst "
                "with expertise in CMS rulemaking, SAMHSA guidance, and VA/DoD behavioral health programs.\n\n"
                "Task types to include: public comment letters responding to CMS proposed rules, "
                "SAMHSA guidance responses, congressional RFI responses, and policy position "
                "statements for federal submissions.\n\n"
                "Output structure: every letter must follow this sequence — organization "
                "introduction (2–3 sentences), position statement (1 paragraph, no hedging), "
                "numbered supporting arguments (3–5 paragraphs, each ending with a concrete "
                "recommendation), and a closing ask naming what NeuroFlow wants the agency to do.\n\n"
                "The skill triggers when the user says phrases like 'draft a comment letter', "
                "'respond to this proposed rule', 'write to CMS', or 'RFI response'.\n\n"
                "Include one explicit constraint: do not fabricate citations, statistics, or "
                "outcome data. If a supporting argument lacks a verifiable source, flag the "
                "gap explicitly rather than inventing one."
            ),
            "hints": [
                "Claude needs enough domain detail to write a role. 'Policy team' is not enough — name the expertise, the regulatory context, and the agencies involved.",
                "The output structure is what makes a skill produce consistent results across users. Name the letter sections explicitly so Claude can enforce them.",
                "The constraint is what prevents the most consequential failure mode. In a federal policy context, what should Claude never do?",
            ],
        },
    },
    3: {
        "concept": """
Project instructions are a system prompt applied to every conversation in the Project. Weak
instructions produce inconsistent outputs regardless of how good individual follow-up prompts
are. Strong instructions eliminate entire categories of re-prompting.

**What makes instructions strong**

Strong Project instructions have four elements:

**Role and context** — who Claude is in this Project and what NeuroFlow does. "You are a
senior BD strategist at NeuroFlow, a behavioral health technology company that serves health
systems, Medicaid MCOs, and federal agencies including the VA and DoD." This grounds every
response in the right domain without staff repeating it.

**Persistent task scope** — what this Project is for and what it produces. "This Project
helps the BD team draft outreach emails, value propositions, and partner briefings."

**Output standards** — format, length, and style expectations. "Default to concise,
benefit-forward prose in active voice. Lead with the business outcome. No bullet points
unless the user asks. No clinical jargon in external-facing outputs."

**Constraints** — what Claude should never do in this Project. "Do not use first-person
plural ('we', 'our'). Do not make claims about outcomes without a source. If a request falls
outside BD use cases, note that and ask for clarification."

**Using Claude to write your own instructions**

The most practical way to write strong Project instructions for a recurring workflow is to
use Claude in that conversation to help. After a session that produced good outputs, prompt
Claude to extract and formalize the working context into instructions:

```
Review this conversation and write Project instructions I can paste
directly into Project Settings. The Project helps the BD team draft
value proposition emails for health system buyers. Incorporate the
product positioning doc and case studies uploaded as knowledge files
so Claude draws on them when generating outreach.
```

Claude reads the conversation, identifies the implicit role and constraints, and formalizes
them. The result is instructions that match what already worked — not instructions you have
to draft from scratch.
""",
        "challenge": {
            "scenario": (
                "The NeuroFlow BD team has been using Claude to draft value proposition emails "
                "for health system and payer audiences. After several good sessions, you want to "
                "formalize this into a Project so the whole team can use it consistently.\n\n"
                "**Task:** Write the prompt you would send to Claude — at the end of a working "
                "conversation — to generate Project instructions for a BD Value Proposition "
                "Project. Your prompt must ask Claude to review the conversation, specify the "
                "Project's purpose, and name the knowledge files that should be referenced."
            ),
            "broken_example": "",
            "rubric": (
                "Score the prompt against four criteria (25 points each):\n\n"
                "1. Asks Claude to review the current conversation or prior session to draw "
                "the instructions from — not to invent instructions from scratch.\n\n"
                "2. Specifies the Project's purpose and who will use it (BD team, value "
                "proposition emails, health system or payer audiences, or similar).\n\n"
                "3. Names at least one knowledge file the Project should reference (product "
                "positioning doc, case studies, BHIQ overview, or similar).\n\n"
                "4. Asks for output that can be pasted directly into Project Settings — "
                "'write Project instructions', 'instructions I can paste', or similar phrasing."
            ),
            "model_answer": (
                "Review this conversation and write Claude Project instructions I can paste "
                "directly into Project Settings. The Project should help the BD team draft "
                "value proposition emails for health system and payer buyers. Incorporate "
                "the product positioning doc and the case studies uploaded as knowledge files "
                "so Claude draws on them when generating outreach."
            ),
            "hints": [
                "The most commonly missed element is asking Claude to review the conversation itself. Without this, Claude has no source to draw the instructions from.",
                "Claude doesn't know which files you plan to upload. Name them in the prompt so the instructions tell Claude how to use them.",
                "The output should be ready to paste into Project Settings — phrase the request so Claude produces instructions, not just advice.",
            ],
        },
    },
    4: {
        "concept": """
Claude maintains two types of persistent information about you: memory and user preferences.
Both reduce friction from re-explaining context, but they work at different scopes and with
different priority levels.

**Memory**

Claude generates memories automatically during regular conversations. When you mention your
role, describe a project, share a decision, or express a preference, Claude distills that
into a stored fact and applies it in future sessions without you restating it.

What Claude retains is not a transcript of your conversations. It is a set of distilled
facts: your job function, the teams and products you work on, and preferences you have
expressed. Over time this means Claude starts conversations with working knowledge of who
you are and what you typically need.

To view, edit, or delete your memories, go to **Settings → Memory**. Review this
periodically. Claude may capture something imprecisely or retain a fact that is no longer
accurate. Memories you delete stop applying immediately.

Memory is global — it applies across all conversations and Projects. It takes lower priority
than Project instructions. If your memory says "use bullet points" but the Project
instructions say "use prose paragraphs," the Project wins inside that Project.

**User preferences**

User preferences are standing instructions for how Claude should communicate with you by
default — tone, format, level of technical detail, response length. Unlike memory, which
Claude generates from conversation, preferences are ones you write explicitly.

To set or update your preferences, go to **Settings → Profile**. A well-configured preference:

```
I am [role] at NeuroFlow, a behavioral health technology company.
I primarily work on [domain]. When I ask for written outputs,
default to professional prose in active voice, no bullet points
unless I ask, and assume I have deep healthcare policy context —
do not define basic terms.
```

This eliminates entire categories of follow-up prompts across every conversation you have.

| Setting | Location |
|---|---|
| Memory — view, edit, delete | Settings → Memory |
| User preferences | Settings → Profile |
| Project instructions | Project Settings → Instructions |
""",
        "quiz": [
            {
                "question": "What is the key difference between Claude memory and Project knowledge files?",
                "options": [
                    "Memory stores personal facts about you globally; Project knowledge stores documents scoped to a specific Project",
                    "They are the same mechanism with different names",
                    "Memory only works inside Projects",
                    "Project knowledge files replace memory in all contexts",
                ],
                "correct_index": 0,
                "hint": "Think about scope — where does each type of information apply?",
            },
            {
                "question": (
                    "You have a global memory that says 'always respond in bullet points.' "
                    "You open a Project whose instructions say 'respond in structured prose.' "
                    "What happens inside the Project?"
                ),
                "options": [
                    "Global memory overrides Project instructions",
                    "Claude averages the two styles",
                    "Whichever was set most recently wins",
                    "Project instructions take precedence inside the Project",
                ],
                "correct_index": 3,
                "hint": "Project instructions are scoped and intentional — they take priority over global defaults inside that Project.",
            },
            {
                "question": "Which best describes a well-configured user preference for NeuroFlow staff?",
                "options": [
                    "Uploading a product brief so Claude references it in all conversations",
                    "Telling Claude your role, domain, and default output format so you do not re-explain it each session",
                    "Setting the model to Haiku for all conversations",
                    "Enabling web search by default",
                ],
                "correct_index": 1,
                "hint": "Preferences configure how Claude communicates with you — not what it knows or what tools it uses.",
            },
        ],
    },
    5: {
        "concept": """
When Claude produces a document, code file, structured table, or any standalone deliverable,
it renders in a side panel as an artifact. Understanding when Claude creates an artifact —
and which artifact format to request — determines whether the output is immediately usable.

**When Claude creates an artifact**

Claude creates an artifact when the output is a standalone deliverable: a document, a
spreadsheet, a code file, a presentation, or an interactive web component. Simple
conversational responses, explanations, and short lists stay in the chat.

**Choosing the right format**

The format determines how the recipient can use the output.

**For documents the recipient needs to edit and share** — request a Word document (.docx).
"Write a word document" triggers document formatting, produces a file the recipient can
open in Word or Google Docs, and allows direct editing without any conversion step.

**For structured data** — request a spreadsheet. "Create an Excel spreadsheet" produces a
.xlsx file with correct column structure, formulas if needed, and formatting.

**For web-based interactive tools** — request an HTML page or React component. Use this
when you need something that runs in a browser, like an ROI calculator or a dynamic
comparison tool. Important: these require hosting to share externally — they cannot be
emailed as a working interactive experience.

**For quick reference tables** — inline markdown tables in the chat are faster than
creating a file. Use files when the recipient needs to edit or distribute the content.

**The right question before requesting a format:** What will the recipient do with this
output? Edit it → Word or Excel. View it in a browser → HTML. Run it as code → the
appropriate code file. Share it via email → Word or PDF.
""",
        "quiz": [
            {
                "question": (
                    "You ask Claude to build a site-by-site completion rate tracker. "
                    "You watch it start generating an HTML page. What should you do?"
                ),
                "options": [
                    "Stop the response and tell Claude you need an Excel spreadsheet, specifying the column structure",
                    "Wait for it to finish — it is faster to convert after it completes",
                    "Let it continue — HTML is fine, you can share the file directly",
                    "Let it continue — HTML generates a URL you can share",
                ],
                "correct_index": 0,
                "hint": "If the format is wrong, stopping early saves more time than converting after completion.",
            },
            {
                "question": (
                    "You built a React app inside Claude that calculates BHIQ ROI inputs dynamically. "
                    "It works well in the artifact panel. What is the primary limitation when sharing it?"
                ),
                "options": [
                    "React artifacts cannot be shared with internal team members inside Claude",
                    "The artifact panel only shows the raw code, not the running app",
                    "It needs to be hosted on a server before it can be shared with anyone outside the organization",
                    "React apps built in Claude cannot be used for demos",
                ],
                "correct_index": 2,
                "hint": "The artifact panel runs the app for you — but external sharing requires a URL, which requires hosting.",
            },
        ],
    },
    6: {
        "concept": """
Claude's training data has a cutoff date. It does not know about recent policy changes,
new research, or current program status unless it searches the web. Web search and Deep
Research are two separate capabilities — both require explicit activation.

**Activating web search**

Web search is not on by default. To enable it, open the Tools panel at the bottom of the
chat input and toggle Search on. Once enabled, Claude can retrieve current information from
the internet during your conversation.

Even with search enabled, Claude does not always search automatically. If your question
looks like something Claude can answer from training data, it may respond without searching.
When you need current information, tell Claude explicitly to search:

```
Search the web for the current status of the CMS ACO REACH model.
Summarize what you find and cite your sources.
```

Without that instruction, Claude may answer from its training data and present outdated
information confidently. Making the search instruction explicit ensures Claude retrieves
current results.

**Activating Deep Research**

Deep Research is a separate mode — not a toggle inside a standard conversation. Access it
from the model selector. Deep Research browses multiple sources, reads full documents, and
compiles a structured report. Use it for landscape assessments, policy surveys, or
competitive overviews that would otherwise require hours of manual searching.

Deep Research is the most token-intensive Claude capability. Each session consumes
substantially more allocation than a standard conversation. Use it for work that genuinely
requires multi-source synthesis, not for single-question lookups.

**When to cite your sources**

Before using a finding in a business document, confirm the source exists and says what Claude
claims. The citation requirement — "cite your sources" — is not optional for externally-facing
work. It is the mechanism that separates a verified answer from a confident but potentially
outdated one.
""",
        "sandbox_lesson": True,
    },
    7: {
        "concept": """
Style settings configure Claude's default output behavior — tone, length, and format — so
you do not repeat those instructions in every prompt. Getting style right once saves you
from adding the same formatting and tone instructions to hundreds of future conversations.

**What you can configure**

- **Tone** — formal, professional, conversational, direct
- **Length** — shorter responses, longer and more detailed
- **Format** — more prose, more lists, more headers, more flowing text

**Two scopes**

**User preferences (global)** — applies to all conversations outside Projects. Set this to
match your personal working style.

**Project instructions (scoped)** — applies only within that Project. Should match the
output expectations for that specific workflow. A policy Project defaults to formal structured
prose. A BD Project defaults to concise, benefit-forward language.

**Project instructions take precedence over global preferences** inside a Project. Global
preferences are the default; Project instructions are the override for that specific workflow.

**Recognizing AI-generated writing patterns**

Style customization also helps you avoid the most recognizable patterns in AI-generated
text. Large language models have stylistic tells that technically literate readers — health
system executives, federal program officers, congressional staff — recognize on sight.

The most common: overuse of em dashes as connective punctuation. A sentence like "Our
platform reduces utilization — at scale" uses a dash where no pause belongs. It reads as
generated text to anyone who encounters it regularly. Setting a constraint like "avoid
em dashes, use plain sentence structure instead" eliminates this before it reaches
a reader who will notice.
""",
        "quiz": [
            {
                "question": (
                    "A BD team member drafts a partner brief using Claude. The output contains "
                    "this sentence: 'NeuroFlow's BHIQ platform identifies high-risk members early "
                    "— enabling care teams to intervene before avoidable utilization occurs — "
                    "at scale across diverse populations.'\n\n"
                    "What is a concern about sending this externally as written?"
                ),
                "options": [
                    "The sentence is too long and should be broken into two",
                    "The claim about reducing utilization needs a citation",
                    "Large language models overuse em dashes as connective punctuation — this pattern is recognizable as AI-generated writing and may undermine credibility with sophisticated readers",
                    "'At scale' is jargon that should be removed for a health system audience",
                ],
                "correct_index": 2,
                "hint": "Think about what the reader — a health system executive or federal program officer — will recognize.",
            },
            {
                "question": (
                    "You set a global style preference for 'concise bullet-point format.' "
                    "You open a Project whose instructions specify 'respond in structured prose "
                    "paragraphs.' What happens inside the Project?"
                ),
                "options": [
                    "Claude uses structured prose — Project instructions take precedence inside the Project",
                    "Claude uses bullet points — global preference overrides Project instructions",
                    "Claude uses both and you choose which to apply",
                    "Claude asks which format you want",
                ],
                "correct_index": 0,
                "hint": "Project instructions are intentional overrides — they win inside that Project.",
            },
            {
                "question": (
                    "A BD team member adds 'be more concise and direct' to every single "
                    "prompt they write. What is a more efficient solution?"
                ),
                "options": [
                    "Write longer prompts with more explicit constraints",
                    "Switch to a faster model",
                    "Use a different AI tool for BD work",
                    "Set a style preference or Project instruction for concise, direct responses once",
                ],
                "correct_index": 3,
                "hint": "If you are repeating the same instruction in every prompt, that instruction belongs in a persistent setting.",
            },
        ],
    },
}


def _render_search_sandbox(lesson_id: int) -> bool:
    """Lesson 4.6 sandbox: learner writes a search prompt, sees result."""
    state_key = f"sandbox_{TRACK_ID}_{lesson_id}"
    if state_key not in st.session_state:
        st.session_state[state_key] = {"submitted": False, "output": "", "searched": False}
    ss = st.session_state[state_key]

    st.markdown("---")
    st.markdown("### Live sandbox — web search")
    st.markdown(
        "NeuroFlow's quality team needs a summary of the 2026 HEDIS behavioral health "
        "quality measures. Write a prompt to retrieve this information from Claude. "
        "**Include an explicit instruction to search the web** so Claude retrieves current "
        "measures rather than answering from training data."
    )

    if ss["submitted"]:
        st.success("✓ Sandbox complete")
        if ss["searched"]:
            st.markdown(
                '<div style="background:#F0FBF9;border:1px solid #2EA799;border-radius:6px;'
                'padding:4px 12px;margin-bottom:8px;font-size:12px;color:#1A6860;">'
                '✓ Claude used web search</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div style="background:#FFF3F3;border:1px solid #F16061;border-radius:6px;'
                'padding:4px 12px;margin-bottom:8px;font-size:12px;color:#C0392B;">'
                '⚠ Claude did not use web search — training data only</div>',
                unsafe_allow_html=True,
            )
        st.markdown("**Output:**")
        st.markdown(
            f'<div style="background:#F9F9F9;border:1px solid #BDBDBD;border-radius:6px;'
            f'padding:14px;font-size:13px;line-height:1.7;">{ss["output"]}</div>',
            unsafe_allow_html=True,
        )
        return True

    input_key = f"{state_key}_input"
    starter = (
        "Search the web for the current 2026 HEDIS behavioral health quality measures "
        "and summarize what you find. Cite your sources."
    )
    st.text_area(
        "Your prompt:", value=starter, key=input_key,
        height=140, label_visibility="collapsed",
    )
    col1, _ = st.columns([1, 5])
    with col1:
        if st.button("Submit →", key=f"{state_key}_submit", type="primary"):
            prompt = st.session_state.get(input_key, "").strip()
            if not prompt:
                st.warning("Enter a prompt before submitting.")
                return False
            with st.spinner("Calling Haiku with web search…"):
                output, searched = call_sandbox_with_search(prompt)
            ss["output"] = output
            ss["searched"] = searched
            ss["submitted"] = True
            complete_lesson(TRACK_ID, lesson_id)
            st.rerun()
    return False


def render_lesson(lesson_id: int) -> bool:
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        st.error(f"Lesson 4.{lesson_id} not found.")
        return False

    already_done = is_lesson_complete(TRACK_ID, lesson_id)
    st.markdown(lesson["concept"])
    st.markdown("---")

    if already_done:
        st.success("✓ Lesson complete")
        return True

    # Lessons with quiz only
    if lesson.get("quiz") and not lesson.get("challenge"):
        return render_quiz(
            track_id=TRACK_ID, lesson_id=lesson_id,
            questions=lesson["quiz"], label="Knowledge check",
        )

    # Graded challenge lessons (4.2, 4.3)
    if lesson.get("challenge"):
        ch = lesson["challenge"]
        return render_graded_challenge(
            track_id=TRACK_ID, lesson_id=lesson_id,
            scenario=ch["scenario"], broken_example=ch["broken_example"],
            rubric=ch["rubric"], model_answer=ch["model_answer"],
            hints=ch["hints"], input_label="Your prompt",
            max_chars=700, single_attempt=False,
        )

    # Lesson 4.6 — web search sandbox
    if lesson.get("sandbox_lesson"):
        return _render_search_sandbox(lesson_id)

    st.info("Content coming soon.", icon="🔜")
    return False
