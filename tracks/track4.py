# tracks/track4.py — Track 4: Claude.ai Skills and Projects, 7 lessons

import streamlit as st
from utils.quiz import render_quiz
from utils.challenge import render_graded_challenge
from utils.session import is_lesson_complete, complete_lesson
from utils.grading import grade_challenge, call_sandbox

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
built in January that no one updates by April is working from stale context. Review Project instructions regularly and archive old projects to prevent confusion.

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
                "correct_index": 1,
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
                "You have been working with Claude on a conversation drafting value proposition "
                "emails for health system and payer audiences. You want to turn this into a "
                "Project the whole BD team can use.\n\n"
                "**Task:** Write a single sentence asking Claude to generate Project instructions "
                "from this conversation. Your prompt should ask Claude to review the conversation, "
                "specify the Project's purpose, and name the knowledge files that should be "
                "referenced — a product positioning doc and case studies uploaded as Project "
                "Knowledge.\n\n"
                "*Hint: what can you copy and paste directly from this challenge description "
                "into your prompt?*"
            ),
            "broken_example": "",
            "rubric": (
                "The learner is writing a single-sentence prompt. Score 25 points for each "
                "of the following four elements present in the sentence:\n\n"
                "1. Asks Claude to review the current conversation — phrases like 'review this "
                "conversation', 'based on what we discussed', or 'from this session'.\n\n"
                "2. Names the Project's purpose — the BD team, value proposition emails, "
                "health system or payer audiences, or similar.\n\n"
                "3. Names at least one knowledge file — product positioning doc, case studies, "
                "BHIQ overview, or similar.\n\n"
                "4. Asks for Project instructions as output — not advice, not a summary. "
                "Phrases like 'write Project instructions' or 'instructions I can paste'.\n\n"
                "If any element is missing, the hint must name the specific missing element "
                "in plain language — e.g. 'Your prompt did not ask Claude to review the "
                "conversation' or 'Your prompt did not name any knowledge files to reference.' "
                "Do not give generic feedback like 'include more detail.' "
                "A genuine single sentence that covers all four elements earns full marks."
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
    3: {
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

**A worked example: writing a skill prompt**

Here is a complete prompt that would produce a working skill for the product team:

```
I want to build a skill called neuroflow-user-stories for the product team.

The skill should assign the role of a senior product manager experienced in
behavioral health technology. The task is to draft well-structured outputs
from raw customer discovery material.

The skill should handle two task types:
- User stories from raw customer discovery notes
- Jobs-to-be-done statements from interview transcripts

Every user story the skill produces must follow this format:
- A one-line title summarizing the need
- The standard structure: "As a [persona], I want [capability] so that [outcome]"
- Acceptance criteria as a numbered list of testable conditions
- A one-sentence context note explaining what the discovery note revealed

The skill should activate when the user says phrases like "write a user story,"
"draft user stories from these notes," "turn these discovery notes into stories,"
or "create a user story."

Constraint: Do not invent capabilities or outcomes that are not directly
supported by the discovery notes. If the notes are ambiguous, flag the gap
rather than filling it in.

Draft a SKILL.md I can install.
```

Notice the structure: it names the role, defines the task types, specifies the
output format with specific required sections, lists trigger phrases for the
description field, and ends with a constraint that prevents the most
consequential failure mode — fabricating product requirements.

**How to develop a skill**

<iframe width="100%" height="380" src="https://www.youtube.com/embed/fHzC9qRGndA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen style="border-radius:6px; display:block; margin:16px 0;"></iframe>

You do not need to write a skill from scratch. Claude can draft it for you through a
process called meta-prompting — using Claude to write instructions for Claude.

Open a standard chat outside any project. Tell Claude what you want to build. A useful
prompt covers three things: what the task is, what the output should look like, and when
the skill should activate. For example: "I want to build a skill for producing a one-page
fit assessment of a federal solicitation for NeuroFlow. The output should always cover
scope, eligibility, key dates, and a fit assessment against NeuroFlow's VA and DoD
capabilities. Draft a SKILL.md I can install."

Claude produces a complete draft including the frontmatter and full instructions. Read the
description field closely — it controls when the skill loads. Claude usually gets close on
the first attempt, but test it against your real trigger phrases before moving on.

Before saving anything, test the draft. Paste the SKILL.md content into a new chat and
ask Claude to use those instructions on a real example — an actual solicitation, an actual
company, an actual document from your workflow. Generic test inputs produce misleading
results. Evaluate the output against your standard, identify what falls short, and tell
Claude specifically what to fix. Most skills reach a working state in two or three iterations.

Once the output consistently meets your standard, save the skill. If Claude produced the
skill as an artifact, click the save option directly on that artifact and Claude installs
it without any additional steps. Alternatively, ask Claude to package the skill as a
`.skill` file, download it, and upload it through the Skills section in the Claude Teams
admin panel.

To modify an existing skill, upload the current `.skill` file into a chat, tell Claude
what needs to change and why, and test the revised version the same way you tested the
original. If a skill is activating at the wrong times or missing cases where it should
trigger, that is almost always a description problem — a one-line fix Claude can diagnose
and correct if you show it an example that failed.

**How to deploy a skill**

Each team member installs and activates skills individually through their own Claude
settings. Skills are not automatically shared or active for everyone on the team — each
person controls which skills are enabled in their own environment.

To install a skill, navigate to **Customize → Skills** in your Claude settings. From there
you can toggle on Anthropic's built-in skills, install skills that have been shared with
you, or upload a custom skill by packaging the skill folder as a ZIP file and selecting
**+ Create skill → Upload a skill**.

Once installed and toggled on, you activate a skill in one of two ways. The first is
automatic — Claude reads the skill's description at the start of each conversation and
loads it when your request matches the trigger phrases in the description field. The second
is manual — type a forward slash followed by the skill name (for example
`/neuroflow-competitive-intel`) to invoke it directly without relying on automatic detection.
Use the manual method when you want to ensure a specific skill runs regardless of how you
phrased the request.

Skills provisioned by an organization owner appear in **Customize → Skills** alongside
Anthropic skills and any skills you have uploaded yourself. If you are on a Team plan and
want to share skills with your organization, an owner must first enable sharing in
**Organization settings → Skills**. Once sharing is enabled, a skill can be distributed to
specific colleagues or published to the organization directory where anyone on the team can
find and install it.
""",
        "quiz": [
            {
                "question": (
                    "A skill prompt for Jira tickets includes a role, two task types, and "
                    "an output structure. Which additional element makes the skill most "
                    "reliable in production?"
                ),
                "options": [
                    "A list of every possible ticket status so Claude can set them automatically",
                    "An explicit constraint — for example: do not leave acceptance criteria "
                    "vague; every criterion must be a testable, binary condition",
                    "A sample of the team's past Jira tickets pasted directly into the prompt",
                    "Instructions to search the web for Jira best practices before responding",
                ],
                "correct_index": 1,
                "hint": "The worked example showed that a constraint prevents the most consequential failure mode — fabricating or leaving vague the elements that matter most.",
            },
            {
                "question": (
                    "Your neuroflow-jira-tickets skill works well for bug reports but "
                    "produces inconsistent feature requests. What is the most targeted fix?"
                ),
                "options": [
                    "Delete the skill and write a new one from scratch covering only feature requests",
                    "Add a second task type block that defines the required sections specifically "
                    "for feature requests — user story, acceptance criteria, definition of done, "
                    "and dependencies",
                    "Switch from the Skills feature to a Project with instructions instead",
                    "Add more examples of good bug reports so Claude learns the pattern better",
                ],
                "correct_index": 1,
                "hint": "Skills can define separate output structures for each task type — adding specificity to the weak task type is faster than rebuilding from scratch.",
            },
            {
                "question": (
                    "You are writing the description field for the neuroflow-jira-tickets skill. "
                    "Which description most clearly controls when the skill activates and "
                    "prevents it from loading on unrelated requests?"
                ),
                "options": [
                    "Helps the product and engineering team with Jira-related work and ticket management",
                    "Activates when the user asks to write a Jira ticket, draft a bug report, "
                    "create a feature request, or write a task for Jira",
                    "Use this skill whenever you need help with project management or task tracking",
                    "A Jira ticket writing skill for the NeuroFlow product team",
                ],
                "correct_index": 1,
                "hint": (
                    "The description field should list specific action phrases users will actually "
                    "type — not a general description of the skill. Vague descriptions load the "
                    "skill too broadly; action phrases give Claude a precise trigger."
                ),
            },
        ],
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

To view, edit, or delete your memories, go to **Settings → Capabilities** in Claude.ai or Claude Desktop, then click "View and edit memory." You can also click your profile icon in the bottom-left corner and select Memory. Review your memories periodically — Claude may capture something imprecisely or retain a fact that is no longer accurate. Memories you delete stop applying immediately.

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

<img src="data:image/png;base64,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/wC7tyv9gsUt3oamOnaDRvbI+JzYmtLXszxNPLOcYwRz64x9smbsftNqS23Orpv4capjbTC3QTNkfbqcNcC+VzSQ15EjiG568Pmdix8MS1362bz3K/GjrqW3V0VOynrGtc2KUiBrXMDxyyC05bnK4aSSSSckoPp7wFdMX1l9vOppbfLFaKm2PpIKp+A2SXtWEhveccDsnuXzzrDS9/0heXWfUdsmt1a1vH2cmPKaSQHAjIIJB5jzLDog+mdcNbv9tTp65abnhm1pp2Ew3C0ukayaoYQ0OkjBxxc2Bwx904dQAda2Y05WbV6kO424lI+y01rp5vY+hqcNqq+oewsDI4z5XCA45eRgcvTjhsb3xvD43uY5pyHNOCF7UTTVEplnlklkPVz3FxP0lB3LwXr/ACXbwkKjU94nihdVQ11bVSvcGsjDmuc4knkGj09AFhtbbObiXLXNzrLLp+S7W641809FX0c0clPNE+Qua/tA7haCCD5RC5GpI6iojifDHPKyOT27GvIDvjHeg7buhfrZorZi3bPWi6UtzuUtT47qCppJOOCOTIc2BrhycQQzJ7uzHnwNKtd329jtlLHW2KplqmQsbM8O5OeGjiP0nK0NEFCIinQIiJoERE0CIiaBERNCeb3Gn+TPrOUakm9xp/kz6zlGoAqgqsqgoMrZ/eit+cQerKq1RZ/eit+cQerKq0BERAREQEREBERAREQEREBERAREQEREBERAREQFsVv1nfaDQly0VTzQiz3KobUVMZiBe57Swgh3Uc42rXUQEREBERAW6XjdHW900XSaOnvBjslNBHTtpoYms42MADQ9wHE4chyJwfMtLRAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREFnf/f8AuPzqX1yqaCuraF7n0NZUUrnDDjDKWEj04Kqv/v8A3H51L65VoEF7XXS510bY6241dUxp4mtmmc8A+fBKtERAREQEREBERAREQUImEwrAi2uXb/UkG3n8Oqymjo7O+dsNMah/BLVF39KJmMuaPuuQ82cFbF4MmnaDUO7lALzSxVNnt1PPcLhHND2rDFHGccTS1wI43MyCOeeXPCDmSLcqPQ+pNU6fvWtdP2dktro6x4qaameHSUrCO0zwADLADjIHceQAWm4QETCYQETCYQTze40/yZ9ZyjUs3uNP8mfWcolAFUFV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XUlSewjk7SJxBLfLacdBzGD6VgERAREQEREBERAREQEREBERAREQEREBERAREQEREBERAREQEREGZtv8yj+n9JVyoKJhZSxtPXGfy81Ogs7/AO/9x+dS+uVaBXd/9/7j86l9cq0CCpERAREQEREBERAREQeIiICIiAiIgIiICIiCaf3Kn+TPruUSln9yp/kz67lEgFUFVlUFBlbP70VvziD1ZVWqLP70VvziD1ZVWgt62nFRFgcnjm0rDyMfG8te0tI862BUSRskGHsDh6QgwCLMmipfvX2iniVL96+0UGGRZnxKl+9faKeJUv3r7RQYZFmfEqX719op4lS/evtFBhkWZ8SpfvX2iniVL96+0UGGRZnxKl+9faKeJUv3r7RQYZFmfEqX719op4lS/evtFBhkWZ8SpfvX2iniVL96+0UGGRZnxKl+9faKeJUv3r7RQYZFmfEqX719op4lS/evtFBhkWZ8SpfvX2iniVL96+0UGGRZnxKl+9faKeJUv3r7RQYZFmfEqX719op4lS/evtFBhkWZ8SpfvX2iniVL96+0UGGRZnxKl+9faKeJUv3r7RQYZFmfEqX719op4lS/evtFBhkWZ8SpfvX2iniVL96+0UGGRZnxKl+9faKeJUv3r7RQYZFmfEqX719op4lS/evtFBhkWZ8SpfvX2iniVL96+0UGGRZnxKl+9faKeJUv3r7RQYZFmfEqX719op4lS/evtFBhkWZ8SpfvX2iniVL96+0UGGRZnxKl+9faKeJUv3r7RQYZFmfEqX719op4lS/evtFBhkWZ8SpfvX2iniVL96+0UGGRZnxKl+9faKeJUv3r7RQYZXlBSOleJJBiMc+fer9lLTsOWxNz6eanQEREFnf/AH/uPzqX1yrQK7v/AL/3H51L65VoEFSIiAiIgIiICIiAiIg8REQEREBERAREQEREE0/uVP8AJn13KJSz+40/yZ9ZyiQCqCqyqCgytn96K35xB6sqrVFn96K35xB6sqrQEREBERARZ61aSvFc2N7o46SOT2jqh3CXfE3r/cpp9JyMnNLFeLZJVNODAZeF2fMMhba+zuKmvNyTr7fqyzxuCLcvNG2torm5W+tts/YV1NJA/u4hyPxHofoVssl6WpM1tGpaa2i0brO4ERFVIiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiICIiAiIgIiIC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" alt="Claude menu showing the plus sign options including Research mode" style="max-width:340px;border-radius:8px;display:block;margin:12px 0;" />
*Click the plus sign to pull up the menu and select Research to activate.*

**Activating Deep Research**

Deep Research is a separate mode — not a toggle inside a standard conversation. Access it
from the model selector. Deep Research browses multiple sources, reads full documents, and
compiles a structured report. Use it for landscape assessments, policy surveys, or
competitive overviews that would otherwise require hours of manual searching.

Deep Research is the most token-intensive Claude capability. Each session consumes
substantially more allocation than a standard conversation. Use it for work that genuinely
requires multi-source synthesis, not for single-question lookups.

**When Claude searches and when it doesn't**

Even with web search enabled, Claude does not always search automatically. If a question looks like something Claude can answer from its training data — a definition, a general concept, a well-known program — it may respond without searching, using information that could be months or years out of date. For current program status, recent policy changes, or active solicitations, Claude's training data is unreliable by design.

Add this standing instruction to any research-focused Project or conversation to eliminate the ambiguity:

```
For any question about current program status, recent policy changes, or active solicitations, search the web before responding.
```

This instruction makes the search behavior explicit rather than leaving it to Claude's judgment about what counts as "current."

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
    """Lesson 4.6 sandbox: learner writes a search prompt, badge confirms search instruction present."""
    state_key = f"sandbox_{TRACK_ID}_{lesson_id}"
    if state_key not in st.session_state:
        st.session_state[state_key] = {"submitted": False, "searched": False}
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
                'padding:8px 14px;margin-bottom:8px;font-size:13px;color:#1A6860;">'
                '✓ Your prompt includes an explicit search instruction — '
                'Claude will retrieve current information rather than relying on training data.</div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div style="background:#FFF3F3;border:1px solid #F16061;border-radius:6px;'
                'padding:8px 14px;margin-bottom:8px;font-size:13px;color:#C0392B;">'
                '⚠ Your prompt does not include an explicit search instruction — '
                'Claude may answer from training data instead of retrieving current measures. '
                'Try adding a phrase like "search the web" or "find current information".</div>',
                unsafe_allow_html=True,
            )
        return True

    input_key = f"{state_key}_input"
    st.text_area(
        "Your prompt:", value="", key=input_key,
        height=140, label_visibility="collapsed",
        placeholder="Write a prompt that explicitly asks Claude to search the web for current information...",
    )
    col1, _ = st.columns([1, 5])
    with col1:
        if st.button("Submit →", key=f"{state_key}_submit", type="primary"):
            prompt = st.session_state.get(input_key, "").strip()
            if not prompt:
                st.warning("Enter a prompt before submitting.")
                return False

            # Check for explicit search instruction — no API call needed
            search_keywords = [
                "search the web", "search the internet", "search online",
                "web search", "look up", "find current", "retrieve current",
                "search for", "google", "browse", "find online",
            ]
            searched = any(kw in prompt.lower() for kw in search_keywords)
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

    # Handle inline HTML (mid-lesson iframes and images)
    concept = lesson["concept"]
    if "<img " in concept or "<iframe " in concept:
        import re
        parts = re.split(r'(<(?:img|iframe)[^>]*/?>(?:.*?</iframe>)?)', concept, flags=re.DOTALL)
        for part in parts:
            if part.startswith("<img ") or part.startswith("<iframe "):
                st.markdown(part, unsafe_allow_html=True)
            elif part.strip():
                st.markdown(part)
    else:
        st.markdown(concept)
    st.markdown("---")

    if already_done:
        # Let sandboxes and challenges fall through to show their output
        # Quiz-only lessons short-circuit here; sandbox/challenge lessons fall through
        if not (lesson.get("sandbox_lesson") or lesson.get("challenge")) and not lesson.get("quiz"):
            st.success("✓ Lesson complete")
            return True
        if not (lesson.get("sandbox_lesson") or lesson.get("challenge")) and lesson.get("quiz"):
            st.success("✓ Lesson complete")
            # Still render quiz for review, but it won't refire completion
            pass

    # Lessons with quiz only
    if lesson.get("quiz") and not lesson.get("challenge"):
        return render_quiz(
            track_id=TRACK_ID, lesson_id=lesson_id,
            questions=lesson["quiz"], label="Knowledge check",
        )

    # Graded challenge lessons (4.2)
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
