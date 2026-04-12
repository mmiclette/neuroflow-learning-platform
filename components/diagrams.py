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
<text x="340" y="68" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#757575">Common model types</text>
<line x1="262" y1="78" x2="418" y2="78" stroke="#C0C4E8" stroke-width="0.5"/>
<text x="340" y="100" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#161BAA" font-weight="600">Logistic regression</text>
<text x="340" y="116" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">Binary outcomes; interpretable</text>
<text x="340" y="144" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#161BAA" font-weight="600">Random forest</text>
<text x="340" y="160" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">Handles mixed data; robust</text>
<text x="340" y="188" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="11" fill="#161BAA" font-weight="600">Gradient boosting</text>
<text x="340" y="204" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#444444">High accuracy on health data</text>
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


def get_diagram_height(diagram_id: str) -> int:
    heights = {
        "context_window": 320,
        "rtcfc": 245,
        "connector_ecosystem": 380,
        "project_structure": 260,
        "agent_loop": 420,
        "ml_pipeline": 310,
        "plugins_by_role": 300,
        "decision_tree": 360,
        "meta_prompting": 290,
    }
    return heights.get(diagram_id, 300)
