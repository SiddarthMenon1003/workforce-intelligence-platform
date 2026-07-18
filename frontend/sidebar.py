"""Sidebar: dataset upload, navigation, and persistent status panels."""

import streamlit as st

NAVIGATION_ITEMS = [
    "\U0001F4CA Overview",
    "\U0001F465 Workforce Analytics",
    "⚠️ Risk Intelligence",
    "\U0001F9E0 Strategic Insights",
]

DEPARTMENTS = ["All", "Sales", "Research & Development", "Human Resources"]


def render_sidebar():
    """Render the dataset upload control and return the uploaded file, if any."""

    st.sidebar.markdown(
        """
        <div style="margin-bottom:10px;">
            <div style="font-size:18px;font-weight:700;color:white;margin-bottom:6px;letter-spacing:-0.4px;">
                Workforce Dataset Upload
            </div>
            <div style="font-size:13px;color:#94A3B8;line-height:1.7;margin-bottom:14px;">
                Import workforce intelligence datasets for
                predictive analytics and risk simulation.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    return st.sidebar.file_uploader(
        "Upload workforce dataset (CSV)", type=["csv"], label_visibility="collapsed"
    )


def render_navigation(navigation_items=NAVIGATION_ITEMS, departments=DEPARTMENTS):
    """Render the section radio and department filter; return the selections."""

    st.sidebar.markdown(
        """
        <div style="background: linear-gradient(135deg, rgba(45,55,72,0.95), rgba(30,41,59,0.92));
        border: 1.5px solid rgba(255,255,255,0.10); border-radius: 28px; padding: 26px 22px;
        margin: 18px 0; box-shadow: 0 12px 35px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.06);">
            <h2 style="color:white; font-size:28px; font-weight:800; line-height:1.15; margin:0 0 12px 0;">
                Workforce Navigator
            </h2>
            <p style="color:#CBD5E1; font-size:13px; line-height:1.8; margin:0;">
                Predictive Workforce Analytics &amp;
                Strategic Attrition Intelligence Platform
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected_section = st.sidebar.radio(
        "Navigation",
        navigation_items,
        label_visibility="collapsed",
        key="sidebar_navigation",
    )

    selected_department = st.sidebar.selectbox(
        "Department Filter",
        departments,
        key="department_filter",
    )

    return selected_section, selected_department


def render_system_status():
    """Persistent sidebar panel showing platform operational status."""

    st.sidebar.markdown(
        """
        <div style='background:rgba(255,255,255,0.05); padding:18px; border-radius:16px;
        border:1px solid rgba(255,255,255,0.08); margin-top:18px;'>
            <h4 style='color:white;margin-bottom:12px;'>System Status</h4>
            <p style='color:#D1D5DB;line-height:1.8;font-size:14px;'>
                \U0001F7E2 Real-Time Workforce Monitoring<br>
                \U0001F7E2 Predictive Risk Scoring<br>
                \U0001F7E2 Department Intelligence Active<br>
                \U0001F7E2 Workforce Forecasting Enabled<br>
                \U0001F7E2 Executive Decision Support Online
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_capabilities_panel():
    """Persistent sidebar panel listing the platform's core capabilities."""

    st.sidebar.markdown(
        """
        <div style='background:linear-gradient(135deg,#1E3A5F 0%,#2563EB 100%); padding:20px;
        border-radius:18px; margin-top:20px; box-shadow:0px 4px 14px rgba(0,0,0,0.25);'>
            <h3 style='color:white;margin-bottom:16px;font-size:20px;'>Platform Capabilities</h3>
            <ul style='color:white;padding-left:18px;line-height:1.9;font-size:14px;'>
                <li>Predictive Attrition Analytics</li>
                <li>Workforce Risk Intelligence</li>
                <li>Strategic Forecasting</li>
                <li>Executive Decision Support</li>
                <li>Retention Optimization</li>
                <li>AI Workforce Simulations</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
