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
<text x="272" y="30" text-anchor="middle" dominant-baseline="central" font-family="sans-serif" font-size="10" fill="#616161">Older messages — dropped when context overflows</text>
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
DIAGRAMS["decision_tree"] = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Choosing the Right Approach</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display&display=swap" rel="stylesheet">
<style>
  :root {
    --nf-primary:         #161B4A;
    --nf-secondary-blue:  #2E4799;
    --nf-secondary-light: #478FCC;
    --nf-secondary-teal:  #4CB6AC;
    --nf-accent:          #F16061;
    --nf-text-primary:    #212121;
    --nf-text-secondary:  #757575;
    --nf-text-on-dark:    #FFFFFF;
    --nf-divider:         #BDBDBD;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: 'DM Sans', sans-serif;
    background: #F4F6FB;
    padding: 48px 32px;
    min-height: 100vh;
  }

  .page-title {
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    color: var(--nf-primary);
    text-align: center;
    margin-bottom: 36px;
    letter-spacing: -0.3px;
  }

  .cards {
    display: flex;
    gap: 16px;
    justify-content: center;
    flex-wrap: wrap;
    max-width: 1100px;
    margin: 0 auto;
  }

  .card {
    background: #fff;
    border-radius: 14px;
    overflow: hidden;
    width: 190px;
    box-shadow: 0 2px 12px rgba(22,27,74,0.09);
    display: flex;
    flex-direction: column;
    transition: transform 0.18s ease, box-shadow 0.18s ease;
  }

  .card:hover {
    transform: translateY(-4px);
    box-shadow: 0 8px 24px rgba(22,27,74,0.14);
  }

  .card-header {
    padding: 18px 16px 14px;
    color: var(--nf-text-on-dark);
    text-align: center;
  }

  .card-header .label {
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    opacity: 0.88;
    margin-bottom: 6px;
  }

  .card-header .headline {
    font-family: 'DM Serif Display', serif;
    font-size: 17px;
    line-height: 1.25;
  }

  .card-body {
    padding: 16px;
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .divider {
    height: 1px;
    background: var(--nf-divider);
    opacity: 0.5;
  }

  .description {
    font-size: 12.5px;
    color: var(--nf-text-primary);
    line-height: 1.55;
    text-align: center;
  }

  .examples {
    font-size: 11.5px;
    color: var(--nf-text-secondary);
    text-align: center;
    font-style: italic;
    line-height: 1.5;
  }

  /* Card color schemes */
  .card-prompt .card-header   { background: var(--nf-primary); }
  .card-connector .card-header { background: var(--nf-secondary-light); }
  .card-skill .card-header    { background: var(--nf-secondary-teal); }
  .card-plugin .card-header   { background: var(--nf-secondary-blue); }
  .card-combo .card-header    {
    background: linear-gradient(135deg, var(--nf-secondary-blue) 0%, var(--nf-secondary-teal) 100%);
  }

  /* Headline color in body matches header */
  .card-prompt   .body-headline { color: var(--nf-primary); }
  .card-connector .body-headline { color: var(--nf-secondary-light); }
  .card-skill    .body-headline { color: var(--nf-secondary-teal); }
  .card-plugin   .body-headline { color: var(--nf-secondary-blue); }
  .card-combo    .body-headline { color: var(--nf-secondary-blue); }

  .body-headline {
    font-size: 13px;
    font-weight: 700;
    text-align: center;
  }
</style>
</head>
<body>

<p class="page-title">Choosing the Right Approach</p>

<div class="cards">

  <!-- Prompt -->
  <div class="card card-prompt">
    <div class="card-header">
      <div class="label">Prompt or Project</div>
      <div class="headline">Deliverable is text?</div>
    </div>
    <div class="card-body">
      <div class="body-headline">Everything you need is already here</div>
      <div class="divider"></div>
      <div class="description">All inputs are in the conversation and the output is text. Use a Project when you want Claude to remember your context across multiple conversations.</div>
      <div class="divider"></div>
      <div class="examples">Drafts, analysis, briefs, summaries, reports</div>
    </div>
  </div>

  <!-- Connector -->
  <div class="card card-connector">
    <div class="card-header">
      <div class="label">Connector</div>
      <div class="headline">Need outside data?</div>
    </div>
    <div class="card-body">
      <div class="body-headline">The information lives somewhere else</div>
      <div class="divider"></div>
      <div class="description">Claude pulls information from or takes action in another tool like Slack, Drive, or your CRM.</div>
      <div class="divider"></div>
      <div class="examples">Gmail, Salesforce, Drive, Slack</div>
    </div>
  </div>

  <!-- Skill -->
  <div class="card card-skill">
    <div class="card-header">
      <div class="label">Skill</div>
      <div class="headline">Need Claude to work a certain way?</div>
    </div>
    <div class="card-body">
      <div class="body-headline">You repeat this type of task often</div>
      <div class="divider"></div>
      <div class="description">Activate a skill in any chat. Claude applies your standards to that task type without you explaining them again.</div>
      <div class="divider"></div>
      <div class="examples">Slide templates, contract review, RFP review and setup</div>
    </div>
  </div>

  <!-- Plugin -->
  <div class="card card-plugin">
    <div class="card-header">
      <div class="label">Plugin</div>
      <div class="headline">Need to automate?</div>
    </div>
    <div class="card-body">
      <div class="body-headline">Claude runs the whole job in Cowork</div>
      <div class="divider"></div>
      <div class="description">Claude executes a multi-step automated process on its own in Cowork. Use a plugin even when external tools are involved — if the task runs automatically across multiple steps, plugin wins over connector alone. Your team installs it once and it works the same way every time.</div>
      <div class="divider"></div>
      <div class="examples">Sales process, Legal review, Finance reporting</div>
    </div>
  </div>

  <!-- Combo -->
  <div class="card card-combo">
    <div class="card-header">
      <div class="label">Connector + Skill or Plugin</div>
      <div class="headline">Need both?</div>
    </div>
    <div class="card-body">
      <div class="body-headline">You need data from outside and Claude to act on it</div>
      <div class="divider"></div>
      <div class="description">Pull data from one or more external tools and apply a skill or plugin to work with it. If the task stops at retrieving and analyzing information, this is your lane. If it also needs to run automatically on a schedule, move to Plugin.</div>
      <div class="divider"></div>
      <div class="examples">Drive files + analysis template, CRM data + sales workflow</div>
    </div>
  </div>

</div>
</body>
</html>

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



# ---------------------------------------------------------------------------
# Lesson 3.4 — XML tags callout
# ---------------------------------------------------------------------------
DIAGRAMS["xml_tags_callout"] = """
<svg width="100%" viewBox="0 0 680 120" role="img" xmlns="http://www.w3.org/2000/svg">
<title>XML tags key insight</title>
<defs>
  <clipPath id="xmltop"><rect x="10" y="8" width="660" height="104" rx="8"/></clipPath>
</defs>
<rect x="10" y="8" width="660" height="104" rx="8" fill="#E8E9F7" stroke="#161BAA" stroke-width="1.5"/>
<rect x="10" y="8" width="660" height="52" clip-path="url(#xmltop)" fill="#161BAA"/>
<text x="28" y="28" font-family="sans-serif" font-size="11" fill="rgba(255,255,255,0.72)">Before covering XML tags,</text>
<text x="28" y="47" font-family="sans-serif" font-size="11.5" font-weight="500" fill="white">a direct answer to the most important question:</text>
<text x="28" y="88" font-family="sans-serif" font-size="18" font-weight="700" fill="#161BAA">You do not need them most of the time.</text>
</svg>
"""


# ---------------------------------------------------------------------------
# Lesson 3.6 — Meta-prompt comparison diagram
# ---------------------------------------------------------------------------
DIAGRAMS["meta_prompt_diagram"] = """
<html><head><style>
body{margin:0;padding:10px 2px 4px;background:transparent;}
</style></head><body>
<style>
*{box-sizing:border-box;}
body,div,span{font-family:var(--font-sans,sans-serif);}
.col-hdr{border-radius:8px;padding:10px 14px;font-size:13px;font-weight:500;color:#fff;margin-bottom:12px;}
.step{border-radius:8px;padding:12px 14px;}
.step-title{font-size:13px;font-weight:500;color:#212121;margin-bottom:3px;}
.step-sub{font-size:11px;color:#757575;}
.step-quote{font-size:11px;color:#4a4a4a;font-style:italic;margin-top:6px;line-height:1.55;}
.arr{display:flex;justify-content:center;margin:5px 0;}
.badge{display:inline-block;font-size:10px;font-weight:500;padding:2px 7px;border-radius:4px;color:#fff;white-space:nowrap;flex-shrink:0;margin-top:2px;}
.out-row{display:flex;gap:10px;margin-bottom:11px;align-items:flex-start;}
.out-text{font-size:12px;color:#C8D4E8;line-height:1.6;}
</style>
<div style="padding:4px 0 0;">
<div style="display:grid;grid-template-columns:1fr 1px 1fr;gap:0 18px;margin-bottom:18px;">
  <div>
    <div class="col-hdr" style="background:#F16061;">Direct approach</div>
    <div class="step" style="background:#FEF0F0;border:0.5px solid #F8A9AA;">
      <div class="step-title">Type a vague request</div>
      <div class="step-quote">"Help me prepare for a meeting with a state Medicaid director about renewing our behavioral health pilot."</div>
    </div>
    <div class="arr"><svg width="10" height="14" viewBox="0 0 10 14" fill="none"><line x1="5" y1="0" x2="5" y2="11" stroke="#2E4799" stroke-width="1.5" stroke-linecap="round"/><path d="M2 8L5 12L8 8" stroke="#2E4799" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
    <div class="step" style="background:#FEF0F0;border:0.5px solid #F8A9AA;">
      <div class="step-title">Claude fills in the gaps</div>
      <div class="step-sub">Scope, format, and goal left undefined</div>
    </div>
    <div class="arr"><svg width="10" height="14" viewBox="0 0 10 14" fill="none"><line x1="5" y1="0" x2="5" y2="11" stroke="#2E4799" stroke-width="1.5" stroke-linecap="round"/><path d="M2 8L5 12L8 8" stroke="#2E4799" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
    <div class="step" style="background:#FEF0F0;border:0.5px solid #F8A9AA;">
      <div class="step-title">Generic output</div>
      <div class="step-sub">What "prepared" means was never defined</div>
    </div>
  </div>
  <div style="background:#BDBDBD;"></div>
  <div>
    <div class="col-hdr" style="background:#4CB6AC;">Meta-prompt approach</div>
    <div class="step" style="background:#E8F7F6;border:0.5px solid #9ED8D4;">
      <div class="step-title">Ask Claude to write the prompt</div>
      <div class="step-quote">"I have a high-stakes meeting tomorrow and I'm not sure what I need. Write a prompt I can use to prepare for a meeting with a state Medicaid director about renewing a behavioral health pilot."</div>
    </div>
    <div class="arr"><svg width="10" height="14" viewBox="0 0 10 14" fill="none"><line x1="5" y1="0" x2="5" y2="11" stroke="#2E4799" stroke-width="1.5" stroke-linecap="round"/><path d="M2 8L5 12L8 8" stroke="#2E4799" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
    <div class="step" style="background:#E8F7F6;border:0.5px solid #9ED8D4;">
      <div class="step-title">Claude defines the brief</div>
      <div class="step-sub">Identifies priorities, objections, framing, and format</div>
    </div>
    <div class="arr"><svg width="10" height="14" viewBox="0 0 10 14" fill="none"><line x1="5" y1="0" x2="5" y2="11" stroke="#2E4799" stroke-width="1.5" stroke-linecap="round"/><path d="M2 8L5 12L8 8" stroke="#2E4799" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
    <div class="step" style="background:#E8F7F6;border:0.5px solid #9ED8D4;">
      <div class="step-title">Receive a working prompt</div>
      <div class="step-sub">Structured and targeted — ready to run or refine</div>
    </div>
    <div class="arr"><svg width="10" height="14" viewBox="0 0 10 14" fill="none"><line x1="5" y1="0" x2="5" y2="11" stroke="#2E4799" stroke-width="1.5" stroke-linecap="round"/><path d="M2 8L5 12L8 8" stroke="#2E4799" stroke-width="1.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
    <div class="step" style="background:#4CB6AC;">
      <div style="font-size:13px;font-weight:500;color:#fff;">Run or tailor the result</div>
    </div>
  </div>
</div>
<div style="background:#161B4A;border-radius:10px;padding:18px 20px;margin-bottom:12px;">
  <div style="font-size:10px;font-weight:500;color:#4CB6AC;letter-spacing:0.07em;margin-bottom:14px;">EXAMPLE — STRUCTURED PROMPT CLAUDE RETURNS</div>
  <div class="out-row">
    <span class="badge" style="background:#4CB6AC;">Role</span>
    <span class="out-text">You are a strategic communications advisor with experience in state Medicaid policy and behavioral health.</span>
  </div>
  <div class="out-row">
    <span class="badge" style="background:#478FCC;">Context</span>
    <span class="out-text">I have a meeting tomorrow with a state Medicaid director about renewing a behavioral health pilot program.</span>
  </div>
  <div class="out-row">
    <span class="badge" style="background:#F16061;">Task</span>
    <span class="out-text">Help me prepare by covering: the two or three things a Medicaid director typically prioritizes at pilot renewal (cost containment, outcomes data, scalability), likely objections I should be ready to address, how to frame the value of continuing the pilot in terms that resonate with state budget and population health goals, and what I should avoid leading with.</span>
  </div>
  <div class="out-row" style="margin-bottom:0;">
    <span class="badge" style="background:#2E4799;">Format</span>
    <span class="out-text">Format this as a prep brief I can read in ten minutes the morning of the meeting.</span>
  </div>
</div>
<div style="background:#2E4799;border-radius:8px;padding:12px 16px;text-align:center;">
  <span style="font-size:12px;color:#fff;">You didn't need to know what to ask. Claude figured out what "prepared" means for you.</span>
</div>
</div>
</body></html>
"""

DIAGRAMS["choosing_tool_cards"] = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Choosing the Right Tool</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">
<style>
  :root {
    --navy: #161B4A;
    --blue-1: #2E4799;
    --blue-2: #478FCC;
    --teal: #4CB6AC;
    --accent: #F16061;
    --accent-inactive: #F8A9AA;
    --text-primary: #212121;
    --text-secondary: #757575;
    --text-white: #FFFFFF;
    --divider: #BDBDBD;
    --bg-light: #F4F6FB;
  }

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--bg-light);
    color: var(--text-primary);
    padding: 16px 8px;
  }

  .wrapper {
    max-width: 1100px;
    margin: 0 auto;
  }

  .header {
    margin-bottom: 18px;
  }

  .header h1 {
    font-family: 'DM Serif Display', serif;
    font-size: 22px;
    color: var(--navy);
    margin-bottom: 10px;
    line-height: 1.2;
  }

  .framing {
    background: white;
    border-left: 3px solid var(--blue-2);
    border-radius: 0 6px 6px 0;
    padding: 12px 14px;
    font-size: 12.5px;
    line-height: 1.6;
    color: var(--text-primary);
  }

  .framing strong {
    color: var(--navy);
  }

  .cards-grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 12px;
    margin-top: 16px;
  }

  .card-wrapper {
    perspective: 1200px;
    height: 460px;
    cursor: pointer;
    position: relative;
  }

  .card-inner {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    transition: transform 0.65s cubic-bezier(0.4, 0, 0.2, 1);
    will-change: transform;
  }

  .card-wrapper.flipped .card-inner {
    transform: rotateY(180deg);
  }

  .card-front,
  .card-back {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    backface-visibility: hidden;
    -webkit-backface-visibility: hidden;
    border-radius: 12px;
    overflow: hidden;
  }

  .card-front {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 20px 18px;
    color: var(--text-white);
    position: relative;
  }

  .card-front::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(160deg, rgba(255,255,255,0.08) 0%, transparent 60%);
    pointer-events: none;
  }

  .card-1 .card-front { background: linear-gradient(145deg, var(--blue-1) 0%, var(--blue-2) 100%); }
  .card-2 .card-front { background: linear-gradient(145deg, var(--navy) 0%, var(--blue-1) 100%); }
  .card-3 .card-front { background: linear-gradient(145deg, #2a7a74 0%, var(--teal) 100%); }

  .card-icon {
    width: 38px;
    height: 38px;
    background: rgba(255,255,255,0.15);
    border-radius: 10px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 14px;
  }

  .card-icon svg {
    width: 20px;
    height: 20px;
    fill: none;
    stroke: white;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  .card-front-content {
    flex: 1;
  }

  .card-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    opacity: 0.7;
    margin-bottom: 6px;
  }

  .card-title {
    font-family: 'DM Serif Display', serif;
    font-size: 20px;
    line-height: 1.15;
    margin-bottom: 10px;
  }

  .card-tagline {
    font-size: 12px;
    line-height: 1.55;
    opacity: 0.9;
    font-weight: 300;
  }

  .card-front-footer {
    margin-top: 14px;
    padding-top: 12px;
    border-top: 1px solid rgba(255,255,255,0.2);
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .flip-hint {
    font-size: 12px;
    opacity: 0.7;
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .flip-hint svg {
    width: 14px;
    height: 14px;
    fill: none;
    stroke: white;
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
    opacity: 0.7;
  }

  .cost-badge {
    font-size: 11px;
    font-weight: 600;
    padding: 4px 10px;
    border-radius: 20px;
    background: rgba(255,255,255,0.18);
    letter-spacing: 0.04em;
  }

  .card-back {
    transform: rotateY(180deg);
    background: white;
    padding: 14px 14px 0;
    display: flex;
    flex-direction: column;
    border: 1px solid var(--divider);
    overflow: hidden;
  }

  .card-back-scroll {
    flex: 1;
    overflow-y: auto;
    padding-bottom: 16px;
    scrollbar-width: thin;
    scrollbar-color: var(--divider) transparent;
  }

  .card-back-scroll::-webkit-scrollbar {
    width: 4px;
  }

  .card-back-scroll::-webkit-scrollbar-track {
    background: transparent;
  }

  .card-back-scroll::-webkit-scrollbar-thumb {
    background: var(--divider);
    border-radius: 4px;
  }

  .card-back-footer {
    flex-shrink: 0;
    padding: 10px 0 14px;
    background: white;
    border-top: 1px solid var(--bg-light);
  }

  .back-header {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 10px;
    padding-bottom: 10px;
    border-bottom: 2px solid var(--bg-light);
    flex-shrink: 0;
  }

  .back-dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    flex-shrink: 0;
  }

  .card-1 .back-dot { background: var(--blue-2); }
  .card-2 .back-dot { background: var(--blue-1); }
  .card-3 .back-dot { background: var(--teal); }

  .back-title {
    font-family: 'DM Serif Display', serif;
    font-size: 16px;
    color: var(--navy);
  }

  .back-section {
    margin-bottom: 8px;
    flex-shrink: 0;
  }

  .back-section-label {
    font-size: 9px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-secondary);
    margin-bottom: 4px;
  }

  .back-section p {
    font-size: 11.5px;
    line-height: 1.55;
    color: var(--text-primary);
  }

  .back-list {
    list-style: none;
    padding: 0;
  }

  .back-list li {
    font-size: 11px;
    line-height: 1.45;
    color: var(--text-primary);
    padding: 3px 0 3px 14px;
    position: relative;
    border-bottom: 1px solid var(--bg-light);
  }

  .back-list li:last-child {
    border-bottom: none;
  }

  .back-list li::before {
    content: '';
    position: absolute;
    left: 0;
    top: 13px;
    width: 6px;
    height: 6px;
    border-radius: 50%;
  }

  .card-1 .back-list.use li::before { background: var(--blue-2); }
  .card-2 .back-list.use li::before { background: var(--blue-1); }
  .card-3 .back-list.use li::before { background: var(--teal); }

  .back-list.avoid li::before { background: var(--accent-inactive); }

  .cost-row {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-shrink: 0;
    margin-bottom: 6px;
  }

  .cost-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--text-secondary);
  }

  .cost-dots {
    display: flex;
    gap: 4px;
  }

  .cost-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--divider);
  }

  .cost-dot.filled { background: var(--navy); }

  .cost-desc {
    font-size: 11px;
    color: var(--text-secondary);
    margin-left: auto;
  }

  .back-flip-back {
    display: flex;
    align-items: center;
    gap: 5px;
    font-size: 11px;
    color: var(--text-secondary);
    margin-top: 8px;
    cursor: pointer;
    flex-shrink: 0;
  }

  .back-flip-back svg {
    width: 12px;
    height: 12px;
    fill: none;
    stroke: var(--text-secondary);
    stroke-width: 2;
    stroke-linecap: round;
    stroke-linejoin: round;
  }

  .card-wrapper:hover .card-front {
    filter: brightness(1.04);
  }

  @media (max-width: 480px) {
    .cards-grid {
      grid-template-columns: 1fr;
    }
    .card-wrapper {
      height: 460px;
    }
  }
</style>
</head>
<body>
<div class="wrapper">

  <div class="header">
    <h1>Choosing the Right Tool</h1>
    <div class="framing">
      <strong>Web Search</strong> and <strong>Research</strong> go outside the conversation to find information you do not have yet.
      <strong>Adaptive Thinking</strong> stays inside the conversation and reasons more carefully through information you have already provided.
      The right choice depends on whether your challenge is <em>finding</em> information or <em>thinking through</em> it.
      <br><br>
      Click any card to learn more.
    </div>
  </div>

  <div class="cards-grid">

    <div class="card-wrapper card-1" onclick="flipCard(this)">
      <div class="card-inner">
        <div class="card-front">
          <div>
            <div class="card-icon">
              <svg viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
            </div>
            <div class="card-front-content">
              <div class="card-label">Feature 01</div>
              <div class="card-title">Web Search</div>
              <div class="card-tagline">You need a current fact. Claude retrieves it from the web and brings it back into your conversation without you leaving the chat.</div>
            </div>
          </div>
          <div class="card-front-footer">
            <div class="flip-hint">
              <svg viewBox="0 0 24 24"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/></svg>
              Tap to flip
            </div>
            <div class="cost-badge">Light</div>
          </div>
        </div>
        <div class="card-back">
          <div class="back-header">
            <div class="back-dot"></div>
            <div class="back-title">Web Search</div>
          </div>
          <div class="card-back-scroll">
            <div class="back-section">
              <div class="back-section-label">What it does</div>
              <p>Retrieves current information from the internet during a standard conversation. Claude searches and brings findings back into your chat. Enable it via the plus button menu and tell Claude explicitly to search.</p>
            </div>
            <div class="back-section">
              <div class="back-section-label">Use this when</div>
              <ul class="back-list use">
                <li>Checking the current status of a CMS program or federal regulation</li>
                <li>Confirming whether a partner, policy, or organization still exists in its current form</li>
                <li>Quick fact checks on recent developments before including them in a document</li>
              </ul>
            </div>
            <div class="back-section">
              <div class="back-section-label">Do not use when</div>
              <ul class="back-list avoid">
                <li>You need synthesis across many sources</li>
                <li>You already have the documents and need Claude to reason through them</li>
                <li>One search result would not be sufficient</li>
              </ul>
            </div>
          </div>
          <div class="card-back-footer">
            <div class="cost-row">
              <div class="cost-label">Cost</div>
              <div class="cost-dots">
                <div class="cost-dot filled"></div>
                <div class="cost-dot"></div>
                <div class="cost-dot"></div>
              </div>
              <div class="cost-desc">Light</div>
            </div>
            <div class="back-flip-back">
              <svg viewBox="0 0 24 24"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/></svg>
              Tap to flip back
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="card-wrapper card-2" onclick="flipCard(this)">
      <div class="card-inner">
        <div class="card-front">
          <div>
            <div class="card-icon">
              <svg viewBox="0 0 24 24"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
            </div>
            <div class="card-front-content">
              <div class="card-label">Feature 02</div>
              <div class="card-title">Research</div>
              <div class="card-tagline">You need comprehensive findings from many sources. Claude investigates autonomously and returns a structured, cited report.</div>
            </div>
          </div>
          <div class="card-front-footer">
            <div class="flip-hint">
              <svg viewBox="0 0 24 24"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/></svg>
              Tap to flip
            </div>
            <div class="cost-badge">Heavy</div>
          </div>
        </div>
        <div class="card-back">
          <div class="back-header">
            <div class="back-dot"></div>
            <div class="back-title">Research</div>
          </div>
          <div class="card-back-scroll">
            <div class="back-section">
              <div class="back-section-label">What it does</div>
              <p>Runs an autonomous multi-source investigation. Claude searches, evaluates findings, identifies gaps, and compiles a structured citation-backed report. You start with a question and end with sourced findings you did not have before. Access it via the plus button menu.</p>
            </div>
            <div class="back-section">
              <div class="back-section-label">Use this when</div>
              <ul class="back-list use">
                <li>Building a competitive landscape brief on behavioral health technology vendors from scratch</li>
                <li>Surveying how state Medicaid programs structure value-based behavioral health contracts</li>
                <li>Gathering comprehensive background on a federal partner before a high-stakes meeting</li>
              </ul>
            </div>
            <div class="back-section">
              <div class="back-section-label">Do not use when</div>
              <ul class="back-list avoid">
                <li>You already have the documents and the challenge is reasoning through them</li>
                <li>You need a single current fact</li>
                <li>One web search would answer the question</li>
              </ul>
            </div>
          </div>
          <div class="card-back-footer">
            <div class="cost-row">
              <div class="cost-label">Cost</div>
              <div class="cost-dots">
                <div class="cost-dot filled"></div>
                <div class="cost-dot filled"></div>
                <div class="cost-dot filled"></div>
              </div>
              <div class="cost-desc">Heavy</div>
            </div>
            <div class="back-flip-back">
              <svg viewBox="0 0 24 24"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/></svg>
              Tap to flip back
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="card-wrapper card-3" onclick="flipCard(this)">
      <div class="card-inner">
        <div class="card-front">
          <div>
            <div class="card-icon">
              <svg viewBox="0 0 24 24"><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><line x1="12" y1="17" x2="12.01" y2="17"/><circle cx="12" cy="12" r="10"/></svg>
            </div>
            <div class="card-front-content">
              <div class="card-label">Feature 03</div>
              <div class="card-title">Adaptive Thinking</div>
              <div class="card-tagline">You already have the content. Claude reasons through it more carefully before responding. No external search. No new information.</div>
            </div>
          </div>
          <div class="card-front-footer">
            <div class="flip-hint">
              <svg viewBox="0 0 24 24"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/></svg>
              Tap to flip
            </div>
            <div class="cost-badge">Varies</div>
          </div>
        </div>
        <div class="card-back">
          <div class="back-header">
            <div class="back-dot"></div>
            <div class="back-title">Adaptive Thinking</div>
          </div>
          <div class="card-back-scroll">
            <div class="back-section">
              <div class="back-section-label">What it does</div>
              <p>Lets Claude reason more carefully through information already in the conversation. It does not search the web or retrieve anything external. Toggle it under the model selector. Enabling it starts a new chat.</p>
            </div>
            <div class="back-section">
              <div class="back-section-label">Use this when</div>
              <ul class="back-list use">
                <li>You have uploaded contracts or RFPs and need Claude to identify key differences or risks</li>
                <li>You have pasted a complex policy document and need thorough reasoning through its implications</li>
                <li>You are working through a multi-variable decision where the reasoning chain must be defensible externally</li>
              </ul>
            </div>
            <div class="back-section">
              <div class="back-section-label">Do not use when</div>
              <ul class="back-list avoid">
                <li>You need information Claude does not already have</li>
                <li>The task is straightforward and does not require deep reasoning</li>
                <li>Response time matters more than reasoning depth</li>
              </ul>
            </div>
          </div>
          <div class="card-back-footer">
            <div class="cost-row">
              <div class="cost-label">Cost</div>
              <div class="cost-dots">
                <div class="cost-dot filled"></div>
                <div class="cost-dot filled"></div>
                <div class="cost-dot"></div>
              </div>
              <div class="cost-desc">Varies with complexity</div>
            </div>
            <div class="back-flip-back">
              <svg viewBox="0 0 24 24"><path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/></svg>
              Tap to flip back
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</div>

<script>
  function flipCard(card) {
    card.classList.toggle('flipped');
  }
</script>
</body>
</html>
"""

DIAGRAMS["style_layers"] = """<html><head><style>
body{margin:0;padding:8px 4px;background:transparent;font-family:'DM Sans',-apple-system,'system-ui','Segoe UI',sans-serif;}
</style></head><body>
<svg width="100%" viewBox="0 0 680 460" role="img" xmlns="http://www.w3.org/2000/svg">
  <title>Four layers of Claude output customization: voice, tone, style, and format</title>
  <desc>A table showing four customization layers with definitions and examples using NeuroFlow brand colors.</desc>

  <text x="40" y="32" fill="#757575" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:500;letter-spacing:0.04em;text-transform:uppercase;">Layer</text>
  <text x="200" y="32" fill="#757575" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:500;letter-spacing:0.04em;text-transform:uppercase;">What it controls</text>
  <text x="474" y="32" fill="#757575" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:500;letter-spacing:0.04em;text-transform:uppercase;">Example</text>

  <line x1="40" y1="44" x2="640" y2="44" stroke="#BDBDBD" stroke-width="0.5"/>
  <line x1="40" y1="144" x2="640" y2="144" stroke="#BDBDBD" stroke-width="0.5"/>
  <line x1="40" y1="244" x2="640" y2="244" stroke="#BDBDBD" stroke-width="0.5"/>
  <line x1="40" y1="344" x2="640" y2="344" stroke="#BDBDBD" stroke-width="0.5"/>
  <line x1="40" y1="444" x2="640" y2="444" stroke="#BDBDBD" stroke-width="0.5"/>

  <line x1="460" y1="44" x2="460" y2="444" stroke="#BDBDBD" stroke-width="0.5"/>

  <!-- Row 1: Voice -->
  <rect x="40" y="60" width="130" height="72" rx="8" fill="#161B4A"/>
  <text x="105" y="91" text-anchor="middle" dominant-baseline="central" fill="#FFFFFF" style="font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;">Voice</text>
  <text x="105" y="112" text-anchor="middle" dominant-baseline="central" fill="rgba(255,255,255,0.75)" style="font-family:'DM Sans',sans-serif;font-size:11px;font-weight:400;">active vs passive</text>
  <text x="200" y="84" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">Whether the actor leads the sentence.</text>
  <text x="200" y="101" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">Active voice is direct and clear.</text>
  <text x="200" y="118" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">Passive voice softens and distances.</text>
  <text x="474" y="88" fill="#444444" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;font-style:italic;">Active: Claude drafts it.</text>
  <text x="474" y="108" fill="#444444" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;font-style:italic;">Passive: It is drafted.</text>

  <!-- Row 2: Tone -->
  <rect x="40" y="160" width="130" height="72" rx="8" fill="#2E4799"/>
  <text x="105" y="191" text-anchor="middle" dominant-baseline="central" fill="#FFFFFF" style="font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;">Tone</text>
  <text x="105" y="212" text-anchor="middle" dominant-baseline="central" fill="rgba(255,255,255,0.75)" style="font-family:'DM Sans',sans-serif;font-size:11px;font-weight:400;">emotional quality</text>
  <text x="200" y="184" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">The attitude Claude brings to content.</text>
  <text x="200" y="201" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">Confident, warm, clinical, urgent.</text>
  <text x="200" y="218" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">Same information, different reception.</text>
  <text x="474" y="188" fill="#444444" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;font-style:italic;">Confident: This works.</text>
  <text x="474" y="208" fill="#444444" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;font-style:italic;">Hedged: Worth considering.</text>

  <!-- Row 3: Style -->
  <rect x="40" y="260" width="130" height="72" rx="8" fill="#478FCC"/>
  <text x="105" y="291" text-anchor="middle" dominant-baseline="central" fill="#FFFFFF" style="font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;">Style</text>
  <text x="105" y="312" text-anchor="middle" dominant-baseline="central" fill="rgba(255,255,255,0.9)" style="font-family:'DM Sans',sans-serif;font-size:11px;font-weight:400;">overall register</text>
  <text x="200" y="284" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">The level of formality and complexity.</text>
  <text x="200" y="301" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">Formal, conversational, technical.</text>
  <text x="200" y="318" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">Shapes vocabulary and sentence length.</text>
  <text x="474" y="288" fill="#444444" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;font-style:italic;">Formal: We recommend.</text>
  <text x="474" y="308" fill="#444444" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;font-style:italic;">Casual: Here's our take.</text>

  <!-- Row 4: Format -->
  <rect x="40" y="360" width="130" height="72" rx="8" fill="#4CB6AC"/>
  <text x="105" y="391" text-anchor="middle" dominant-baseline="central" fill="#FFFFFF" style="font-family:'DM Sans',sans-serif;font-size:14px;font-weight:600;">Format</text>
  <text x="105" y="412" text-anchor="middle" dominant-baseline="central" fill="rgba(255,255,255,0.9)" style="font-family:'DM Sans',sans-serif;font-size:11px;font-weight:400;">structure and length</text>
  <text x="200" y="384" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">How the output is laid out on the page.</text>
  <text x="200" y="401" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">Bullets vs paragraphs, headers, length.</text>
  <text x="200" y="418" fill="#212121" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;">Affects scannability and document feel.</text>
  <text x="474" y="388" fill="#444444" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;font-style:italic;">Paragraphs: full sentences.</text>
  <text x="474" y="408" fill="#444444" style="font-family:'DM Sans',sans-serif;font-size:12px;font-weight:400;font-style:italic;">Structured: bullets only.</text>
</svg>
</body></html>
"""

DIAGRAMS["plugin_ui_diagram"] = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cowork Plugin Interface</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --nf-primary: #161B4A;
    --nf-secondary-blue: #2E4799;
    --nf-secondary-light: #478FCC;
    --nf-secondary-teal: #4CB6AC;
    --nf-accent: #F16061;
    --nf-text-primary: #212121;
    --nf-text-secondary: #757575;
    --nf-divider: #BDBDBD;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #ECEEF4;
    font-family: 'DM Sans', sans-serif;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    min-height: 0;
    padding: 4px 12px 16px;
  }

  .wrapper { width: 100%; max-width: 1020px; }

  .lesson-label {
    font-size: 11px; font-weight: 600; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--nf-secondary-blue); margin-bottom: 6px;
  }
  .lesson-title { font-size: 18px; font-weight: 600; color: var(--nf-primary); margin-bottom: 3px; }
  .lesson-sub { font-size: 12px; color: var(--nf-text-secondary); margin-bottom: 14px; }

  /* Window */
  .window {
    background: #1C1C1E;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 20px 60px rgba(22,27,74,0.25);
  }

  .title-bar {
    background: #2A2A2C;
    height: 40px;
    display: flex;
    align-items: center;
    padding: 0 16px;
    gap: 8px;
    border-bottom: 1px solid #3A3A3C;
    flex-shrink: 0;
  }

  .dot { width: 12px; height: 12px; border-radius: 50%; }
  .dot-r { background: #FF5F57; }
  .dot-y { background: #FEBC2E; }
  .dot-g { background: #28C840; }

  .window-title { font-size: 13px; font-weight: 600; color: #DDDDE0; margin-left: 12px; }

  /* Two panels */
  .panels { display: flex; height: 540px; }

  /* Left nav — not scrollable, annotations stay put */
  .left-nav {
    width: 220px;
    background: #242426;
    border-right: 1px solid #3A3A3C;
    padding: 10px 0;
    flex-shrink: 0;
    overflow-y: auto;
  }

  .nav-item {
    display: flex; align-items: center; gap: 8px;
    padding: 7px 16px; font-size: 12px; color: #8E8E93; cursor: pointer;
  }
  .nav-item:hover { background: #2E2E30; }
  .nav-divider { height: 1px; background: #3A3A3C; margin: 6px 0; }

  .nav-section-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 8px 16px 4px;
  }
  .nav-section-label {
    font-size: 10px; font-weight: 600; letter-spacing: 0.08em;
    text-transform: uppercase; color: #636366;
  }
  .nav-add-btn {
    width: 16px; height: 16px; border-radius: 50%;
    border: 1px solid #48484A; display: flex; align-items: center;
    justify-content: center; color: #636366; font-size: 12px; cursor: pointer;
  }

  .nav-plugin-row {
    display: flex; align-items: center; gap: 8px;
    padding: 7px 16px; font-size: 12px; color: #8E8E93; cursor: pointer;
  }
  .nav-plugin-row.active {
    background: rgba(71,143,204,0.15); color: #FFFFFF;
    border-left: 2px solid var(--nf-secondary-light);
  }
  .nav-plugin-row:hover:not(.active) { background: #2E2E30; }

  .nav-sub-item {
    display: flex; align-items: center; gap: 8px;
    padding: 5px 16px 5px 34px; font-size: 11px; color: #636366; cursor: pointer;
  }
  .nav-sub-item:hover { background: #2E2E30; color: #8E8E93; }

  .nav-org-note {
    font-size: 10px; color: #48484A;
    padding: 6px 16px; font-style: italic; line-height: 1.5;
  }

  /* Annotation ring — placed inline, not as overlay */
  .annotated {
    position: relative;
  }

  .anno-ring {
    position: absolute;
    border: 2px solid var(--nf-accent);
    border-radius: 6px;
    pointer-events: none;
    animation: blink 2.4s ease-in-out infinite;
    z-index: 10;
  }

  @keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
  }

  .anno-badge {
    position: absolute;
    width: 24px; height: 24px; border-radius: 50%;
    background: var(--nf-accent); color: white;
    font-size: 12px; font-weight: 700;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 2px 10px rgba(241,96,97,0.5);
    pointer-events: none;
    z-index: 11;
  }

  /* Right detail panel — scrollable */
  .detail-panel {
    flex: 1;
    background: #1C1C1E;
    overflow-y: auto;
  }

  .detail-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 20px 24px 16px;
    border-bottom: 1px solid #3A3A3C;
    position: relative;
  }

  .detail-plugin-name { font-size: 20px; font-weight: 600; color: #FFFFFF; }

  .detail-actions { display: flex; align-items: center; gap: 8px; }

  .btn-outline {
    background: transparent; border: 1px solid #48484A; border-radius: 7px;
    padding: 5px 13px; font-size: 12px; font-weight: 500; color: #AEAEB2;
    font-family: 'DM Sans', sans-serif; cursor: pointer;
  }
  .btn-solid {
    background: #2E2E30; border: 1px solid #48484A; border-radius: 7px;
    padding: 5px 13px; font-size: 12px; font-weight: 500; color: #DDDDE0;
    font-family: 'DM Sans', sans-serif; cursor: pointer;
  }

  .toggle-pill {
    width: 44px; height: 26px; border-radius: 13px;
    background: var(--nf-secondary-light); position: relative; cursor: pointer;
  }
  .toggle-pill-knob {
    width: 20px; height: 20px; background: white; border-radius: 50%;
    position: absolute; top: 3px; left: 21px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.3);
  }

  .detail-meta {
    display: flex; gap: 28px;
    padding: 14px 24px; border-bottom: 1px solid #3A3A3C;
  }
  .meta-label {
    font-size: 10px; font-weight: 600; text-transform: uppercase;
    letter-spacing: 0.07em; color: #636366; margin-bottom: 3px;
  }
  .meta-value { font-size: 12px; color: #AEAEB2; }
  .meta-value.link { color: var(--nf-secondary-light); }

  .detail-desc-section {
    padding: 14px 24px; border-bottom: 1px solid #3A3A3C;
  }
  .detail-section-title {
    font-size: 10px; font-weight: 600; text-transform: uppercase;
    letter-spacing: 0.07em; color: #636366; margin-bottom: 6px;
  }
  .detail-desc-text { font-size: 12px; color: #8E8E93; line-height: 1.6; }

  .skills-section { padding: 16px 24px; position: relative; }

  .skills-header {
    display: flex; align-items: center; justify-content: space-between; margin-bottom: 10px;
  }
  .skills-pill {
    background: #2E2E30; border: 1px solid #48484A; border-radius: 5px;
    padding: 3px 10px; font-size: 11px; font-weight: 500; color: #DDDDE0;
  }
  .skills-invoke-note {
    font-size: 11px; color: #636366; margin-bottom: 12px; font-style: italic;
  }
  .skills-invoke-note code {
    font-family: 'DM Mono', monospace; font-size: 11px;
    color: var(--nf-secondary-light);
    background: rgba(71,143,204,0.1); padding: 1px 5px; border-radius: 3px;
  }

  .skills-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }

  .skill-card {
    background: #2A2A2C; border: 1px solid #3A3A3C;
    border-radius: 8px; padding: 11px 13px; cursor: pointer;
  }
  .skill-card:hover { border-color: #48484A; background: #2E2E30; }
  .skill-card-desc {
    font-size: 11px; color: #AEAEB2; line-height: 1.5; margin-bottom: 8px;
    display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
  }
  .skill-cmd { font-family: 'DM Mono', monospace; font-size: 10px; color: var(--nf-secondary-light); }

  .try-section { padding: 0 24px 24px; }
  .try-label { font-size: 13px; font-weight: 600; color: #8E8E93; margin-bottom: 8px; }
  .try-item {
    padding: 9px 12px; background: #242426; border: 1px solid #3A3A3C;
    border-radius: 6px; font-size: 12px; color: #8E8E93; margin-bottom: 6px; cursor: pointer;
  }
  .try-item:hover { background: #2E2E30; color: #AEAEB2; }

  /* Legend */
  .legend { display: flex; gap: 12px; margin-top: 20px; }

  .legend-card {
    flex: 1; background: white; border-radius: 10px; padding: 14px 16px;
    border-top: 3px solid var(--nf-accent);
    box-shadow: 0 2px 8px rgba(22,27,74,0.07);
  }
  .legend-head { display: flex; align-items: center; gap: 8px; margin-bottom: 7px; }
  .legend-num {
    width: 24px; height: 24px; border-radius: 50%;
    background: var(--nf-accent); color: white; font-size: 12px; font-weight: 700;
    display: flex; align-items: center; justify-content: center; flex-shrink: 0;
  }
  .legend-title { font-size: 13px; font-weight: 600; color: var(--nf-primary); }
  .legend-desc { font-size: 12px; color: var(--nf-text-secondary); line-height: 1.6; }

  code {
    font-family: 'DM Mono', monospace; font-size: 10.5px;
    background: #F0F1F5; color: var(--nf-secondary-blue);
    padding: 1px 4px; border-radius: 3px;
  }
</style>
</head>
<body>
<div class="wrapper">

  <div class="lesson-label">Cowork Interface Guide</div>
  <div class="lesson-title">Finding and using plugins in Cowork</div>
  <div class="lesson-sub">Claude Desktop app · Cowork tab · macOS and Windows</div>

  <div class="window">

    <div class="title-bar">
      <div class="dot dot-r"></div>
      <div class="dot dot-y"></div>
      <div class="dot dot-g"></div>
      <div class="window-title">Customize</div>
    </div>

    <div class="panels">

      <!-- Left nav -->
      <div class="left-nav">

        <div class="nav-item">
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><rect x="1.5" y="1.5" width="11" height="11" rx="2" stroke="#8E8E93" stroke-width="1.3"/><path d="M4.5 7h5M4.5 9.5h3" stroke="#8E8E93" stroke-width="1.1" stroke-linecap="round"/></svg>
          Skills
        </div>
        <div class="nav-item">
          <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><circle cx="7" cy="7" r="5" stroke="#8E8E93" stroke-width="1.3"/><path d="M7 2V1M7 13v-1M13 7h-1M2 7H1" stroke="#8E8E93" stroke-width="1.1" stroke-linecap="round"/></svg>
          Connectors
        </div>

        <div class="nav-divider"></div>

        <!-- ANNOTATION 1: Personal plugins section -->
        <div class="annotated">
          <div class="anno-ring" style="top: -2px; left: 2px; right: 2px; bottom: -2px;"></div>
          <div class="anno-badge" style="top: -10px; left: -2px;">1</div>

          <div class="nav-section-header">
            <span class="nav-section-label">Personal plugins</span>
            <div class="nav-add-btn">+</div>
          </div>

          <div class="nav-plugin-row active">
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M2 9l3-3 2.5 2.5L11 4" stroke="#478FCC" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>
            Legal
          </div>
          <div class="nav-sub-item">
            <svg width="11" height="11" viewBox="0 0 11 11" fill="none"><rect x="1" y="1" width="9" height="9" rx="1.5" stroke="#636366" stroke-width="1"/></svg>
            Skills
          </div>
          <div class="nav-sub-item">
            <svg width="11" height="11" viewBox="0 0 11 11" fill="none"><circle cx="5.5" cy="5.5" r="4" stroke="#636366" stroke-width="1"/></svg>
            Connectors
          </div>
          <div class="nav-plugin-row">
            <svg width="14" height="14" viewBox="0 0 14 14" fill="none"><path d="M2 9l3-3 2.5 2.5L11 4" stroke="#636366" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg>
            Data
          </div>
        </div>

        <div class="nav-divider"></div>

        <div class="nav-section-header">
          <span class="nav-section-label">Organization plugins</span>
          <div class="nav-add-btn">+</div>
        </div>
        <div class="nav-org-note">Plugins managed by your org will appear here.</div>

      </div>

      <!-- Detail panel — scrollable, annotations inside elements -->
      <div class="detail-panel">

        <!-- ANNOTATION 2: active toggle lives inside detail-header -->
        <div class="detail-header annotated">
          <div class="detail-plugin-name">Legal</div>
          <div class="detail-actions">
            <button class="btn-outline">Update</button>
            <button class="btn-solid">Customize</button>
            <!-- ring wraps just the toggle -->
            <div style="position:relative; display:flex; align-items:center;">
              <div class="anno-ring" style="top: -5px; left: -5px; right: -5px; bottom: -5px; border-radius: 16px;"></div>
              <div class="anno-badge" style="top: -14px; right: -8px;">2</div>
              <div class="toggle-pill"><div class="toggle-pill-knob"></div></div>
            </div>
          </div>
        </div>

        <div class="detail-meta">
          <div class="meta-item">
            <div class="meta-label">Source</div>
            <div class="meta-value">Marketplace <span class="link">(Anthropic & Partners)</span></div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Version</div>
            <div class="meta-value">1.4.0</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Author</div>
            <div class="meta-value">Anthropic</div>
          </div>
          <div class="meta-item">
            <div class="meta-label">Last updated</div>
            <div class="meta-value">9 days ago</div>
          </div>
        </div>

        <div class="detail-desc-section">
          <div class="detail-section-title">Description</div>
          <div class="detail-desc-text">Review regulatory documents, analyze compliance requirements, and research policy provisions. Built for legal and policy teams working with federal rules, contracts, and statutory language.</div>
        </div>

        <!-- ANNOTATION 3: skills section -->
        <div class="skills-section annotated">
          <div class="anno-ring" style="top: -2px; left: 2px; right: 2px; bottom: -2px; border-radius: 8px;"></div>
          <div class="anno-badge" style="top: -10px; right: 4px;">3</div>

          <div class="skills-header">
            <div class="skills-pill">Skills</div>
            <span style="font-size:11px;color:var(--nf-secondary-light);cursor:pointer;">See all</span>
          </div>
          <div class="skills-invoke-note">Invoke by typing <code>/</code> in chat, or let Claude use them automatically for relevant tasks.</div>
          <div class="skills-grid">
            <div class="skill-card">
              <div class="skill-card-desc">Scan a federal rule for provisions affecting a specified topic or stakeholder.</div>
              <div class="skill-cmd">/regulatory-scan</div>
            </div>
            <div class="skill-card">
              <div class="skill-card-desc">Map regulatory requirements to compliance obligations and flag gaps.</div>
              <div class="skill-cmd">/compliance-check</div>
            </div>
            <div class="skill-card">
              <div class="skill-card-desc">Summarize key changes between a proposed and final rule.</div>
              <div class="skill-cmd">/rule-diff</div>
            </div>
            <div class="skill-card">
              <div class="skill-card-desc">Analyze a contract for non-standard terms or risk exposures.</div>
              <div class="skill-cmd">/contract-review</div>
            </div>
            <div class="skill-card">
              <div class="skill-card-desc">Research legislative history and committee reports for a named statute.</div>
              <div class="skill-cmd">/legislative-history</div>
            </div>
            <div class="skill-card">
              <div class="skill-card-desc">Draft a public comment structured to address each element of the preamble.</div>
              <div class="skill-cmd">/public-comment</div>
            </div>
          </div>
        </div>

        <div class="try-section">
          <div class="try-label">Try asking...</div>
          <div class="try-item">Scan this CMS final rule for behavioral health reimbursement provisions</div>
          <div class="try-item">Compare the proposed and final language on network adequacy standards</div>
          <div class="try-item">Draft a public comment responding to the preamble of this proposed rule</div>
        </div>

      </div>
    </div>
  </div>

  <!-- Legend -->
  <div class="legend">
    <div class="legend-card">
      <div class="legend-head"><div class="legend-num">1</div><div class="legend-title">Personal plugins</div></div>
      <div class="legend-desc">Installed plugins appear under <code>Personal plugins</code> in the left nav. Click any plugin to open its detail view. Click <code>+</code> to browse the Anthropic catalog and install new ones.</div>
    </div>
    <div class="legend-card">
      <div class="legend-head"><div class="legend-num">2</div><div class="legend-title">Active toggle</div></div>
      <div class="legend-desc">The blue toggle in the top right of the detail view confirms a plugin is active. Toggle it off to disable the plugin without uninstalling it.</div>
    </div>
    <div class="legend-card">
      <div class="legend-head"><div class="legend-num">3</div><div class="legend-title">Skills and slash commands</div></div>
      <div class="legend-desc">Each plugin lists its skills as cards with a description and slash command. Type <code>/</code> inside any Cowork task to invoke them, or let Claude call them automatically when relevant.</div>
    </div>
  </div>

</div>
</body>
</html>

"""

DIAGRAMS["metaprompt_cowork"] = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Meta-prompt visualization</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,wght@0,300;0,400;0,500;0,600;1,400&family=DM+Mono:wght@400;500&display=swap');

  :root {
    --nf-primary: #161B4A;
    --nf-secondary-blue: #2E4799;
    --nf-secondary-light: #478FCC;
    --nf-secondary-teal: #4CB6AC;
    --nf-accent: #F16061;
    --nf-text-primary: #212121;
    --nf-text-secondary: #757575;
    --nf-divider: #BDBDBD;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: #ECEEF4;
    font-family: 'DM Sans', sans-serif;
    display: flex;
    align-items: flex-start;
    justify-content: center;
    min-height: 100vh;
    padding: 36px 24px;
  }

  .wrapper { width: 100%; max-width: 960px; }

  .lesson-label {
    font-size: 11px; font-weight: 600; letter-spacing: 0.12em;
    text-transform: uppercase; color: var(--nf-secondary-blue); margin-bottom: 8px;
  }
  .lesson-title { font-size: 21px; font-weight: 600; color: var(--nf-primary); margin-bottom: 4px; }
  .lesson-sub { font-size: 13px; color: var(--nf-text-secondary); margin-bottom: 28px; }

  /* ── Prompt display at top ── */
  .prompt-row {
    background: white;
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 20px;
    box-shadow: 0 2px 10px rgba(22,27,74,0.07);
    display: flex;
    align-items: flex-start;
    gap: 14px;
  }

  .prompt-avatar {
    width: 32px; height: 32px; border-radius: 50%;
    background: linear-gradient(135deg, var(--nf-secondary-blue), var(--nf-secondary-light));
    color: white; font-size: 13px; font-weight: 700;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
  }

  .prompt-body { flex: 1; }

  .prompt-label {
    font-size: 10px; font-weight: 600; letter-spacing: 0.08em;
    text-transform: uppercase; color: var(--nf-text-secondary); margin-bottom: 6px;
  }

  .prompt-text {
    font-size: 13px; color: var(--nf-text-primary); line-height: 1.6;
  }

  .prompt-text em {
    font-style: italic; color: var(--nf-secondary-blue);
  }

  .attach-pill {
    display: inline-flex; align-items: center; gap: 5px;
    background: #F0F4FA; border: 1px solid #D0D8EC;
    border-radius: 6px; padding: 3px 9px;
    font-size: 11px; color: var(--nf-secondary-blue);
    margin-top: 8px;
  }

  /* ── Arrow ── */
  .arrow-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin-bottom: 20px;
  }

  .arrow-line {
    flex: 1;
    height: 1px;
    background: var(--nf-divider);
  }

  .arrow-label {
    font-size: 11px; font-weight: 600; letter-spacing: 0.07em;
    text-transform: uppercase; color: var(--nf-text-secondary);
    white-space: nowrap;
  }

  .arrow-icon {
    color: var(--nf-secondary-teal);
    font-size: 20px;
    line-height: 1;
  }

  /* ── Side by side ── */
  .comparison {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;
    margin-bottom: 20px;
  }

  .panel {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 12px rgba(22,27,74,0.09);
  }

  .panel-header {
    padding: 12px 18px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .panel-header.bad {
    background: #FFF0F0;
    border-bottom: 2px solid var(--nf-accent);
  }

  .panel-header.good {
    background: #EDF7F6;
    border-bottom: 2px solid var(--nf-secondary-teal);
  }

  .panel-icon {
    width: 26px; height: 26px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 13px; flex-shrink: 0;
  }

  .panel-icon.bad { background: rgba(241,96,97,0.15); }
  .panel-icon.good { background: rgba(76,182,172,0.18); }

  .panel-title {
    font-size: 12px; font-weight: 600;
  }

  .panel-title.bad { color: var(--nf-accent); }
  .panel-title.good { color: #2A8C83; }

  .panel-subtitle {
    font-size: 11px; color: var(--nf-text-secondary); margin-top: 1px;
  }

  .panel-body { background: white; padding: 16px 18px; }

  /* Bad panel: vague instruction */
  .vague-instruction {
    background: #FFF8F8;
    border: 1px solid #FDDCDC;
    border-radius: 8px;
    padding: 14px 16px;
    font-size: 13px;
    color: var(--nf-text-primary);
    line-height: 1.6;
    font-style: italic;
    margin-bottom: 14px;
  }

  .gap-list { display: flex; flex-direction: column; gap: 8px; }

  .gap-item {
    display: flex; align-items: flex-start; gap: 8px;
  }

  .gap-dot {
    width: 7px; height: 7px; border-radius: 50%;
    background: var(--nf-accent); flex-shrink: 0; margin-top: 5px;
  }

  .gap-text { font-size: 12px; color: var(--nf-text-secondary); line-height: 1.5; }

  .gap-question {
    font-size: 11px; font-weight: 600; color: var(--nf-accent);
    margin-top: 2px;
  }

  /* Good panel: structured steps */
  .step-list { display: flex; flex-direction: column; gap: 8px; }

  .step-item {
    display: flex; align-items: flex-start; gap: 10px;
  }

  .step-num {
    width: 22px; height: 22px; border-radius: 50%;
    background: linear-gradient(135deg, var(--nf-secondary-blue), var(--nf-secondary-teal));
    color: white; font-size: 10px; font-weight: 700;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0; margin-top: 1px;
  }

  .step-body-text { flex: 1; }

  .step-main {
    font-size: 12px; color: var(--nf-text-primary); line-height: 1.5; font-weight: 500;
  }

  .step-detail {
    font-size: 11px; color: var(--nf-text-secondary); line-height: 1.5; margin-top: 2px;
  }

  .step-tag {
    display: inline-block;
    font-size: 9px; font-weight: 600; letter-spacing: 0.07em; text-transform: uppercase;
    padding: 1px 6px; border-radius: 3px; margin-top: 4px;
  }

  .step-tag.order { background: rgba(71,143,204,0.12); color: var(--nf-secondary-blue); }
  .step-tag.guard { background: rgba(76,182,172,0.12); color: #2A8C83; }
  .step-tag.source { background: rgba(46,71,153,0.1); color: var(--nf-secondary-blue); }
  .step-tag.ambig { background: rgba(241,96,97,0.1); color: var(--nf-accent); }
  .step-tag.output { background: rgba(76,182,172,0.12); color: #2A8C83; }

  /* ── Callout bar at bottom ── */
  .callout-bar {
    background: var(--nf-primary);
    border-radius: 12px;
    padding: 16px 22px;
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .callout-icon {
    width: 36px; height: 36px; border-radius: 50%;
    background: rgba(76,182,172,0.2);
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
  }

  .callout-text {
    flex: 1;
    font-size: 12px; color: #C8CCDE; line-height: 1.6;
  }

  .callout-text strong { color: white; }

</style>
</head>
<body>
<div class="wrapper">

  <div class="lesson-label">Cowork · Meta-prompting</div>
  <div class="lesson-title">What meta-prompting does to a task instruction</div>
  <div class="lesson-sub">Ask Claude to write the Cowork instruction before you run it.</div>

  <!-- The meta-prompt itself -->
  <div class="prompt-row">
    <div class="prompt-avatar">M</div>
    <div class="prompt-body">
      <div class="prompt-label">You ask Claude</div>
      <div class="prompt-text">
        I'm attaching a partner tracking spreadsheet. I want Cowork to review it, find the missing information online, and fill in the gaps.
        <em>Write me a step-by-step Cowork task instruction that handles this in the right order.</em>
      </div>
      <div class="attach-pill">
        <svg width="12" height="12" viewBox="0 0 12 12" fill="none"><rect x="1.5" y="1.5" width="9" height="9" rx="1.5" stroke="#2E4799" stroke-width="1.2"/><path d="M4 6h4M6 4v4" stroke="#2E4799" stroke-width="1.1" stroke-linecap="round"/></svg>
        partner-tracking.xlsx
      </div>
    </div>
  </div>

  <!-- Arrow divider -->
  <div class="arrow-row">
    <div class="arrow-line"></div>
    <div class="arrow-label">Claude examines the file and returns</div>
    <div class="arrow-icon">↓</div>
    <div class="arrow-line"></div>
  </div>

  <!-- Side by side -->
  <div class="comparison">

    <!-- Left: without meta-prompt -->
    <div class="panel">
      <div class="panel-header bad">
        <div class="panel-icon bad">✕</div>
        <div>
          <div class="panel-title bad">Without meta-prompting</div>
          <div class="panel-subtitle">What most people write</div>
        </div>
      </div>
      <div class="panel-body">
        <div class="vague-instruction">"Review my spreadsheet and fill in the gaps."</div>
        <div class="gap-list">
          <div class="gap-item">
            <div class="gap-dot"></div>
            <div class="gap-text">
              Cowork decides the order itself.
              <div class="gap-question">Does it audit first or start searching?</div>
            </div>
          </div>
          <div class="gap-item">
            <div class="gap-dot"></div>
            <div class="gap-text">
              No rule for existing data.
              <div class="gap-question">Will it overwrite cells that already have values?</div>
            </div>
          </div>
          <div class="gap-item">
            <div class="gap-dot"></div>
            <div class="gap-text">
              No sourcing constraint.
              <div class="gap-question">How old can the news be? What counts as confirmed?</div>
            </div>
          </div>
          <div class="gap-item">
            <div class="gap-dot"></div>
            <div class="gap-text">
              No ambiguity rule.
              <div class="gap-question">What happens when it cannot find information?</div>
            </div>
          </div>
          <div class="gap-item">
            <div class="gap-dot"></div>
            <div class="gap-text">
              No output specification.
              <div class="gap-question">Does it save the file, create a new one, or report in chat?</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Right: with meta-prompt -->
    <div class="panel">
      <div class="panel-header good">
        <div class="panel-icon good">✓</div>
        <div>
          <div class="panel-title good">With meta-prompting</div>
          <div class="panel-subtitle">What Claude produces for you</div>
        </div>
      </div>
      <div class="panel-body">
        <div class="step-list">
          <div class="step-item">
            <div class="step-num">1</div>
            <div class="step-body-text">
              <div class="step-main">Read the spreadsheet. Identify every empty or TBD cell.</div>
              <div class="step-detail">Do not overwrite any cell that already contains data.</div>
              <span class="step-tag order">order: audit first</span>
              <span class="step-tag guard">guard: no overwrite</span>
            </div>
          </div>
          <div class="step-item">
            <div class="step-num">2</div>
            <div class="step-body-text">
              <div class="step-main">For each gap, search the web using the company name as your anchor.</div>
              <div class="step-detail">Pull solution category and key contacts from the company's current website.</div>
              <span class="step-tag source">source: current website</span>
            </div>
          </div>
          <div class="step-item">
            <div class="step-num">3</div>
            <div class="step-body-text">
              <div class="step-main">For recent news, use coverage from the last 90 days only.</div>
              <div class="step-detail">Summarize in one sentence. Add source URL in an adjacent note cell.</div>
              <span class="step-tag source">source: 90-day window</span>
            </div>
          </div>
          <div class="step-item">
            <div class="step-num">4</div>
            <div class="step-body-text">
              <div class="step-main">For contract status, do not guess or infer.</div>
              <div class="step-detail">If no confirmed public source exists, enter "Not confirmed" rather than leaving the cell blank.</div>
              <span class="step-tag ambig">ambiguity rule</span>
            </div>
          </div>
          <div class="step-item">
            <div class="step-num">5</div>
            <div class="step-body-text">
              <div class="step-main">Add a Last Updated column. Enter today's date for every modified row.</div>
              <span class="step-tag output">output spec</span>
            </div>
          </div>
          <div class="step-item">
            <div class="step-num">6</div>
            <div class="step-body-text">
              <div class="step-main">Save the file. Do not delete or reorganize any existing rows or columns.</div>
              <span class="step-tag guard">guard: preserve structure</span>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>

  <!-- Callout bar -->
  <div class="callout-bar">
    <div class="callout-icon">
      <svg width="18" height="18" viewBox="0 0 18 18" fill="none"><path d="M9 2L11.09 6.26L16 7.27L12.5 10.68L13.18 15.59L9 13.36L4.82 15.59L5.5 10.68L2 7.27L6.91 6.26L9 2Z" stroke="#4CB6AC" stroke-width="1.5" stroke-linejoin="round"/></svg>
    </div>
    <div class="callout-text">
      <strong>The meta-prompt surfaces decisions before the task runs, not after something goes wrong.</strong>
      Every unanswered question in a vague instruction becomes a guess Cowork makes on your behalf.
      Ordering, sourcing rules, ambiguity handling, and output format all need to be explicit
      for a task that touches real data in a live file.
    </div>
  </div>

</div>
</body>
</html>

"""

DIAGRAMS["phi_decision"] = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Claude Teams PHI decision · NeuroFlow</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --nf-primary: #161B4A;
    --nf-sec-blue: #2E4799;
    --nf-teal: #4CB6AC;
    --nf-accent: #F16061;
    --nf-ink: #1A1B2E;
    --nf-bg-1: #FBFBFD;
    --nf-bg-2: #F1F3F9;
    --nf-card: #FFFFFF;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; }

  body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    background:
      radial-gradient(ellipse 1000px 500px at 15% 0%, rgba(46, 71, 153, 0.08), transparent 60%),
      radial-gradient(ellipse 800px 400px at 100% 100%, rgba(76, 182, 172, 0.09), transparent 60%),
      linear-gradient(180deg, var(--nf-bg-1) 0%, var(--nf-bg-2) 100%);
    color: var(--nf-ink);
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 56px 24px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  .poster {
    width: 100%;
    max-width: 820px;
    background: var(--nf-card);
    border-radius: 24px;
    padding: 56px 64px;
    box-shadow:
      0 1px 2px rgba(22, 27, 74, 0.04),
      0 2px 8px rgba(22, 27, 74, 0.04),
      0 28px 56px -20px rgba(22, 27, 74, 0.14);
    border: 1px solid rgba(22, 27, 74, 0.05);
    animation: rise 0.7s cubic-bezier(0.2, 0.8, 0.2, 1) both;
  }

  @keyframes rise {
    from { opacity: 0; transform: translateY(14px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .diagram-wrap {
    display: flex;
    justify-content: center;
  }

  .diagram-wrap svg {
    width: 100%;
    max-width: 700px;
    height: auto;
    display: block;
    overflow: visible;
  }

  .diagram-wrap svg text {
    font-family: 'Plus Jakarta Sans', sans-serif;
  }

  @media (max-width: 680px) {
    .poster { padding: 36px 24px; border-radius: 18px; }
  }
</style>
</head>
<body>
  <div class="poster">
    <div class="diagram-wrap">
      <svg viewBox="0 0 700 410" xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="dtitle ddesc">
        <title id="dtitle">Two-gate decision for Claude Teams</title>
        <desc id="ddesc">Work content enters at the top. Gate one asks whether it is patient data. If no, it routes to Claude Teams. If yes, gate two asks whether it contains individual-level identifiers. If no, it routes to Claude Teams as de-identified data. If yes, it routes to HIPAA-compliant systems only.</desc>

        <defs>
          <marker id="arrhead" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse">
            <path d="M2 2 L8 5 L2 8" fill="none" stroke="context-stroke" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>
          </marker>
          <filter id="cardshadow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="2" stdDeviation="5" flood-color="#161B4A" flood-opacity="0.08"/>
          </filter>
          <filter id="endshadow" x="-20%" y="-20%" width="140%" height="140%">
            <feDropShadow dx="0" dy="5" stdDeviation="10" flood-color="#161B4A" flood-opacity="0.20"/>
          </filter>
        </defs>

        <!-- Entry -->
        <g>
          <rect x="140" y="22" width="200" height="52" rx="12" fill="#FFFFFF" stroke="#161B4A" stroke-width="1.25" filter="url(#cardshadow)"/>
          <text x="240" y="54" text-anchor="middle" font-size="14" font-weight="500" fill="#161B4A">Work content</text>
        </g>
        <line x1="240" y1="74" x2="240" y2="104" stroke="#2E4799" stroke-width="1.25" marker-end="url(#arrhead)"/>

        <!-- Gate 01 -->
        <g>
          <rect x="100" y="108" width="280" height="56" rx="12" fill="#FFFFFF" stroke="#2E4799" stroke-width="1.25" filter="url(#cardshadow)"/>
          <text x="116" y="128" font-size="10" font-weight="700" letter-spacing="1.5" fill="#F16061">01</text>
          <text x="240" y="146" text-anchor="middle" font-size="15" font-weight="500" fill="#161B4A">Is this patient data?</text>
        </g>

        <!-- Gate 01 → Claude Teams A (longer arrow, label has room) -->
        <line x1="380" y1="136" x2="465" y2="136" stroke="#2E4799" stroke-width="1.25" marker-end="url(#arrhead)"/>
        <text x="422" y="129" text-anchor="middle" font-size="11" font-style="italic" fill="#8E90A3">no</text>

        <!-- Gate 01 → Gate 02 -->
        <line x1="240" y1="164" x2="240" y2="214" stroke="#2E4799" stroke-width="1.25" marker-end="url(#arrhead)"/>
        <text x="253" y="192" font-size="11" font-style="italic" fill="#8E90A3">yes</text>

        <!-- Gate 02 -->
        <g>
          <rect x="90" y="218" width="300" height="56" rx="12" fill="#FFFFFF" stroke="#2E4799" stroke-width="1.25" filter="url(#cardshadow)"/>
          <text x="106" y="238" font-size="10" font-weight="700" letter-spacing="1.5" fill="#F16061">02</text>
          <text x="240" y="256" text-anchor="middle" font-size="15" font-weight="500" fill="#161B4A">Individual-level identifiers?</text>
        </g>

        <!-- Gate 02 → Claude Teams B (longer arrow fixes crunched label) -->
        <line x1="390" y1="246" x2="465" y2="246" stroke="#2E4799" stroke-width="1.25" marker-end="url(#arrhead)"/>
        <text x="427" y="239" text-anchor="middle" font-size="11" font-style="italic" fill="#8E90A3">no</text>

        <!-- Gate 02 → HIPAA -->
        <line x1="240" y1="274" x2="240" y2="324" stroke="#2E4799" stroke-width="1.25" marker-end="url(#arrhead)"/>
        <text x="253" y="302" font-size="11" font-style="italic" fill="#8E90A3">yes</text>

        <!-- Claude Teams A (Internal) -->
        <g filter="url(#endshadow)">
          <rect x="470" y="108" width="210" height="56" rx="12" fill="#4CB6AC"/>
          <path d="M488 132 L494 138 L504 126" stroke="#FFFFFF" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="518" y="130" font-size="14" font-weight="600" fill="#FFFFFF">Claude Teams</text>
          <text x="518" y="148" font-size="12" font-weight="400" fill="#FFFFFF" opacity="0.92">Internal work content</text>
        </g>

        <!-- Claude Teams B (De-identified) -->
        <g filter="url(#endshadow)">
          <rect x="470" y="218" width="210" height="56" rx="12" fill="#4CB6AC"/>
          <path d="M488 242 L494 248 L504 236" stroke="#FFFFFF" stroke-width="1.8" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
          <text x="518" y="240" font-size="14" font-weight="600" fill="#FFFFFF">Claude Teams</text>
          <text x="518" y="258" font-size="12" font-weight="400" fill="#FFFFFF" opacity="0.92">De-identified data</text>
        </g>

        <!-- HIPAA (widened so the "y" descender clears the right edge) -->
        <g filter="url(#endshadow)">
          <rect x="120" y="328" width="240" height="62" rx="12" fill="#F16061"/>
          <g transform="translate(-16, 0)">
            <path d="M158 354 C158 348 162 344 168 344 L170 344 L170 342 C170 338 173 335 177 335 C181 335 184 338 184 342 L184 344 L186 344 C192 344 196 348 196 354 L196 362 C196 365 194 367 191 367 L163 367 C160 367 158 365 158 362 Z" fill="none" stroke="#FFFFFF" stroke-width="1.4" stroke-linejoin="round"/>
            <text x="210" y="356" font-size="14" font-weight="600" fill="#FFFFFF">HIPAA systems only</text>
            <text x="210" y="374" font-size="12" font-weight="400" fill="#FFFFFF" opacity="0.92">Required for any PHI</text>
          </g>
        </g>
      </svg>
    </div>
  </div>
</body>
</html>

"""

DIAGRAMS["when_to_ground"] = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>When to ground Claude with an example · NeuroFlow</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,500&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --nf-primary: #161B4A;
    --nf-sec-blue: #2E4799;
    --nf-sec-light: #478FCC;
    --nf-teal: #4CB6AC;
    --nf-teal-soft: rgba(76, 182, 172, 0.10);
    --nf-accent: #F16061;
    --nf-ink: #1A1B2E;
    --nf-text-2: #5B5D72;
    --nf-text-3: #8E90A3;
    --nf-divider: #E8E9F0;
    --nf-bg-1: #FBFBFD;
    --nf-bg-2: #F1F3F9;
    --nf-card: #FFFFFF;
    --nf-front-tint: #F9FAFD;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; }

  body {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
    background:
      radial-gradient(ellipse 1000px 500px at 15% 0%, rgba(46, 71, 153, 0.08), transparent 60%),
      radial-gradient(ellipse 800px 400px at 100% 100%, rgba(76, 182, 172, 0.09), transparent 60%),
      linear-gradient(180deg, var(--nf-bg-1) 0%, var(--nf-bg-2) 100%);
    color: var(--nf-ink);
    min-height: 100vh;
    padding: 56px 24px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
  }

  .poster {
    width: 100%;
    max-width: 980px;
    margin: 0 auto;
    background: var(--nf-card);
    border-radius: 24px;
    padding: 48px 48px 40px;
    box-shadow:
      0 1px 2px rgba(22, 27, 74, 0.04),
      0 2px 8px rgba(22, 27, 74, 0.04),
      0 28px 56px -20px rgba(22, 27, 74, 0.14);
    border: 1px solid rgba(22, 27, 74, 0.05);
    animation: rise 0.7s cubic-bezier(0.2, 0.8, 0.2, 1) both;
  }
  @keyframes rise {
    from { opacity: 0; transform: translateY(14px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
  }

  /* Card shell */
  .card {
    position: relative;
    width: 100%;
    height: 520px;
    perspective: 1400px;
    background: none;
    border: none;
    padding: 0;
    cursor: pointer;
    font-family: inherit;
    text-align: left;
    outline: none;
  }
  .card:focus-visible .card-inner {
    box-shadow: 0 0 0 3px rgba(46, 71, 153, 0.35);
    border-radius: 16px;
  }

  .card-inner {
    position: relative;
    width: 100%;
    height: 100%;
    transition: transform 0.75s cubic-bezier(0.4, 0.0, 0.2, 1);
    transform-style: preserve-3d;
  }
  .card.flipped .card-inner {
    transform: rotateY(180deg);
  }

  .card-face {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    -webkit-backface-visibility: hidden;
    backface-visibility: hidden;
    border-radius: 16px;
    padding: 38px 24px 26px;
    display: flex;
    flex-direction: column;
    border: 1px solid var(--nf-divider);
    background: var(--nf-card);
    box-shadow:
      0 1px 2px rgba(22, 27, 74, 0.04),
      0 8px 20px -12px rgba(22, 27, 74, 0.12);
    transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease;
  }
  .card-back { transform: rotateY(180deg); }

  /* Hover lift (only when not flipped for front, and when flipped for back) */
  .card:not(.flipped):hover .card-front,
  .card.flipped:hover .card-back {
    transform: translateY(-3px);
    box-shadow:
      0 1px 2px rgba(22, 27, 74, 0.04),
      0 16px 28px -14px rgba(22, 27, 74, 0.20);
    border-color: rgba(46, 71, 153, 0.18);
  }
  .card.flipped:hover .card-back {
    transform: rotateY(180deg) translateY(-3px);
  }

  /* Front face */
  .card-front {
    background: linear-gradient(160deg, #FFFFFF 0%, var(--nf-front-tint) 100%);
  }
  .card-num {
    display: block;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.2em;
    color: var(--nf-accent);
    text-transform: uppercase;
    line-height: 1;
    flex-shrink: 0;
  }
  .card-num::before {
    content: '';
    display: inline-block;
    width: 18px;
    height: 1.5px;
    background: var(--nf-accent);
    vertical-align: middle;
    margin-right: 8px;
    position: relative;
    top: -2px;
  }
  .card-back .card-num::before {
    display: none;
  }
  .card-front-title {
    font-family: 'Fraunces', Georgia, serif;
    font-size: 30px;
    font-weight: 500;
    color: var(--nf-primary);
    line-height: 1.08;
    letter-spacing: -0.02em;
    margin: auto 0;
  }
  .flip-indicator {
    display: flex;
    align-items: center;
    gap: 8px;
    color: var(--nf-text-3);
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.04em;
    margin-top: auto;
  }
  .flip-indicator svg {
    width: 14px;
    height: 14px;
    color: var(--nf-sec-blue);
  }

  /* Back face */
  .card-back-title {
    font-family: 'Fraunces', Georgia, serif;
    font-size: 19px;
    font-weight: 500;
    color: var(--nf-primary);
    line-height: 1.15;
    letter-spacing: -0.015em;
    margin-top: 10px;
    margin-bottom: 14px;
  }
  .card-body {
    font-size: 12.75px;
    color: var(--nf-text-2);
    line-height: 1.55;
    margin-bottom: 14px;
  }
  .card-example {
    margin-top: auto;
    padding: 10px 12px 11px;
    background: var(--nf-teal-soft);
    border-left: 3px solid var(--nf-teal);
    border-radius: 0 6px 6px 0;
  }
  .example-label {
    display: block;
    font-size: 9.5px;
    font-weight: 700;
    letter-spacing: 0.18em;
    color: var(--nf-teal);
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .example-text {
    font-size: 12px;
    color: var(--nf-ink);
    line-height: 1.45;
    font-weight: 500;
  }
  .example-text + .example-text {
    margin-top: 6px;
  }

  /* Responsive */
  @media (max-width: 860px) {
    .grid { grid-template-columns: repeat(2, 1fr); }
  }
  @media (max-width: 540px) {
    .poster { padding: 32px 20px 28px; border-radius: 18px; }
    .grid { grid-template-columns: 1fr; gap: 16px; }
    .card { height: 500px; }
    .card-front-title { font-size: 26px; }
  }
</style>
</head>
<body>
  <div class="poster">
    <div class="grid">

      <button class="card" type="button" aria-pressed="false">
        <div class="card-inner">
          <div class="card-face card-front">
            <span class="card-num">01</span>
            <h3 class="card-front-title">Tone and voice</h3>
            <div class="flip-indicator">
              <svg viewBox="0 0 14 14" fill="none" aria-hidden="true">
                <path d="M11.5 6.5A4.5 4.5 0 1 1 9.3 2.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
                <path d="M9.3 0.8L9.3 3L11.5 3" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              Tap to see why
            </div>
          </div>
          <div class="card-face card-back">
            <span class="card-num">01</span>
            <h3 class="card-back-title">Tone and voice</h3>
            <p class="card-body">Paste an example when the voice is hard to describe. An RFP response sounds formal and compliance-driven. A sales one-pager sounds direct and benefit-forward. Your own writing sounds like you, not a template. Staff recognize these differences instantly but struggle to articulate them. An example does the work.</p>
            <div class="card-example">
              <span class="example-label">Examples</span>
              <div class="example-text">A prior RFP response transmits formal, compliance-driven voice.</div>
              <div class="example-text">Your own recent writing transmits personal voice and cadence.</div>
            </div>
          </div>
        </div>
      </button>

      <button class="card" type="button" aria-pressed="false">
        <div class="card-inner">
          <div class="card-face card-front">
            <span class="card-num">02</span>
            <h3 class="card-front-title">Shape and length</h3>
            <div class="flip-indicator">
              <svg viewBox="0 0 14 14" fill="none" aria-hidden="true">
                <path d="M11.5 6.5A4.5 4.5 0 1 1 9.3 2.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
                <path d="M9.3 0.8L9.3 3L11.5 3" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              Tap to see why
            </div>
          </div>
          <div class="card-face card-back">
            <span class="card-num">02</span>
            <h3 class="card-back-title">Shape and length</h3>
            <p class="card-body">Paste an example when the skeleton matters. A weekly status report has a fixed order. Executive summary, progress, blockers, next week. Each section runs two to four sentences. Claude reading a sample reproduces both the section sequence and the per-section density. Without an example, Claude invents an outline and picks a default length.</p>
            <div class="card-example">
              <span class="example-label">Example</span>
              <div class="example-text">Last quarter's status report sets section order and section length.</div>
            </div>
          </div>
        </div>
      </button>

      <button class="card" type="button" aria-pressed="false">
        <div class="card-inner">
          <div class="card-face card-front">
            <span class="card-num">03</span>
            <h3 class="card-front-title">Argument logic</h3>
            <div class="flip-indicator">
              <svg viewBox="0 0 14 14" fill="none" aria-hidden="true">
                <path d="M11.5 6.5A4.5 4.5 0 1 1 9.3 2.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
                <path d="M9.3 0.8L9.3 3L11.5 3" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              Tap to see why
            </div>
          </div>
          <div class="card-face card-back">
            <span class="card-num">03</span>
            <h3 class="card-back-title">Argument logic</h3>
            <p class="card-body">Paste an example when reasoning order matters. A recommendation memo opens with the recommendation and defends it afterward. A discovery brief opens with the question and walks through findings before reaching a conclusion. A competitive intelligence report opens with the market landscape before naming the threat. Same subject, three different sequences. The example carries the sequence.</p>
            <div class="card-example">
              <span class="example-label">Example</span>
              <div class="example-text">A past recommendation memo locks in recommendation reasoning and format.</div>
            </div>
          </div>
        </div>
      </button>

      <button class="card" type="button" aria-pressed="false">
        <div class="card-inner">
          <div class="card-face card-front">
            <span class="card-num">04</span>
            <h3 class="card-front-title">Evidentiary standard</h3>
            <div class="flip-indicator">
              <svg viewBox="0 0 14 14" fill="none" aria-hidden="true">
                <path d="M11.5 6.5A4.5 4.5 0 1 1 9.3 2.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
                <path d="M9.3 0.8L9.3 3L11.5 3" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              Tap to see why
            </div>
          </div>
          <div class="card-face card-back">
            <span class="card-num">04</span>
            <h3 class="card-back-title">Evidentiary standard</h3>
            <p class="card-body">Paste an example when the rigor bar matters. An RFP response cites every quantitative claim. An internal strategy memo asserts more freely. A peer-reviewed manuscript attaches a source to every factual sentence. Claude cannot guess which standard applies. If your example carries a source after every figure, new findings will too. If your example asserts without backing, Claude follows suit.</p>
            <div class="card-example">
              <span class="example-label">Example</span>
              <div class="example-text">A prior case study sets citation format and style.</div>
            </div>
          </div>
        </div>
      </button>

      <button class="card" type="button" aria-pressed="false">
        <div class="card-inner">
          <div class="card-face card-front">
            <span class="card-num">05</span>
            <h3 class="card-front-title">House style</h3>
            <div class="flip-indicator">
              <svg viewBox="0 0 14 14" fill="none" aria-hidden="true">
                <path d="M11.5 6.5A4.5 4.5 0 1 1 9.3 2.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
                <path d="M9.3 0.8L9.3 3L11.5 3" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              Tap to see why
            </div>
          </div>
          <div class="card-face card-back">
            <span class="card-num">05</span>
            <h3 class="card-back-title">House style</h3>
            <p class="card-body">Paste an example to transmit conventions. How NeuroFlow refers to its own products. Whether the audience is members, patients, or clients. Acronym rules, list styles, date formats, and whether titles use sentence case or title case. One example carries what would take a style guide to explain.</p>
            <div class="card-example">
              <span class="example-label">Example</span>
              <div class="example-text">A recent product one-pager carries naming, acronym, and formatting conventions.</div>
            </div>
          </div>
        </div>
      </button>

      <button class="card" type="button" aria-pressed="false">
        <div class="card-inner">
          <div class="card-face card-front">
            <span class="card-num">06</span>
            <h3 class="card-front-title">What to lead with</h3>
            <div class="flip-indicator">
              <svg viewBox="0 0 14 14" fill="none" aria-hidden="true">
                <path d="M11.5 6.5A4.5 4.5 0 1 1 9.3 2.5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/>
                <path d="M9.3 0.8L9.3 3L11.5 3" stroke="currentColor" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
              </svg>
              Tap to see why
            </div>
          </div>
          <div class="card-face card-back">
            <span class="card-num">06</span>
            <h3 class="card-back-title">What to lead with</h3>
            <p class="card-body">Paste an example when what matters shifts by reader. A clinical program briefed to a health plan CMO leads with quality metrics and staff satisfaction. The same program briefed to a CFO leads with cost trend and total cost of care. Briefed to an FQHC administrator, it leads with operational lift and mission fit. Which facts make the cut, and the order they appear in, depends on the reader.</p>
            <div class="card-example">
              <span class="example-label">Example</span>
              <div class="example-text">A prior deck built for the same audience type anchors value proposition and messaging priority.</div>
            </div>
          </div>
        </div>
      </button>

    </div>
  </div>

  <script>
    document.querySelectorAll('.card').forEach(card => {
      card.addEventListener('click', () => {
        const isFlipped = card.classList.toggle('flipped');
        card.setAttribute('aria-pressed', isFlipped ? 'true' : 'false');
      });
    });
  </script>
</body>
</html>

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
        "xml_tags_callout": 130,
        "meta_prompt_diagram": 660,
        "choosing_tool_cards": 670,
        "style_layers": 500,
        "plugin_ui_diagram": 820,
        "metaprompt_cowork": 640,
        "phi_decision": 520,
        "when_to_ground": 1780,
    }
    return heights.get(diagram_id, 300)
