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
</style>
""", unsafe_allow_html=True)


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
    }.get(level, "badge-foundation")
    return f'<span class="{cls}">{level}</span>'


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
