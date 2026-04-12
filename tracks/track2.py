# tracks/track2.py
# Track 2 — Claude Fundamentals
# 5 lessons, Foundation level. Lesson 2.4 uses a Haiku graded challenge.

import streamlit as st
from utils.quiz import render_quiz
from utils.challenge import render_graded_challenge
from utils.session import is_lesson_complete

TRACK_ID = 2

LESSONS = {
    1: {
        "concept": """
Claude is a large language model built by Anthropic. Understanding how it processes your
input explains why some prompts work and others do not — and why verifying outputs is
always necessary.

**How Claude generates a response**

Claude does not search a database or retrieve a stored answer. It reads your entire
input — every word in the conversation up to that point — and generates a response one
token at a time, predicting the most statistically likely next token given everything
it has processed.

Four terms appear throughout this program:

**Token** — the unit Claude processes. Roughly equivalent to a word or word fragment.
"Hello" is one token. "Measurement-based" is likely two. You are billed for tokens
consumed, which is why heavier models cost more of your usage allocation per conversation.

**Context window** — the total amount of text Claude can hold in its working memory at
once. Claude's context window is 200,000 tokens — roughly 150,000 words or about 500
pages of text. Everything in your current conversation counts against this limit. When a
conversation grows very long, earlier content can fall outside the active window and Claude
loses access to it.

**Corpus** — the large body of text Claude was trained on: books, articles, code, web
content, up to its training cutoff date. Claude's knowledge comes from this corpus.

**Hallucination** — when Claude generates text that has the structure and confidence of an
accurate statement but is partially or entirely fabricated. Hallucinations happen because
Claude is optimizing for statistically plausible text, not verified facts. A fabricated
case study with plausible-sounding statistics is a hallucination. A citation to a real
journal with invented author names is a hallucination. Both appear with the same confident
tone as accurate output. Always verify specific claims before using them in external documents.

**Why prompt quality determines output quality**

Because Claude generates responses based on patterns learned from its corpus, the quality
of what it produces depends almost entirely on the quality and specificity of what you
provide. A vague prompt activates a broad range of patterns and produces a generic response.
A specific, structured prompt narrows the activation and produces a targeted response.
""",
        "quiz": [
            {
                "question": "What does Claude do when it generates a response?",
                "options": [
                    "Searches a connected database for the correct answer",
                    "Retrieves a pre-written response from its training corpus",
                    "Reads all input in the current conversation and predicts the next token based on learned patterns",
                    "Consults a live knowledge base and summarizes the results",
                ],
                "correct_index": 2,
                "hint": "Claude is a generative model — it produces text one token at a time from what you have given it.",
            },
            {
                "question": (
                    "You are working on a complex policy analysis and your conversation with Claude "
                    "has become very long. Claude starts giving responses that seem to ignore context "
                    "you established early in the conversation. What is the most likely cause?"
                ),
                "options": [
                    "Claude is confused by the complexity of the topic",
                    "The early conversation content has moved outside Claude's active context window",
                    "Claude's usage limit has been reached",
                    "The model needs to be switched to Opus",
                ],
                "correct_index": 1,
                "hint": "The 200K context window is large but finite — older content can fall outside it.",
            },
            {
                "question": "Why is it essential to verify specific statistics and citations that Claude produces?",
                "options": [
                    "Claude deliberately fabricates information to appear helpful",
                    "Claude generates statistically likely text and can produce plausible-sounding but inaccurate details — including citations to studies that do not exist — because it has no built-in verification step",
                    "Claude's training data is always outdated",
                    "Statistics are outside Claude's capability regardless of prompt quality",
                ],
                "correct_index": 1,
                "hint": "Claude is optimizing for plausible text, not verified facts — hallucinations look exactly like accurate output.",
            },
        ],
    },
    2: {
        "concept": """
NeuroFlow uses Claude Teams, a managed enterprise instance of Claude operated under
Anthropic's data policies for business customers. Understanding what can and cannot go
into Claude Teams matters more than knowing which AI products exist — because putting
the wrong information into the wrong tool creates legal and compliance risk.

**What you can put into Claude Teams**

Almost everything related to your work. Internal strategy documents, product specifications,
partner briefs, RFPs, policy drafts, competitive analysis, meeting notes, code, data models,
presentations, and email drafts are all appropriate. Claude Teams does not train Anthropic's
models on your conversations and operates under data agreements that protect NeuroFlow's
proprietary information.

**What you cannot put into Claude Teams**

**Protected Health Information (PHI).** PHI includes any information that could identify a
specific patient: names, dates of birth, medical record numbers, assessment scores linked
to an individual, diagnosis information, or any combination of data that would allow someone
to identify a specific patient. PHI belongs in HIPAA-compliant systems.

This is a hard line. It does not matter whether you are analyzing aggregate trends or doing
research — if the data includes individual-level patient identifiers, it does not go into
Claude Teams. Analyze that data in tools that operate under NeuroFlow's HIPAA agreements.

**The practical test**

Before entering information into Claude Teams, ask one question: does this contain anything
that could identify a specific patient? If yes, stop. If no, proceed.

**What about research?**

When a task requires accessing external research, use a web-enabled tool first to find
publicly available information, then bring your analysis into Claude Teams. Using Perplexity,
Google Scholar, or web search to find publicly available research, then using Claude Teams
to synthesize those findings, is the correct workflow.
""",
        "quiz": [
            {
                "question": (
                    "A NeuroFlow data analyst wants to benchmark BHIQ's performance against "
                    "published academic research. They have de-identified aggregate outcomes "
                    "data (no patient identifiers). Which approach is appropriate?"
                ),
                "options": [
                    "Entering NeuroFlow's proprietary outcome data into ChatGPT to compare against published research",
                    "Using Perplexity or web search to find publicly available research, then bringing those findings into Claude Teams for analysis",
                    "Only using Claude Teams for all research, never using other tools",
                    "Avoiding AI tools for research entirely since accuracy cannot be guaranteed",
                ],
                "correct_index": 1,
                "hint": "Think about where each type of information belongs — external research vs. internal proprietary data.",
            },
            {
                "question": "What is the single most important restriction on what can be entered into Claude Teams?",
                "options": [
                    "No information about competitors",
                    "No documents longer than a certain page count",
                    "No Protected Health Information of any kind",
                    "No information created after Claude's training cutoff",
                ],
                "correct_index": 2,
                "hint": "The restriction that creates legal and compliance risk, not just quality risk.",
            },
        ],
    },
    3: {
        "concept": """
The Claude Teams interface is where most daily work happens. Knowing how it is organized —
and understanding context management — prevents the most common frustrations staff encounter.

**Core interface areas**

**Conversations** — each conversation is a self-contained session. Claude has access to
everything in that conversation but nothing from past conversations unless you are inside
a Project. Long conversations can improve coherence within a session but consume your token
allocation faster.

**Projects** — a persistent workspace. You write custom instructions once, upload knowledge
files, and every conversation inside that Project uses that context automatically. Recurring
NeuroFlow workflows belong here.

**Memory** — Claude can store facts and preferences about you across conversations globally.
Unlike Project knowledge, memory applies everywhere. View, edit, and delete memories in
Settings → Memory.

**Tools panel** — controls web search, file analysis, code execution, and connected integrations.

**Artifacts** — when Claude produces a document or code file, it renders in a side panel
for separate editing and download.

**Model selector** — at the bottom of the chat input. One of the most consequential settings.

**Understanding models and usage limits**

**Haiku** — fastest and most efficient. Best for simple tasks: summarizing short documents,
answering specific questions, grammar and spelling checks. Uses the least allocation per exchange.

**Sonnet** — the default for most work. Handles document analysis, structured writing,
multi-step tasks, and instruction-following reliably. The majority of daily work should
happen here.

**Opus** — most capable for complex reasoning. Use for tasks requiring judgment across
competing considerations, analysis of lengthy complex documents, or nuanced policy and
clinical work where quality on the first attempt matters more than speed. Opus consumes
significantly more allocation than Sonnet.

Choosing the right model is about using your allocation wisely. Opus for a grammar check
wastes allocation. Haiku for a 40-page regulatory analysis produces a shallow result. Use
the lightest model that reliably handles the task.

**Managing context effectively**

Keep conversations focused on one topic. Start a new conversation when you shift tasks.
When a long conversation has done its job, extract the valuable output — decisions, documents,
instructions — and move those into a Claude Project. The conversation becomes the working
session; the Project becomes the persistent memory.
""",
        "quiz": [
            {
                "question": (
                    "You are mid-way through a long conversation analyzing a federal RFP when "
                    "Claude's responses start contradicting context you established early in the "
                    "conversation. The most practical corrective action is:"
                ),
                "options": [
                    "Switch to Opus — it has a larger context window",
                    "Start a new conversation and copy in only the most relevant context from the prior session",
                    "Repeat all your earlier context in a new message",
                    "Enable web search to help Claude find the information again",
                ],
                "correct_index": 1,
                "hint": "When early context is unreliable, a focused new session works better than more messages in the same one.",
            },
            {
                "question": "Where do you check your current usage against your allocation limit?",
                "options": [
                    "The model selector dropdown",
                    "The Tools panel",
                    "Settings → Usage",
                    "Project Settings",
                ],
                "correct_index": 2,
                "hint": "It is in the main Settings menu.",
            },
            {
                "question": (
                    "You need to check grammar and spelling in a short email before sending it. "
                    "Which model should you use, and why?"
                ),
                "options": [
                    "Opus — it is the most capable and will catch every error",
                    "Sonnet — it is the default and always the safest choice",
                    "Haiku — the task is simple and requires no deep reasoning, so using a lighter model preserves your allocation for work that actually needs it",
                    "It does not matter — all models perform identically on simple tasks",
                ],
                "correct_index": 2,
                "hint": "Match model capability to task complexity — spending more allocation than needed reduces what is available for harder work.",
            },
            {
                "question": (
                    "You have been working with Claude in a long conversation to develop a method "
                    "for evaluating Jira tickets. The approach is working well. You want to "
                    "evaluate future tickets the same way without starting from scratch each time. "
                    "What is the best next step?"
                ),
                "options": [
                    "Keep using the same conversation — Claude will remember as long as you do not close it",
                    "Copy and paste your best prompt to the top of every new conversation",
                    "Use the current conversation to build Claude Project instructions, then evaluate future tickets inside that Project",
                    "Switch to Opus, which retains memory across conversations automatically",
                ],
                "correct_index": 2,
                "hint": "Projects persist your context reliably — a long conversation does not.",
            },
        ],
    },
    4: {
        "concept": """
Claude produces statistically likely text. This means it can generate outputs that are
fluent, confident, and wrong. Understanding where it fails — and what NeuroFlow policy
requires — protects you and the organization.

**What hallucinations look like in practice**

Hallucinations are not random errors. They are fluent, plausible text that fits the pattern
of what a correct answer would look like. Common failure patterns at NeuroFlow:

A fabricated study in the correct journal, by a plausible author, with a specific and
believable finding. You cannot distinguish it from a real study without checking.

A specific statistic — "34% reduction in readmission rates" — attached to a program that
has never been evaluated. The number sounds reasonable, which is why it passed review.

A policy brief that attributes a position to an agency using real agency language, on a
topic the agency has never formally addressed.

All three appear with the same confident tone as accurate output.

**Grounding reduces hallucination risk**

The most effective mitigation is grounding — giving Claude the source material and
instructing it to stay within it:

"Use only the information in the attached reports. Do not add claims, statistics, or
examples that are not present in these documents."

This substantially reduces the risk for the most consequential category: specific facts
in externally-facing documents.

**The key habit: ask where it came from**

When Claude produces something specific that you did not provide — a precise statistic,
a named study, a dollar figure — ask for the source before using it. If Claude cannot
produce a verifiable citation, the claim should be removed or replaced.

**NeuroFlow policy**

Before using Claude-generated content in any external document, verify all specific factual
claims. The person submitting the document is responsible for its accuracy regardless of
how it was produced.
""",
        "quiz": [
            {
                "question": (
                    "A policy analyst is drafting a federal brief using three internal NeuroFlow "
                    "reports they attached to the conversation. They want to make sure Claude "
                    "does not add claims from outside those documents. Which prompt instruction "
                    "best achieves this?"
                ),
                "options": [
                    "Please be careful not to include anything inaccurate.",
                    "Use only the information in the attached reports. Do not add claims, statistics, or examples that are not present in these documents.",
                    "Double-check your work before responding.",
                    "Only include information you are confident about.",
                ],
                "correct_index": 1,
                "hint": "You need an explicit boundary — vague accuracy instructions do not constrain source material.",
            },
        ],
        "challenge": {
            "scenario": (
                "You are reviewing a Claude-generated partner brief draft. It contains this paragraph:\n\n"
                "> *\"According to a 2023 study published in JAMA Psychiatry by researchers at "
                "Johns Hopkins, a behavioral health measurement platform reduced 30-day readmission "
                "rates by 34% across 47 health systems, generating an average ROI of \\$4.2M per "
                "system annually.\"*\n\n"
                "You did not provide this study to Claude. Write the follow-up prompt you would "
                "send to Claude to verify whether this claim is real before using it in the brief."
            ),
            "broken_example": "",
            "rubric": (
                "Score the learner's follow-up prompt on whether it requests traceable source "
                "detail sufficient for independent external verification.\n\n"
                "Pass (score ≥ 70): The prompt asks for the study name, a direct link, a DOI, "
                "author names, journal volume/issue number, or any combination that would allow "
                "the learner to look it up outside of Claude.\n\n"
                "Fail (score < 70): The prompt only asks Claude to 'verify', 'confirm', "
                "'double-check', or 'make sure it is accurate' without requesting traceable "
                "details that exist outside the Claude conversation.\n\n"
                "Award partial credit if the prompt asks for some but not all needed verification details."
            ),
            "model_answer": (
                "Can you provide the full citation for the JAMA Psychiatry study — "
                "including the author names, publication year, volume and issue numbers, "
                "and a DOI or direct link — so I can verify it independently before "
                "including it in the brief?"
            ),
            "hints": [
                "Do you know the name of the study referenced in that paragraph?",
                "Do you know which issue of JAMA Psychiatry this appeared in, or the DOI number?",
                "Ask Claude to provide the full citation with a link or DOI so you can look it up yourself before using it.",
            ],
        },
    },
    5: {
        "concept": """
Claude is one tool in a larger ecosystem. Understanding which surface to use for which
job — and when to layer in other capabilities — determines how much value staff actually
extract from the platform.

**The three primary Claude surfaces**

**Claude chat** is for thinking and drafting. Use it when the task is cognitive: analyzing
a document, drafting a brief, developing a strategy, working through a problem. Chat is
interactive — you exchange messages, refine, and iterate. Nothing runs autonomously.

**Cowork** is for acting. Use it when the task involves operating on local files autonomously
— renaming a folder of documents, converting files, synthesizing a report from scattered
local notes, running a scheduled weekly digest. Cowork reads and writes files on your machine.
You define the task; it executes without requiring you to stay in the loop for each step.

**Claude Code** is for building. Use it when the task involves writing, running, or modifying
code. Claude Code has direct access to your project's file system, reads and edits source
files, runs tests, and proposes code changes as diffs you review and approve.

**Extended capabilities within Claude chat**

**Deep Research** — Claude browses multiple web sources and compiles a structured research
report. Use when you need a landscape assessment, policy survey, or competitive overview.
Deep Research is the most token-intensive option.

**Connectors** — link Claude to the tools your team already uses. With the HubSpot connector
active, Claude can pull deal notes directly from your CRM. Connectors stay active in a
conversation until you disable them.

**Plugins** — extend what Claude can do within a session with domain-specific defaults.
The Data plugin enables executing queries and rendering charts. The Legal plugin adds
document review reasoning for regulatory work. The Sales plugin adds pipeline reasoning
and outreach generation patterns.

**The cost principle**

Every capability layer adds to your usage allocation. A focused prompt alone is lightest.
Connectors add retrieval overhead. Plugins add domain tooling. Deep Research is the most
intensive. For staff who hit usage limits frequently, simplifying the tool stack is the
first step.
""",
        "quiz": [
            {
                "question": (
                    "What is the correct mental model for choosing between Claude chat, "
                    "Cowork, and Claude Code?"
                ),
                "options": [
                    "They are interchangeable — use whichever is most familiar",
                    "Chat is for thinking and drafting, Cowork is for acting on local files autonomously, Claude Code is for writing and modifying code",
                    "Claude Code is always the most powerful option and should be used whenever possible",
                    "Cowork replaces Claude chat for all tasks once you have the desktop app installed",
                ],
                "correct_index": 1,
                "hint": "Each surface is designed for a different job: cognitive work, autonomous file operations, and code.",
            },
            {
                "question": (
                    "A NeuroFlow policy analyst needs to compile a landscape assessment of "
                    "state Medicaid behavioral health technology programs — covering which "
                    "states are active, what programs exist, and recent policy trends. "
                    "Which Claude feature is most appropriate?"
                ),
                "options": [
                    "A standard conversation with Haiku",
                    "A Claude Project with relevant policy documents uploaded",
                    "Deep Research mode, which browses multiple sources and compiles structured findings",
                    "Cowork pointed at a local folder of downloaded policy documents",
                ],
                "correct_index": 2,
                "hint": "This requires synthesizing information from many external sources — which capability is designed for that?",
            },
            {
                "question": (
                    "Your team uses HubSpot for deal tracking. You want Claude to reference your "
                    "most recent deal notes from HubSpot during a conversation, without copying "
                    "and pasting them manually. What do you need?"
                ),
                "options": [
                    "Upload a HubSpot export to a Project knowledge file before each conversation",
                    "The HubSpot connector active so Claude can retrieve deal notes directly during the conversation",
                    "Switch to Opus, which has access to more external data sources",
                    "A Cowork task that downloads HubSpot notes to a local folder first",
                ],
                "correct_index": 1,
                "hint": "The feature that creates a live bridge between Claude and external services during a conversation.",
            },
        ],
    },
}


def render_lesson(lesson_id: int) -> bool:
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        st.error(f"Lesson 2.{lesson_id} not found.")
        return False

    already_done = is_lesson_complete(TRACK_ID, lesson_id)

    st.markdown(lesson["concept"])
    st.markdown("---")

    if already_done:
        st.success("✓  Lesson complete")
        return True

    # Lessons with quiz only (no challenge)
    if lesson.get("quiz") and not lesson.get("challenge"):
        return render_quiz(
            track_id=TRACK_ID,
            lesson_id=lesson_id,
            questions=lesson["quiz"],
            label="Knowledge check",
        )

    # Lesson 2.4 — quiz followed by graded challenge
    if lesson.get("quiz") and lesson.get("challenge"):
        quiz_passed = render_quiz(
            track_id=TRACK_ID,
            lesson_id=lesson_id,
            questions=lesson["quiz"],
            label="Knowledge check",
        )

        if not quiz_passed:
            return False

        ch = lesson["challenge"]
        return render_graded_challenge(
            track_id=TRACK_ID,
            lesson_id=lesson_id,
            scenario=ch["scenario"],
            broken_example=ch["broken_example"],
            rubric=ch["rubric"],
            model_answer=ch["model_answer"],
            hints=ch["hints"],
            input_label="Your verification prompt",
            max_chars=400,
        )

    st.info("Content coming soon.", icon="🔜")
    return False
