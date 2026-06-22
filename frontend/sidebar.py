import streamlit as st

NAVIGATION_ITEMS = [
    "📊 Overview",
    "👥 Workforce Analytics",
    "⚠️ Risk Intelligence",
    "🧠 Strategic Insights"
]

DEPARTMENTS = [
    "All",
    "Sales",
    "Research & Development",
    "Human Resources"
]


def render_sidebar():
    """Render dataset upload sidebar."""

    st.sidebar.markdown("""
    <div style="
    margin-bottom:10px;
    ">

    <div style="
    font-size:18px;
    font-weight:700;
    color:white;
    margin-bottom:6px;
    letter-spacing:-0.4px;
    ">
    Workforce Dataset Upload
    </div>

    <div style="
    font-size:13px;
    color:#94A3B8;
    line-height:1.7;
    margin-bottom:14px;
    ">
    Import workforce intelligence datasets for
    predictive analytics and risk simulation.
    </div>

    </div>
    """, unsafe_allow_html=True)

    uploaded_file = st.sidebar.file_uploader(
        "",
        type=["csv"]
    )

    return uploaded_file


def render_navigation(
    navigation_items=NAVIGATION_ITEMS,
    departments=DEPARTMENTS
):
    """Render sidebar navigation and filters."""

    st.sidebar.markdown("""
    <div style="background: linear-gradient(135deg, rgba(45,55,72,0.95), rgba(30,41,59,0.92)); border: 1.5px solid rgba(255,255,255,0.10); border-radius: 32px; padding: 28px 24px; margin: 20px 0; box-shadow: 0 12px 35px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.06);">

    <h2 style="color:white; font-size:32px; font-weight:800; line-height:1.15; margin:0 0 14px 0;">
    Workforce Intelligence Navigator
    </h2>

    <p style="color:#CBD5E1; font-size:13px; line-height:1.8; margin:0;">
    Predictive Workforce Analytics &
    Strategic Attrition Intelligence Platform
    </p>

    </div>
    """, unsafe_allow_html=True)
    
    selected_section = st.sidebar.radio(
    "Navigation",
    navigation_items,
    label_visibility="collapsed",
    key="sidebar_navigation"
)

    selected_department = st.sidebar.selectbox(
        "Department Filter",
        departments,
        key="department_filter"
    )

    return selected_section, selected_department