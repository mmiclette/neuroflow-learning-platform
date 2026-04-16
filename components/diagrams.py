# components/diagrams.py
# Five SVG diagrams for the NeuroFlow AI Learning Platform.
# All colors are hardcoded NeuroFlow brand hex values.
# Render via: st.components.v1.html(get_diagram("id"), height=N)

DIAGRAMS = {}

# ---------------------------------------------------------------------------
# Lesson 2.1 — Context window
# ---------------------------------------------------------------------------
DIAGRAMS["context_window"] = """
<svg width="100%" viewBox="0 0 680 300" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Context window: what Claude sees</title>
<desc>The 200,000-token context window showing four content types stacked inside — system prompt, uploaded documents, your messages, and Claude's responses — with older content shown above falling out of context.</desc>
<defs>
  <marker id="arrw" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="#BDBDBD" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <clipPath id="win"><rect x="50" y="60" width="445" height="210" rx="8"/></clipPath>
</defs>
<rect x="50" y="12" width="445" height="36" rx="4" fill="#F5F5F5" stroke="#BDBDBD" stroke-width="0.5" stroke-dasharray="4 3"/>
<text x="272" y="30" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#BDBDBD">Older messages — dropped when context overflows</text>
<line x1="272" y1="48" x2="272" y2="58" stroke="#BDBDBD" stroke-width="1" marker-end="url(#arrw)"/>
<rect x="50" y="60" width="445" height="40" clip-path="url(#win)" fill="#E8E9F7"/>
<rect x="50" y="100" width="445" height="60" clip-path="url(#win)" fill="#EBF3FA"/>
<rect x="50" y="160" width="445" height="54" clip-path="url(#win)" fill="#E4F5F3"/>
<rect x="50" y="214" width="445" height="56" clip-path="url(#win)" fill="#E7F6F5"/>
<rect x="50" y="60" width="445" height="210" rx="8" fill="none" stroke="#161BAA" stroke-width="1"/>
<text x="70" y="80" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="500" fill="#161BAA">System prompt</text>
<text x="485" y="80" text-anchor="end" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575">~500 tokens</text>
<text x="70" y="130" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="500" fill="#2A5C8A">Uploaded documents</text>
<text x="485" y="130" text-anchor="end" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575">variable</text>
<text x="70" y="187" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="500" fill="#1A6860">Your messages</text>
<text x="485" y="187" text-anchor="end" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575">grows over time</text>
<text x="70" y="242" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="500" fill="#2A6E68">Claude's responses</text>
<text x="485" y="242" text-anchor="end" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575">grows over time</text>
<path d="M512 60 L522 60 L522 270 L512 270" fill="none" stroke="#161BAA" stroke-width="0.8"/>
<text x="528" y="155" dominant-baseline="central" font-family="sans-serif" font-size="10" font-weight="500" fill="#161BAA">200K</text>
<text x="528" y="169" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#161BAA">token</text>
<text x="528" y="182" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#161BAA">limit</text>
<text x="272" y="291" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#757575">Every message, document, and response counts — start a new conversation when context grows very long</text>
</svg>
"""

# ---------------------------------------------------------------------------
# Lesson 3.1 — RTCFC framework
# ---------------------------------------------------------------------------
DIAGRAMS["rtcfc"] = """
<svg width="100%" viewBox="0 0 680 220" role="img" xmlns="http://www.w3.org/2000/svg">
<title>RTCFC prompt framework</title>
<desc>Five prompt components: Role, Task, Context, Format, Constraints.</desc>
<defs>
  <clipPath id="cr0"><rect x="43" y="40" width="113" height="140" rx="6"/></clipPath>
  <clipPath id="cr1"><rect x="164" y="40" width="113" height="140" rx="6"/></clipPath>
  <clipPath id="cr2"><rect x="285" y="40" width="113" height="140" rx="6"/></clipPath>
  <clipPath id="cr3"><rect x="406" y="40" width="113" height="140" rx="6"/></clipPath>
  <clipPath id="cr4"><rect x="527" y="40" width="113" height="140" rx="6"/></clipPath>
</defs>
<rect x="43" y="40" width="113" height="140" rx="6" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.5"/>
<rect x="43" y="40" width="113" height="44" clip-path="url(#cr0)" fill="#161BAA"/>
<text x="100" y="62" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="13" font-weight="500" fill="#FFFFFF">Role</text>
<text x="100" y="105" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">Who Claude is</text>
<text x="100" y="120" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">acting as for</text>
<text x="100" y="135" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">this task</text>
<rect x="164" y="40" width="113" height="140" rx="6" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.5"/>
<rect x="164" y="40" width="113" height="44" clip-path="url(#cr1)" fill="#2EA799"/>
<text x="221" y="62" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="13" font-weight="500" fill="#FFFFFF">Task</text>
<text x="221" y="105" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">What you are</text>
<text x="221" y="120" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">asking Claude</text>
<text x="221" y="135" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">to do</text>
<rect x="285" y="40" width="113" height="140" rx="6" fill="#EBF3FA" stroke="#478FCC" stroke-width="0.5"/>
<rect x="285" y="40" width="113" height="44" clip-path="url(#cr2)" fill="#478FCC"/>
<text x="342" y="62" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="13" font-weight="500" fill="#FFFFFF">Context</text>
<text x="342" y="105" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">Information</text>
<text x="342" y="120" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">Claude needs to</text>
<text x="342" y="135" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">perform the task</text>
<rect x="406" y="40" width="113" height="140" rx="6" fill="#E7F6F5" stroke="#4CB8AC" stroke-width="0.5"/>
<rect x="406" y="40" width="113" height="44" clip-path="url(#cr3)" fill="#4CB8AC"/>
<text x="463" y="62" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="13" font-weight="500" fill="#FFFFFF">Format</text>
<text x="463" y="105" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">Structure, tone,</text>
<text x="463" y="120" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">and length of</text>
<text x="463" y="135" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">the output</text>
<rect x="527" y="40" width="113" height="140" rx="6" fill="#ECEDF9" stroke="#3B42C4" stroke-width="0.5"/>
<rect x="527" y="40" width="113" height="44" clip-path="url(#cr4)" fill="#3B42C4"/>
<text x="584" y="62" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="500" fill="#FFFFFF">Constraints</text>
<text x="584" y="105" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">What to avoid</text>
<text x="584" y="120" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#212121">or exclude</text>
<text x="340" y="202" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#757575">Use only what the task actually needs — not all five by default</text>
</svg>
"""

# ---------------------------------------------------------------------------
# Lesson 5.3 — Connector ecosystem
# ---------------------------------------------------------------------------
DIAGRAMS["connector_ecosystem"] = """
<svg width="100%" viewBox="0 0 680 360" role="img" xmlns="http://www.w3.org/2000/svg">
<title>NeuroFlow's active MCP connections</title>
<desc>Hub and spoke: Claude Teams at center connected to Slack, Google Drive, HubSpot, Atlassian, Asana, Gmail, and Google Calendar via MCP.</desc>
<text x="340" y="22" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="500" fill="#161BAA">NeuroFlow's active MCP connections</text>
<line x1="340" y1="192" x2="340" y2="83" stroke="#2EA799" stroke-width="0.8"/>
<line x1="340" y1="192" x2="442" y2="114" stroke="#2EA799" stroke-width="0.8"/>
<line x1="340" y1="192" x2="467" y2="222" stroke="#2EA799" stroke-width="0.8"/>
<line x1="340" y1="192" x2="397" y2="298" stroke="#2EA799" stroke-width="0.8"/>
<line x1="340" y1="192" x2="284" y2="298" stroke="#2EA799" stroke-width="0.8"/>
<line x1="340" y1="192" x2="214" y2="222" stroke="#2EA799" stroke-width="0.8"/>
<line x1="340" y1="192" x2="239" y2="114" stroke="#2EA799" stroke-width="0.8"/>
<circle cx="340" cy="192" r="42" fill="#161BAA"/>
<text x="340" y="192" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="13" font-weight="500" fill="#FFFFFF">Claude</text>
<rect x="299" y="47" width="82" height="36" rx="4" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.5"/>
<text x="340" y="65" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="500" fill="#1A6860">Slack</text>
<rect x="401" y="92" width="82" height="44" rx="4" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.5"/>
<text x="442" y="109" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="500" fill="#1A6860">Google</text>
<text x="442" y="124" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="500" fill="#1A6860">Drive</text>
<rect x="426" y="204" width="82" height="36" rx="4" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.5"/>
<text x="467" y="222" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="500" fill="#1A6860">HubSpot</text>
<rect x="356" y="280" width="82" height="36" rx="4" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.5"/>
<text x="397" y="298" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="500" fill="#1A6860">Atlassian</text>
<rect x="243" y="280" width="82" height="36" rx="4" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.5"/>
<text x="284" y="298" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="500" fill="#1A6860">Asana</text>
<rect x="172" y="204" width="82" height="36" rx="4" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.5"/>
<text x="213" y="222" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="500" fill="#1A6860">Gmail</text>
<rect x="198" y="92" width="82" height="44" rx="4" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.5"/>
<text x="239" y="109" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="500" fill="#1A6860">Google</text>
<text x="239" y="124" text-anchor="middle" font-family="sans-serif" font-size="11" font-weight="500" fill="#1A6860">Calendar</text>
<text x="340" y="350" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#757575">All connections support read and write — enable only what your task requires</text>
</svg>
"""

# ---------------------------------------------------------------------------
# Lesson 7.3 — Project structure
# ---------------------------------------------------------------------------
DIAGRAMS["project_structure"] = """
<svg width="100%" viewBox="0 0 680 235" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Claude Code project structure</title>
<desc>Annotated directory tree showing CLAUDE.md, .claude/ with settings.json and commands/, and .mcp.json.</desc>
<line x1="60" y1="50" x2="60" y2="193" stroke="#BDBDBD" stroke-width="0.8"/>
<line x1="60" y1="72" x2="78" y2="72" stroke="#BDBDBD" stroke-width="0.8"/>
<line x1="60" y1="104" x2="78" y2="104" stroke="#BDBDBD" stroke-width="0.8"/>
<line x1="60" y1="193" x2="60" y2="200" stroke="#BDBDBD" stroke-width="0.8"/>
<line x1="60" y1="200" x2="78" y2="200" stroke="#BDBDBD" stroke-width="0.8"/>
<line x1="82" y1="115" x2="82" y2="168" stroke="#BDBDBD" stroke-width="0.8"/>
<line x1="82" y1="136" x2="100" y2="136" stroke="#BDBDBD" stroke-width="0.8"/>
<line x1="82" y1="168" x2="100" y2="168" stroke="#BDBDBD" stroke-width="0.8"/>
<text x="48" y="43" font-family="sans-serif" font-size="12" fill="#757575">project-root/</text>
<text x="82" y="72" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="500" fill="#161BAA">CLAUDE.md</text>
<text x="82" y="104" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="500" fill="#478FCC">.claude/</text>
<text x="104" y="136" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="500" fill="#2EA799">settings.json</text>
<text x="104" y="168" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="500" fill="#4CB8AC">commands/</text>
<text x="82" y="200" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="500" fill="#2EA799">.mcp.json</text>
<rect x="250" y="59" width="400" height="26" rx="4" fill="#E8E9F7"/>
<rect x="250" y="59" width="4" height="26" rx="2" fill="#161BAA"/>
<text x="262" y="72" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#161BAA">Claude reads this first — sets context, rules, and behavior</text>
<rect x="250" y="91" width="400" height="26" rx="4" fill="#EBF3FA"/>
<rect x="250" y="91" width="4" height="26" rx="2" fill="#478FCC"/>
<text x="262" y="104" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#2A5C8A">All Claude Code configuration lives here</text>
<rect x="250" y="123" width="400" height="26" rx="4" fill="#E4F5F3"/>
<rect x="250" y="123" width="4" height="26" rx="2" fill="#2EA799"/>
<text x="262" y="136" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#1A6860">Controls which tools Claude can use in this project</text>
<rect x="250" y="155" width="400" height="26" rx="4" fill="#E7F6F5"/>
<rect x="250" y="155" width="4" height="26" rx="2" fill="#4CB8AC"/>
<text x="262" y="168" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#2A6E68">Custom slash commands — /review, /test, /deploy, etc.</text>
<rect x="250" y="187" width="400" height="26" rx="4" fill="#E4F5F3"/>
<rect x="250" y="187" width="4" height="26" rx="2" fill="#2EA799"/>
<text x="262" y="200" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#1A6860">Project-scoped MCP server config — shared via git</text>
</svg>
"""

# ---------------------------------------------------------------------------
# Lesson 8.1 — Agent loop
# ---------------------------------------------------------------------------
DIAGRAMS["agent_loop"] = """
<svg width="100%" viewBox="0 0 680 390" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Agentic loop: task to completion</title>
<desc>Flowchart: task prompt → plan next step → execute tool (with external MCP call) → process result → stop condition check, then either loop back or complete.</desc>
<defs>
  <marker id="al" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="#757575" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <marker id="al2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="#2EA799" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
  <marker id="al3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
    <path d="M2 1L8 5L2 9" fill="none" stroke="#161BAA" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </marker>
</defs>
<line x1="340" y1="76" x2="340" y2="98" stroke="#757575" stroke-width="1" marker-end="url(#al)"/>
<line x1="340" y1="146" x2="340" y2="168" stroke="#757575" stroke-width="1" marker-end="url(#al)"/>
<line x1="340" y1="216" x2="340" y2="238" stroke="#757575" stroke-width="1" marker-end="url(#al)"/>
<line x1="340" y1="286" x2="340" y2="308" stroke="#757575" stroke-width="1" marker-end="url(#al)"/>
<line x1="440" y1="184" x2="460" y2="184" stroke="#2EA799" stroke-width="0.8" marker-end="url(#al2)"/>
<line x1="460" y1="200" x2="440" y2="200" stroke="#2EA799" stroke-width="0.8" marker-end="url(#al2)"/>
<path d="M240,332 L120,332 L120,122 L240,122" fill="none" stroke="#161BAA" stroke-width="1" marker-end="url(#al3)"/>
<line x1="440" y1="332" x2="460" y2="332" stroke="#2EA799" stroke-width="0.8" marker-end="url(#al2)"/>
<rect x="240" y="30" width="200" height="44" rx="6" fill="#161BAA"/>
<text x="340" y="52" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="500" fill="#FFFFFF">Task prompt</text>
<rect x="240" y="100" width="200" height="44" rx="6" fill="#EBF3FA" stroke="#478FCC" stroke-width="0.5"/>
<text x="340" y="122" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="500" fill="#2A5C8A">Plan next step</text>
<rect x="240" y="170" width="200" height="44" rx="6" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.5"/>
<text x="340" y="192" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="500" fill="#1A6860">Execute tool</text>
<rect x="240" y="240" width="200" height="44" rx="6" fill="#EBF3FA" stroke="#478FCC" stroke-width="0.5"/>
<text x="340" y="262" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="500" fill="#2A5C8A">Process result</text>
<rect x="240" y="310" width="200" height="44" rx="6" fill="#F5F5F5" stroke="#BDBDBD" stroke-width="0.5"/>
<text x="340" y="332" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="500" fill="#757575">Stop condition?</text>
<rect x="462" y="170" width="148" height="44" rx="6" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.5"/>
<text x="536" y="188" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#1A6860">External</text>
<text x="536" y="203" text-anchor="middle" font-family="sans-serif" font-size="11" fill="#1A6860">tool / MCP</text>
<rect x="462" y="310" width="148" height="44" rx="6" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.5"/>
<text x="536" y="332" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="500" fill="#1A6860">Task complete</text>
<text x="62" y="228" font-family="sans-serif" font-size="10" fill="#161BAA">Continue</text>
<text x="226" y="364" text-anchor="end" font-family="sans-serif" font-size="10" fill="#757575">No — loop back</text>
<text x="443" y="364" font-family="sans-serif" font-size="10" fill="#757575">Yes — done</text>
</svg>
"""


def get_diagram(diagram_id: str) -> str | None:
    """Return the SVG string for a given diagram ID, wrapped in a basic HTML page."""
    svg = DIAGRAMS.get(diagram_id)
    if not svg:
        return None
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ margin: 0; padding: 8px 0; background: transparent; }}
  svg {{ max-width: 100%; height: auto; display: block; }}
</style>
</head>
<body>{svg}</body>
</html>
"""



# ---------------------------------------------------------------------------
# Lesson 1.2 — Machine learning pipeline
# ---------------------------------------------------------------------------
DIAGRAMS["ml_pipeline"] = """
<svg width="100%" viewBox="0 0 680 280" role="img" xmlns="http://www.w3.org/2000/svg">
<title>How machine learning works</title>
<desc>Three-column pipeline: training data, ML model, prediction</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<rect x="14" y="14" width="186" height="250" rx="8" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.8"/>
<rect x="14" y="14" width="186" height="38" rx="8" fill="#161BAA"/>
<rect x="14" y="38" width="186" height="14" fill="#161BAA"/>
<text x="107" y="35" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="13" font-weight="600" fill="#FFFFFF">Training data</text>
<text x="107" y="72" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#161BAA" font-weight="600">EHR</text>
<text x="107" y="90" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">High signal, messy, real-time</text>
<line x1="30" y1="104" x2="182" y2="104" stroke="#C0C4E8" stroke-width="0.5"/>
<text x="107" y="120" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#161BAA" font-weight="600">Claims</text>
<text x="107" y="138" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">Structured, longitudinal,</text>
<text x="107" y="152" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">complete across systems</text>
<line x1="202" y1="139" x2="238" y2="139" stroke="#888888" stroke-width="1.4" marker-end="url(#arrow)"/>
<rect x="246" y="14" width="188" height="250" rx="8" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.8"/>
<rect x="246" y="14" width="188" height="38" rx="8" fill="#161BAA"/>
<rect x="246" y="38" width="188" height="14" fill="#161BAA"/>
<text x="340" y="35" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="13" font-weight="600" fill="#FFFFFF">ML model</text>
<text x="340" y="68" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575">What the model does</text>
<line x1="262" y1="78" x2="418" y2="78" stroke="#C0C4E8" stroke-width="0.5"/>
<text x="340" y="104" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#161BAA" font-weight="600">Learns patterns</text>
<text x="340" y="120" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">From thousands of labeled examples</text>
<text x="340" y="150" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#161BAA" font-weight="600">Identifies signals</text>
<text x="340" y="166" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">Combinations that predict outcome</text>
<text x="340" y="196" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#161BAA" font-weight="600">Assigns probability</text>
<text x="340" y="212" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">Score for each new patient</text>
<line x1="436" y1="139" x2="470" y2="139" stroke="#888888" stroke-width="1.4" marker-end="url(#arrow)"/>
<rect x="478" y="14" width="188" height="250" rx="8" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.8"/>
<rect x="478" y="14" width="188" height="38" rx="8" fill="#2EA799"/>
<rect x="478" y="38" width="188" height="14" fill="#2EA799"/>
<text x="572" y="35" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="13" font-weight="600" fill="#FFFFFF">Prediction</text>
<text x="572" y="68" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#1A6860">Risk scores for new patients</text>
<line x1="494" y1="78" x2="650" y2="78" stroke="#9ED5D0" stroke-width="0.5"/>
<text x="572" y="100" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#212121">30-day readmission risk</text>
<text x="572" y="118" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#212121">Behavioral health risk score</text>
<text x="572" y="136" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#212121">Crisis / acute care risk</text>
<text x="572" y="154" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#212121">Treatment non-response risk</text>
<text x="572" y="172" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#212121">Engagement / no-show risk</text>
<text x="572" y="204" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="9" fill="#1A6860" font-style="italic">Output: a probability score,</text>
<text x="572" y="218" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="9" fill="#1A6860" font-style="italic">not a diagnosis or decision</text>
</svg>
"""

# ---------------------------------------------------------------------------
# Lesson 5.2 — Plugins by NeuroFlow role
# ---------------------------------------------------------------------------
DIAGRAMS["plugins_by_role"] = """
<svg width="100%" viewBox="0 0 680 280" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Recommended plugins by NeuroFlow role</title>
<rect x="12" y="12" width="310" height="32" rx="4" fill="#161BAA"/>
<text x="167" y="32" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="600" fill="#FFFFFF">Role</text>
<rect x="328" y="12" width="340" height="32" rx="4" fill="#161BAA"/>
<text x="498" y="32" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="600" fill="#FFFFFF">Best plugins</text>
<rect x="12" y="48" width="310" height="36" fill="#F8F9FA" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="24" y="70" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">BD / Sales</text>
<rect x="328" y="48" width="340" height="36" fill="#F8F9FA" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="340" y="62" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">Sales</text>
<text x="340" y="77" font-family="sans-serif" font-size="10" fill="#757575">Deal coaching, outreach generation, pipeline reasoning</text>
<rect x="12" y="84" width="310" height="36" fill="#FFFFFF" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="24" y="106" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">Marketing</text>
<rect x="328" y="84" width="340" height="36" fill="#FFFFFF" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="340" y="98" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">Marketing</text>
<text x="340" y="113" font-family="sans-serif" font-size="10" fill="#757575">Campaign copy, brand voice, content strategy defaults</text>
<rect x="12" y="120" width="310" height="36" fill="#F8F9FA" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="24" y="142" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">Finance</text>
<rect x="328" y="120" width="340" height="36" fill="#F8F9FA" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="340" y="134" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">Data + Finance</text>
<text x="340" y="149" font-family="sans-serif" font-size="10" fill="#757575">Calculations, model outputs, financial analysis defaults</text>
<rect x="12" y="156" width="310" height="36" fill="#FFFFFF" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="24" y="178" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">People Ops</text>
<rect x="328" y="156" width="340" height="36" fill="#FFFFFF" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="340" y="170" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">Productivity</text>
<text x="340" y="185" font-family="sans-serif" font-size="10" fill="#757575">Hiring workflows, policy drafting, task coordination</text>
<rect x="12" y="192" width="310" height="36" fill="#F8F9FA" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="24" y="214" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">Product</text>
<rect x="328" y="192" width="340" height="36" fill="#F8F9FA" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="340" y="206" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">Data + Productivity</text>
<text x="340" y="221" font-family="sans-serif" font-size="10" fill="#757575">Metrics analysis, roadmap planning, spec writing</text>
<rect x="12" y="228" width="310" height="36" fill="#FFFFFF" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="24" y="250" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">Engineering</text>
<rect x="328" y="228" width="340" height="36" fill="#FFFFFF" stroke="#E0E0E0" stroke-width="0.5"/>
<text x="340" y="242" font-family="sans-serif" font-size="11" fill="#212121" font-weight="500">Engineering</text>
<text x="340" y="257" font-family="sans-serif" font-size="10" fill="#757575">Code review, architecture decisions, incident docs</text>
</svg>
"""

# ---------------------------------------------------------------------------
# Lesson 5.4 — Plugin / connector / prompt decision tree
# ---------------------------------------------------------------------------
DIAGRAMS["decision_tree"] = """
<svg width="100%" viewBox="0 0 680 230" role="img" xmlns="http://www.w3.org/2000/svg">
<title>When to use prompt, connector, plugin, or combination</title>
<desc>Four-column chart mapping task type to the right Claude tool</desc>
<rect x="14" y="14" width="152" height="200" rx="8" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.8"/>
<rect x="14" y="14" width="152" height="40" rx="8" fill="#161BAA"/>
<rect x="14" y="40" width="152" height="14" fill="#161BAA"/>
<text x="90" y="35" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="13" font-weight="600" fill="#FFFFFF">Prompt</text>
<text x="90" y="74" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" fill="#161BAA" font-weight="600">Just thinking?</text>
<line x1="28" y1="88" x2="152" y2="88" stroke="#C0C4E8" stroke-width="0.5"/>
<text x="90" y="110" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">All info is already</text>
<text x="90" y="126" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">in the conversation.</text>
<text x="90" y="142" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">Deliverable is text.</text>
<text x="90" y="175" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575" font-style="italic">Drafts, analysis,</text>
<text x="90" y="191" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575" font-style="italic">briefs, summaries</text>
<rect x="180" y="14" width="152" height="200" rx="8" fill="#EBF3FA" stroke="#478FCC" stroke-width="0.8"/>
<rect x="180" y="14" width="152" height="40" rx="8" fill="#478FCC"/>
<rect x="180" y="40" width="152" height="14" fill="#478FCC"/>
<text x="256" y="35" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="13" font-weight="600" fill="#FFFFFF">Connector</text>
<text x="256" y="74" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" fill="#2A5C8A" font-weight="600">Need outside data?</text>
<line x1="194" y1="88" x2="318" y2="88" stroke="#B5D4F4" stroke-width="0.5"/>
<text x="256" y="110" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">Info lives in an</text>
<text x="256" y="126" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">external service.</text>
<text x="256" y="142" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">Claude retrieves it.</text>
<text x="256" y="175" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575" font-style="italic">Gmail, Salesforce,</text>
<text x="256" y="191" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575" font-style="italic">Drive, Monday</text>
<rect x="346" y="14" width="152" height="200" rx="8" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.8"/>
<rect x="346" y="14" width="152" height="40" rx="8" fill="#2EA799"/>
<rect x="346" y="40" width="152" height="14" fill="#2EA799"/>
<text x="422" y="35" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="13" font-weight="600" fill="#FFFFFF">Plugin</text>
<text x="422" y="74" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" fill="#0F6E56" font-weight="600">Need to compute?</text>
<line x1="360" y1="88" x2="484" y2="88" stroke="#9ED5D0" stroke-width="0.5"/>
<text x="422" y="110" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">Task needs execution</text>
<text x="422" y="126" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">beyond text output.</text>
<text x="422" y="142" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">Charts, calculations.</text>
<text x="422" y="175" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575" font-style="italic">Data, Engineering,</text>
<text x="422" y="191" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575" font-style="italic">Sales, Legal</text>
<rect x="512" y="14" width="154" height="200" rx="8" fill="#ECEDF9" stroke="#3B42C4" stroke-width="0.8"/>
<rect x="512" y="14" width="154" height="40" rx="8" fill="#3B42C4"/>
<rect x="512" y="40" width="154" height="14" fill="#3B42C4"/>
<text x="589" y="35" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="600" fill="#FFFFFF">Connector + Plugin</text>
<text x="589" y="74" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" fill="#3B42C4" font-weight="600">Need both?</text>
<line x1="526" y1="88" x2="652" y2="88" stroke="#C0C4E8" stroke-width="0.5"/>
<text x="589" y="110" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">Retrieve data from</text>
<text x="589" y="126" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">outside + execute</text>
<text x="589" y="142" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">on it. Use both.</text>
<text x="589" y="175" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575" font-style="italic">Drive files + chart,</text>
<text x="589" y="191" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575" font-style="italic">CRM data + analysis</text>
</svg>
"""


# ---------------------------------------------------------------------------
# Lesson 3.5 — Meta-prompting
# ---------------------------------------------------------------------------
DIAGRAMS["meta_prompting"] = """
<svg width="100%" viewBox="0 0 680 272" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Meta-prompting: 7-step process for using Claude to write a prompt</title>
<desc>Two rows showing the meta-prompting loop: steps 1-3 are the drafting and revision cycle, steps 5-7 are deploy and run</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<path d="M562 56 L562 28 L340 28 L340 56" fill="none" stroke="#161BAA" stroke-width="1.2" stroke-dasharray="5,3" marker-end="url(#arrow)"/>
<text x="452" y="20" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#161BAA">revise and repeat</text>
<rect x="25" y="56" width="186" height="62" rx="8" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.8"/>
<rect x="25" y="56" width="186" height="28" rx="8" fill="#161BAA"/>
<rect x="25" y="70" width="186" height="14" fill="#161BAA"/>
<text x="33" y="74" font-family="sans-serif" font-size="9" fill="#9BAAEE">Step 1</text>
<text x="118" y="74" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="600" fill="#FFFFFF">Ask Claude</text>
<text x="118" y="96" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#2A3A8A">Describe the job to be done</text>
<text x="118" y="110" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#2A3A8A">and what good output looks like</text>
<line x1="213" y1="87" x2="239" y2="87" stroke="#888888" stroke-width="1.4" marker-end="url(#arrow)"/>
<rect x="241" y="56" width="186" height="62" rx="8" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.8"/>
<rect x="241" y="56" width="186" height="28" rx="8" fill="#2EA799"/>
<rect x="241" y="70" width="186" height="14" fill="#2EA799"/>
<text x="249" y="74" font-family="sans-serif" font-size="9" fill="#9EE2D6">Step 2</text>
<text x="334" y="74" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="600" fill="#FFFFFF">Claude drafts a prompt</text>
<text x="334" y="96" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#1A6860">A complete, structured prompt</text>
<text x="334" y="110" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#1A6860">ready to test and refine</text>
<line x1="429" y1="87" x2="455" y2="87" stroke="#888888" stroke-width="1.4" marker-end="url(#arrow)"/>
<rect x="457" y="56" width="186" height="62" rx="8" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.8"/>
<rect x="457" y="56" width="186" height="28" rx="8" fill="#161BAA"/>
<rect x="457" y="70" width="186" height="14" fill="#161BAA"/>
<text x="465" y="74" font-family="sans-serif" font-size="9" fill="#9BAAEE">Step 3</text>
<text x="550" y="74" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="600" fill="#FFFFFF">Revise the prompt</text>
<text x="550" y="96" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#2A3A8A">Test it, note what&apos;s off,</text>
<text x="550" y="110" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#2A3A8A">tell Claude what to fix</text>
<path d="M550 118 L550 156 L112 156 L112 170" fill="none" stroke="#888888" stroke-width="1.2" marker-end="url(#arrow)"/>
<text x="330" y="148" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#757575">when satisfied, deploy the prompt</text>
<rect x="25" y="170" width="172" height="62" rx="8" fill="#EBF3FA" stroke="#478FCC" stroke-width="0.8"/>
<rect x="25" y="170" width="172" height="28" rx="8" fill="#478FCC"/>
<rect x="25" y="184" width="172" height="14" fill="#478FCC"/>
<text x="33" y="188" font-family="sans-serif" font-size="9" fill="#C8E0F4">Step 5</text>
<text x="111" y="188" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="600" fill="#FFFFFF">Copy the prompt</text>
<text x="111" y="210" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#2A5C8A">Select and copy the</text>
<text x="111" y="224" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#2A5C8A">finalized prompt text</text>
<line x1="199" y1="201" x2="225" y2="201" stroke="#888888" stroke-width="1.4" marker-end="url(#arrow)"/>
<rect x="227" y="170" width="196" height="62" rx="8" fill="#EBF3FA" stroke="#478FCC" stroke-width="0.8"/>
<rect x="227" y="170" width="196" height="28" rx="8" fill="#478FCC"/>
<rect x="227" y="184" width="196" height="14" fill="#478FCC"/>
<text x="235" y="188" font-family="sans-serif" font-size="9" fill="#C8E0F4">Step 6</text>
<text x="325" y="188" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="600" fill="#FFFFFF">Paste the prompt</text>
<text x="325" y="210" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#2A5C8A">Into project instructions</text>
<text x="325" y="224" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#2A5C8A">or a new chat window</text>
<line x1="425" y1="201" x2="449" y2="201" stroke="#888888" stroke-width="1.4" marker-end="url(#arrow)"/>
<rect x="451" y="170" width="204" height="62" rx="8" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.8"/>
<rect x="451" y="170" width="204" height="28" rx="8" fill="#2EA799"/>
<rect x="451" y="184" width="204" height="14" fill="#2EA799"/>
<text x="459" y="188" font-family="sans-serif" font-size="9" fill="#9EE2D6">Step 7</text>
<text x="553" y="188" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="12" font-weight="600" fill="#FFFFFF">Claude responds</text>
<text x="553" y="210" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#1A6860">Strong understanding of</text>
<text x="553" y="224" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#1A6860">exactly what&apos;s being asked</text>
<rect x="25" y="248" width="10" height="10" rx="2" fill="#161BAA"/>
<text x="40" y="257" font-family="sans-serif" font-size="9" fill="#757575">You</text>
<rect x="70" y="248" width="10" height="10" rx="2" fill="#2EA799"/>
<text x="85" y="257" font-family="sans-serif" font-size="9" fill="#757575">Claude</text>
<rect x="120" y="248" width="10" height="10" rx="2" fill="#478FCC"/>
<text x="135" y="257" font-family="sans-serif" font-size="9" fill="#757575">Action</text>
</svg>
"""


# ---------------------------------------------------------------------------
# Lesson 1.3 — NLP clinical symptom detection
# ---------------------------------------------------------------------------
DIAGRAMS["nlp_clinical"] = """
<html><head><style>
body{margin:0;padding:0;font-family:sans-serif;background:transparent;}
.step{font-size:13px;font-weight:600;color:#161BAA;text-align:center;margin:0 0 8px 0;}
.card{border-radius:8px;padding:14px 16px;margin-bottom:10px;}
.arr{text-align:center;color:#888;font-size:18px;margin:2px 0 10px;line-height:1;}
.lbl{font-size:11px;color:#888;border-bottom:1px solid #C0C4E8;margin-bottom:10px;padding-bottom:6px;font-weight:500;}
.tag{background:#E4F5F3;border:1px solid #2EA799;border-radius:3px;padding:1px 6px;font-size:13px;color:#0F6E56;white-space:nowrap;}
</style></head><body>
<div style="max-width:520px;margin:0 auto;padding:14px 20px 8px;"><p style="text-align:center;font-size:12px;font-weight:600;color:#757575;letter-spacing:0.5px;margin:0 0 14px 0;text-transform:uppercase;">Example of NLP in action</p>
<p class="step">1. Scan provider notes</p>
<div class="card" style="background:#EBF3FA;border:1px solid #B5D4F4;">
<div class="lbl" style="border-bottom-color:#B5D4F4;">Encounter note</div>
<div style="font-size:13px;color:#212121;line-height:2.1;">
Patient reports feeling <span class="tag">sad</span> and <span class="tag">depressed mood</span> for past month.
Also experiencing <span class="tag">poor sleep</span> and <span class="tag">fatigue</span>.
</div></div>
<div class="arr">&#8595;</div>
<p class="step">2. Entity recognition</p>
<div class="card" style="background:#E8E9F7;border:1px solid #C0C4E8;">
<div class="lbl">Pattern matching</div>
<div style="font-size:13px;color:#212121;line-height:2.2;">
&#8220;sad&#8221; <span style="color:#888;">&#8594;</span> Depressed mood<br>
&#8220;depressed mood&#8221; <span style="color:#888;">&#8594;</span> Depressed mood<br>
&#8220;poor sleep&#8221; <span style="color:#888;">&#8594;</span> Sleep disturbance<br>
&#8220;fatigue&#8221; <span style="color:#888;">&#8594;</span> Loss of energy
</div></div>
<div class="arr">&#8595;</div>
<p class="step">3. Flag patients without a diagnosis</p>
<div class="card" style="background:#E4F5F3;border:1px solid #2EA799;">
<div class="lbl" style="border-bottom-color:#9ED5D0;color:#0F6E56;">Clinical decision</div>
<div style="font-size:13px;color:#212121;line-height:2.2;">
<span style="color:#2EA799;font-weight:600;">&#10003;</span> Mental health symptoms detected<br>
<span style="color:#E24B4A;font-weight:600;">&#10007;</span> No mental health diagnosis code (F-code)<br>
<span style="color:#161BAA;font-weight:600;">&#8594;</span> Flag patient for assessment
</div></div>
</div>
</body></html>
"""


# ---------------------------------------------------------------------------
# Lesson 2.3 — Model comparison: Haiku, Sonnet, Opus
# ---------------------------------------------------------------------------
DIAGRAMS["model_comparison"] = """
<svg width="100%" viewBox="0 0 680 285" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Choosing the right Claude model</title>
<desc>Three-column card comparison of Haiku, Sonnet, and Opus with task examples and allocation guidance</desc>
<rect x="14" y="14" width="200" height="252" rx="8" fill="#EBF3FA" stroke="#478FCC" stroke-width="0.8"/>
<rect x="14" y="14" width="200" height="42" rx="8" fill="#478FCC"/>
<rect x="14" y="42" width="200" height="14" fill="#478FCC"/>
<text x="114" y="38" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="14" font-weight="600" fill="#FFFFFF">Haiku</text>
<text x="114" y="72" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#2A5C8A" font-weight="600">FASTEST · LOWEST COST</text>
<line x1="30" y1="83" x2="198" y2="83" stroke="#B5D4F4" stroke-width="0.5"/>
<text x="28" y="100" font-family="sans-serif" font-size="10" fill="#212121">· Summarizing short documents</text>
<text x="28" y="117" font-family="sans-serif" font-size="10" fill="#212121">· Answering specific questions</text>
<text x="28" y="134" font-family="sans-serif" font-size="10" fill="#212121">· Grammar and spelling checks</text>
<text x="28" y="151" font-family="sans-serif" font-size="10" fill="#212121">· Simple rewrites and edits</text>
<text x="28" y="168" font-family="sans-serif" font-size="10" fill="#212121">· Quick lookups and definitions</text>
<rect x="28" y="220" width="172" height="30" rx="4" fill="#D4E8F8" stroke="#478FCC" stroke-width="0.5"/>
<text x="114" y="235" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#2A5C8A" font-weight="600">Use when speed matters most</text>
<rect x="240" y="14" width="200" height="252" rx="8" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.8"/>
<rect x="240" y="14" width="200" height="42" rx="8" fill="#161BAA"/>
<rect x="240" y="42" width="200" height="14" fill="#161BAA"/>
<text x="340" y="35" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="14" font-weight="600" fill="#FFFFFF">Sonnet</text>
<text x="340" y="50" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="9" fill="#AAB4F0">DEFAULT FOR MOST WORK</text>
<text x="340" y="72" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#2A3A8A" font-weight="600">BALANCED · RECOMMENDED</text>
<line x1="256" y1="83" x2="424" y2="83" stroke="#C0C4E8" stroke-width="0.5"/>
<text x="254" y="100" font-family="sans-serif" font-size="10" fill="#212121">· Document analysis and synthesis</text>
<text x="254" y="117" font-family="sans-serif" font-size="10" fill="#212121">· Structured writing and drafting</text>
<text x="254" y="134" font-family="sans-serif" font-size="10" fill="#212121">· Multi-step research tasks</text>
<text x="254" y="151" font-family="sans-serif" font-size="10" fill="#212121">· RFP and brief preparation</text>
<text x="254" y="168" font-family="sans-serif" font-size="10" fill="#212121">· Instruction-following reliably</text>
<rect x="254" y="220" width="172" height="30" rx="4" fill="#D0D3F0" stroke="#161BAA" stroke-width="0.5"/>
<text x="340" y="235" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#161BAA" font-weight="600">Use for most daily work</text>
<rect x="466" y="14" width="200" height="252" rx="8" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.8"/>
<rect x="466" y="14" width="200" height="42" rx="8" fill="#2EA799"/>
<rect x="466" y="42" width="200" height="14" fill="#2EA799"/>
<text x="566" y="38" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="14" font-weight="600" fill="#FFFFFF">Opus</text>
<text x="566" y="72" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#0F6E56" font-weight="600">MOST CAPABLE · HIGHEST COST</text>
<line x1="482" y1="83" x2="650" y2="83" stroke="#9ED5D0" stroke-width="0.5"/>
<text x="480" y="100" font-family="sans-serif" font-size="10" fill="#212121">· Complex multi-document reasoning</text>
<text x="480" y="117" font-family="sans-serif" font-size="10" fill="#212121">· Nuanced policy and clinical work</text>
<text x="480" y="134" font-family="sans-serif" font-size="10" fill="#212121">· Competing considerations / tradeoffs</text>
<text x="480" y="151" font-family="sans-serif" font-size="10" fill="#212121">· Lengthy regulatory analysis</text>
<text x="480" y="168" font-family="sans-serif" font-size="10" fill="#212121">· When first-attempt quality matters</text>
<rect x="480" y="220" width="172" height="30" rx="4" fill="#B8E8E3" stroke="#2EA799" stroke-width="0.5"/>
<text x="566" y="228" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#0F6E56" font-weight="600">Use when judgment quality</text>
<text x="566" y="242" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#0F6E56" font-weight="600">matters most</text>
<text x="340" y="278" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#757575">Use the lightest model that reliably handles the task — Opus for a grammar check wastes allocation</text>
</svg>
"""


# ---------------------------------------------------------------------------
# Lesson 2.4 — Hallucination check traffic light
# ---------------------------------------------------------------------------
DIAGRAMS["hallucination_check"] = """
<svg width="100%" viewBox="0 0 680 385" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Hallucination check: when and how to verify Claude output</title>
<desc>Three-zone guide showing which Claude outputs to trust, spot-check, or always verify externally, with verification methods for each</desc>
<rect x="14" y="14" width="650" height="90" rx="8" fill="#EAF3DE" stroke="#3B6D11" stroke-width="0.8"/>
<rect x="14" y="14" width="14" height="90" rx="4" fill="#3B6D11"/>
<rect x="20" y="14" width="8" height="90" fill="#3B6D11"/>
<circle cx="51" cy="59" r="13" fill="#639922"/>
<text x="51" y="59" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">G</text>
<text x="76" y="33" font-family="sans-serif" font-size="12" font-weight="600" fill="#27500A">Use directly — low hallucination risk</text>
<text x="76" y="51" font-family="sans-serif" font-size="10" fill="#444444">Reasoning, structure, tone, drafting from your own source material, formatting,</text>
<text x="76" y="65" font-family="sans-serif" font-size="10" fill="#444444">summaries of content you provided, rewriting, brainstorming, and task planning.</text>
<text x="76" y="84" font-family="sans-serif" font-size="10" fill="#3B6D11" font-weight="600">How to verify: re-read for logic and completeness — no external lookup needed.</text>
<rect x="14" y="118" width="650" height="90" rx="8" fill="#FAEEDA" stroke="#854F0B" stroke-width="0.8"/>
<rect x="14" y="118" width="14" height="90" rx="4" fill="#854F0B"/>
<rect x="20" y="118" width="8" height="90" fill="#854F0B"/>
<circle cx="51" cy="163" r="13" fill="#BA7517"/>
<text x="51" y="163" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">Y</text>
<text x="76" y="137" font-family="sans-serif" font-size="12" font-weight="600" fill="#633806">Spot-check — moderate risk</text>
<text x="76" y="155" font-family="sans-serif" font-size="10" fill="#444444">Named organizations, general legislation, product capabilities, broad industry statistics,</text>
<text x="76" y="169" font-family="sans-serif" font-size="10" fill="#444444">regulatory body positions, and named individuals&apos; roles or affiliations.</text>
<text x="76" y="188" font-family="sans-serif" font-size="10" fill="#854F0B" font-weight="600">How to verify: web search the claim — confirm the source exists and says what Claude claims.</text>
<rect x="14" y="222" width="650" height="104" rx="8" fill="#FCEBEB" stroke="#A32D2D" stroke-width="0.8"/>
<rect x="14" y="222" width="14" height="104" rx="4" fill="#A32D2D"/>
<rect x="20" y="222" width="8" height="104" fill="#A32D2D"/>
<circle cx="51" cy="270" r="13" fill="#E24B4A"/>
<text x="51" y="270" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="700" fill="#FFFFFF">R</text>
<text x="76" y="241" font-family="sans-serif" font-size="12" font-weight="600" fill="#791F1F">Always verify externally — high risk</text>
<text x="76" y="259" font-family="sans-serif" font-size="10" fill="#444444">Specific citations, named studies, statistics attributed to a source, journal names, DOIs,</text>
<text x="76" y="273" font-family="sans-serif" font-size="10" fill="#444444">dates of rulings or publications, funding amounts, and clinical outcome data.</text>
<text x="76" y="293" font-family="sans-serif" font-size="10" fill="#A32D2D" font-weight="600">How to verify: ask Claude for the full citation and DOI, then confirm it exists</text>
<text x="76" y="307" font-family="sans-serif" font-size="10" fill="#A32D2D" font-weight="600">in PubMed, Google Scholar, or the original publication.</text>
<rect x="14" y="340" width="650" height="30" rx="6" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.5"/>
<text x="339" y="355" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#161BAA" font-weight="600">Rule: the more specific and attributable the claim, the higher the verification requirement</text>
</svg>
"""


# ---------------------------------------------------------------------------
# Lesson 3.6 — Gating: standard gate and self-checking gate
# ---------------------------------------------------------------------------
DIAGRAMS["gating"] = """
<svg width="100%" viewBox="-40 0 720 560" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Gating prompt patterns: standard gate and self-checking gate</title>
<desc>Side-by-side flowcharts showing standard and self-checking gates with exact prompt language at each step</desc>
<defs><marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<text x="162" y="16" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="600" fill="#161BAA">Standard gate</text>
<rect x="62" y="26" width="200" height="54" rx="8" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.8"/>
<rect x="62" y="26" width="200" height="28" rx="8" fill="#161BAA"/>
<rect x="62" y="40" width="200" height="14" fill="#161BAA"/>
<text x="162" y="42" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="600" fill="#FFFFFF">Stage 1</text>
<text x="162" y="62" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#2A3A8A">"Do not begin the next stage until I reply GO."</text>
<line x1="162" y1="80" x2="162" y2="102" stroke="#161BAA" stroke-width="1.2" marker-end="url(#arrow)"/>
<rect x="62" y="104" width="200" height="56" rx="8" fill="#EBF3FA" stroke="#478FCC" stroke-width="0.8"/>
<rect x="62" y="104" width="200" height="28" rx="8" fill="#478FCC"/>
<rect x="62" y="118" width="200" height="14" fill="#478FCC"/>
<text x="162" y="120" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="600" fill="#FFFFFF">Gate 1 — Claude stops</text>
<text x="162" y="142" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#2A5C8A">"GATE 1 — ready for review.</text>
<text x="162" y="153" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#2A5C8A">Reply GO to continue."</text>
<line x1="162" y1="160" x2="162" y2="182" stroke="#478FCC" stroke-width="1.2" marker-end="url(#arrow)"/>
<polygon points="162,184 238,218 162,252 86,218" fill="#FAEEDA" stroke="#BA7517" stroke-width="0.8"/>
<text x="162" y="211" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#633806">You review</text>
<text x="162" y="224" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#633806">the output</text>
<line x1="162" y1="252" x2="162" y2="274" stroke="#3B6D11" stroke-width="1.2" marker-end="url(#arrow)"/>
<text x="176" y="265" font-family="sans-serif" font-size="9" fill="#3B6D11" font-weight="600">You: "GO"</text>
<path d="M86 218 L44 218 L44 132 L62 132" fill="none" stroke="#A32D2D" stroke-width="1.1" stroke-dasharray="4,3" marker-end="url(#arrow)"/>
<text x="42" y="178" text-anchor="end" font-family="sans-serif" font-size="9" fill="#A32D2D" font-weight="600">You revise:</text>
<text x="42" y="192" text-anchor="end" font-family="sans-serif" font-size="9" fill="#A32D2D">"Change the</text>
<text x="42" y="204" text-anchor="end" font-family="sans-serif" font-size="9" fill="#A32D2D">tone to..."</text>
<rect x="62" y="276" width="200" height="40" rx="8" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.8"/>
<rect x="62" y="276" width="200" height="20" rx="8" fill="#161BAA"/>
<rect x="62" y="286" width="200" height="10" fill="#161BAA"/>
<text x="162" y="288" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="600" fill="#FFFFFF">Stage 2</text>
<text x="162" y="306" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#2A3A8A">Builds on confirmed Stage 1</text>
<line x1="162" y1="316" x2="162" y2="334" stroke="#161BAA" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arrow)"/>
<text x="162" y="348" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#757575">continues...</text>
<line x1="340" y1="8" x2="340" y2="490" stroke="#DDDDDD" stroke-width="0.8" stroke-dasharray="5,4"/>
<text x="518" y="16" text-anchor="middle" font-family="sans-serif" font-size="12" font-weight="600" fill="#161BAA">Self-checking gate</text>
<rect x="418" y="26" width="200" height="54" rx="8" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.8"/>
<rect x="418" y="26" width="200" height="28" rx="8" fill="#161BAA"/>
<rect x="418" y="40" width="200" height="14" fill="#161BAA"/>
<text x="518" y="42" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="600" fill="#FFFFFF">Stage 1</text>
<text x="518" y="62" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#2A3A8A">"Before presenting, check criteria</text>
<text x="518" y="73" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#2A3A8A">and fix issues first."</text>
<line x1="518" y1="80" x2="518" y2="102" stroke="#161BAA" stroke-width="1.2" marker-end="url(#arrow)"/>
<rect x="418" y="104" width="200" height="56" rx="8" fill="#E4F5F3" stroke="#2EA799" stroke-width="0.8"/>
<rect x="418" y="104" width="200" height="28" rx="8" fill="#2EA799"/>
<rect x="418" y="118" width="200" height="14" fill="#2EA799"/>
<text x="518" y="120" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="600" fill="#FFFFFF">Self-check (internal)</text>
<text x="518" y="142" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#1A6860">Claude checks against criteria</text>
<text x="518" y="153" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#1A6860">and fixes before stopping</text>
<path d="M618 124 L642 124 L642 52 L618 52" fill="none" stroke="#2EA799" stroke-width="1" stroke-dasharray="4,3" marker-end="url(#arrow)"/>
<text x="646" y="92" font-family="sans-serif" font-size="9" fill="#0F6E56" font-weight="600">Fix &amp;</text>
<text x="646" y="104" font-family="sans-serif" font-size="9" fill="#0F6E56">retry</text>
<line x1="518" y1="160" x2="518" y2="182" stroke="#2EA799" stroke-width="1.2" marker-end="url(#arrow)"/>
<rect x="418" y="184" width="200" height="56" rx="8" fill="#EBF3FA" stroke="#478FCC" stroke-width="0.8"/>
<rect x="418" y="184" width="200" height="28" rx="8" fill="#478FCC"/>
<rect x="418" y="198" width="200" height="14" fill="#478FCC"/>
<text x="518" y="200" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="600" fill="#FFFFFF">Gate 1 — Claude stops</text>
<text x="518" y="222" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#2A5C8A">"GATE 1 — self-check passed.</text>
<text x="518" y="233" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#2A5C8A">Reply GO to continue."</text>
<line x1="518" y1="240" x2="518" y2="262" stroke="#478FCC" stroke-width="1.2" marker-end="url(#arrow)"/>
<polygon points="518,264 594,298 518,332 442,298" fill="#FAEEDA" stroke="#BA7517" stroke-width="0.8"/>
<text x="518" y="291" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#633806">You review</text>
<text x="518" y="304" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#633806">the output</text>
<line x1="518" y1="332" x2="518" y2="354" stroke="#3B6D11" stroke-width="1.2" marker-end="url(#arrow)"/>
<text x="532" y="345" font-family="sans-serif" font-size="9" fill="#3B6D11" font-weight="600">You: "GO"</text>
<path d="M442 298 L400 298 L400 212 L418 212" fill="none" stroke="#A32D2D" stroke-width="1.1" stroke-dasharray="4,3" marker-end="url(#arrow)"/>
<text x="398" y="258" text-anchor="end" font-family="sans-serif" font-size="9" fill="#A32D2D" font-weight="600">You revise:</text>
<text x="398" y="272" text-anchor="end" font-family="sans-serif" font-size="9" fill="#A32D2D">"Shorten</text>
<text x="398" y="284" text-anchor="end" font-family="sans-serif" font-size="9" fill="#A32D2D">section 2"</text>
<rect x="418" y="356" width="200" height="40" rx="8" fill="#E8E9F7" stroke="#161BAA" stroke-width="0.8"/>
<rect x="418" y="356" width="200" height="20" rx="8" fill="#161BAA"/>
<rect x="418" y="366" width="200" height="10" fill="#161BAA"/>
<text x="518" y="368" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" font-weight="600" fill="#FFFFFF">Stage 2</text>
<text x="518" y="386" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#2A3A8A">Builds on confirmed Stage 1</text>
<line x1="518" y1="396" x2="518" y2="414" stroke="#161BAA" stroke-width="1" stroke-dasharray="3,3" marker-end="url(#arrow)"/>
<text x="518" y="428" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#757575">continues...</text>
<rect x="14" y="450" width="12" height="10" rx="2" fill="#9BAAEE" stroke="#161BAA" stroke-width="0.5"/>
<text x="32" y="456" dominant-baseline="central" font-family="sans-serif" font-size="9" fill="#444">Stage</text>
<rect x="82" y="450" width="12" height="10" rx="2" fill="#B5D4F4" stroke="#478FCC" stroke-width="0.5"/>
<text x="100" y="456" dominant-baseline="central" font-family="sans-serif" font-size="9" fill="#444">Gate</text>
<rect x="142" y="450" width="12" height="10" rx="2" fill="#5DCAA5" stroke="#2EA799" stroke-width="0.5"/>
<text x="160" y="456" dominant-baseline="central" font-family="sans-serif" font-size="9" fill="#444">Self-check</text>
<polygon points="240,455 248,460 240,465 232,460" fill="#FAEEDA" stroke="#BA7517" stroke-width="0.7"/>
<text x="256" y="456" dominant-baseline="central" font-family="sans-serif" font-size="9" fill="#757575">Your review</text>
<text x="340" y="500" text-anchor="middle" font-family="sans-serif" font-size="9" fill="#757575">Self-check catches predictable errors before they reach your review pass</text>
</svg>
"""


# ---------------------------------------------------------------------------
# Lesson 1.1 — AI type hierarchy (nested)
# ---------------------------------------------------------------------------
DIAGRAMS["ai_hierarchy"] = """
<html><head><style>
body{margin:0;padding:8px;background:transparent;}
</style></head><body>
<style>
*{box-sizing:border-box;margin:0;padding:0}
.wrap{padding:16px 0 24px;font-family:var(--font-sans,sans-serif)}
.diagram-row{display:flex;gap:24px;align-items:flex-start;flex-wrap:wrap}
.svg-col{flex:0 0 360px;min-width:300px}
.info-col{flex:1;min-width:220px;padding-top:4px}
.info-box{border-radius:12px;padding:18px 20px;transition:background .2s,border-color .2s;border:1.5px solid #2E4799;background:#f0f4ff}
.info-title{font-size:15px;font-weight:500;margin-bottom:6px}
.info-body{font-size:13px;line-height:1.65;color:#212121}
.info-body p{margin-bottom:8px}
.info-body p:last-child{margin-bottom:0}
.info-nf{margin-top:10px;font-size:12px;line-height:1.6;padding:9px 11px;border-radius:7px}
.info-nf-label{font-size:11px;font-weight:500;opacity:.75;margin-bottom:3px}
.info-ex{margin-top:8px;font-size:12px;line-height:1.55;padding:9px 11px;border-radius:7px}
.legend{display:flex;flex-wrap:wrap;gap:7px;margin-top:14px}
.leg{display:flex;align-items:center;gap:6px;font-size:12px;cursor:pointer;padding:4px 10px;border-radius:20px;border:1.5px solid transparent;transition:all .15s;white-space:nowrap}
.leg-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
svg .ring{cursor:pointer}
svg .ring:hover > ellipse{opacity:.82}
svg .sym-btn{cursor:pointer}
svg .sym-btn:hover > rect{opacity:.88}
</style>

<div class="wrap">
<div class="diagram-row">
<div class="svg-col">
<svg width="100%" viewBox="0 0 360 385" role="img">
  <title>AI taxonomy — nested rings</title>
  <desc>Concentric rings inside an AI boundary. Symbolic AI sits as a tappable box in the foreground left, inside the AI ring but outside ML. Inner rings: ML, neural networks, deep learning, generative AI, LLMs.</desc>

  <!-- AI outermost ring -->
  <g class="ring" id="r-ai" onclick="show('ai')">
    <ellipse cx="200" cy="210" rx="155" ry="165" fill="#161B4A" stroke="#2E4799" stroke-width="1.2"/>
    <text x="200" y="72" text-anchor="middle" font-size="13" font-weight="500" fill="#fff" font-family="var(--font-sans,sans-serif)">Artificial intelligence</text>
  </g>

  <!-- ML ring -->
  <g class="ring" id="r-ml" onclick="show('ml')">
    <ellipse cx="215" cy="223" rx="116" ry="122" fill="#2E4799" stroke="#478FCC" stroke-width="1"/>
    <text x="215" y="122" text-anchor="middle" font-size="13" font-weight="500" fill="#fff" font-family="var(--font-sans,sans-serif)">Machine learning</text>
  </g>

  <!-- Neural networks ring -->
  <g class="ring" id="r-nn" onclick="show('nn')">
    <ellipse cx="215" cy="232" rx="86" ry="92" fill="#1e5c9e" stroke="#478FCC" stroke-width="1"/>
    <text x="215" y="160" text-anchor="middle" font-size="12" font-weight="500" fill="#fff" font-family="var(--font-sans,sans-serif)">Neural networks</text>
  </g>

  <!-- Deep learning ring -->
  <g class="ring" id="r-dl" onclick="show('dl')">
    <ellipse cx="215" cy="241" rx="62" ry="68" fill="#1a7a8a" stroke="#4CB6AC" stroke-width="1"/>
    <text x="215" y="192" text-anchor="middle" font-size="12" font-weight="500" fill="#fff" font-family="var(--font-sans,sans-serif)">Deep learning</text>
  </g>

  <!-- Generative AI ring -->
  <g class="ring" id="r-gen" onclick="show('gen')">
    <ellipse cx="215" cy="250" rx="43" ry="49" fill="#2a9aaa" stroke="#4CB6AC" stroke-width="0.8"/>
    <text x="215" y="217" text-anchor="middle" font-size="11" font-weight="500" fill="#fff" font-family="var(--font-sans,sans-serif)">Generative AI</text>
  </g>

  <!-- LLM innermost ring -->
  <g class="ring" id="r-llm" onclick="show('llm')">
    <ellipse cx="215" cy="258" rx="28" ry="33" fill="#4CB6AC" stroke="#fff" stroke-width="0.8" stroke-opacity="0.3"/>
    <text x="215" y="255" text-anchor="middle" font-size="11" font-weight="500" fill="#0a3d35" font-family="var(--font-sans,sans-serif)">LLMs</text>
    <text x="215" y="269" text-anchor="middle" font-size="9" fill="#085041" font-family="var(--font-sans,sans-serif)">Claude · GPT · Llama</text>
  </g>

  <!-- Symbolic AI — drawn LAST so it paints above all rings -->
  <g class="sym-btn" id="r-sym" onclick="show('sym')">
    <rect x="18" y="178" width="96" height="58" rx="9" fill="#2E4799" stroke="#478FCC" stroke-width="1.5"/>
    <text x="66" y="198" text-anchor="middle" font-size="12" font-weight="500" fill="#fff" font-family="var(--font-sans,sans-serif)">Symbolic AI</text>
    <text x="66" y="214" text-anchor="middle" font-size="10" fill="#b5d4f4" font-family="var(--font-sans,sans-serif)">Rule-based</text>
    <text x="66" y="228" text-anchor="middle" font-size="10" fill="#b5d4f4" font-family="var(--font-sans,sans-serif)">No learning</text>
  </g>

  <text x="190" y="356" text-anchor="middle" font-size="11" fill="#757575" font-family="var(--font-sans,sans-serif)">Tap any layer to learn more</text>
</svg>
</div>

<div class="info-col">
<div class="info-box" id="info-box">
  <div class="info-title" id="info-title" style="color:#161B4A">Select a layer</div>
  <div class="info-body" id="info-body">Tap any ring or the Symbolic AI box to see what it means and how NeuroFlow uses it.</div>
  <div class="info-nf" id="info-nf" style="display:none"><div class="info-nf-label" id="info-nf-label"></div><div id="info-nf-text"></div></div>
  <div class="info-ex" id="info-ex" style="display:none"></div>
</div>
<div class="legend">
  <div class="leg" onclick="show('sym')" style="background:#2E4799;color:#fff;border-color:#478FCC"><div class="leg-dot" style="background:#478FCC"></div>Symbolic AI</div>
  <div class="leg" onclick="show('ai')" style="background:#161B4A;color:#fff;border-color:#2E4799"><div class="leg-dot" style="background:#4CB6AC"></div>AI</div>
  <div class="leg" onclick="show('ml')" style="background:#1a2f7a;color:#fff;border-color:#478FCC"><div class="leg-dot" style="background:#2E4799"></div>ML</div>
  <div class="leg" onclick="show('nn')" style="background:#e8f2fb;color:#161B4A;border-color:#478FCC"><div class="leg-dot" style="background:#1e5c9e"></div>Neural networks</div>
  <div class="leg" onclick="show('dl')" style="background:#e4f5f4;color:#085041;border-color:#4CB6AC"><div class="leg-dot" style="background:#1a7a8a"></div>Deep learning</div>
  <div class="leg" onclick="show('gen')" style="background:#e0f4f3;color:#085041;border-color:#4CB6AC"><div class="leg-dot" style="background:#2a9aaa"></div>Generative AI</div>
  <div class="leg" onclick="show('llm')" style="background:#f0faf9;color:#085041;border-color:#4CB6AC"><div class="leg-dot" style="background:#4CB6AC"></div>LLMs</div>
</div>
</div>
</div>
</div>

<script>
const D={
  sym:{title:"Symbolic AI",body:"<p>Symbolic AI is the oldest and most intuitive form. A symbolic AI system follows explicit rules that a human wrote. If this condition is true, do that. There is no learning — the system only does exactly what its rules specify, nothing more.</p><p>This makes symbolic AI predictable and auditable. You can always trace an output back to the rule that produced it. The limitation is brittleness: if a situation arises that no rule covers, the system cannot adapt.</p>",nfLabel:"NeuroFlow today",nf:"The logic that determines which content a patient receives, which assessment to deliver next, and when to trigger a clinical alert is rule-based. A clinician or product team defined those rules and the system executes them.",ex:"A clinical decision tree that routes a patient to crisis resources if PHQ-9 item 9 scores above zero is symbolic AI.",bg:"#2E4799",border:"#478FCC",titleC:"#fff",bodyC:"#d4e4ff",nfBg:"#1a3070",nfC:"#b5d4f4",exBg:"#1f3c8a",exC:"#b5d4f4"},
  ai:{title:"Artificial intelligence",body:"<p>AI is the broadest category — any technique that lets a computer perform tasks we associate with human thinking. Machine learning is one approach within AI. Symbolic AI is another. Both sit inside the AI boundary, but they work in fundamentally different ways.</p>",nfLabel:"",nf:"",ex:"The outer boundary contains everything: rule-based clinical alerts, risk stratification models, and large language models are all AI.",bg:"#161B4A",border:"#2E4799",titleC:"#fff",bodyC:"#d4dfff",nfBg:"",nfC:"",exBg:"#0f1e55",exC:"#b5d4f4"},
  ml:{title:"Machine learning",body:"<p>Instead of following rules, an ML model learns from examples. A developer provides a large dataset of past cases with known outcomes, and the model identifies statistical patterns connecting inputs to those outcomes. When it encounters a new case, it applies those learned patterns to generate a prediction.</p>",nfLabel:"NeuroFlow — BHIQ",nf:"The risk stratification models were trained on historical behavioral health data — assessment scores, utilization patterns, diagnosis codes — paired with known outcomes. The model learned which combinations of factors are statistically associated with higher risk.",ex:"A fraud detection model trained on millions of labeled transactions learns to flag unusual patterns without anyone writing explicit rules.",bg:"#1a2f7a",border:"#478FCC",titleC:"#fff",bodyC:"#d4e4ff",nfBg:"#0f2060",nfC:"#b5d4f4",exBg:"#152878",exC:"#b5d4f4"},
  nn:{title:"Neural networks",body:"<p>Neural networks are ML architectures loosely inspired by the brain. They stack layers of simple computational units that transform inputs step by step. Each layer learns to detect increasingly abstract features.</p><p>NLP (natural language processing) lives here. It is a task domain — language translation, summarization, classification, sentiment analysis — not a separate architectural layer. Most modern NLP runs on deep neural networks.</p>",nfLabel:"",nf:"",ex:"An image classifier uses early layers to detect edges, middle layers to detect shapes, and final layers to recognize specific objects.",bg:"#1e5c9e",border:"#478FCC",titleC:"#fff",bodyC:"#d0e8ff",nfBg:"",nfC:"",exBg:"#0f3a6a",exC:"#b5d4f4"},
  dl:{title:"Deep learning",body:"<p>Deep learning refers to neural networks with many layers — deep enough to learn highly complex patterns. Medical imaging analysis, speech recognition, and translation are all deep learning applications.</p><p>Deep learning is the foundation that large language models are built on. Every LLM is a deep learning model, but most deep learning models are not LLMs.</p>",nfLabel:"",nf:"",ex:"Detecting abnormalities in radiology scans requires deep learning — the patterns are too subtle for hand-written rules or shallow ML models.",bg:"#1a7a8a",border:"#4CB6AC",titleC:"#fff",bodyC:"#c8ede9",nfBg:"",nfC:"",exBg:"#0d5060",exC:"#9FE1CB"},
  gen:{title:"Generative AI",body:"<p>Generative AI creates new content rather than classifying inputs or predicting outcomes. The output can be text, images, video, audio, or code depending on what the model was trained on.</p><p>LLMs are one type of generative AI. DALL-E generates images. Sora generates video. These are generative AI systems but not language models.</p>",nfLabel:"",nf:"",ex:"DALL-E generates images. Sora generates video. Both are generative AI — generative AI is a broader category that includes LLMs but is not limited to them.",bg:"#1a6870",border:"#4CB6AC",titleC:"#fff",bodyC:"#c8ede9",nfBg:"",nfC:"",exBg:"#0f4a52",exC:"#9FE1CB"},
  llm:{title:"Large language models",body:"<p>LLMs are a specific type of generative AI trained on text. They understand language, follow instructions, reason through problems, and generate fluent written output. Every LLM is a generative AI system built on deep learning, but most generative AI systems are not LLMs.</p><p>Claude, GPT-5, Gemini, and Llama are all LLMs. Open-source models like Llama and Mistral are available for anyone to run. Closed-source models like GPT and Claude are accessed via API.</p>",nfLabel:"",nf:"",ex:"Claude reads your prompt, weighs the relationships between every word using attention, and generates a response one token at a time.",bg:"#085041",border:"#4CB6AC",titleC:"#fff",bodyC:"#c8ede9",nfBg:"#04342C",nfC:"#9FE1CB",exBg:"#052e28",exC:"#9FE1CB"}
};
function show(key){
  const d=D[key];
  document.getElementById('info-box').style.background=d.bg;
  document.getElementById('info-box').style.borderColor=d.border;
  const title=document.getElementById('info-title');
  title.style.color=d.titleC; title.textContent=d.title;
  const body=document.getElementById('info-body');
  body.style.color=d.bodyC; body.innerHTML=d.body;
  const nf=document.getElementById('info-nf');
  if(d.nf){
    nf.style.display='block'; nf.style.background=d.nfBg; nf.style.color=d.nfC;
    document.getElementById('info-nf-label').textContent=d.nfLabel;
    document.getElementById('info-nf-label').style.color=d.nfC;
    document.getElementById('info-nf-text').textContent=d.nf;
  } else { nf.style.display='none'; }
  const ex=document.getElementById('info-ex');
  ex.style.display='block'; ex.style.background=d.exBg; ex.style.color=d.exC; ex.textContent=d.ex;
}
</script>
</body></html>
"""


def get_diagram_height(diagram_id: str) -> int:
    heights = {
        "context_window": 320,
        "rtcfc": 245,
        "connector_ecosystem": 380,
        "project_structure": 260,
        "agent_loop": 420,
        "ml_pipeline": 290,
        "plugins_by_role": 300,
        "decision_tree": 360,
        "meta_prompting": 290,
        "nlp_clinical": 650,
        "model_comparison": 300,
        "hallucination_check": 400,
        "gating": 540,
        "ai_hierarchy": 620,
    }
    return heights.get(diagram_id, 300)
