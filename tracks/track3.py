# tracks/track3.py — Track 3: Prompt Engineering, 8 lessons

import streamlit as st
from utils.quiz import render_quiz
from utils.challenge import render_graded_challenge
from utils.sandbox import render_comparison_sandbox, render_sandbox
from utils.session import is_lesson_complete, complete_lesson

TRACK_ID = 3

LESSONS = {
    1: {
        "concept": """
Most underwhelming Claude outputs trace back to one problem: the prompt did not give
Claude enough information to know what a good answer looks like. The RTCFC framework is
a checklist for the five things Claude needs.

**Role** — Who should Claude be for this task? A role focuses the model on the right domain
vocabulary. "You are a senior federal health policy analyst" produces a meaningfully different
answer than no role at all. Roles work best when they describe relevant expertise, not just a job title.

**Task** — What exactly should Claude produce? "Write a 500-word blog post arguing that
measurement-based care is a prerequisite for value-based contracts" is a task. "Write
something about MBC" is not.

**Context** — What does Claude need to know to do this well? Include the audience, purpose,
relevant background, and any NeuroFlow-specific information Claude does not have by default.

**Format** — How should the output be structured? Table, numbered list, JSON, prose paragraphs,
specific sections with headers. If you do not specify, Claude picks — and its pick may not
match what you need.

**Constraints** — What should Claude avoid, limit, or require? Word count, tone, sources to
exclude, things that must not appear.

You do not need all five in every prompt. A simple task might need only Task and Constraints.
The skill is diagnosing which components are absent — not adding all five by default.

**Worked example**

Weak prompt: `Write a blog post about measurement-based care.`

Strong RTCFC prompt:
```
[ROLE] You are a healthcare writer with expertise in value-based care and behavioral health policy.
[TASK] Write a 500-word blog post arguing that measurement-based care is a foundational requirement
for any behavioral health value-based contract.
[CONTEXT] The audience is health plan medical directors and CMOs who understand value-based care
in primary care but are skeptical of its applicability in behavioral health.
[FORMAT] Three sections: the problem with unmeasured care, how MBC solves it, and what health plans
should require from behavioral health partners. No headers — flowing prose.
[CONSTRAINTS] Avoid clinical jargon. Do not mention specific vendors or products. End with a single,
direct call to action.
```
""",
        "sandbox": {
            "type": "comparison",
            "weak_prompt": "Write a blog post about measurement-based care.",
            "instruction": (
                "The starting prompt is missing four of five RTCFC components. "
                "Add Role, Context, Format, and Constraints in the box below. "
                "Click **Run both** to see how your improved version compares "
                "to what the weak prompt produces."
            ),
        },
    },
    2: {
        "concept": """
Claude takes the shortest path to satisfying your request. If the request is vague, the
shortest path is a generic response. Specificity means telling Claude exactly what a good
output looks like before it starts writing.

**What specificity means in practice**

Name the exact deliverable. "A 500-word blog post" is specific. "Something for our website" is not.
Name the audience. "Health system CFOs focused on total cost of care" is specific. "Healthcare people" is not.
Name the outcome. "An argument for why MBC is a prerequisite for value-based contracts" is specific.

**Format is part of specificity**

If you do not tell Claude the structure, it guesses. If you want a table, ask for a table.

| Weak prompt | What is missing | Better prompt |
|---|---|---|
| Write a blog post about MBC. | Audience, argument, length, format | Write a 500-word blog post for health plan CMOs arguing MBC is a prerequisite for value-based behavioral health contracts. |
| Summarize this document. | Audience, length, structure | Summarize in three bullets under 25 words each for a non-clinical executive audience. |

**The test:** If you handed your prompt to a capable colleague with no other context, would
they produce the same deliverable you have in mind? If not, the prompt needs more specificity.
""",
        "challenge": {
            "single_attempt": True,
            "scenario": (
                "Your manager asks you to use Claude to draft outreach to health system CFOs "
                "about NeuroFlow's BHIQ analytics product.\n\n"
                "**Task:** Write a complete prompt — not the email itself — that would produce "
                "a single high-quality outreach email. Your prompt must include all five components:\n\n"
                "- **Role** — who should Claude be for this task (e.g. a specific type of expert)\n"
                "- **Task** — the exact deliverable Claude should produce\n"
                "- **Context** — what Claude needs to know about the audience or situation\n"
                "- **Format** — how the output should be structured (length, sections, etc.)\n"
                "- **Constraints** — what Claude should avoid, limit, or require"
            ),
            "broken_example": "",
            "rubric": (
                "Evaluate the prompt against five criteria (20 points each):\n"
                "1. Role defined with relevant expertise\n"
                "2. Task specifies exact deliverable: outreach email to a health system CFO about BHIQ\n"
                "3. Context names at least one specific CFO concern (total cost of care, ROI, quality metrics, or similar)\n"
                "4. Format includes at least one length element (word count, paragraphs, or sentence limit)\n"
                "5. Constraints name at least one specific prohibition"
            ),
            "model_answer": (
                "[ROLE] You are a healthcare sales strategist with expertise in value-based care.\n"
                "[TASK] Write a cold outreach email to a health system CFO introducing NeuroFlow's BHIQ.\n"
                "[CONTEXT] The CFO is focused on reducing total cost of care and demonstrating ROI.\n"
                "[FORMAT] Include a subject line. Body is 150-200 words.\n"
                "[CONSTRAINTS] Do not use clinical jargon."
            ),
            "hints": [
                "Your prompt needs a defined Role — who should Claude be for this task?",
                "Check your Context: does it name a specific concern this CFO actually has?",
                "Your Constraints should name at least one specific thing Claude should NOT do.",
            ],
        },
    },
    3: {
        "concept": """
Describing what you want and showing Claude what you want are two different prompts. For tasks
where output consistency matters, providing one to three examples of the desired output is
more reliable than any description.

This technique is called few-shot prompting. You include example input/output pairs directly
inside your prompt. Claude reads the examples, identifies the pattern, and replicates it.

**When examples help most**

- Recurring structured outputs where every instance must follow the same format
- Tone or voice that is difficult to specify in words alone
- Cases where Claude's default format is plausible but wrong

**When examples add noise**

- Simple one-off tasks where Claude's format judgment is appropriate
- Tasks where you want Claude to apply its own judgment rather than replicate a fixed pattern

**How to format examples in a prompt**

Wrap examples in XML tags so Claude distinguishes them from instructions:

```
[TASK] Write a one-sentence value proposition for the payer audience below.

<examples>
<example>
Payer: Medicare Advantage plan focused on reducing total cost of care
Value prop: BHIQ identifies high-risk behavioral health members before avoidable
utilization, enabling care teams to intervene earlier and reduce total cost of care.
</example>
</examples>

Now write a value proposition for:
Payer: Commercial insurer launching a value-based behavioral health contract.
```

**The diversity rule:** If two examples share a structural quirk, Claude will treat that
quirk as a requirement. Include examples that vary in structure while converging on the
format or tone that matters.
""",
        "quiz": [
            {
                "question": (
                    "A BD team member wants every value proposition Claude produces for health "
                    "system audiences to end with a sentence referencing total cost of care impact. "
                    "They have a detailed RTCFC prompt but Claude keeps ending with quality-metric "
                    "language. What addition would most reliably fix this?"
                ),
                "options": [
                    "Add a constraint: 'Always end with a sentence about total cost of care impact.'",
                    "Provide one or two example value propositions that end with a total cost of care sentence, showing Claude the pattern directly",
                    "Add a stronger Role that emphasizes financial expertise over clinical knowledge",
                    "Switch to a stepped prompt that produces the ending sentence in a separate step",
                ],
                "correct_index": 1,
                "hint": "For format-consistency tasks, showing Claude the pattern is more reliable than naming the rule.",
            },
            {
                "question": (
                    "You provide three examples to help Claude produce a consistent partner briefing "
                    "format. All three examples start with 'The partner's primary concern is...' and "
                    "end with a recommended action. Claude follows that structure exactly, but the "
                    "quality of the middle sections varies. What does this tell you?"
                ),
                "options": [
                    "The examples are working — they taught the structural pattern. Quality variation in the middle sections means the examples need more variety there",
                    "Few-shot prompting only controls format, not content quality — you need a different technique",
                    "The examples are too similar and Claude is picking up unintended patterns throughout",
                    "Three examples are too many — reduce to one to give Claude more flexibility",
                ],
                "correct_index": 0,
                "hint": "The examples did their job — the issue is in what the examples showed for the middle sections.",
            },
        ],
    },
    4: {
        "concept": """
Claude handles focused tasks better than sprawling ones. A prompt asking Claude to read a
document, extract themes, write three audience versions, and format them for email will
produce mediocre results across all four tasks. The same work broken into sequential prompts
produces strong outputs at each step.

**When steps help**

- The task has more than two distinct phases
- The output of one phase shapes the next
- You need to review intermediate outputs before proceeding

**Single prompt (weak):**
```
See our product positioning attached. Write an email campaign for BHIQ for health systems.
```

**Stepped approach (strong):**
```
Step 1: Review the attached product positioning for BHIQ.
Step 2: Write a 4-sentence positioning statement for a health system audience.
Step 3: Identify 3 key value propositions for health system CFOs.
Step 4: Draft subject lines for a 3-part email sequence.
Step 5: Write body copy for each email (150-200 words each), highlighting a distinct value proposition.
```

Each step produces output you can evaluate and correct before moving forward.

**Planning tasks require analysis before writing.** If your first step in a planning task
is to write something, the steps are probably in the wrong order.
""",
        "sandbox": {
            "type": "standard",
            "starter_prompt": (
                "Write a competitive analysis of NeuroFlow versus other "
                "behavioral health technology platforms."
            ),
            "instruction": (
                "This single prompt will produce a shallow, generic output. "
                "Rewrite it as a 4-to-6-step sequential prompt where each step "
                "produces output the next step builds on. Submit your stepped "
                "version to see what Haiku produces."
            ),
        },
        "quiz": [
            {
                "question": (
                    "You asked Claude to write a partner brief and the result is accurate but far "
                    "too formal and long. Which follow-up instruction is most likely to produce "
                    "a useful revision?"
                ),
                "options": [
                    "Make this better",
                    "This doesn't sound right, please fix it",
                    "Cut to 200 words and rewrite in a direct, conversational tone",
                    "Try again",
                ],
                "correct_index": 2,
                "hint": "Effective feedback is specific and testable — it names the exact change to make.",
            },
            {
                "question": (
                    "You have been refining a Claude response across six turns and it still is not "
                    "working — the structure is fundamentally wrong for your purpose. What is the "
                    "most effective next step?"
                ),
                "options": [
                    "Continue adding more constraints to the current response until it improves",
                    "Switch to Opus, which will produce a better result on the same conversation",
                    "Start a new conversation with a corrected prompt — refinement of a structurally wrong response is less effective than starting fresh",
                    "Ask Claude to explain what went wrong before trying again",
                ],
                "correct_index": 2,
                "hint": "Refinement compounds a structural problem — a fresh start with a corrected prompt is faster.",
            },
        ],
    },
    5: {
        "concept": """
Meta-prompting means using Claude to help you design better prompts rather than writing
every instruction from scratch yourself.

**Five methods**

**Prompt creation** — give Claude the goal and ask it to write the prompt:
```
Write a prompt that would instruct Claude to generate a tailored value proposition
for a Medicare Advantage plan considering NeuroFlow's BHIQ product.
Include a defined role, specific goal, output format, and constraints around citation.
```

**Prompt analysis** — give Claude a draft prompt and ask what is wrong:
```
Review this prompt. Explain how you would interpret it, identify anything unclear,
and suggest what should be added to make outputs more consistent.
```

**Prompt refinement** — run the prompt, show Claude the output, ask what caused the problem:
```
This prompt produced the attached output, which is too generic.
Which part of the prompt caused this, and what would fix it?
```

**Parameter exploration** — ask Claude what variables matter for a task:
```
I want to generate tailored implementation briefs for behavioral health technology partners.
What variables should I capture about each partner to make the briefs most relevant?
```

**Automated iteration** — ask Claude to produce multiple variants for different audiences:
```
Write three versions of this prompt optimized for:
(1) a health system CFO audience, (2) a clinical medical director, (3) a state Medicaid director.
```

Meta-prompting is most valuable for prompts you will use repeatedly. It is less useful
for one-off tasks where writing the prompt yourself is faster than explaining what you need.
""",
        "quiz": [
            {
                "question": (
                    "Your team has written draft Project instructions for a value proposition "
                    "generator. You want to find gaps before the team starts using it. "
                    "Which meta-prompting method should you use?"
                ),
                "options": [
                    "Parameter exploration — ask Claude what the instructions should include",
                    "Automated iteration — ask Claude to produce multiple versions",
                    "Prompt analysis — paste your draft instructions and ask Claude how it interprets them, what is unclear, and what is missing",
                    "Prompt creation — ask Claude to write the instructions from scratch",
                ],
                "correct_index": 2,
                "hint": "You have a draft and want to find what is wrong with it — which method is designed for that?",
            },
        ],
    },
    6: {
        "concept": """
Chain-of-thought (CoT) prompting asks Claude to work through a problem step by step before
producing an answer. On tasks involving logic, trade-offs, or multi-factor analysis, CoT
produces more accurate and defensible outputs than asking Claude to answer directly.

**When CoT helps**

- Analyzing a policy document for compliance implications
- Comparing multiple options against a set of criteria
- Working through a decision with competing considerations
- Any task where reasoning quality matters more than speed

**When CoT adds noise**

- Simple factual questions
- Formatting or conversion tasks
- Short drafting tasks where you want the output, not the reasoning

**How to invoke it**

For complex tasks:
```
Before producing your recommendation, reason through the key considerations and trade-offs explicitly.
```

For simpler tasks:
```
Think through this step by step before answering.
```

The first form is stronger — it names the content of the reasoning and links it to the output.
""",
        "quiz": [
            {
                "question": (
                    "You need Claude to evaluate whether NeuroFlow should pursue a partnership "
                    "with a regional health system. The decision involves contract terms, market "
                    "access, resource requirements, and strategic fit. Which prompt approach "
                    "produces the most useful output?"
                ),
                "options": [
                    "Should NeuroFlow partner with this health system?",
                    "Think through this step by step. Consider: the contract terms and financial implications, the market access this partnership opens, the internal resources required, and how it fits our current strategic priorities. Then provide a structured recommendation.",
                    "List the pros and cons of this partnership",
                    "What do you think about this partnership opportunity?",
                ],
                "correct_index": 1,
                "hint": "Name the specific considerations you want Claude to reason through before it concludes.",
            },
            {
                "question": (
                    "You ask Claude: 'What is the PHQ-9 cutoff score for moderate depression?' "
                    "Would chain-of-thought prompting help here?"
                ),
                "options": [
                    "Yes — CoT always improves output quality regardless of task type",
                    "No — this is a simple factual question that does not require step-by-step reasoning; adding CoT would produce unnecessary output without improving accuracy",
                    "Yes — medical questions always benefit from CoT to ensure accuracy",
                    "No — CoT only works for coding tasks",
                ],
                "correct_index": 1,
                "hint": "Match the prompting technique to the task complexity.",
            },
        ],
    },
    7: {
        "concept": """
When Claude produces a bad output, the cause is almost always in the prompt. Five failure
patterns account for most cases:

**Too generic** — no specificity in task or context. Fix: add criteria, audience, and an example.

**Too complex** — multiple deliverables in one prompt. Fix: break into separate focused prompts.

**Missing key points** — Claude omitted something the prompt did not require. Fix: list what must be present.

**Wrong length** — output is too long or too short. Fix: specify word count, items, or sections.

**Off-topic or unfocused** — Claude addressed a related but different question. Fix: state the core focus explicitly and add a constraint ruling out adjacent topics.

**The diagnostic question:** If you handed this prompt to a capable new employee with no other context, would they produce the exact deliverable you have in mind? If not, find which component is missing.

| Weak feedback | Strong feedback |
|---|---|
| Make this more concise | Cut to 150 words by removing the second and fourth paragraphs |
| This doesn't sound right | Rewrite as a direct Slack message — conversational, no formal language |
| Add more detail | Add a paragraph between sections 2 and 3 explaining how BHIQ integrates with Epic |
""",
        "quiz": [
            {
                "question": (
                    "A team member submitted this prompt: 'Write something about how NeuroFlow "
                    "helps ACOs and also explain what ACOs are and how MBC fits in and what our "
                    "ROI looks like.' Claude produced a disorganized response. Which failure "
                    "pattern does this prompt exhibit?"
                ),
                "options": [
                    "Too generic — no specificity in the task or audience",
                    "Multiple deliverables in one prompt — each distinct output needs its own focused prompt",
                    "Too complex — Claude cannot handle healthcare topics in a single prompt",
                    "Missing constraints — the prompt needs more rules about what to avoid",
                ],
                "correct_index": 1,
                "hint": "Count how many distinct deliverables this prompt is asking for.",
            },
            {
                "question": (
                    "A prompt reads: 'You are an expert. Analyze the attached RFP and tell me "
                    "if we should respond.' The output was vague. What is wrong with the Role "
                    "and Task in this prompt?"
                ),
                "options": [
                    "The Role is too short and the Task is too long",
                    "The Role does not name any relevant expertise domain, and the Task does not specify what criteria should guide the analysis or what format the recommendation should take",
                    "The Role should not be included at all for analysis tasks",
                    "The Task should be split into two separate prompts",
                ],
                "correct_index": 1,
                "hint": "What does 'expert' actually tell Claude about domain, vocabulary, and perspective?",
            },
            {
                "question": (
                    "A policy analyst generates a response that is accurate but three times "
                    "longer than needed. Which follow-up instruction is most effective?"
                ),
                "options": [
                    "Please make this shorter.",
                    "This is too long.",
                    "Cut this to 200 words. Keep the core argument in paragraph 1 and the three supporting points. Remove all other content.",
                    "Summarize the above.",
                ],
                "correct_index": 2,
                "hint": "Effective refinement names the target length and what to keep.",
            },
        ],
    },
    8: {
        "concept": """
This lesson tests your ability to write a complete RTCFC prompt for a complex, real
NeuroFlow use case. The rubric evaluates whether your prompt would produce a high-quality
output if submitted to Claude — not whether it is long, but whether it is complete.

**Review checklist before submitting**

- Does your Role name specific expertise, not just a job title?
- Does your Task name the exact deliverable?
- Does your Context name the audience and at least one thing they care about?
- Does your Format specify structure and length?
- Does your Constraints name at least one specific prohibition?

If any of these are missing, add them before submitting.
""",
        "challenge": {
            "single_attempt": False,
            "scenario": (
                "NeuroFlow is pursuing a contract with a large regional ACO participating in "
                "the ACO REACH program. The ACO's medical director has asked for a one-page "
                "brief explaining how BHIQ's behavioral health risk stratification can help "
                "them close care gaps and hit quality benchmarks.\n\n"
                "**Task:** Write a complete RTCFC prompt that would produce this brief. "
                "Do not write the brief itself — write the prompt."
            ),
            "broken_example": "",
            "rubric": (
                "Score the prompt against five criteria (20 points each):\n\n"
                "1. Role names specific domain expertise (value-based care, behavioral health analytics, ACO operations, or similar) — not just a job title.\n\n"
                "2. Task specifies the exact deliverable: a one-page brief for an ACO medical director about BHIQ risk stratification.\n\n"
                "3. Context names at least one specific audience concern: care gap closure, quality benchmarks, total cost of care, ACO REACH performance, or similar.\n\n"
                "4. Format specifies at least page length and one structural element (sections, headers, bullets, or word count).\n\n"
                "5. Constraints name at least one specific prohibition: no clinical jargon, no unsupported statistics, no competitor mentions, or similar."
            ),
            "model_answer": (
                "[ROLE] You are a healthcare strategy writer with expertise in value-based care, "
                "ACO operations, and behavioral health analytics.\n\n"
                "[TASK] Write a one-page brief for a regional ACO medical director explaining how "
                "NeuroFlow's BHIQ behavioral health risk stratification platform can help the ACO "
                "close behavioral health care gaps and improve ACO REACH quality benchmarks.\n\n"
                "[CONTEXT] The medical director oversees an ACO participating in ACO REACH. Their "
                "priorities are closing care gaps, improving quality metrics, and demonstrating "
                "total cost of care savings to CMS.\n\n"
                "[FORMAT] One page. Three sections: the problem with unidentified behavioral health "
                "risk in ACO populations, how BHIQ identifies that risk before it drives utilization, "
                "and what outcomes ACOs have achieved. End with a two-sentence call to action.\n\n"
                "[CONSTRAINTS] Do not include unverifiable statistics. Do not mention specific "
                "competitors. Do not use clinical jargon — write for a physician executive, not a clinician."
            ),
            "hints": [
                "Your Role should name specific domain expertise — what does this person know about ACOs and behavioral health?",
                "Your Context should name at least one thing the ACO medical director specifically cares about.",
                "Review your Constraints: does your prompt name at least one specific prohibition?",
            ],
        },
    },
}


def render_lesson(lesson_id: int) -> bool:
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        st.error(f"Lesson 3.{lesson_id} not found.")
        return False

    already_done = is_lesson_complete(TRACK_ID, lesson_id)
    st.markdown(lesson["concept"])
    st.markdown("---")

    if already_done:
        st.success("Lesson complete")
        return True

    # 3.1 — comparison sandbox
    if lesson.get("sandbox") and lesson["sandbox"]["type"] == "comparison":
        sb = lesson["sandbox"]
        return render_comparison_sandbox(
            track_id=TRACK_ID, lesson_id=lesson_id,
            weak_prompt=sb["weak_prompt"], instruction=sb["instruction"],
        )

    # 3.2 — single-attempt graded challenge
    if lesson.get("challenge") and lesson["challenge"].get("single_attempt"):
        ch = lesson["challenge"]
        return render_graded_challenge(
            track_id=TRACK_ID, lesson_id=lesson_id,
            scenario=ch["scenario"], broken_example=ch["broken_example"],
            rubric=ch["rubric"], model_answer=ch["model_answer"],
            hints=ch["hints"], input_label="Your prompt", max_chars=600,
            single_attempt=True,
        )

    # 3.4 — standard sandbox then quiz
    if lesson.get("sandbox") and lesson["sandbox"]["type"] == "standard":
        sb = lesson["sandbox"]
        sandbox_done = render_sandbox(
            track_id=TRACK_ID, lesson_id=lesson_id,
            starter_prompt=sb["starter_prompt"], instruction=sb["instruction"],
        )
        if not sandbox_done:
            return False
        if lesson.get("quiz"):
            return render_quiz(
                track_id=TRACK_ID, lesson_id=lesson_id,
                questions=lesson["quiz"], label="Knowledge check",
            )
        return sandbox_done

    # Quiz-only lessons (3.3, 3.5, 3.6, 3.7)
    if lesson.get("quiz") and not lesson.get("challenge"):
        return render_quiz(
            track_id=TRACK_ID, lesson_id=lesson_id,
            questions=lesson["quiz"], label="Knowledge check",
        )

    # Standard graded challenge (3.8)
    if lesson.get("challenge"):
        ch = lesson["challenge"]
        return render_graded_challenge(
            track_id=TRACK_ID, lesson_id=lesson_id,
            scenario=ch["scenario"], broken_example=ch["broken_example"],
            rubric=ch["rubric"], model_answer=ch["model_answer"],
            hints=ch["hints"], input_label="Your prompt", max_chars=700,
            single_attempt=False,
        )

    st.info("Content coming soon.", icon="🔜")
    return False
