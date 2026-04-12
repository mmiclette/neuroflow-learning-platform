# tracks/track1.py
# Track 1 — AI Fundamentals
# 3 lessons, Foundation level, no API calls.

import streamlit as st
from utils.quiz import render_quiz
from utils.session import complete_lesson, is_lesson_complete


# ---------------------------------------------------------------------------
# Lesson content
# ---------------------------------------------------------------------------

LESSONS = {
    1: {
        "concept": """
Artificial intelligence is a broad term for computer systems that perform tasks that would
otherwise require human judgment. The word "AI" gets applied to everything from a spam filter
to a diagnostic imaging system to Claude, which creates confusion about what any given AI
system can actually do. The clearest way to cut through that confusion is to understand five
major types — in order from most concrete to most specific.

**Symbolic AI** is the oldest and most intuitive form. A symbolic AI system follows explicit
rules that a human wrote. If this condition is true, do that. There is no learning — the
system only does exactly what its rules specify, nothing more.

NeuroFlow uses symbolic AI today. The logic that determines which content a patient receives,
which assessment to deliver next, and when to trigger a clinical alert is rule-based. A
clinician or product team defined those rules and the system executes them. This makes
symbolic AI predictable and auditable — you can always trace an output back to the rule
that produced it. The limitation is brittleness: if a situation arises that no rule covers,
the system cannot adapt.

**Statistical machine learning** takes a different approach. Instead of following rules, an
ML model learns from examples. A developer provides a large dataset of past cases with known
outcomes, and the model identifies statistical patterns that connect inputs to those outcomes.
When it encounters a new case, it applies those learned patterns to generate a prediction.

BHIQ uses statistical ML. The risk stratification models were trained on historical behavioral
health data — assessment scores, utilization patterns, diagnosis codes — paired with known
outcomes. The model learned which combinations of factors are statistically associated with
higher risk.

**Deep learning** is a type of machine learning that uses neural networks — computational
structures with many processing layers that can learn highly complex patterns. Medical imaging
analysis — detecting abnormalities in radiology scans — is a deep learning application.
Deep learning is also the foundation that large language models are built on.

**Generative AI** is AI that creates new content rather than classifying inputs or predicting
outcomes. The content it produces can be text, images, video, audio, or code — depending on
what the model was trained on. DALL-E generates images. Sora generates video. These are all
generative AI systems, and none of them are language models.

**Large language models (LLMs)** are a specific type of generative AI trained on text. They
understand language, follow instructions, reason through problems, and generate fluent written
output. Claude, GPT-5, Gemini, and Llama are all LLMs. Every LLM is a generative AI system
built on deep learning, but most generative AI systems are not LLMs.

This distinction matters for NeuroFlow staff when explaining what Claude can and cannot do —
Claude is an LLM and cannot generate images or video natively — and when discussing AI with
technically literate partners, where conflating these terms signals imprecision.

Across all five types, human oversight remains essential. An ML model's risk score informs
a clinical decision; it does not make it. An LLM's drafted policy brief requires review before
submission. The role of human judgment shifts from generating the analysis to reviewing,
interpreting, and acting on AI outputs.
""",
        "quiz": [
            {
                "question": (
                    "NeuroFlow's logic for determining which assessment to deliver to a "
                    "patient is based on criteria a clinical team defined — if PHQ-9 score "
                    "exceeds a threshold, trigger the next step. No data training was involved. "
                    "Which type of AI does this describe?"
                ),
                "options": [
                    "Statistical machine learning",
                    "Deep learning",
                    "Symbolic / rule-based AI",
                    "Generative AI",
                ],
                "correct_index": 2,
                "hint": "Think about whether this system learned from data or follows rules a human wrote.",
            },
            {
                "question": (
                    "BHIQ's risk stratification model was trained on historical patient data "
                    "with known outcomes. When a new patient's data is entered, it generates "
                    "a risk score. Which type of AI does this describe?"
                ),
                "options": [
                    "Symbolic AI — it follows rules a clinician wrote",
                    "Generative AI — it produces new content from training data",
                    "Statistical machine learning — it learned patterns from labeled historical data to predict outcomes on new patients",
                    "Large language model — it processes language to generate responses",
                ],
                "correct_index": 2,
                "hint": "BHIQ generates a prediction by applying patterns learned from historical data.",
            },
        ],
    },
    2: {
        "concept": """
Machine learning is the AI paradigm most directly relevant to NeuroFlow's analytics products.
Understanding how these models work, what they learn from, and where they fail makes staff more
effective when explaining BHIQ to health system and payer audiences.

**How machine learning works**

An ML model learns from examples. A developer does not write rules that say "if X then Y."
They provide the model with a large dataset of inputs paired with known outcomes, and the model
identifies statistical patterns connecting the two. Once trained, the model applies those patterns
to new inputs it has never seen to generate predictions.

**Three core ML approaches**

**Supervised learning** trains on labeled data — historical cases where the correct outcome is
already known. A behavioral health risk model is trained on thousands of patient records where
the actual outcome (hospitalization, deterioration, disengagement) is documented. The model
learns which input combinations are associated with which outcomes. BHIQ uses supervised learning.

**Unsupervised learning** trains on unlabeled data to find natural structure. A population
segmentation model might cluster patients into groups based on behavioral health patterns without
being told in advance what the groups should be.

**Reinforcement learning** trains a model through feedback — rewarding desired behaviors and
penalizing undesired ones. This is how many AI systems that play games or optimize processes
are trained.

**Where ML models fail**

Understanding failure modes helps staff set appropriate expectations with partners.

**Overfitting** occurs when a model learns the training data too well — it memorizes specific
examples rather than general patterns — and performs poorly on new data.

**Distribution shift** occurs when the population the model is deployed on differs
meaningfully from the population it was trained on. A risk model trained on commercial
insurance claims may underperform when applied to a Medicaid population with different
care patterns, documentation practices, and social determinants of health.

**Data poisoning** involves adversarial manipulation of training data. Less common in
healthcare ML but relevant for any system where data inputs are not tightly controlled.

**Explainability gaps** occur when a model's reasoning cannot be traced back to
interpretable factors. This creates challenges for clinical adoption — "the model said so"
is not sufficient justification for a clinical decision.

NeuroFlow's position spans both symbolic AI (rule-based logic in the platform) and
statistical ML (BHIQ risk stratification). Being able to describe the difference accurately
is a meaningful differentiator in health system and federal partner conversations.
""",
        "quiz": [
            {
                "question": (
                    "BHIQ was originally trained on behavioral health data from a large commercial "
                    "insurer. A health system now wants to deploy it with their Medicaid population. "
                    "The model's accuracy is lower than expected on this population. "
                    "What ML failure mode does this describe?"
                ),
                "options": [
                    "Overfitting — the model memorized training data",
                    "Data poisoning — someone altered the training data",
                    "Explainability failure — the model's reasoning cannot be traced",
                    "Distribution shift — the model was trained on a different population than it is now being applied to",
                ],
                "correct_index": 3,
                "hint": "Think about whether the deployment population matches the training population.",
            },
            {
                "question": (
                    "What is the key distinction between how a symbolic AI system and a "
                    "statistical ML model arrive at an output?"
                ),
                "options": [
                    "Symbolic AI follows explicit rules a human defined; ML identifies patterns in historical data and applies them to new cases",
                    "Symbolic AI is more accurate; ML is faster",
                    "ML systems always require more data than symbolic systems to function",
                    "Symbolic AI can only be used for simple tasks; ML is required for complex ones",
                ],
                "correct_index": 0,
                "hint": "One system uses human-defined rules; the other learns patterns from data.",
            },
        ],
    },
    3: {
        "concept": """
Natural language processing (NLP) is the branch of AI focused on understanding, interpreting,
and generating human language. It is the field that produced large language models. Understanding
NLP grounds the rest of this program in something more substantial than "here is how to use
a chatbot."

**The evolution of NLP**

Early NLP systems used rules. To detect depression in a clinical note, a developer might write:
if the note contains "depressed," "hopeless," or "PHQ-9," flag it. This worked until language
varied in ways the rules did not anticipate.

Statistical NLP improved on this by learning patterns from labeled text data rather than coding
rules manually. Early text classification, sentiment analysis, and named entity recognition
systems used these methods.

Unlike earlier rule-based systems that relied on hand-coded linguistic patterns, or
statistical models that treated words as isolated counts, transformers build contextual
representations of meaning — the same word carries different weight depending on everything
around it. At sufficient scale, these models gain capabilities that earlier approaches could
not: understanding long documents, generating coherent multi-paragraph text, following complex
instructions, and reasoning across domains.

**NLP, LLMs, and small language models**

These three terms describe related but distinct technologies. Understanding the differences
explains why Claude behaves so differently from the AI already embedded in EHR systems and
screening tools.

| | Traditional NLP | Large language models (LLMs) | Small language models (SLMs) |
|---|---|---|---|
| **How it works** | Hand-coded rules or statistical pattern matching on text | Transformer neural network trained on massive general corpora | Transformer architecture, smaller parameter count, often fine-tuned on domain-specific data |
| **Examples** | EHR symptom extractors, ICD code mappers, clinical text parsers | Claude, GPT-4, Gemini | Phi-3, Mistral 7B, BioMedLM |
| **Strengths** | Fast, predictable, explainable, low cost | General reasoning, instruction following, long context, generation | Fast inference, lower cost, deployable on-premise, fine-tunable for specific domains |
| **Limitations** | Brittle — breaks on unfamiliar phrasing; no generation capability | High compute cost, cloud dependency, general rather than specialized | Less capable on open-ended tasks; requires fine-tuning investment for best results |

The symptom detection diagram above shows traditional NLP at work — rules and lexicons mapping
clinical phrases to standardized codes. It is fast and reliable for that narrow task, but it
cannot explain a regulatory change, draft a BD brief, or reason across multiple documents.
That is the domain where LLMs like Claude operate.

SLMs are worth knowing because they represent the direction healthcare AI is heading for
embedded, real-time, or PHI-sensitive applications where cloud dependency is a constraint.

**What NLP is used for in healthcare**

**Clinical documentation** — extracting structured information from unstructured clinical
notes. Identifying diagnoses, medications, symptoms, and risk factors from free text clinicians
write rather than structured fields they fill in.

**Measurement and screening** — processing patient-reported text to identify clinical signals
that structured assessments might miss.

**Prior authorization and coding** — automating identification of relevant diagnosis codes
and clinical justifications from documentation.

**NeuroFlow's position in this ecosystem**

NeuroFlow spans three types of AI in its current product portfolio:

- **Symbolic AI** — the rule-based logic in the BHL and BHIQ platforms that controls assessment delivery, content sequencing, and clinical alerts
- **Statistical ML** — the BHIQ risk stratification models trained on behavioral health outcomes data
- **LLMs** — Claude Teams, used internally for staff productivity across BD, product, policy, and clinical operations

Being able to describe those accurately — and to distinguish BHIQ's ML capabilities from
Claude's generative AI capabilities — is a meaningful differentiator in health system and
federal partner conversations.

The constant across all AI types: **human oversight remains essential.** A risk score informs
a clinical decision; it does not make it. A drafted policy brief requires review before
submission. The role of human judgment does not disappear with AI — it shifts.
""",
        "quiz": [
            {
                "question": (
                    "A health system partner asks whether BHIQ uses 'the same kind of AI "
                    "as Claude.' What is the most accurate response?"
                ),
                "options": [
                    "Yes — all modern AI products use the same underlying technology",
                    "No — BHIQ uses statistical machine learning trained on behavioral health outcomes data to generate risk scores; Claude is a large language model that processes and generates text. They are different types of AI with different capabilities and appropriate uses",
                    "Yes — both products use neural networks so they work the same way",
                    "No — BHIQ does not use AI, it uses analytics",
                ],
                "correct_index": 1,
                "hint": "Think about whether BHIQ and Claude were trained on the same kind of data for the same kind of task.",
            },
            {
                "question": (
                    "A clinical director says 'I don't want a computer making decisions "
                    "about my patients.' What is the most accurate and constructive response?"
                ),
                "options": [
                    "AI models are more accurate than clinicians so the concern is misplaced",
                    "The concern only applies to generative AI, not to predictive models like BHIQ",
                    "Regulatory requirements will eventually require AI adoption regardless of provider preference",
                    "You are raising the right concern — none of these tools are designed to replace clinical judgment. A risk model generates a score that helps you prioritize which patients to reach out to first. The clinical decision remains entirely yours",
                ],
                "correct_index": 3,
                "hint": "What does the risk model actually produce, and who makes the final decision?",
            },
        ],
    },
}


# ---------------------------------------------------------------------------
# Render function
# ---------------------------------------------------------------------------

def render_lesson(lesson_id: int) -> bool:
    """
    Render Track 1 lesson content. Returns True when the lesson is complete.
    """
    lesson = LESSONS.get(lesson_id)
    if not lesson:
        st.error(f"Lesson 1.{lesson_id} not found.")
        return False

    track_id = 1

    # Already complete — still show content, skip quiz
    already_done = is_lesson_complete(track_id, lesson_id)

    # Concept brief
    st.markdown(lesson["concept"])

    st.markdown("---")

    # Quiz
    if already_done:
        st.success("✓  Lesson complete")
        return True

    quiz_passed = render_quiz(
        track_id=track_id,
        lesson_id=lesson_id,
        questions=lesson["quiz"],
        label="Concept check",
    )

    return quiz_passed
