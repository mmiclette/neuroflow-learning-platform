# tracks/track7.py — Track 7: Claude Code, 5 lessons (Advanced)

import streamlit as st
from utils.quiz import render_quiz
from utils.challenge import render_graded_challenge
from utils.session import is_lesson_complete

TRACK_ID = 7

WEAK_CLAUDE_MD = """# NeuroFlow Assessment Data Service

Python service for processing behavioral health data.

## Stack
Python, some SQL, AWS

## Rules
- Write good Python
- Don't break anything important
- Tests should pass
- Be careful with patient data"""

LESSONS = {
    1: {
        "concept": """
🏗️ **Under construction** — this track is still being developed and content may change.

---

Claude Code is an agentic coding tool. You give it a task in natural language. It reads the
relevant files in your project, plans the work, proposes changes, and — after your approval —
executes them.

In Claude chat, Claude reads what you provide and produces a text response. You copy, adapt,
and implement it yourself. In Claude Code, Claude has direct access to your file system. It
reads files on its own, generates diffs, and writes changes directly. The review step is a
diff approval, not a text response.

**How a session works**

Claude reads your CLAUDE.md file at session start. You describe a task. Claude maps the work,
identifies which files to read, proposes each change before touching anything. You accept or
reject. When you accept, Claude applies the edit and continues. You can interrupt at any point.

**Two entry points**

The **desktop app** installs like any native application on macOS or Windows. No Node.js required.
No terminal setup. It shows diffs inline and lets you preview a running dev server. Product
members and engineers who do not live in the terminal often start here.

The **terminal CLI** installs with a shell script and runs from the command line. It is faster for
engineers who prefer staying in the terminal and supports automation and CI/CD pipelines.

**When Claude Code creates more work than it saves**

Large, underspecified refactors. "Refactor the data pipeline to be more modular" without a
specific file list, target pattern, and acceptance criteria will produce a large diff harder
to review than the change itself. Scope the task first — use Claude chat to think through the
design, then use Claude Code to execute it.

Tasks that require domain knowledge not in the codebase. If the correct implementation depends
on a clinical protocol or business rule that lives outside the repository, Claude will implement
something plausible rather than correct.

Security-sensitive code. Authentication flows, permission checks, and any code gating access to
patient data warrant full security review before merge.
""",
        "quiz": [
            {
                "question": (
                    "A NeuroFlow product engineer uses Claude Code to add structured logging to "
                    "a Python module in the data pipeline. She approves the proposed changes. A "
                    "product manager uses Claude chat for the same task and gets a code snippet "
                    "back. What is the fundamental difference in what each person did?"
                ),
                "options": [
                    "Claude Code used a more capable model than Claude chat",
                    "Claude chat cannot write Python; Claude Code can",
                    "Claude Code required the engineer to write a prompt; Claude chat did not",
                    "The engineer's changes were applied directly to the file after approval; the PM received text she would need to paste and implement herself",
                ],
                "correct_index": 3,
                "hint": "The key distinction is whether changes were applied to actual files or returned as text.",
            },
            {
                "question": (
                    "A NeuroFlow product engineer who has never used a terminal wants to start "
                    "using Claude Code today. Which entry point is designed for this situation?"
                ),
                "options": [
                    "The terminal CLI, because it gives more control",
                    "The VS Code extension, because it requires no installation",
                    "The desktop app, which installs like a native application and requires no terminal or Node.js setup",
                    "Claude chat, which handles file editing without a separate tool",
                ],
                "correct_index": 2,
                "hint": "One entry point has zero prerequisites for someone who has never used a terminal.",
            },
            {
                "question": (
                    "An engineer on the BHIQ team asks Claude Code to 'refactor the scoring "
                    "module to be more modular.' The session produces a 400-line diff touching "
                    "12 files. What went wrong before the session started?"
                ),
                "options": [
                    "The task was underspecified — no file list, target pattern, or acceptance criteria — so Claude filled the gaps with its own judgment, producing a diff harder to review than the change itself",
                    "The engineer should have used Claude chat instead of Claude Code for this task",
                    "The context window was too small for a task of this size",
                    "Claude Code cannot handle refactoring tasks — only feature additions",
                ],
                "correct_index": 0,
                "hint": "What information would Claude need to produce a scoped, reviewable diff rather than a sweeping change?",
            },
        ],
    },
    2: {
        "concept": """
Claude Code has two installation paths. Desktop installs in minutes with no prerequisites.
CLI requires a terminal and a one-line install command.

**Desktop app installation**

Download from claude.ai. On macOS, open the .dmg and drag Claude to Applications. On Windows,
run the installer. Sign in with your Anthropic account, then click the **Code** tab. If Code
prompts you to upgrade, you need an active Pro, Max, Teams, or Enterprise subscription — the
Code tab does not appear on free accounts.

**CLI installation**

On macOS, Linux, or WSL:
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

On Windows PowerShell:
```powershell
irm https://claude.ai/install.ps1 | iex
```

Start a session:
```bash
cd /path/to/your/project
claude
```

Common CLI setup errors: `command not found: claude` means the PATH was not updated — close
the terminal and open a new one, or run `source ~/.zshrc`. Login loops mean stale credentials —
run `claude auth logout` then `claude` again.

**Key session commands**

| Command | What it does |
|---|---|
| `/init` | Generate a starter CLAUDE.md from your project |
| `/compact` | Compress conversation history mid-session |
| `/clear` | Start a completely fresh session |
| `/rewind` | Select a checkpoint and summarize from that point |
| `/btw` | Quick question — answer never enters conversation history |
| `/cost` | Show token usage for current session |
| `/permissions` | Review and adjust tool permissions |

**Do not enable auto-accept on production codebases** — it removes the diff review step.
Do not hard-code credentials in any file Claude can read.
""",
        "quiz": [
            {
                "question": (
                    "A NeuroFlow product engineer downloads the Claude Code desktop app, signs "
                    "in, opens the Code tab, and sees a prompt to upgrade her subscription. "
                    "What does this mean?"
                ),
                "options": [
                    "Her Node.js version is too old for the desktop app",
                    "The desktop app requires a separate license from the terminal CLI",
                    "The Code tab requires a paid subscription — Pro, Max, Teams, or Enterprise — and her account does not have one",
                    "She needs to reinstall with administrator permissions",
                ],
                "correct_index": 2,
                "hint": "The Code tab is a paid feature — what does that imply about free accounts?",
            },
            {
                "question": (
                    "A NeuroFlow engineer installs the CLI on macOS using the native install "
                    "script, then runs `claude` and gets `command not found`. What should he "
                    "try first?"
                ),
                "options": [
                    "Reinstall using npm instead of the native script",
                    "Log out of his Anthropic account and log back in",
                    "Upgrade to Node.js 20",
                    "Close the terminal and open a new one, or source his shell config file, so the updated PATH takes effect",
                ],
                "correct_index": 3,
                "hint": "The install script updates PATH — what needs to happen before the shell sees the change?",
            },
            {
                "question": (
                    "During a long Claude Code session on the NeuroFlow-Intelligence repo, an "
                    "engineer wants to ask a quick question about how a function works without "
                    "adding the exchange to the session's conversation history. Which command "
                    "does this?"
                ),
                "options": [
                    "/clear — which starts a fresh session",
                    "/compact — which compresses history to free context",
                    "/btw — which answers in a dismissible overlay that never enters conversation history",
                    "/rewind — which selects a checkpoint to summarize from",
                ],
                "correct_index": 2,
                "hint": "The command is designed for side questions that should not pollute the session context.",
            },
        ],
    },
    3: {
        "concept": """
CLAUDE.md is a plain text file at the root of your project. Claude Code reads it at the start
of every session. It is the difference between an agent that works correctly in your codebase
on the first task and one that makes sensible-but-wrong choices you have to reverse.

Write CLAUDE.md like onboarding documentation for a highly capable engineer who knows nothing
specific about your project. That engineer understands Python, knows common patterns, and
follows conventions — but has no idea that your pipeline uses psycopg2 instead of SQLAlchemy,
that `migrations/` should never be touched manually, or that PHI handling must follow the
patterns in `src/utils/privacy.py`.

**What to include**

A project description covering what the system does, what data it processes, and what it
connects to.

The tech stack in concrete terms — version, key libraries, database, infrastructure. Not
"we use Python" but "Python 3.11, psycopg2, AWS RDS, pytest."

Coding conventions that are actually enforced. If you run black with line length 88 and
require type hints, say so explicitly.

Testing requirements with the exact command and coverage threshold. "Tests should pass"
is not sufficient. `pytest src/tests/ --cov=src --cov-fail-under=80` is.

Protected files and directories. List what Claude should not touch without explicit instruction.

Data handling rules that name specific fields. Any project touching PHI needs explicit rules —
name the fields that cannot appear in logs, and reference the pattern file.

**What not to include:** Aspirational instructions. "Be careful" and "write clean code" do not
constrain behavior. Instructions without a specific action, file, constraint, or pattern are filler.

**Start with `/init`:** Run this at the start of your first Claude Code session in any project.
Claude analyzes the codebase and generates a starter CLAUDE.md. Add PHI rules, protected
directories, and constraints Claude cannot infer from code alone.
""",
        "challenge": {
            "setup": WEAK_CLAUDE_MD,
            "scenario": (
                "This CLAUDE.md was written quickly for a NeuroFlow Python service.\n\n"
                "**Task:** In 2–4 sentences, name the four specific problems with this "
                "CLAUDE.md. You do not need to write a corrected version."
            ),
            "rubric": (
                "Score the response against four criteria (25 points each):\n\n"
                "1. Identifies the vague/underspecified stack — 'Python, some SQL, AWS' is "
                "present but unactionable. Claude needs version numbers and specific library "
                "names to make correct dependency and import choices.\n\n"
                "2. Identifies at least one unactionable rule — 'Write good Python' or "
                "'Be careful with patient data' names no specific action, file, or field.\n\n"
                "3. Identifies missing protected files or directories — the CLAUDE.md names no "
                "files or directories that Claude should not touch.\n\n"
                "4. Identifies incomplete testing requirement — 'Tests should pass' has no test "
                "command and no coverage threshold. Claude cannot run tests without the command."
            ),
            "model_answer": (
                "Four problems: (1) The stack is present but too vague — 'Python, some SQL, AWS' "
                "gives Claude no version, library names, or tooling information to act on. "
                "(2) 'Write good Python' is unactionable — it needs a specific formatter, linter, "
                "and enforced conventions like type hints. (3) 'Be careful with patient data' "
                "names no specific fields and references no pattern file in the codebase. "
                "(4) 'Tests should pass' has no test command and no coverage threshold — "
                "Claude cannot run tests without knowing the exact command."
            ),
            "hints": [
                "'Python, some SQL, AWS' exists but tells Claude nothing it can act on. What does Claude actually need to make correct dependency and import choices?",
                "Two of the rules cannot be followed literally because they name no specific action, file, or field. Which are they?",
                "'Don't break anything important' names nothing. 'Tests should pass' gives Claude no way to run them. Both need specifics.",
            ],
        },
    },
    4: {
        "concept": """
When Claude Code completes a task, it produces a log showing what it read, modified, created,
and why. Reading task logs is not optional — it is the review step that keeps you in control
of what goes into your codebase.

**What a log shows**

Every file Claude opened, often with line ranges. Every file modified, with a diff or description.
Any files created. Any commands run. Claude's reasoning at each decision point. A final summary.

**What to check**

Did Claude read the right files? Did it modify only what the task required? Does the reasoning
match the instruction?

**Common out-of-scope patterns to flag**

Touching files the task did not name. Adding dependencies beyond what the fix requires.
Refactoring existing code the instruction did not ask to change. Creating test or migration
files without explicit instruction. Modifying function signatures when the task was only to
add logic inside a function.

**Reading a diff before you approve**

*Scope:* does the changed code match only what the task required, or did Claude touch adjacent
functions? Changes outside the named function are a flag.

*Imports:* a new `import tenacity` means Claude added a dependency. Check whether it belongs.

*Signature changes:* if the function definition line changed, that is a breaking change for
any caller.

*New files:* if a new file appears in the diff summary, Claude created something the task did
not ask for.

**Steering a session that's going wrong**

For scope creep: reject the specific diff that exceeds scope, then type a narrowing instruction.
"Only modify `calculate_phq9_score` — do not touch validators.py" is sufficient.

For wrong direction: stop immediately, correct in the same session or start fresh. After two
failed corrections, use `/clear` and write a better prompt incorporating what you learned.

Correct in place when Claude read the right files but made a specific wrong choice. Start fresh
when Claude misunderstood the scope entirely or context degradation is likely. Use `/rewind`
when the session went wrong at a specific step but earlier work was good.

Always commit before starting fresh.
""",
        "challenge": {
            "setup": "",
            "scenario": (
                "A NeuroFlow engineer ran Claude Code with this instruction:\n\n"
                "> \"Add input validation to the `calculate_phq9_score` function in "
                "`src/scoring/phq9.py`. Validate that `responses` is a list of exactly 9 "
                "integers, each between 0 and 3. Raise ValueError for each invalid input.\"\n\n"
                "The task log shows four out-of-scope actions: the function signature changed "
                "from `*args` to `responses: list`, a new helper was added to "
                "`src/utils/validators.py`, a new test file was created, and `mypy==1.9.0` "
                "was added to `requirements.txt`.\n\n"
                "**Task:** In 1–3 sentences, identify which single out-of-scope action "
                "carries the highest risk and explain why."
            ),
            "rubric": (
                "Score the response against two criteria (50 points each):\n\n"
                "1. Identifies the function signature change or the mypy dependency as the "
                "highest-risk action — not the new helper or the new test file.\n\n"
                "2. Gives a specific reason tied to codebase impact beyond 'it was out of scope': "
                "signature change breaks every existing caller at runtime; mypy adds type errors "
                "across the codebase for every developer. The new helper and test file are "
                "isolated additions — they can be deleted without breaking anything."
            ),
            "model_answer": (
                "The function signature change carries the highest risk. Changing from `*args` "
                "to `responses: list` is a breaking change for every existing caller — any code "
                "that calls `calculate_phq9_score` with positional arguments will raise a "
                "TypeError at runtime after this diff is merged. The new test file and helper "
                "are additive and can be deleted without consequence; the signature change cannot "
                "be safely undone without finding and updating all callers."
            ),
            "hints": [
                "'It was out of scope' is not a risk. What specifically breaks or changes for other engineers if this gets merged?",
                "One action affects every existing caller of the function. Another affects every developer's environment. Which has the harder rollback?",
                "A new test file is easy to delete. A dependency that introduces type errors across the codebase is not. A signature change that breaks a calling function at runtime is discovered only when the code runs.",
            ],
        },
    },
    5: {
        "concept": """
A Claude Code task prompt is not a description of what you want — it is a specification of
what Claude should do. The difference is observable: a vague task prompt produces a large
diff that includes Claude's guesses. A well-scoped prompt produces a small, reviewable diff
that touches only what you named.

**Five elements of a well-scoped task prompt**

1. **Name the exact file and function.** Not "the writer" but
   `src/pipeline/writer.py`, function `push_assessment_results`.

2. **Specify the expected behavior.** Not "add retry logic" but "retry 3 times with
   exponential backoff on 429 or 503 responses."

3. **Define what happens after the last attempt.** "Re-raise the original exception after
   the third failure" is a specification. "Handle the error" is not.

4. **Set explicit boundaries.** "Do not modify the function signature or add new
   dependencies." Without this, Claude may improve adjacent code it encountered while reading.

5. **Reference the existing pattern.** "Follow the retry pattern in
   `push_fhir_resource` in `src/clients/fhir_client.py`." Claude reads that function and
   replicates the pattern — producing consistent code that matches what already exists.

**NeuroFlow-specific context**

PHI handling patterns live in `src/utils/privacy.py`. Any prompt involving patient data
should reference this file explicitly.

The NeuroFlow-Intelligence pipeline uses structured logging via the `logger` object from
`src/utils/logging.py`. If a task adds logging, specify this logger.

Without expected behavior, Claude writes what seems reasonable. Without boundaries, Claude
may improve adjacent code it encountered while reading. It means well. It still requires
your review.

**The uncertainty handling rule**

The most common Claude Code failure mode is not incorrect logic — it is a plausible-looking diff that implements the wrong behavior because Claude filled in a gap rather than asking. Add this rule explicitly to any task prompt where ambiguity exists:

```
If you cannot confidently determine the correct file to modify or the correct pattern to follow, stop and ask rather than proceeding with a guess.
```

This single instruction prevents Claude from making a confident-sounding change to the wrong function, adopting the wrong pattern, or modifying a file it was not meant to touch. Claude's default is to proceed; this instruction overrides that default at the specific moments where proceeding causes the most damage.
""",
        "challenge": {
            "setup": "",
            "scenario": (
                "A NeuroFlow engineer needs to add retry logic to the "
                "`push_assessment_results` function in `src/pipeline/writer.py`. The function "
                "calls an external API and fails silently on 429 or 503 errors. It should retry "
                "3 times with exponential backoff and re-raise the original exception after the "
                "final failure. A similar retry pattern already exists in "
                "`src/clients/fhir_client.py`.\n\n"
                "**Current prompt:** \"Add retry logic to the writer.\"\n\n"
                "**Task:** Rewrite this as a well-scoped task prompt. One to three sentences maximum."
            ),
            "rubric": (
                "Score the prompt against five criteria (20 points each):\n\n"
                "1. Names the exact file path and function name — `src/pipeline/writer.py` and "
                "`push_assessment_results`.\n\n"
                "2. Specifies retry count and backoff type — 3 retries, exponential backoff "
                "(or 'exponential').\n\n"
                "3. Specifies behavior after final failure — re-raise the original exception "
                "(or equivalent: 'raise the exception after the third failure').\n\n"
                "4. Sets at least one explicit boundary — do not modify the function signature, "
                "do not add new dependencies, or similar constraint on scope.\n\n"
                "5. References the existing pattern in `fhir_client.py` — names the file and "
                "optionally the function `push_fhir_resource`."
            ),
            "model_answer": (
                "Add retry logic to the `push_assessment_results` function in "
                "`src/pipeline/writer.py`. Retry up to 3 times with exponential backoff on "
                "429 or 503 responses; re-raise the original exception after the third failure. "
                "Do not modify the function signature or add new dependencies. Follow the retry "
                "pattern in `push_fhir_resource` in `src/clients/fhir_client.py`."
            ),
            "hints": [
                "'The writer' is ambiguous — name the exact file path and function name.",
                "'Retry logic' needs two parameters: how many retries, and what kind of backoff.",
                "After the retries are exhausted, what happens? And what should Claude leave unchanged?",
            ],
        },
    },
}


def render_lesson(lesson_id: int) -> bool:
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        st.error(f"Lesson 7.{lesson_id} not found.")
        return False

    already_done = is_lesson_complete(TRACK_ID, lesson_id)

    if lesson_id == 3:
        st.markdown(lesson["concept"])
        st.markdown("**Weak CLAUDE.md to critique:**")
        st.code(lesson["challenge"]["setup"], language="markdown")
        st.markdown("---")
    else:
        st.markdown(lesson["concept"])
        st.markdown("---")

    if already_done:
        if not lesson.get("challenge"):
            st.success("✓ Lesson complete")
            return True

    if lesson.get("quiz"):
        from utils.quiz import render_quiz
        return render_quiz(
            track_id=TRACK_ID, lesson_id=lesson_id,
            questions=lesson["quiz"], label="Knowledge check",
        )

    if lesson.get("challenge"):
        ch = lesson["challenge"]
        return render_graded_challenge(
            track_id=TRACK_ID, lesson_id=lesson_id,
            scenario=ch["scenario"], broken_example=ch.get("setup", ""),
            rubric=ch["rubric"], model_answer=ch["model_answer"],
            hints=ch["hints"], input_label="Your response",
            max_chars=400,
        )

    st.info("Content coming soon.", icon="🔜")
    return False
