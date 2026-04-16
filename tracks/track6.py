# tracks/track6.py — Track 6: Cowork and Desktop Automation, 6 lessons
# No live sandbox API calls — graded challenges use Haiku for scoring only.

import streamlit as st
from utils.quiz import render_quiz
from utils.challenge import render_graded_challenge
from utils.session import is_lesson_complete

TRACK_ID = 6

LESSONS = {
    1: {
        "concept": """
Cowork is the agentic desktop tool inside Claude. It reads and writes files on your local
machine, executes multi-step tasks autonomously, and can run on a schedule without you
manually triggering it each time.

**The three-mode mental model**

| Mode | Best for |
|---|---|
| Claude chat | Thinking, drafting, analyzing, advising |
| Cowork | Acting — producing deliverables by operating on local files |
| Claude Code | Building — writing, running, and modifying code |

**What Cowork can do**

- Read files in a folder and organize or rename them based on content — not just filename or metadata
- Pull from multiple documents and produce a consolidated output
- Convert files between formats
- Run scheduled tasks automatically on a recurring cadence
- Coordinate parallel workstreams using sub-agents for complex tasks
- Access external services through active connectors during task execution
- Control your desktop using keyboard and mouse via computer use mode

**What Cowork cannot do**

- Access files outside folders you explicitly grant
- Connect to NeuroFlow clinical systems or EHRs
- Process PHI — the same rule applies as in Claude Teams
- Run tasks when your computer is asleep or the app is closed

**Security note:** Cowork asks permission before deleting files or taking significant
actions. Grant access only to trusted directories. Like any agentic tool, Cowork is
vulnerable to prompt injection — malicious instructions embedded in files it reads.

**A note on Claude Code**

The table above includes Claude Code as one of the three modes. Claude Code is covered in
depth in Track 7 — but since it appears here, here is the one-line distinction: Claude Code
is a command-line tool for software engineers. It reads and modifies code files, runs tests,
and operates inside a terminal. It is not a general-purpose productivity tool. If your work
does not involve writing or debugging code, Cowork and Claude chat handle the automation
and drafting use cases you need.
""",
        "quiz": [
            {
                "question": (
                    "You need to think through a complex response to a federal RFP question. "
                    "Which tool is appropriate?"
                ),
                "options": [
                    "Cowork — it can read the RFP file and generate a response autonomously",
                    "Claude Code — it can process documents efficiently",
                    "Claude chat",
                    "Any of the above — they all produce the same result",
                ],
                "correct_index": 2,
                "hint": "This task is cognitive — thinking through and drafting a response. Which mode handles that?",
            },
            {
                "question": (
                    "You have 150 inconsistently named partner briefing files across a folder "
                    "and need them renamed and sorted by partner name and date. "
                    "Which tool fits this task?"
                ),
                "options": [
                    "Claude chat — paste in the filenames and ask for a renaming scheme",
                    "Claude Code — write a script to rename the files",
                    "Cowork — it reads the file contents to make informed naming decisions and acts on the files directly",
                    "A connector to Google Drive",
                ],
                "correct_index": 2,
                "hint": "The task involves reading file contents and acting on files — which mode is designed for that?",
            },
            {
                "question": (
                    "You schedule a Cowork task to run every Monday at 8 AM. On Sunday night "
                    "you close your laptop and it goes to sleep. What happens Monday morning?"
                ),
                "options": [
                    "The task runs in the background regardless of sleep state",
                    "The task runs the next time you open Claude Desktop",
                    "Claude sends a notification to run the task manually",
                    "The task does not run because the computer is asleep",
                ],
                "correct_index": 3,
                "hint": "Cowork cannot run tasks when the computer is asleep — this is a hard constraint.",
            },
        ],
    },
    2: {
        "concept": """
Cowork reads the content of files — not just their names or metadata — and uses that content
to make informed decisions about how to organize them. A rename script looks at a filename and
applies a pattern. Cowork opens the file, reads what is inside, determines what type of
document it is, who it involves, and when it was created, and then renames and sorts it
accordingly.

**Effective Cowork file organization instructions include five elements:**

1. Which folder to access
2. The naming convention to apply, with at least two identifying elements
3. The subfolder structure to create, with named categories
4. How to handle ambiguous files — skip, flag, or apply a default prefix
5. Whether to ask before changes or proceed autonomously

**Why the ambiguity rule matters**

Without an explicit rule for files Cowork cannot confidently classify, it guesses. Guessed
filenames on important documents create more cleanup work than you started with. A rule like
"add the prefix REVIEW_ to any file you cannot confidently classify and do not move it"
protects important documents from being misclassified and buried in the wrong subfolder.

**Why the permission rule matters**

Renaming is reversible. Deletion is not. Specifying which actions Cowork should take
autonomously — and which require your approval — prevents irreversible mistakes in large
batch operations.

**File format note**

Cowork reads file content as text. Standard formats — DOCX, PDF, plain text, Markdown —
work reliably. Files formatted for visual display rather than data extraction can produce
unreliable results.
""",
        "challenge": {
            "scenario": (
                "You are a product manager at NeuroFlow. Over the past two years your team "
                "ran discovery interviews, collected design feedback, exported Jira tickets, "
                "and assembled competitive research — all saved to a single folder with no "
                "consistent naming convention. File names like `notes.docx`, `final_v2.pdf`, "
                "and `interview copy (3).docx` make the folder nearly unsearchable.\n\n"
                "**Task:** Write the Cowork task instruction to organize this folder. "
                "Your instruction must specify the naming convention, subfolder structure, "
                "ambiguous file handling, and permission behavior."
            ),
            "broken_example": "",
            "rubric": (
                "Score the instruction against four criteria (25 points each):\n\n"
                "1. Naming convention includes at least two identifying elements — document type, "
                "source, date, or topic (e.g., DocumentType_Source_YYYY-MM-DD). A single element "
                "like a date alone does not distinguish two files from the same week.\n\n"
                "2. Subfolder structure defined with at least two named categories — actual folder "
                "names like CustomerInterviews, DesignFeedback, JiraExports. 'Organize by type' "
                "without naming the folders does not earn this criterion.\n\n"
                "3. Ambiguous file handling specified with a concrete rule — what happens to a file "
                "Cowork cannot confidently classify? Must name a specific action: add a REVIEW_ "
                "prefix, place in a REVIEW subfolder, or skip it.\n\n"
                "4. Permission behavior addressed — specifies what Cowork should do autonomously "
                "and what requires approval before acting. At minimum, must say whether deletion "
                "or overwriting requires confirmation."
            ),
            "model_answer": (
                "Access the /Product_Discovery folder. Read every file.\n\n"
                "Rename each file using this format: DocumentType_Source_YYYY-MM-DD\n"
                "(examples: Interview_MeadowsHealth_2026-03-14, DesignFeedback_UX_2025-11-02, "
                "JiraExport_Backlog_2025-08-19)\n\n"
                "Sort files into subfolders: CustomerInterviews, DesignFeedback, JiraExports, "
                "CompetitiveResearch, StakeholderComms.\n\n"
                "If you cannot confidently determine the document type and source from the file "
                "content, add the prefix REVIEW_ to the filename, place it in a REVIEW subfolder, "
                "and do not attempt to rename or categorize it further.\n\n"
                "Proceed with renaming and sorting without asking for each file. "
                "Ask before deleting or overwriting anything."
            ),
            "hints": [
                "A filename with only one element — like a date alone — will not distinguish two interview notes from the same week. What second element makes each file uniquely identifiable six months from now?",
                "Cowork needs category names to sort into. 'Organize by type' is not enough — name the actual folders. What are the two or three most common document types in this folder?",
                "Without a rule, Cowork guesses on files it cannot identify. What should happen to a file it cannot confidently classify — and where should it go?",
            ],
        },
    },
    3: {
        "concept": """
Cowork supports scheduled tasks — instructions you configure once that run automatically on
a cadence without manual triggering each time.

**How to create a scheduled task**

1. In a Cowork session, type `/schedule`
2. Write the task instruction (same format as any Cowork task)
3. Set the frequency: daily, weekly, on a specific day and time
4. Cowork saves and runs it automatically on schedule

**Requirements**

- Computer must be awake when the task runs
- Claude Desktop app must be open
- Complex tasks consume more of your usage allocation per run — batch related work

**NeuroFlow example — weekly program status report**

```
Every Monday at 8:00 AM, access the /EVIDENT/Deliverables folder.
Read all files modified in the past 7 days. Produce a weekly status
report with four sections: completed milestones, in-progress items,
upcoming deadlines in the next 30 days, and items flagged for review.
Save as YYYY-MM-DD_EVIDENT_WeeklyStatus.md in /Reports.
```

A well-written scheduled task names the folder, defines the cadence, specifies the output
structure, and names the save location. Vague instructions produce inconsistent outputs
across runs because Cowork cannot compensate for missing scope with prior session memory.
""",
        "quiz": [
            {
                "question": (
                    "You configure a Cowork task to run every Friday at 5 PM. That Friday at "
                    "4:45 PM your computer goes to sleep. What happens?"
                ),
                "options": [
                    "The task runs in the background regardless",
                    "The task does not run because the computer is asleep",
                    "The task runs the next time you open Claude Desktop",
                    "The task runs at 5 PM Saturday instead",
                ],
                "correct_index": 1,
                "hint": "Scheduled tasks require the computer to be awake — this is a hard constraint, not a recoverable failure.",
            },
            {
                "question": "What does typing /schedule do inside a Cowork session?",
                "options": [
                    "Sends the current task output to your calendar",
                    "Pauses the current task until a scheduled time",
                    "Opens the scheduling interface to create a recurring automated task",
                    "Emails the output to your team on a recurring schedule",
                ],
                "correct_index": 2,
                "hint": "/schedule is the command that turns a one-time task into a recurring automated one.",
            },
        ],
    },
    4: {
        "concept": """
Cowork gained computer use capabilities in March 2026 — allowing Claude to directly control
your macOS desktop using keyboard and mouse input. Combined with the Claude in Chrome
extension, this enables Claude to operate as a genuine desktop agent across applications
and the web.

**Computer use in Cowork**

Computer use allows Cowork to open applications, navigate browser windows, fill forms, click
buttons, and complete multi-step workflows on your screen — tasks that previously required
you to be sitting at your computer executing each step manually.

Practical example:
```
Navigate to our internal Confluence site. Find all pages under the
Engineering space updated in the last 14 days. For each page, capture
the title, author, and a one-sentence summary of what changed. Save
as YYYY-MM-DD_EngineeringDocs_RecentUpdates.md in /Reports.
```

**Security risks: prompt injection through browser content**

When Cowork operates a browser, it reads whatever appears on the page — including content
you did not put there. Malicious actors can embed hidden instructions in web pages designed
to redirect an agent's behavior. A page might contain invisible text instructing Cowork to
send data somewhere or take an action outside the original task scope. The agent cannot
always distinguish between page content and instructions.

Three practices reduce this risk:
- Limit computer use to trusted, internal websites and applications
- Review the task log after every computer use session before relying on the output
- Never grant computer use access to sessions involving sensitive credentials or financial systems

**Note:** Computer use is in research preview — available on macOS only as of April 2026.
Validate outputs carefully and expect rough edges.
""",
        "quiz": [
            {
                "question": "What does Cowork computer use enable that file-based Cowork cannot do?",
                "options": [
                    "Access to files on your local computer",
                    "Scheduled recurring tasks",
                    "Controlling desktop applications and browsers using keyboard and mouse input",
                    "Connecting to external services like Slack or Monday",
                ],
                "correct_index": 2,
                "hint": "File-based Cowork reads and writes files. Computer use extends beyond the file system.",
            },
            {
                "question": (
                    "You use Cowork computer use to automate a research task that reads several "
                    "external websites. After the session, you notice Cowork posted a message "
                    "to Slack that was not part of your original instruction. What most likely "
                    "caused this?"
                ),
                "options": [
                    "Cowork exceeded its token limit and defaulted to a fallback action",
                    "A web page contained embedded instructions that redirected Cowork's behavior — a prompt injection attack",
                    "The Slack connector triggered automatically when Cowork detected relevant content",
                    "Computer use mode shares output to Slack by default when no save location is specified",
                ],
                "correct_index": 1,
                "hint": "When an agent reads external web content, that content can contain instructions. What is this attack called?",
            },
        ],
    },
    5: {
        "concept": """
Without connectors, Cowork works only with files in folders you have explicitly granted
access to on your local machine. With connectors, Cowork can pull live data from external
services, use it during task execution, and write outputs back to those services — all as
part of a single automated workflow.

**What changes with connectors**

Without connectors:
```
Access /Product/SprintNotes folder. Read all notes from the
last sprint. Produce a sprint summary and save to /Reports.
```
This works only if the sprint notes are already downloaded locally.

With a Google Drive connector:
```
Search Google Drive for all documents in the Product Sprint Notes
folder modified in the last two weeks. Read each document. Produce
a sprint summary and save to /Reports on my local machine.
```
No manual download required. Cowork retrieves files through the connector and saves the output locally.

**The highest-value Cowork pattern at NeuroFlow**

Local proprietary files + live connector data, with output written back to a team channel.
Here are concrete examples across three teams:

*Product:*
```
Access /Product/RoadmapDocs on my local machine. Pull all Jira
tickets in the current sprint that are unresolved. Produce a
weekly engineering status report combining roadmap documents with
open Jira tickets. Post the summary to #product-updates in Slack
and save a copy to /Reports as YYYY-MM-DD_SprintStatus.md.
```

*Sales:*
```
Access /Sales/AccountResearch on my local machine. Pull the five
most recent emails from each account in my HubSpot pipeline stage
"Proposal Sent." Produce a one-paragraph call prep brief for each
account combining the research file with the email history. Save
each brief to /Sales/CallPrep as AccountName_CallPrep.md.
```

*Marketing:*
```
Access /Marketing/ContentDrafts on my local machine. Pull the
last 30 days of top-performing LinkedIn posts from our company
page. Identify the three content formats with the highest
engagement. Produce a one-page brief comparing our draft
headlines against those formats. Save it as ContentAudit.md.
```

**PHI reminder:** Do not grant Cowork access to folders or connectors that contain patient-identifiable information.
""",
        "quiz": [
            {
                "question": (
                    "What is the key advantage of using connectors inside a Cowork session?"
                ),
                "options": [
                    "Connectors allow Cowork to run without the computer being awake",
                    "Connectors reduce the token cost of Cowork tasks",
                    "Connectors allow Cowork to retrieve live data from external services without requiring manual file download first",
                    "Connectors give Cowork access to more capable models",
                ],
                "correct_index": 2,
                "hint": "The key distinction is where the data comes from — local files only, or live from external services.",
            },
            {
                "question": (
                    "A product manager wants to pull all unresolved Jira tickets from the current "
                    "sprint and post a summary to the #engineering Slack channel. No local files "
                    "are involved. What is the right tool?"
                ),
                "options": [
                    "Claude chat with Jira and Slack connectors active",
                    "Cowork with Jira and Slack connectors active",
                    "Computer use mode to navigate Jira in the browser",
                    "A scheduled Cowork task",
                ],
                "correct_index": 0,
                "hint": "No local files means no need for Cowork's file access. Which mode handles conversational tasks with connectors?",
            },
            {
                "question": (
                    "The same product manager wants this Jira-to-Slack summary to happen "
                    "automatically every Monday morning without manual triggering. What changes?"
                ),
                "options": [
                    "Nothing — chat with connectors runs on a schedule automatically",
                    "Enable Deep Research mode to automate the retrieval",
                    "Use computer use mode to trigger the chat task on a schedule",
                    "Switch to Cowork and configure a scheduled task with the Jira and Slack connectors active",
                ],
                "correct_index": 3,
                "hint": "Scheduled automation requires Cowork — chat doesn't run on a schedule.",
            },
        ],
    },
    6: {
        "concept": """
Every standalone Cowork session starts fresh. When you open Cowork, select a folder, and
run a task, Claude has no memory of previous sessions in that folder. Any context,
preferences, or conclusions from prior sessions must be re-established explicitly — either
by including them in the task instruction or by maintaining context files in the folder itself.

Cowork Projects, launched in March 2026, solve this. A Project is a persistent workspace
inside Claude Desktop that bundles a folder, custom instructions, memory, and scheduled
tasks into a single named environment. When you run tasks inside a Project, Claude
accumulates memory across sessions.

**What a Project adds over a folder-only session**

| Capability | Folder only | Project |
|---|---|---|
| File access | Yes | Yes |
| Instructions applied to every task | No | Yes |
| Memory across sessions | No | Yes |
| Scheduled tasks scoped to this workspace | No | Yes |

**The practical rule:** If a workflow involves more than one session — any recurring task,
any multi-phase project, any work that builds on prior outputs — create a Project. Selecting
a folder alone will not carry context forward.

**Setting up a Cowork Project**

1. Open the Cowork tab in Claude Desktop
2. Click Projects in the left sidebar
3. Click the + icon and name the project, attach a folder, and add standing instructions
4. Memory is on by default

Once created, every task you run inside the project builds the memory Claude holds for that
workspace. Memory is scoped — what Claude learns in one project does not carry into other
projects or standalone sessions.
""",
        "quiz": [
            {
                "question": (
                    "A NeuroFlow program manager runs a weekly ARPA-H status report using Cowork. "
                    "Each week they have to re-explain the project structure, document conventions, "
                    "and reporting standards before Cowork can produce a consistent report. "
                    "What is the most efficient fix?"
                ),
                "options": [
                    "Add the context to the task instruction at the start of each session",
                    "Use a scheduled task — it preserves context between runs",
                    "Create a Cowork Project with standing instructions that apply to every task automatically",
                    "Store the context in a text file in the folder and reference it in each task",
                ],
                "correct_index": 2,
                "hint": "Re-explaining context every session is exactly what Projects are designed to eliminate.",
            },
            {
                "question": (
                    "You create a Cowork Project for NeuroFlow's ARPA-H EVIDENT deliverables. "
                    "After three weeks of work, Claude has accumulated memory about the project "
                    "team, milestone structure, and document format. You open a different Project "
                    "for your BD pipeline work. What memory does Claude have in the BD project?"
                ),
                "options": [
                    "All memory from the EVIDENT project, since it is the same account",
                    "Only the formatting preferences, not the project-specific content",
                    "Memory from global settings only, not project-specific memory",
                    "No memory — Project memory is scoped and does not carry between projects",
                ],
                "correct_index": 3,
                "hint": "Project memory is scoped to prevent different workflows from bleeding into each other.",
            },
        ],
    },
}


def render_lesson(lesson_id: int) -> bool:
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        st.error(f"Lesson 6.{lesson_id} not found.")
        return False

    already_done = is_lesson_complete(TRACK_ID, lesson_id)
    st.markdown(lesson["concept"])
    st.markdown("---")

    if already_done:
        if not lesson.get("challenge"):
            st.success("✓ Lesson complete")
            return True

    if lesson.get("challenge"):
        ch = lesson["challenge"]
        return render_graded_challenge(
            track_id=TRACK_ID, lesson_id=lesson_id,
            scenario=ch["scenario"], broken_example=ch["broken_example"],
            rubric=ch["rubric"], model_answer=ch["model_answer"],
            hints=ch["hints"], input_label="Your Cowork task instruction",
            max_chars=600,
        )

    if lesson.get("quiz"):
        return render_quiz(
            track_id=TRACK_ID, lesson_id=lesson_id,
            questions=lesson["quiz"], label="Knowledge check",
        )

    st.info("Content coming soon.", icon="🔜")
    return False
