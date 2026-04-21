# utils/certificate.py
# Renders a printable certificate using st.components.v1.html().

import streamlit as st
from datetime import date


def render_certificate_page(track_id: int, track_title: str, certificate_title: str):
    """
    Full certificate page. Prompts for learner name, then renders
    a printable certificate with a Print/Save PDF button.
    """
    st.markdown(
        """
        <div style="text-align:center;padding:24px 0 8px 0;">
          <div style="font-size:28px;font-weight:600;color:#161BAA;">Track complete</div>
          <div style="font-size:15px;color:#757575;margin-top:6px;">
            Enter your name to generate your certificate.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    name_key = f"cert_name_{track_id}"
    if name_key not in st.session_state:
        st.session_state[name_key] = ""

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        name = st.text_input(
            "Your full name",
            key=name_key,
            placeholder="e.g. Alex Chen",
            max_chars=80,
        )

    if not name or not name.strip():
        st.markdown(
            '<p style="text-align:center;color:#757575;font-size:13px;">'
            "Enter your name above to display the certificate.</p>",
            unsafe_allow_html=True,
        )
        return

    completion_date = date.today().strftime("%B %d, %Y")

    # Compute save-as filename from the last whitespace-separated token of the
    # learner name. Sanitize to an ASCII-safe filename so browsers accept it as
    # the default Save-as-PDF name.
    cleaned_name = name.strip()
    tokens = cleaned_name.split()
    last_token = tokens[-1] if tokens else cleaned_name
    safe_last = "".join(ch for ch in last_token if ch.isalnum())
    if not safe_last:
        safe_last = "Certificate"
    save_name = f"{safe_last}_Track{track_id}"

    cert_html = _build_certificate_html(
        learner_name=cleaned_name,
        certificate_title=certificate_title,
        completion_date=completion_date,
        track_number=track_id,
        save_name=save_name,
    )

    st.components.v1.html(cert_html, height=560, scrolling=False)
    st.caption(
        f'Tip: when the print dialog opens, the suggested filename will be '
        f'"{save_name}". You can still edit it before saving.'
    )

    # Back to home
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        from utils.session import go_home
        if st.button("← Back to course directory", key=f"cert_home_{track_id}", use_container_width=True):
            go_home()


def _build_certificate_html(
    learner_name: str,
    certificate_title: str,
    completion_date: str,
    track_number: int = 0,
    save_name: str = "Certificate",
) -> str:
    return f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{save_name}</title>
<style>
  body {{
    margin: 0;
    font-family: -apple-system, 'Helvetica Neue', Arial, sans-serif;
    background: #f8f8f8;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 24px 0;
  }}
  .cert {{
    width: 640px;
    background: #FFFFFF;
    border: 3px solid #161BAA;
    border-radius: 8px;
    padding: 48px 56px;
    text-align: center;
    box-sizing: border-box;
  }}
  .issuer {{
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: #161BAA;
    margin-bottom: 32px;
  }}
  .label {{
    font-size: 14px;
    color: #757575;
    margin-bottom: 12px;
  }}
  .name {{
    font-size: 30px;
    font-weight: 600;
    color: #161BAA;
    border-bottom: 2px solid #2EA799;
    padding-bottom: 10px;
    margin: 0 auto 24px auto;
    display: inline-block;
  }}
  .completed-label {{
    font-size: 14px;
    color: #212121;
    margin-bottom: 8px;
  }}
  .track-title {{
    font-size: 22px;
    font-weight: 500;
    color: #161BAA;
    margin-bottom: 36px;
  }}
  .footer {{
    font-size: 12px;
    color: #757575;
    border-top: 1px solid #BDBDBD;
    padding-top: 20px;
    margin-top: 8px;
  }}
  .print-btn {{
    margin-top: 16px;
    background: #161BAA;
    color: white;
    padding: 10px 28px;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 500;
    font-family: inherit;
  }}
  .print-btn:hover {{
    background: #1219CC;
  }}
  @media print {{
    body {{ background: white; padding: 0; }}
    .cert {{ border: 3px solid #161BAA; box-shadow: none; }}
    .print-btn {{ display: none; }}
  }}
</style>
</head>
<body>
  <div class="cert">
    <div class="issuer">NeuroFlow AI Learning Platform</div>
    <div class="label">This certifies that</div>
    <div>
      <span class="name">{learner_name}</span>
    </div>
    <div class="completed-label">has successfully completed</div>
    <div class="track-title">{certificate_title}</div>
    <div class="footer">
      Track {track_number} &nbsp;·&nbsp; Issued by NeuroFlow &nbsp;·&nbsp; {completion_date}
    </div>
  </div>
  <button class="print-btn" id="print-btn">
    Print / Save as PDF
  </button>
<script>
  // Set a filename-friendly title on this iframe. Also attempt to set the
  // parent Streamlit page's title, since some browsers use the top-level
  // document title for the default PDF filename. Cross-origin access may be
  // blocked; if so, we silently fall back to the iframe title.
  (function() {{
    var saveName = {save_name!r};
    document.title = saveName;
    var previousParentTitle = null;
    try {{
      previousParentTitle = window.top.document.title;
    }} catch (e) {{ /* cross-origin blocked */ }}

    document.getElementById('print-btn').addEventListener('click', function() {{
      try {{ window.top.document.title = saveName; }} catch (e) {{}}
      window.focus();
      window.print();
      // Restore the parent title after the print dialog closes.
      setTimeout(function() {{
        try {{
          if (previousParentTitle !== null) {{
            window.top.document.title = previousParentTitle;
          }}
        }} catch (e) {{}}
      }}, 2000);
    }});
  }})();
</script>
</body>
</html>
"""
