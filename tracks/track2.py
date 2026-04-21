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
input explains why some prompts work and others do not, and why verifying outputs is
always necessary.

**How Claude generates a response**

Claude does not search a database or retrieve a stored answer. It reads your entire input,
every word in the conversation up to that point, and generates a response one token at a
time, predicting the most statistically likely next token given everything it has processed.

Four terms appear throughout this program.

**Token:** the unit Claude processes. Roughly equivalent to a word or word fragment.
"Hello" is one token. "Measurement-based" is likely two. You are billed for tokens
consumed, which is why heavier models cost more of your usage allocation per conversation.

**Context window:** the total amount of text Claude can hold in its working memory at
once. Claude's context window is 200,000 tokens, roughly 150,000 words or about 500 pages
of text. Everything in your current conversation counts against this limit. When a
conversation grows very long, earlier content can fall outside the active window and Claude
loses access to it.

**Corpus:** the large body of text Claude was trained on, including books, articles, code,
and web content up to its training cutoff date. Claude's knowledge comes from this corpus.

**Hallucination:** when Claude generates text that has the structure and confidence of an
accurate statement but is partially or entirely fabricated. Hallucinations happen because
Claude is optimizing for statistically plausible text, not verified facts. A fabricated
case study with plausible-sounding statistics is a hallucination. A citation to a real
journal with invented author names is a hallucination. Both appear with the same confident
tone as accurate output. Always verify specific claims before using them in external documents.

**How Claude 4 changed: literal instruction following**

Claude 4 models behave differently from earlier versions in one way that affects every task
you give them. Earlier Claude models would infer your intent and fill in gaps. If you asked
for a dashboard, Claude would assume you wanted charts, filters, and data tables. If you
asked for a summary, it would apply its judgment about what a useful summary looks like for
your context.

Claude 4 takes you literally. If you ask for a dashboard without specifying its components,
you may get a blank frame with a title. If you ask for a summary without specifying length
or format, you get whatever Claude judges as technically consistent with the word "summary."
The output is not wrong by the model's interpretation. It did exactly what you asked,
nothing more.

Anthropic describes this directly: customers who want Claude to go "above and beyond" now
need to request that behavior explicitly.

In practice, this means three things.

Gaps in your prompt produce gaps in the output. Claude 3 would often cover for an
underspecified prompt by doing the reasonable thing. Claude 4 will not. If you want three
bullets, ask for three bullets. If you want the output to lead with cost implications, say
so. If you want Claude to flag what it is uncertain about, you have to include that
instruction.

Your first response is more diagnostic than it used to be. A narrow or incomplete output
on Claude 4 is almost always telling you what the prompt was missing, not that Claude
misunderstood you. The diagnostic step before writing a follow-up is now more important,
not less.

The fix is always more specificity, not more effort. Restating the prompt more forcefully
or adding phrases like "be thorough" does not change the output. Claude 4 responds to
precise instructions, not emphasis. "Write a 400-word value proposition for a health system
CFO that leads with total cost of care reduction and closes with a single call to action"
will outperform "write a really thorough and complete value proposition" every time.

This shift is also why the RTCFC framework in Track 3 works the way it does. Each component
closes a gap Claude will no longer fill on its own. Role, Task, Context, Format, and
Constraints are not optional scaffolding. They are the specification the model now requires
to produce the output you actually want.

**Why prompt quality determines output quality**

Because Claude generates responses based on patterns learned from its corpus, the quality
of what it produces depends almost entirely on the quality and specificity of what you
provide. A vague prompt activates a broad range of patterns and produces a generic response.
A specific, structured prompt narrows the activation and produces a targeted response.

**Context and conversation length affect output quality**

Claude's context window holds 200,000 tokens, roughly 500 pages of text. Everything in
the current conversation counts against that limit: your messages, Claude's responses, and
any uploaded files. Claude can technically hold all of it at once, but performance does not
stay flat as context grows.

Research on LLM attention shows that relevant content buried in the middle of a long
conversation receives less model attention than content at the start or end. A 2024 Stanford
study found accuracy dropped over 30% when key information was positioned in the middle of
long inputs. This means a constraint or requirement you stated early in a conversation can
quietly carry less weight in later responses, even though it is still within the window.

A conversation is getting too long when you notice Claude ignoring earlier instructions,
producing outputs that contradict context you already provided, or when you find yourself
scrolling back to re-paste something you already shared. Those are reliable signals to close
the conversation and start fresh.

Before you do, ask Claude to draft the opening prompt for the next conversation. This is not
a summary of what happened. It is a ready-to-use prompt you paste directly into a new chat
or Project to resume exactly where you left off:

*"Read back through our full conversation from the beginning. Then write an opening prompt
I can paste into a new conversation to continue this work without losing context. Write it
as instructions for Claude, covering the goal we are working toward, the decisions and
constraints already established, relevant background, and the specific task to pick up next."*

If the work is ongoing rather than a single session, that handoff pattern becomes inefficient
quickly. Sustained work on the same topic belongs in a Project, where context persists
automatically across every conversation. Track 4 covers Projects in detail.
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
                "hint": "Claude is a generative model. It produces text one token at a time from what you have given it.",
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
                "hint": "The 200K context window is large but finite; older content can fall outside it.",
            },
            {
                "question": "Why is it essential to verify specific statistics and citations that Claude produces?",
                "options": [
                    "Claude deliberately fabricates information to appear helpful",
                    "Claude generates statistically likely text and can produce plausible-sounding but inaccurate details (including citations to studies that do not exist) because it has no built-in verification step",
                    "Claude's training data is always outdated",
                    "Statistics are outside Claude's capability regardless of prompt quality",
                ],
                "correct_index": 1,
                "hint": "Claude is optimizing for plausible text, not verified facts. Hallucinations look exactly like accurate output.",
            },
        ],
    },
    2: {
        "concept": """
NeuroFlow uses Claude Teams, a managed enterprise instance of Claude operated under
Anthropic's data policies for business customers. Understanding what can and cannot go
into Claude Teams matters more than knowing which AI products exist, because putting
the wrong information into the wrong tool creates legal and compliance risk.

**What you can put into Claude Teams**

Almost everything related to your daily work. Internal strategy documents, product
specifications, partner briefs, RFPs, policy drafts, competitive analysis, meeting notes,
code, data models, presentations, customer agreements, and email drafts are all appropriate.
Claude Teams does not train Anthropic's models on your conversations and operates under
data agreements that protect NeuroFlow's proprietary information.

**What you cannot put into Claude Teams**

**Protected Health Information (PHI).** PHI includes any information that could identify a
specific patient: names, dates of birth, medical record numbers, assessment scores linked
to an individual, diagnosis information, or any combination of data that would allow someone
to identify a specific patient. PHI belongs in HIPAA-compliant systems only.

This is a hard line. It applies regardless of your role or the purpose of your work. A
clinical team member analyzing patient outcomes, a data analyst running population reports,
and a researcher reviewing study findings all face the same rule: if the data includes
individual-level patient identifiers, it does not go into Claude Teams. Analyze that data
in tools that operate under NeuroFlow's HIPAA agreements.

**What about de-identified or aggregate data?**

De-identified data and aggregate population data that contain no individual patient
identifiers are not PHI. Summary statistics, population-level trends, anonymized cohort
findings, and published research results do not identify specific patients and are
appropriate to bring into Claude Teams for analysis, drafting, or synthesis.

If you are ever uncertain whether a dataset or document crosses the PHI line, apply the
practical test below before proceeding.

**The practical test**

Before entering any information into Claude Teams, ask one question: could this data or
document identify a specific patient? If yes, stop. If no, proceed.

When in doubt, leave it out and consult your manager or NeuroFlow's compliance team.

**Your responsibility**

Every work product you create using Claude is yours to review and confirm before it leaves
your hands. Claude can produce incorrect, outdated, or incomplete information, and it will
do so with the same confident tone as accurate output. Catching that before it reaches a
partner, regulator, or patient is part of your professional responsibility. Using AI
assistance does not transfer ownership of the output or reduce your obligation to verify
what you submit.

This is not a limitation unique to Claude. It is the standard that applies to any tool
that assists your work. The expectation is the same whether you used Claude, a junior
colleague, or your own first draft.

**Finding information with Claude Teams**

Claude Teams includes built-in web search, which handles most information gathering tasks
directly. Ask Claude to search the web for publicly available information and it will
retrieve, summarize, and synthesize findings in the same conversation.

For tasks that require more targeted searching (specific academic databases, regulatory
archives, or known sources), tools like Perplexity, Google Scholar, or direct web search
can complement Claude. The typical workflow is to search externally when you need precision
on a specific source, then bring those findings into Claude Teams for analysis, drafting,
or synthesis.

External tools are appropriate for this kind of targeted searching as long as two conditions
are met. First, the tool is not on NeuroFlow's prohibited tools list. Second, only publicly
available information goes into those tools. Internal strategy, proprietary product details,
partner information, financial data, and anything else that is not already public should
never be entered into an external tool that does not operate under NeuroFlow's data
agreements.

For multi-source landscape work that would otherwise take hours of manual gathering,
Research mode in Claude Teams automates that process. Track 4 covers Research mode, web
search, and Adaptive Thinking in detail, including when to use each and how they differ.

The PHI rule applies equally to all of these workflows. No patient-identifiable information
enters Claude Teams regardless of how the information was originally gathered or what form
it takes when you bring it in.
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
                "hint": "Think about where each type of information belongs: external research vs. internal proprietary data.",
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
            {
                "question": "Who is responsible for a work product created with Claude's help?",
                "options": [
                    "I am. Claude assists, but I own and am accountable for everything I submit",
                    "Claude is. It generated the content",
                ],
                "correct_index": 0,
                "hint": "Claude is a tool. The person who submits the work is responsible for it.",
            },
            {
                "question": (
                    "A NeuroFlow researcher has a dataset showing BHIQ completion rates by age "
                    "group with no names, dates of birth, or any other patient identifiers. "
                    "Is this appropriate to bring into Claude Teams?"
                ),
                "options": [
                    "No: any data derived from patient records is PHI regardless of whether identifiers have been removed",
                    "Yes: de-identified aggregate data with no individual patient identifiers is not PHI and is appropriate for Claude Teams",
                    "Only if the researcher's manager approves it first",
                    "Only if fewer than 500 patients are represented in the dataset",
                ],
                "correct_index": 1,
                "hint": "The PHI definition centers on whether specific individuals can be identified, not on whether the data was originally derived from patient records.",
            },
        ],
    },
    3: {
        "concept": """
The Claude Teams interface is where most daily work happens. Knowing how it is organized,
how documents and attachments behave, and how to manage context prevents the most common
frustrations staff encounter.

**Core interface areas**

**Conversations:** each conversation is a self-contained session. Claude has access to
everything in that conversation but nothing from past conversations unless you are inside
a Project. Long conversations can improve coherence within a session but consume your
token allocation faster.

**Projects:** a persistent workspace. You write custom instructions once, upload
knowledge files, and every conversation inside that Project uses that context
automatically. Recurring NeuroFlow workflows belong here.

**Memory:** Claude can store facts and preferences about you across conversations
globally. Unlike Project knowledge, memory applies everywhere. View, edit, and delete
memories in Settings and then Memory.

**Tools panel:** controls web search, file analysis, code execution, and connected
integrations.

**Artifacts:** when Claude produces a document or code file, it renders in a side panel
for separate editing and download.

**Model selector:** at the bottom of the chat input. One of the most consequential
settings.

[[MODEL_COMPARISON_DIAGRAM]]

**Understanding models and usage limits**

**Haiku:** fastest and most efficient. Best for simple tasks such as summarizing short
documents, answering specific questions, and grammar and spelling checks. Uses the least
allocation per exchange.

**Sonnet:** the default for most work. Handles document analysis, structured writing,
multi-step tasks, and instruction-following reliably. The majority of daily work should
happen here.

**Opus:** most capable for complex reasoning. Use for tasks requiring judgment across
competing considerations, analysis of lengthy complex documents, or nuanced policy and
clinical work where quality on the first attempt matters more than speed. Opus consumes
significantly more allocation than Sonnet.

Choosing the right model is about using your allocation wisely. Opus for a grammar check
wastes allocation. Haiku for a 40-page regulatory analysis produces a shallow result. Use
the lightest model that reliably handles the task.

**Working with attachments and document cards**

One of the most frequently used features in Claude Teams is the ability to bring documents
into a conversation. Understanding how Claude receives and displays that content determines
how you refer to it in your instructions.

When you upload a file using the attachment button, or paste a long block of text into the
chat input, Claude automatically converts it into a document card. That card sits above
the text input field, visually separated from your typed instructions. Uploaded files show
the filename on the card. Pasted content shows a "PASTED" label with a preview of the
first few lines of text.

This behavior matters because everything you write goes below the cards. Claude reads the
cards and your typed instructions together as one complete message, but it already treats
them as separate pieces of content because the interface created that boundary automatically.

**Referring to a single card**

When you have one card, reference it simply and naturally in your typed instructions:

```
Using the document above, write a two-paragraph value 
proposition for a health system CFO that leads with 
total cost of care reduction.
```

Claude knows "the document above" refers to the card. It is unambiguous because there is
only one.

<img src="data:image/png;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/4gHYSUNDX1BST0ZJTEUAAQEAAAHIAAAAAAQwAABtbnRyUkdCIFhZWiAH4AABAAEAAAAAAABhY3NwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAA9tYAAQAAAADTLQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAlkZXNjAAAA8AAAACRyWFlaAAABFAAAABRnWFlaAAABKAAAABRiWFlaAAABPAAAABR3dHB0AAABUAAAABRyVFJDAAABZAAAAChnVFJDAAABZAAAAChiVFJDAAABZAAAAChjcHJ0AAABjAAAADxtbHVjAAAAAAAAAAEAAAAMZW5VUwAAAAgAAAAcAHMAUgBHAEJYWVogAAAAAAAAb6IAADj1AAADkFhZWiAAAAAAAABimQAAt4UAABjaWFlaIAAAAAAAACSgAAAPhAAAts9YWVogAAAAAAAA9tYAAQAAAADTLXBhcmEAAAAAAAQAAAACZmYAAPKnAAANWQAAE9AAAApbAAAAAAAAAABtbHVjAAAAAAAAAAEAAAAMZW5VUwAAACAAAAAcAEcAbwBvAGcAbABlACAASQBuAGMALgAgADIAMAAxADb/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh7/wAARCAMUBhIDASIAAhEBAxEB/8QAHQABAAEFAQEBAAAAAAAAAAAAAAQCAwUGBwgBCf/EAGMQAAEDAwEEBQUIDAsFBAgFBQABAgMEBREGBxIhMQgTFEFRImFzktEVMlNUcYGishY0NTdSdZGUobGz0hcjMzY4QlVWcoLTGGJ0k8G0wsTwJCVDV2Ojw+FIg4WGpURGZHaE/8QAGwEBAQEAAwEBAAAAAAAAAAAAAAECAwUGBAf/xAAzEQEAAgEBBAcGBQUAAAAAAAAAARECAwQFEjEhQVJhcZGhBhMyM1HRFRY0gbEiJMHh8P/aAAwDAQACEQMRAD8A8yAAyAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAGF8BhfAABhfAYXwAAYXwGF8AAAAAAAAAAAAAAAAAAAAAAAAVRRvlkRjEy5QPjUVyo1qKqryRCZFRInGd+6v4DeK/OvcX4o2U6YjXL/AOs/x+TzH0D4xkLP5OFiedyby/pLiSyJwR6p8nAoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfXS/Cv9ZR10vwr/WUoAFfX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F9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kTAwBL7e74vF9L2jt7vi8X0vaRMDAEvt7vi8X0vaO3u+LxfS9pEwMAS+3u+LxfS9o7e74vF9L2kUASu3v7oIk/L7Sl1bULycjP8DUT9PMjgA5Vcqq5VVV5qoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//9k=" alt="Claude Teams interface showing a pasted card and an uploaded PDF card with a typed instruction below" style="max-width:100%;border-radius:8px;display:block;margin:16px 0;" />

**Referring to multiple cards**

When you have more than one card, you need to distinguish between them clearly so Claude
knows which one to use for which purpose. The approach differs depending on whether the
content was uploaded or pasted.

For uploaded files, reference by the filename as it appears on the card:

```
Using BHIQ_Positioning.pdf as the primary source and 
NeuroFlow_CaseStudy.pdf as supporting evidence, write a 
two-paragraph value proposition for a health system CFO.
```

For pasted cards, there is no filename to reference. Instead, refer to each card
descriptively based on what the content is about. Claude has already read every card
before it reads your instructions, so a descriptive reference like "the pasted information
about NeuroFlow's federal pipeline" or "the pasted Q1 partner summary" gives Claude enough
to match your reference to the right card.

```
Using the pasted NeuroFlow positioning information as the 
primary source and the pasted case study summary as supporting 
evidence, write a two-paragraph value proposition for a 
health system CFO.
```

This is the same way you would direct a colleague: "look at the NeuroFlow notes I sent
you" rather than "look at document two." Claude responds to descriptive references the
same way because it read the content and can match your description to it.

**The habit worth building: title your pasted content**

Descriptive references work best when the pasted content has a clear subject. If your
pasted card opens with a strong title like "NeuroFlow BHIQ Positioning Q1 2026," your
reference in the instructions can be tight and precise. If it opens with a generic
sentence, your descriptive reference has to work harder and introduces room for ambiguity.

Before pasting content you intend to reference by name, make sure the first line is a
clear descriptive title. Think of it the same way you would name a file before uploading
it. That first line becomes the identity of the card in your instructions.

**What counts as a card versus inline text**

Not all pasted content becomes a card. Short text pasted directly into the text field
stays inline as part of your typed message. Claude receives it as regular text with no
automatic boundary between that content and your instructions.

When pasted content stays inline, you are responsible for creating the boundary between
the source material and your instructions. Track 3 covers how to do that using XML tags,
and it builds directly on what you have learned here about cards and descriptive
referencing.

**Managing context effectively**

Keep conversations focused on one topic. Start a new conversation when you shift tasks.
When a long conversation has done its job, extract the valuable output including
decisions, documents, and instructions, and move those into a Claude Project. The
conversation becomes the working session. The Project becomes the persistent memory.
""",
        "quiz": [
            {
                "question": (
                    "You are mid-way through a long conversation analyzing a federal RFP when "
                    "Claude's responses start contradicting context you established early in the "
                    "conversation. The most practical corrective action is:"
                ),
                "options": [
                    "Switch to Opus, since it has a larger context window",
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
                    "Opus: it is the most capable and will catch every error",
                    "Sonnet: it is the default and always the safest choice",
                    "Haiku: the task is simple and requires no deep reasoning, so using a lighter model preserves your allocation for work that actually needs it",
                    "It does not matter: all models perform identically on simple tasks",
                ],
                "correct_index": 2,
                "hint": "Match model capability to task complexity; spending more allocation than needed reduces what is available for harder work.",
            },
            {
                "question": (
                    "You have been working with Claude in a long conversation to develop a method "
                    "for evaluating Jira tickets. The approach is working well. You want to "
                    "evaluate future tickets the same way without starting from scratch each time. "
                    "What is the best next step?"
                ),
                "options": [
                    "Keep using the same conversation, since Claude will remember as long as you do not close it",
                    "Copy and paste your best prompt to the top of every new conversation",
                    "Use the current conversation to build Claude Project instructions, then evaluate future tickets inside that Project",
                    "Switch to Opus, which retains memory across conversations automatically",
                ],
                "correct_index": 2,
                "hint": "Projects persist your context reliably; a long conversation does not.",
            },
        ],
    },
    4: {
        "concept": """
Because Claude generates responses by predicting statistically likely text rather than retrieving verified facts, fluent and confident output can still be wrong. Knowing what to do about that is the most important habit to build before using Claude for work that leaves NeuroFlow.

Claude produces statistically likely text. This means it can generate outputs that are
fluent, confident, and wrong. Understanding where it fails, and what NeuroFlow policy
requires, protects you and the organization.

**What hallucinations look like in practice**

Hallucinations are not random errors. They are fluent, plausible text that fits the pattern
of what a correct answer would look like. Common failure patterns at NeuroFlow:

A fabricated study in the correct journal, by a plausible author, with a specific and
believable finding. You cannot distinguish it from a real study without checking.

A specific statistic like "34% reduction in readmission rates" attached to a program that
has never been evaluated. The number sounds reasonable, which is why it passed review.

A policy brief that attributes a position to an agency using real agency language, on a
topic the agency has never formally addressed.

All three appear with the same confident tone as accurate output.

**A note on math**

The same risk applies to calculations. Claude can perform arithmetic incorrectly and present the result with the same confidence as a correct answer. If Claude produces a number derived from inputs you provided (a percentage, a cost projection, a year-over-year change) verify it independently before it goes into a document. A spreadsheet check takes thirty seconds and catches errors that would otherwise reach a partner or regulator.

**Grounding reduces hallucination risk**

The most effective mitigation is grounding: giving Claude the source material and
instructing it to stay within it:

"Use only the information in the attached reports. Do not add claims, statistics, or
examples that are not present in these documents."

This substantially reduces the risk for the most consequential category: specific facts
in externally-facing documents.

**The key habit: ask where it came from**

When Claude produces something specific that you did not provide, such as a precise statistic,
a named study, or a dollar figure, ask for the source before using it. If Claude cannot
produce a verifiable citation, the claim should be removed or replaced.

**NeuroFlow policy**

Before using Claude-generated content in any external document, verify all specific factual
claims. The person submitting the document is responsible for its accuracy regardless of
how it was produced.

**The first response is a starting point**

Most new Claude users treat a weak first response as a failure. It is not. It is
information. Claude responded to exactly what you asked, and if the output missed the
mark, the output is telling you what the prompt was missing.

The working pattern for any real task looks like this: send a prompt, read the response
critically, identify the specific gap, and write a targeted follow-up that addresses only
that gap. Repeat until the output meets the standard. Claude's outputs tend to improve
significantly with iteration. While the first version might be good, after two or three
iterations it will typically look much better.

The diagnostic step is what most people skip. Before writing a follow-up, read the output
and name the problem precisely. The follow-up should then target that problem alone, not
restate the entire original prompt.

A NeuroFlow example: you ask Claude to draft a value proposition paragraph for a health
system CFO audience and the output is too clinical and reads like a product spec. The
diagnosis is wrong audience register, not a bad paragraph. The follow-up is one sentence:

*"Rewrite this for a CFO audience. Lead with cost and risk, not clinical features. No
technical terminology."*

That is faster and more effective than re-sending the full original prompt with additional
instructions appended.

This pattern applies to every task. Deep Research outputs that need tighter scope, policy
briefs that need a different tone, outreach emails that need a harder call to action. The
skill is reading the output as a signal rather than a result.

If a prompt produces weak outputs repeatedly and targeted follow-ups are not fixing it,
the cause is either the prompt or the conversation. Try opening a fresh chat and running
the same prompt from scratch. If the output improves, the conversation accumulated context
that was interfering. If the output is still weak, the prompt itself is structurally
broken.
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
                    "Please be careful not to include anything inaccurate. I need this to be factually correct.",
                    "Use only the information in the attached reports. Do not add claims, statistics, or examples that are not present in these documents.",
                    "Double-check your work before responding and make sure everything is accurate and well-supported.",
                    "Only include information you are confident about.",
                ],
                "correct_index": 1,
                "hint": "You need an explicit boundary; vague accuracy instructions do not constrain source material.",
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
                "Full marks (score 100): The prompt asks for a full citation, a DOI, a direct "
                "link, or enough specific identifiers that the study can be located and verified "
                "independently. Asking for 'the full citation' earns full marks, since a complete "
                "citation contains all required identifying elements by convention.\n\n"
                "Pass (score 70–99): The prompt asks for some but not all traceable details, "
                "for example, author names but no DOI, or a link but no other identifiers.\n\n"
                "Fail (score < 70): The prompt only asks Claude to 'verify', 'confirm', "
                "'double-check', or 'make sure it is accurate' without requesting traceable "
                "details that exist outside the Claude conversation.\n\n"
                "Award partial credit if the prompt asks for some but not all needed verification details."
            ),
            "model_answer": (
                "Can you provide the full citation for the JAMA Psychiatry study, "
                "including a DOI or direct link, so I can verify it independently "
                "before including it in the brief?"
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
job, and when to layer in other capabilities, determines how much value staff actually
extract from the platform.

**The three primary Claude surfaces**

**Claude chat** is for thinking and drafting. Use it when the task is cognitive: analyzing
a document, drafting a brief, developing a strategy, working through a problem. Chat is
interactive. You exchange messages, refine, and iterate. Nothing runs autonomously.

**Cowork** is for acting. Use it when the task involves operating on local files autonomously,
such as renaming a folder of documents, converting files, synthesizing a report from scattered
local notes, or running a scheduled weekly digest. Cowork reads and writes files on your machine.
You define the task; it executes without requiring you to stay in the loop for each step.
Track 6 covers Cowork in depth.

**Claude Code** is for building. Use it when the task involves writing, running, or modifying
code. Claude Code has direct access to your project's file system, reads and edits source
files, runs tests, and proposes code changes as diffs you review and approve.
Track 7 covers Claude Code and is intended for engineering staff.

**Extended capabilities within Claude chat**

**Deep Research:** Claude browses multiple web sources and compiles a structured research
report. Use when you need a landscape assessment, policy survey, or competitive overview.
Deep Research is the most token-intensive option.

**Connectors:** link Claude to the tools your team already uses. With the HubSpot connector
active, Claude can pull deal notes directly from your CRM. Connectors stay active in a
conversation until you disable them.

**Plugins:** extend what Claude can do within a session with domain-specific defaults.
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
                    "They are interchangeable; use whichever is most familiar",
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
                    "state Medicaid behavioral health technology programs, covering which "
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
                "hint": "This requires synthesizing information from many external sources. Which capability is designed for that?",
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

    # Handle diagram sentinels and embedded img tags in concept
    concept = lesson["concept"]

    def render_concept_part(text):
        import re
        img_pattern = re.compile(r'(<img [^>]+>)', re.DOTALL)
        segments = img_pattern.split(text)
        for seg in segments:
            if not seg.strip():
                continue
            if seg.startswith("<img "):
                st.markdown(seg, unsafe_allow_html=True)
            else:
                st.markdown(seg)

    if "[[MODEL_COMPARISON_DIAGRAM]]" in concept:
        import streamlit.components.v1 as components
        from components.diagrams import get_diagram, get_diagram_height
        parts = concept.split("[[MODEL_COMPARISON_DIAGRAM]]")
        for i, part in enumerate(parts):
            if part.strip():
                render_concept_part(part)
            if i < len(parts) - 1:
                html = get_diagram("model_comparison")
                height = get_diagram_height("model_comparison")
                if html:
                    components.html(html, height=height, scrolling=False)
    else:
        render_concept_part(concept)
    st.markdown("---")

    if already_done:
        if not lesson.get("challenge"):
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

    # Lesson 2.4: quiz followed by graded challenge
    if lesson.get("quiz") and lesson.get("challenge"):
        quiz_passed = render_quiz(
            track_id=TRACK_ID,
            lesson_id=lesson_id,
            questions=lesson["quiz"],
            label="Knowledge check",
            mark_complete=False,
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
