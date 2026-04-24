# app.py
# NeuroFlow AI Learning Platform — main entry point.
# Single-file Streamlit app with session-state routing.

import streamlit as st
from data.curriculum import TRACKS, get_track, get_lesson, get_lesson_count, is_last_lesson
from utils.session import (
    init_session_state, navigate,
    is_lesson_complete, is_track_complete,
    get_track_completion_count, get_first_incomplete_lesson,
    go_home, go_track, go_lesson, go_certificate, go_reference,
    complete_lesson,
)
from utils.certificate import render_certificate_page
from components.diagrams import get_diagram, get_diagram_height

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="NeuroFlow AI Learning Platform",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------------------------------
# Global CSS
# ---------------------------------------------------------------------------
st.markdown("""
<style>
  /* ── Force light mode regardless of system setting ────────────────── */
  :root { color-scheme: light only; }

  /* Hide default Streamlit chrome */
  #MainMenu { visibility: hidden; }
  footer { visibility: hidden; }
  header { visibility: hidden; }
  [data-testid="collapsedControl"] { display: none; }
  section[data-testid="stSidebar"] { display: none; }

  /* App background */
  .stApp { background-color: #FFFFFF !important; }
  .block-container { padding-top: 16px !important; max-width: 860px; }

  /* ── All text defaults to dark ─────────────────────────────────────── */
  body, p, div, span, li, td, th, label { color: #212121 !important; }

  /* ── Override: button text is always white (navy bg) or navy (secondary) ─ */
  [data-testid="baseButton-primary"] *,
  [data-testid="baseButton-primary"] p,
  [data-testid="baseButton-primary"] span,
  [data-testid="baseButton-primary"] div,
  .stButton button[kind="primary"] *,
  .stButton button[kind="primary"] p,
  .stButton button[kind="primary"] span {
    color: #FFFFFF !important;
  }
  [data-testid="baseButton-secondary"] *,
  [data-testid="baseButton-secondary"] p,
  [data-testid="baseButton-secondary"] span,
  .stButton button[kind="secondary"] * {
    color: #161BAA !important;
  }

  /* ── Primary button — navy with white text ─────────────────────────── */
  [data-testid="baseButton-primary"],
  .stButton button[kind="primary"] {
    background-color: #161BAA !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 6px !important;
    font-weight: 500 !important;
    padding: 10px 24px !important;
  }
  [data-testid="baseButton-primary"]:hover,
  .stButton button[kind="primary"]:hover {
    background-color: #1219CC !important;
    color: #FFFFFF !important;
  }

  /* ── Secondary button ──────────────────────────────────────────────── */
  [data-testid="baseButton-secondary"],
  .stButton button[kind="secondary"] {
    border: 1.5px solid #161BAA !important;
    color: #161BAA !important;
    background-color: #FFFFFF !important;
    border-radius: 6px !important;
  }

  /* ── Disabled button — grey ────────────────────────────────────────── */
  .stButton button:disabled,
  [data-testid="baseButton-primary"]:disabled,
  [data-testid="baseButton-secondary"]:disabled {
    background-color: #BDBDBD !important;
    color: #FFFFFF !important;
    border: none !important;
    cursor: not-allowed !important;
    border-radius: 6px !important;
  }

  /* ── Radio buttons ─────────────────────────────────────────────────── */
  .stRadio > div { gap: 4px; }
  .stRadio label, .stRadio label span,
  .stRadio [data-testid="stMarkdownContainer"] p {
    color: #212121 !important;
    font-size: 14px !important;
  }

  /* ── Alert / warning / info banners ───────────────────────────────── */
  [data-testid="stAlert"],
  [data-testid="stAlert"] p,
  [data-testid="stAlert"] div,
  [data-testid="stAlert"] span,
  .stAlert p { color: #212121 !important; }

  /* ── Markdown tables ───────────────────────────────────────────────── */
  .stMarkdown table { width: 100%; border-collapse: collapse; margin: 16px 0; }
  .stMarkdown table th {
    background-color: #E8E9F7 !important;
    color: #161BAA !important;
    font-weight: 600 !important;
    padding: 8px 12px !important;
    border: 1px solid #BDBDBD !important;
    text-align: left !important;
  }
  .stMarkdown table td {
    color: #212121 !important;
    padding: 8px 12px !important;
    border: 1px solid #BDBDBD !important;
    background-color: #FFFFFF !important;
  }
  .stMarkdown table tr:nth-child(even) td {
    background-color: #F8F9FA !important;
  }

  /* ── Spinner text ──────────────────────────────────────────────────── */
  [data-testid="stSpinner"] p,
  [data-testid="stSpinner"] div { color: #212121 !important; }

  /* ── Code blocks ───────────────────────────────────────────────────── */
  .stMarkdown code { background-color: #F0F2F6 !important; color: #161BAA !important; padding: 2px 5px; border-radius: 3px; }
  .stMarkdown pre  { background-color: #F0F2F6 !important; color: #212121 !important; }

  /* ── Captions ──────────────────────────────────────────────────────── */
  .stCaption, [data-testid="stCaptionContainer"] p { color: #757575 !important; }

  /* ── Horizontal rule ───────────────────────────────────────────────── */
  hr { border-color: #BDBDBD; margin: 24px 0; }

  /* ── Markdown prose ────────────────────────────────────────────────── */
  .stMarkdown p      { font-size: 15px; line-height: 1.7; color: #212121 !important; }
  .stMarkdown h3     { color: #161BAA !important; margin-top: 24px; }
  .stMarkdown h4     { color: #212121 !important; }
  .stMarkdown li     { color: #212121 !important; }
  .stMarkdown strong { color: #212121 !important; }

  /* ── Track card ────────────────────────────────────────────────────── */
  .track-card {
    border: 1px solid #BDBDBD;
    border-radius: 10px;
    padding: 20px 22px;
    margin-bottom: 12px;
    cursor: pointer;
    transition: box-shadow 0.15s;
  }
  .track-card:hover { box-shadow: 0 2px 12px rgba(22,27,170,0.10); }

  /* ── Level badges ──────────────────────────────────────────────────── */
  .badge-foundation   { background:#E4F5F3; color:#1A6860 !important; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:500; }
  .badge-intermediate { background:#EBF3FA; color:#2A5C8A !important; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:500; }
  .badge-advanced     { background:#E7F6F5; color:#2A6E68 !important; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:500; }
  .badge-wip          { background:#FDECEC; color:#B11F1F !important; padding:3px 10px; border-radius:12px; font-size:11px; font-weight:500; }

  /* ── Inline image spacing ─ single focused rule ─────────────────────
     Zero the paragraph that wraps a standalone image. Everything else
     (element-container gap, image margin) is controlled at the widget
     level using st.image() rather than embedded <img> markdown. */
  [data-testid="stMarkdown"] p:has(> img:only-child) {
    margin: 0 !important;
    line-height: 0 !important;
    font-size: 0 !important;
  }
</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Email gate
# ---------------------------------------------------------------------------
# The platform tracks progress per learner in Supabase. Before any other
# session state exists, prompt the learner for their NeuroFlow email and
# use that as the identifier under which their progress is saved and
# restored. Nothing else renders until this is set.

def _render_email_gate():
    # Force the Submit button's label to render white on the dark blue
    # primary-button background. Must be the very first call in this
    # function so it also applies when the login screen re-renders after
    # st.session_state.clear(). Selectors cover every known Streamlit
    # button DOM layout (data-testid attribute, kind attribute, and
    # nested <p>/<span>/SVG label children) so the override survives
    # Streamlit version upgrades.
    st.markdown(
        """
        <style>
          div[data-testid="stForm"] button[kind="primaryFormSubmit"],
          div[data-testid="stForm"] button[kind="primaryFormSubmit"] *,
          div[data-testid="stForm"] button[data-testid="baseButton-primaryFormSubmit"],
          div[data-testid="stForm"] button[data-testid="baseButton-primaryFormSubmit"] *,
          div[data-testid="stForm"] [data-testid="stFormSubmitButton"] button,
          div[data-testid="stForm"] [data-testid="stFormSubmitButton"] button *,
          div[data-testid="stForm"] button[type="submit"],
          div[data-testid="stForm"] button[type="submit"] * {
            color: white !important;
            fill: white !important;
          }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="text-align:center;padding:48px 0 8px 0;">
          <div style="font-size:11px;letter-spacing:2px;text-transform:uppercase;
                      color:#2EA799;margin-bottom:6px;">NeuroFlow</div>
          <div style="font-size:28px;font-weight:600;color:#161BAA;margin-bottom:6px;">
            AI Learning Platform
          </div>
          <div style="font-size:14px;color:#757575;margin-bottom:28px;">
            Enter your NeuroFlow email to begin or resume your progress.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("email_gate_form", clear_on_submit=False):
            email_input = st.text_input(
                "Work email",
                key="_email_gate_input",
                placeholder="firstname.lastname@neuroflow.com",
                max_chars=120,
                label_visibility="collapsed",
            )
            submitted = st.form_submit_button("Submit", type="primary", use_container_width=True)
        if submitted:
            candidate = (email_input or "").strip().lower()
            if not candidate.endswith("@neuroflow.com"):
                st.markdown(
                    '<p style="color:#C0392B;font-size:13px;margin:8px 0 0 0;'
                    'text-align:center;">Please use your @neuroflow.com email address.</p>',
                    unsafe_allow_html=True,
                )
            else:
                st.session_state.user_email = candidate
                st.rerun()


if "user_email" not in st.session_state:
    _render_email_gate()
    st.stop()


# ---------------------------------------------------------------------------
# Session init
# ---------------------------------------------------------------------------
init_session_state()


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _badge(level: str) -> str:
    cls = {
        "Foundation": "badge-foundation",
        "Intermediate": "badge-intermediate",
        "Advanced": "badge-advanced",
        "Still Under Development": "badge-wip",
    }.get(level, "badge-foundation")
    return f'<span class="{cls}">{level}</span>'


def _render_lesson_footer(track_id: int, lesson_id: int) -> None:
    """Render the 'Last reviewed / Next review due' footer for a lesson.

    Reads `last_reviewed` (YYYY-MM-DD string) and `review_cadence_days` (int)
    from the lesson meta in curriculum.py. Falls back to platform defaults
    when not specified.
    """
    from datetime import datetime, timedelta
    DEFAULT_REVIEWED = "2026-04-22"
    DEFAULT_CADENCE_DAYS = 90
    lesson_meta = get_lesson(track_id, lesson_id) or {}
    reviewed_str = lesson_meta.get("last_reviewed", DEFAULT_REVIEWED)
    cadence_days = int(lesson_meta.get("review_cadence_days", DEFAULT_CADENCE_DAYS))
    try:
        reviewed_date = datetime.strptime(reviewed_str, "%Y-%m-%d").date()
    except ValueError:
        reviewed_date = datetime.strptime(DEFAULT_REVIEWED, "%Y-%m-%d").date()
    next_due = reviewed_date + timedelta(days=cadence_days)
    st.markdown(
        f'<p style="font-size:11px;color:#757575;margin:28px 0 0 0;'
        f'padding-top:14px;border-top:1px solid #E5E7EB;">'
        f'Last reviewed {reviewed_date.isoformat()}. '
        f'Next review due {next_due.isoformat()}.</p>',
        unsafe_allow_html=True,
    )


def _progress_bar(done: int, total: int) -> str:
    pct = int((done / total) * 100) if total else 0
    return (
        f'<div style="background:#BDBDBD;border-radius:4px;height:6px;margin:6px 0;">'
        f'<div style="background:#161BAA;border-radius:4px;height:6px;width:{pct}%;"></div>'
        f'</div>'
        f'<span style="font-size:11px;color:#757575;">{done}/{total} lessons</span>'
    )


def _nav_header(track_id: int = None, lesson_id: int = None):
    """Top navigation bar shown on all non-home pages."""
    col1, col2, col3 = st.columns([1, 4, 1])
    with col1:
        if track_id and lesson_id:
            if st.button("← Track", key="nav_back"):
                go_track(track_id)
        else:
            if st.button("← Home", key="nav_home"):
                go_home()
    with col2:
        if track_id:
            track = get_track(track_id)
            label = f"Track {track_id} — {track.get('title', '')}"
            if lesson_id:
                total = get_lesson_count(track_id)
                label += f" &nbsp;·&nbsp; Lesson {lesson_id} of {total}"
            st.markdown(
                f'<p style="text-align:center;color:#161BAA;font-weight:500;'
                f'font-size:14px;margin:6px 0;">{label}</p>',
                unsafe_allow_html=True,
            )
    with col3:
        if track_id and not lesson_id:
            pass  # track overview — no extra nav
        elif track_id and lesson_id:
            done, total = get_track_completion_count(track_id)
            st.markdown(
                f'<p style="text-align:right;color:#757575;font-size:12px;margin:6px 0;">'
                f'{done}/{total} done</p>',
                unsafe_allow_html=True,
            )
    st.markdown("<hr style='margin:8px 0 20px 0;border-color:#BDBDBD;'>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Views
# ---------------------------------------------------------------------------

def view_home():
    """Home page — 8 track cards + Course Reference."""
    st.markdown(
        """
        <div style="padding: 24px 0 8px 0;">
          <div style="font-size:11px;letter-spacing:2px;text-transform:uppercase;
                      color:#2EA799;margin-bottom:6px;">NeuroFlow</div>
          <div style="font-size:30px;font-weight:600;color:#161BAA;margin-bottom:4px;">
            AI Learning Platform
          </div>
          <div style="font-size:15px;color:#757575;">
            Eight self-paced tracks. Start anywhere. Complete at your own pace.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # 2-column grid of track cards
    track_ids = list(TRACKS.keys())
    for row_start in range(0, len(track_ids), 2):
        col1, col2 = st.columns(2, gap="medium")
        for col, t_id in zip([col1, col2], track_ids[row_start: row_start + 2]):
            track = TRACKS[t_id]
            done, total = get_track_completion_count(t_id)
            complete = is_track_complete(t_id)
            with col:
                st.markdown(
                    f"""
                    <div style="border:1px solid {'#2EA799' if complete else '#BDBDBD'};
                                border-radius:10px;padding:20px 22px;margin-bottom:4px;
                                background:{'#F0FBF9' if complete else '#FFFFFF'};">
                      <div style="display:flex;justify-content:space-between;
                                  align-items:flex-start;margin-bottom:10px;">
                        <span style="font-size:12px;color:#757575;font-weight:500;">
                          Track {t_id}
                        </span>
                        {_badge(track['level'])}
                      </div>
                      <div style="font-size:17px;font-weight:600;color:#212121;
                                  margin-bottom:6px;">{track['title']}</div>
                      <div style="font-size:12px;color:#757575;margin-bottom:10px;">
                        {total} lessons &nbsp;·&nbsp; ~{track['time_estimate']} min
                      </div>
                      {_progress_bar(done, total)}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
                btn_label = "✓ View certificate" if complete else (
                    "Continue →" if done > 0 else "Start track →"
                )
                if st.button(btn_label, key=f"track_btn_{t_id}", use_container_width=True):
                    if complete:
                        go_certificate(t_id)
                    else:
                        go_track(t_id)

    # Course Reference card
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style="border:1px solid #BDBDBD;border-radius:10px;padding:18px 22px;
                    background:#FAFAFA;display:flex;align-items:center;
                    justify-content:space-between;">
          <div>
            <div style="font-size:16px;font-weight:600;color:#212121;">Course Reference</div>
            <div style="font-size:13px;color:#757575;margin-top:3px;">
              All lesson content across every track — no quizzes. Use any time.
            </div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button("Open Course Reference →", key="ref_btn"):
        go_reference()

    # --- Account footer: signed-in identity + reset progress ------------
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        "<hr style='border-color:#E5E7EB;margin:8px 0 14px 0;'>",
        unsafe_allow_html=True,
    )
    current_email = st.session_state.get("user_email", "")
    st.markdown(
        f'<p style="font-size:12px;color:#757575;margin:0 0 10px 0;">'
        f'Signed in as <strong>{current_email}</strong></p>',
        unsafe_allow_html=True,
    )

    # --- Storage status -------------------------------------------------
    # Persistence failures (most often RLS policies blocking the anon key)
    # are otherwise invisible because save/load are silent by design. This
    # panel is self-contained on purpose: it does not depend on any
    # importable helper from utils/persistence beyond the top-level module
    # itself, so a partial deploy or a stale import cache cannot break the
    # expander. Every step is wrapped in its own try/except and surfaces
    # the raw exception string.
    #
    # Hidden by default. Append `?debug=1` to the app URL to reveal it —
    # e.g., https://your-app.streamlit.app/?debug=1
    _show_debug = False
    try:
        # Streamlit ≥ 1.30 exposes the dict-like st.query_params.
        _show_debug = st.query_params.get("debug") == "1"
    except Exception:
        try:
            _show_debug = (
                st.experimental_get_query_params().get("debug", ["0"])[0] == "1"
            )
        except Exception:
            _show_debug = False
    if _show_debug:
        with st.expander("Storage status (save / load diagnostics)"):
          if st.button("Run check", key="storage_diagnose_btn"):
              from datetime import datetime, timezone

              def _row(label, ok, detail=""):
                  icon = "✓" if ok else "✗"
                  color = "#1A6860" if ok else "#C0392B"
                  suffix = f' <span style="color:#757575;">— {detail}</span>' if detail else ""
                  st.markdown(
                      f'<p style="font-size:13px;margin:2px 0;">'
                      f'<span style="color:{color};font-weight:600;">{icon}</span> '
                      f'{label}{suffix}</p>',
                      unsafe_allow_html=True,
                  )

              # Step 1: secrets
              secrets_ok = True
              secrets_detail = ""
              url = ""
              key = ""
              try:
                  url = st.secrets["SUPABASE_URL"]
                  key = st.secrets["SUPABASE_KEY"]
                  if not url or not key:
                      secrets_ok = False
                      secrets_detail = "SUPABASE_URL or SUPABASE_KEY is empty"
              except Exception as exc:
                  secrets_ok = False
                  secrets_detail = f"missing from st.secrets: {exc}"
              _row("Supabase secrets present", secrets_ok, secrets_detail)

              # Step 1b: surface the exact URL shape so we can catch typos,
              # trailing slashes, stray /rest/v1 suffixes, or the wrong
              # Supabase project URL being pasted into secrets.
              if url:
                  display_url = url
                  # Mask the 20-char project ref between "https://" and ".supabase.co"
                  try:
                      import re
                      m = re.match(r"^(https?://)([^.]+)(\.supabase\.co.*)$", url)
                      if m:
                          ref = m.group(2)
                          masked = ref[:4] + "…" + ref[-4:] if len(ref) > 10 else "…"
                          display_url = f"{m.group(1)}{masked}{m.group(3)}"
                  except Exception:
                      pass
                  url_issues = []
                  if not url.startswith("https://"):
                      url_issues.append("not https")
                  if url.endswith("/"):
                      url_issues.append("has trailing slash")
                  if "/rest/v1" in url:
                      url_issues.append("includes /rest/v1 (should be base URL only)")
                  if ".supabase.co" not in url:
                      url_issues.append("does not contain .supabase.co")
                  issues_txt = "; ".join(url_issues) if url_issues else "looks well-formed"
                  _row(f"URL shape: <code>{display_url}</code>", not url_issues, issues_txt)

              # Step 2: package
              pkg_ok = False
              pkg_detail = ""
              create_client = None
              try:
                  from supabase import create_client as _cc
                  create_client = _cc
                  pkg_ok = True
              except Exception as exc:
                  pkg_detail = f"import failed: {exc}"
              _row("supabase package installed", pkg_ok, pkg_detail)

              # Step 3: client init
              client = None
              client_ok = False
              client_detail = ""
              if secrets_ok and pkg_ok:
                  try:
                      client = create_client(url, key)
                      client_ok = client is not None
                  except Exception as exc:
                      client_detail = f"init failed: {exc}"
              _row("Client initialized", client_ok, client_detail)

              # Step 4: read probe
              read_ok = False
              row_exists = False
              read_detail = ""
              if client_ok:
                  try:
                      resp = (
                          client.table("progress")
                          .select("state")
                          .eq("user_id", current_email)
                          .limit(1)
                          .execute()
                      )
                      rows = getattr(resp, "data", None) or []
                      read_ok = True
                      row_exists = bool(rows)
                      read_detail = "row found" if row_exists else "no row yet for this email"
                  except Exception as exc:
                      read_detail = f"{exc}"
              _row("Read probe", read_ok, read_detail)

              # Step 5: write probe (upsert current live state)
              write_ok = False
              write_detail = ""
              if client_ok:
                  try:
                      progress_payload = {}
                      for t_id, lessons in (st.session_state.get("progress") or {}).items():
                          progress_payload[str(t_id)] = {
                              str(l_id): bool(v) for l_id, v in (lessons or {}).items()
                          }
                      cert_payload = {
                          str(t_id): str(n)
                          for t_id, n in (st.session_state.get("certificate_names") or {}).items()
                      }
                      row = {
                          "user_id": current_email,
                          "state": {
                              "view": st.session_state.get("view", "home"),
                              "current_track": st.session_state.get("current_track"),
                              "current_lesson": st.session_state.get("current_lesson"),
                              "progress": progress_payload,
                              "certificate_names": cert_payload,
                          },
                          "updated_at": datetime.now(timezone.utc).isoformat(),
                      }
                      client.table("progress").upsert(row, on_conflict="user_id").execute()
                      write_ok = True
                  except Exception as exc:
                      write_detail = f"{exc}"
              _row("Write probe (upsert current state)", write_ok, write_detail)

              # Step 6: raw HTTP probe. Bypasses the supabase client and calls
              # PostgREST directly so we can see what the Supabase project
              # itself returns, along with the precise URL used. Catches
              # cases where SUPABASE_URL points to the wrong project or has
              # a structural problem the client library silently tolerates.
              raw_ok = False
              raw_detail = ""
              if secrets_ok:
                  try:
                      import requests
                      base = url.rstrip("/")
                      # Strip an accidentally-included REST path suffix so we
                      # always hit the correct endpoint.
                      if base.endswith("/rest/v1"):
                          base = base[: -len("/rest/v1")]
                      probe_url = f"{base}/rest/v1/progress?select=user_id&limit=1"
                      resp = requests.get(
                          probe_url,
                          headers={
                              "apikey": key,
                              "Authorization": f"Bearer {key}",
                              "Accept": "application/json",
                          },
                          timeout=10,
                      )
                      if resp.status_code == 200:
                          raw_ok = True
                          raw_detail = f"HTTP 200; body={resp.text[:200]}"
                      else:
                          raw_detail = (
                              f"HTTP {resp.status_code}; body={resp.text[:300]}"
                          )
                  except Exception as exc:
                      raw_detail = f"request failed: {exc}"
              _row("Raw HTTP GET /rest/v1/progress", raw_ok, raw_detail)

              if client_ok and not write_ok:
                  st.markdown(
                      '<p style="font-size:12px;color:#757575;margin:10px 0 0 0;">'
                      '<strong>Interpreting PGRST125 "Invalid path":</strong><br>'
                      '• The <code>progress</code> table does not exist in the '
                      'project your <code>SUPABASE_URL</code> points to, '
                      '<strong>or</strong><br>'
                      '• <code>SUPABASE_URL</code> points to a different project '
                      'than the one where you ran <code>create table</code>, '
                      '<strong>or</strong><br>'
                      '• PostgREST\'s schema cache is stale. In the Supabase '
                      'SQL editor, run <code>notify pgrst, \'reload schema\';</code>. '
                      'If that does not help, open Project Settings → API → '
                      'click <strong>Restart server</strong>.<br><br>'
                      'Verify the project match: open Supabase → Project Settings '
                      '→ API → Project URL. It must equal the masked URL above.</p>',
                      unsafe_allow_html=True,
                  )
    # Two-step confirmation so a single stray click cannot delete progress.
    if not st.session_state.get("_reset_confirm_open"):
        if st.button("Reset my progress", key="reset_progress_open", type="secondary"):
            st.session_state._reset_confirm_open = True
            st.rerun()
    else:
        st.markdown(
            '<p style="font-size:13px;color:#C0392B;margin:0 0 8px 0;">'
            'This will delete all your saved progress across every track. '
            'This cannot be undone.</p>',
            unsafe_allow_html=True,
        )
        col_a, col_b, _ = st.columns([1, 1, 4])
        with col_a:
            if st.button("Confirm reset", key="reset_progress_confirm", type="primary"):
                from utils.persistence import reset_user_progress
                reset_user_progress(current_email)
                st.session_state.clear()
                st.rerun()
        with col_b:
            if st.button("Cancel", key="reset_progress_cancel"):
                st.session_state._reset_confirm_open = False
                st.rerun()


def view_track_overview(track_id: int):
    """Track overview — lesson list + Start/Continue button."""
    _nav_header(track_id=track_id)

    track = get_track(track_id)
    lessons = track.get("lessons", {})
    done, total = get_track_completion_count(track_id)

    st.markdown(
        f"""
        <div style="margin-bottom:20px;">
          <div style="margin-bottom:6px;">{_badge(track['level'])}</div>
          <div style="font-size:26px;font-weight:600;color:#161BAA;margin-bottom:6px;">
            Track {track_id} — {track['title']}
          </div>
          <div style="font-size:13px;color:#757575;">
            {total} lessons &nbsp;·&nbsp; ~{track['time_estimate']} min
            &nbsp;·&nbsp; Certificate: {track['certificate_title']}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Under construction notice for advanced tracks still in development
    if track_id in (7, 8):
        st.markdown(
            '<div style="background:#FFF8E1;border-left:4px solid #F5A623;border-radius:0 6px 6px 0;'
            'padding:12px 16px;margin:0 0 20px 0;">'
            '<span style="font-size:16px;">🏗️</span> '
            '<strong style="color:#7A5500;">Under construction</strong>'
            '<span style="color:#212121;"> — this track is still being developed and content may change.</span>'
            '</div>',
            unsafe_allow_html=True,
        )

    # Lesson list
    for l_id, lesson_meta in sorted(lessons.items()):
        complete = is_lesson_complete(track_id, l_id)
        icon = "✓" if complete else f"{l_id}"
        icon_color = "#2EA799" if complete else "#161BAA"
        col1, col2 = st.columns([6, 1])
        with col1:
            st.markdown(
                f"""
                <div style="display:flex;align-items:center;padding:12px 0;
                            border-bottom:1px solid #F0F0F0;">
                  <span style="width:28px;height:28px;border-radius:50%;
                               background:{'#E4F5F3' if complete else '#E8E9F7'};
                               color:{icon_color};font-size:13px;font-weight:600;
                               display:flex;align-items:center;justify-content:center;
                               margin-right:14px;flex-shrink:0;">{icon}</span>
                  <div>
                    <span style="font-size:14px;color:#212121;font-weight:{'600' if not complete else '400'};">
                      {l_id}.&nbsp;&nbsp;{lesson_meta['title']}
                    </span>
                    <br>
                    <span style="font-size:11px;color:#757575;">
                      ~{lesson_meta['time_estimate']} min
                    </span>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            if st.button(
                "Review" if complete else "Start",
                key=f"lesson_btn_{track_id}_{l_id}",
            ):
                go_lesson(track_id, l_id)

    # Certificate row in lesson list when all complete
    if is_track_complete(track_id):
        st.markdown("<div style='border-top:1px solid #F0F0F0;'></div>", unsafe_allow_html=True)
        col1, col2 = st.columns([6, 1])
        with col1:
            st.markdown(
                """
                <div style="display:flex;align-items:center;padding:12px 0;">
                  <span style="width:28px;height:28px;border-radius:50%;
                               background:#E4F5F3;color:#2EA799;font-size:13px;font-weight:600;
                               display:flex;align-items:center;justify-content:center;
                               margin-right:14px;flex-shrink:0;">✓</span>
                  <div>
                    <span style="font-size:14px;color:#212121;font-weight:400;">Certificate of completion</span>
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with col2:
            if st.button("View", key=f"cert_row_{track_id}", type="primary"):
                go_certificate(track_id)

    st.markdown("<br>", unsafe_allow_html=True)

    # Start / Continue CTA
    if is_track_complete(track_id):
        if st.button("View certificate →", type="primary", key=f"track_cert_{track_id}"):
            go_certificate(track_id)
        # Track 3 — prompt engineering flashcard download
        if track_id == 3:
            try:
                with open("track3_flashcard.html", "rb") as f:
                    flashcard_bytes = f.read()
                st.download_button(
                    label="⬇ Download prompt engineering quick reference",
                    data=flashcard_bytes,
                    file_name="NeuroFlow_PromptEngineering_QuickReference.html",
                    mime="text/html",
                    key="track3_flashcard_dl",
                )
                st.caption("Open the downloaded file in any browser to view or print.")
            except FileNotFoundError:
                pass
    else:
        next_lesson = get_first_incomplete_lesson(track_id)
        lbl = f"Continue — Lesson {next_lesson}" if done > 0 else f"Start — Lesson 1"
        if st.button(lbl, type="primary", key=f"track_start_{track_id}"):
            go_lesson(track_id, next_lesson)


def view_lesson(track_id: int, lesson_id: int):
    """Lesson page — warning banner, content, next/complete button."""
    _nav_header(track_id=track_id, lesson_id=lesson_id)

    # Session-only warning
    st.warning(
        "Progress is session-only — refreshing this page will reset your work.",
        icon="⚠️",
    )

    track = get_track(track_id)
    lesson_meta = get_lesson(track_id, lesson_id)

    st.markdown(
        f"""
        <div style="margin-bottom:18px;">
          <div style="font-size:12px;color:#757575;margin-bottom:4px;">
            Track {track_id} · Lesson {lesson_id}
          </div>
          <div style="font-size:22px;font-weight:600;color:#161BAA;">
            {lesson_meta.get('title', '')}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------- Diagram (before content, where applicable) ----------
    if (lesson_meta.get("has_diagram") and not lesson_meta.get("has_video")
            and lesson_meta.get("diagram_position") != "after"):
        diagram_id = lesson_meta.get("diagram_id")
        if diagram_id:
            html = get_diagram(diagram_id)
            height = get_diagram_height(diagram_id)
            if html:
                st.components.v1.html(html, height=height, scrolling=False)
                st.markdown("<br>", unsafe_allow_html=True)

    # ---------- Video ----------
    if lesson_meta.get("has_video"):
        video_url = lesson_meta.get("video_url", "")
        st.markdown(
            f'<iframe width="100%" height="400" src="{video_url}" '
            f'frameborder="0" '
            f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
            f'allowfullscreen style="border-radius:6px; display:block;"></iframe>',
            unsafe_allow_html=True,
        )
        st.markdown("<br>", unsafe_allow_html=True)

    # ---------- Diagram after video (Track 5.3 etc.) ----------
    if lesson_meta.get("has_diagram") and lesson_meta.get("has_video"):
        diagram_id = lesson_meta.get("diagram_id")
        if diagram_id:
            html = get_diagram(diagram_id)
            height = get_diagram_height(diagram_id)
            if html:
                st.components.v1.html(html, height=height, scrolling=False)
                st.markdown("<br>", unsafe_allow_html=True)

    # ---------- Track lesson content ----------
    lesson_passed = _render_track_lesson(track_id, lesson_id)

    # ---------- Diagram after content (diagram_position="after") ----------
    if (lesson_meta.get("has_diagram")
            and lesson_meta.get("diagram_position") == "after"):
        diagram_id = lesson_meta.get("diagram_id")
        if diagram_id:
            html = get_diagram(diagram_id)
            height = get_diagram_height(diagram_id)
            if html:
                st.markdown("<br>", unsafe_allow_html=True)
                st.components.v1.html(html, height=height, scrolling=False)

    # ---------- Next / Complete Track button ----------
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")

    last = is_last_lesson(track_id, lesson_id)
    all_done = is_track_complete(track_id)

    if lesson_passed or is_lesson_complete(track_id, lesson_id):
        if last and all_done:
            if st.button("View certificate →", type="primary", key=f"next_{track_id}_{lesson_id}"):
                go_certificate(track_id)
        elif last and not all_done:
            if st.button("Back to track →", type="primary", key=f"next_{track_id}_{lesson_id}"):
                go_track(track_id)
            st.caption("Complete all lessons to unlock the certificate.")
        else:
            if st.button("Next lesson →", type="primary", key=f"next_{track_id}_{lesson_id}"):
                go_lesson(track_id, lesson_id + 1)
    else:
        btn_label = "View certificate →" if (last and all_done) else ("Next lesson →" if not last else "Back to track →")
        st.button(btn_label, disabled=True, key=f"next_dis_{track_id}_{lesson_id}")
        st.caption("Complete the lesson to continue.")

    # ---------- Last reviewed footer ----------
    # Staff use this to tell whether a lesson reflects the current state of the
    # platform. Cadence defaults to 90 days for fast-moving features; lessons
    # can override to 180 days in curriculum.py for stable content.
    _render_lesson_footer(track_id, lesson_id)


def _render_track_lesson(track_id: int, lesson_id: int) -> bool:
    """Dispatch to the correct track module's render_lesson function."""
    try:
        if track_id == 1:
            from tracks.track1 import render_lesson
        elif track_id == 2:
            from tracks.track2 import render_lesson
        elif track_id == 3:
            from tracks.track3 import render_lesson
        elif track_id == 4:
            from tracks.track4 import render_lesson
        elif track_id == 5:
            from tracks.track5 import render_lesson
        elif track_id == 6:
            from tracks.track6 import render_lesson
        elif track_id == 7:
            from tracks.track7 import render_lesson
        elif track_id == 8:
            from tracks.track8 import render_lesson
        else:
            st.error(f"Track {track_id} not found.")
            return False
        return render_lesson(lesson_id)
    except ImportError:
        st.info(
            f"Track {track_id} content is coming soon. "
            "Check back after the next update.",
            icon="🔜",
        )
        # Allow bypass during development
        if st.button("Mark complete (dev)", key=f"dev_complete_{track_id}_{lesson_id}"):
            complete_lesson(track_id, lesson_id)
            st.rerun()
        return is_lesson_complete(track_id, lesson_id)


def view_certificate(track_id: int):
    """Certificate page."""
    _nav_header(track_id=track_id)
    track = get_track(track_id)
    render_certificate_page(
        track_id=track_id,
        track_title=track.get("title", ""),
        certificate_title=track.get("certificate_title", ""),
    )


def view_reference():
    """Course Reference — all lesson content, no quizzes."""
    col1, _ = st.columns([1, 8])
    with col1:
        if st.button("← Home", key="ref_home"):
            go_home()

    st.markdown(
        """
        <div style="padding: 16px 0 24px 0;">
          <div style="font-size:26px;font-weight:600;color:#161BAA;margin-bottom:6px;">
            Course Reference
          </div>
          <div style="font-size:14px;color:#757575;">
            All lesson content across every track. No quizzes or challenges.
            Use this any time to review material.
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for t_id, track in TRACKS.items():
        with st.expander(f"Track {t_id} — {track['title']}", expanded=False):
            for l_id, lesson_meta in sorted(track["lessons"].items()):
                st.markdown(
                    f"#### {l_id}. {lesson_meta['title']}",
                )
                _render_reference_lesson(t_id, l_id)
                st.markdown("---")


def _render_reference_lesson(track_id: int, lesson_id: int):
    """Render lesson concept content only — no quiz, no challenge."""
    try:
        if track_id == 1:
            from tracks.track1 import LESSONS
        elif track_id == 2:
            from tracks.track2 import LESSONS
        elif track_id == 3:
            from tracks.track3 import LESSONS
        elif track_id == 4:
            from tracks.track4 import LESSONS
        elif track_id == 5:
            from tracks.track5 import LESSONS
        elif track_id == 6:
            from tracks.track6 import LESSONS
        elif track_id == 7:
            from tracks.track7 import LESSONS
        elif track_id == 8:
            from tracks.track8 import LESSONS
        else:
            st.caption("Content not available.")
            return

        # Render diagram if this lesson has one
        lesson_meta = get_lesson(track_id, lesson_id)
        if lesson_meta.get("has_diagram"):
            diagram_id = lesson_meta.get("diagram_id")
            if diagram_id:
                html = get_diagram(diagram_id)
                height = get_diagram_height(diagram_id)
                if html:
                    st.components.v1.html(html, height=height, scrolling=False)
                    st.markdown("<br>", unsafe_allow_html=True)

        lesson = LESSONS.get(lesson_id)
        if not lesson or not lesson.get("concept"):
            st.caption("Content coming soon.")
            return

        concept = lesson["concept"]

        # Handle inline HTML (images, iframes) — split and render with unsafe_allow_html
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

    except (ImportError, AttributeError):
        st.caption("Content coming soon.")


# ---------------------------------------------------------------------------
# Router
# ---------------------------------------------------------------------------

view = st.session_state.get("view", "home")
track_id = st.session_state.get("current_track")
lesson_id = st.session_state.get("current_lesson")

# If a navigation action just flagged a scroll-to-top, emit a script that
# scrolls the Streamlit app window back to the top. Because Streamlit renders
# the app inside nested iframes and also restores scroll position across
# reruns, we have to:
#   1. Walk up to the top-level window explicitly.
#   2. Try scrolling both the window and the Streamlit container elements.
#   3. Repeat on a short timer so the scroll wins the race against any
#      Streamlit scroll restoration that runs after our initial call.
# A cache-busting nonce is included so the iframe content is different on
# every navigation — otherwise Streamlit's component cache would reuse the
# old iframe and the inline script would not run again.
if st.session_state.pop("scroll_to_top", False):
    import time as _time
    _nonce = int(_time.time() * 1000)
    st.components.v1.html(
        f"""
        <script>
          (function() {{
            var nonce = {_nonce};
            function tryScroll(w) {{
              if (!w) return;
              try {{ w.scrollTo(0, 0); }} catch (e) {{}}
              try {{
                if (w.document && w.document.documentElement) {{
                  w.document.documentElement.scrollTop = 0;
                }}
                if (w.document && w.document.body) {{
                  w.document.body.scrollTop = 0;
                }}
                // Streamlit main content is inside a scrollable container.
                var selectors = [
                  'section.main',
                  '[data-testid="stAppViewContainer"]',
                  '[data-testid="stMain"]',
                  'div.main'
                ];
                for (var i = 0; i < selectors.length; i++) {{
                  var el = w.document.querySelector(selectors[i]);
                  if (el) el.scrollTop = 0;
                }}
              }} catch (e) {{ /* cross-origin — ignore */ }}
            }}
            function scrollAll() {{
              tryScroll(window);
              tryScroll(window.parent);
              tryScroll(window.top);
            }}
            scrollAll();
            // Streamlit restores scroll position on rerun; keep scrolling to
            // the top for a short window so we win the race.
            setTimeout(scrollAll, 50);
            setTimeout(scrollAll, 150);
            setTimeout(scrollAll, 350);
            setTimeout(scrollAll, 700);
          }})();
        </script>
        <!-- nonce:{_nonce} -->
        """,
        height=0,
    )

if view == "home":
    view_home()
elif view == "track" and track_id:
    view_track_overview(track_id)
elif view == "lesson" and track_id and lesson_id:
    view_lesson(track_id, lesson_id)
elif view == "certificate" and track_id:
    view_certificate(track_id)
elif view == "reference":
    view_reference()
else:
    view_home()
