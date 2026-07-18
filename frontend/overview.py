"""Overview page — executive snapshot of organizational workforce health."""

from datetime import datetime

import streamlit as st

from backend.analytics import (
    get_department_intelligence,
    get_department_overview_metrics,
    get_overview_metrics,
)
from backend.insights_engine import get_overview_executive_brief, get_overview_insights
from backend.risk_engine import (
    classify_overtime_risk,
    classify_risk,
    classify_workforce_health,
    get_primary_driver,
)
from frontend.components import card_title, divider, glass_card, kpi_row, page_header, section_title, stat_rows
from frontend.theme import STATUS_CRITICAL, STATUS_GOOD, STATUS_WARNING


def render_overview(filtered_df, df, selected_department, model_accuracy):
    """Render the Overview page."""

    page_header(
        eyebrow="AI Workforce Intelligence Platform",
        title="Workforce Overview",
        description=(
            "Predictive attrition analytics, workforce risk detection, and "
            "executive-level organizational insights, updated in real time."
        ),
        badge_text="● Live Analysis Active",
        badge_color=STATUS_GOOD,
    )

    st.caption(f"Last Intelligence Refresh: {datetime.now().strftime('%d %b %Y • %H:%M')}")

    # =========================================================
    # KPI CALCULATIONS
    # =========================================================

    overview_metrics = get_overview_metrics(filtered_df)
    total_employees = overview_metrics["total_employees"]
    attrition_rate = overview_metrics["attrition_rate"]
    overtime_percentage = overview_metrics["overtime_percentage"]
    retention_percent = overview_metrics["retention_percent"]

    risk_data = classify_risk(attrition_rate)
    overview_title, attention_area = get_overview_executive_brief(risk_data["label"])

    # =========================================================
    # EXECUTIVE INTELLIGENCE BRIEF
    # =========================================================

    section_title("Executive Intelligence Brief")

    kpi_row(
        [
            {
                "icon": "\U0001F3AF",
                "label": "Primary Workforce Risk",
                "value": overview_title,
                "accent": "#60A5FA",
            },
            {
                "icon": "\U0001F50D",
                "label": "Highest Attention Area",
                "value": attention_area,
                "accent": "#A78BFA",
            },
            {
                "icon": "\U0001F916",
                "label": "Model Confidence",
                "value": f"{model_accuracy * 100:.1f}%",
                "accent": STATUS_GOOD,
            },
        ]
    )

    divider()

    # =========================================================
    # HEADLINE KPIs
    # =========================================================

    kpi_row(
        [
            {"icon": "\U0001F465", "label": "Total Workforce", "value": f"{total_employees:,}", "accent": "#60A5FA"},
            {"icon": "\U0001F4C9", "label": "Attrition Rate", "value": f"{attrition_rate}%", "accent": STATUS_CRITICAL},
            {"icon": "⚠️", "label": "High-Risk Workforce (%)", "value": f"{overtime_percentage}%", "accent": STATUS_WARNING},
            {"icon": "\U0001F9E0", "label": "Model Accuracy", "value": f"{model_accuracy * 100:.1f}%", "accent": STATUS_GOOD},
        ]
    )

    # =========================================================
    # ORGANIZATIONAL RISK STATUS
    # =========================================================

    divider()
    section_title("Organizational Risk Status")
    st.info(f"Current Organizational Risk Level: {risk_data['status']}")

    # =========================================================
    # KEY BUSINESS INSIGHTS
    # =========================================================

    section_title("Key Workforce Insights")

    department_data = get_department_intelligence(df)

    st.markdown(
        get_overview_insights(
            selected_department,
            department_data["highest_attrition_dept"],
            department_data["stable_dept"],
            attrition_rate,
            overtime_percentage,
        )
    )

    # =========================================================
    # VISUAL ANALYTICS
    # =========================================================

    divider()
    section_title("Workforce Analytics Overview")

    chart1, chart2 = st.columns(2)

    with chart1:
        health_data = classify_workforce_health(retention_percent)
        engagement_score = round(((100 - attrition_rate) + (100 - overtime_percentage)) / 2, 1)
        driver_data = get_primary_driver(attrition_rate, overtime_percentage, engagement_score)
        driver_score = round(overtime_percentage if overtime_percentage > 30 else engagement_score)

        with glass_card():
            card_title("Workforce Health Intelligence")

            stat_rows(
                [
                    {
                        "icon": "◉",
                        "color": "#60A5FA",
                        "title": "Workforce Health",
                        "subtitle": health_data["label"],
                        "value": f"{retention_percent}%",
                        "caption": "score",
                        "show_bar": True,
                        "bar_pct": retention_percent,
                    },
                    {
                        "icon": "◈",
                        "color": STATUS_CRITICAL,
                        "title": "Attrition Risk",
                        "subtitle": "Organizational Risk",
                        "value": f"{attrition_rate}%",
                        "caption": "risk",
                        "show_bar": True,
                        "bar_pct": attrition_rate,
                    },
                    {
                        "icon": "⚡",
                        "color": "#FB923C",
                        "title": "Primary Workforce Driver",
                        "subtitle": driver_data["driver"],
                        "value": f"{driver_score}%",
                        "caption": "influence",
                        "show_bar": True,
                        "bar_pct": driver_score,
                    },
                    {
                        "icon": "↗",
                        "color": health_data["color"],
                        "title": "Stability Outlook",
                        "subtitle": "Long-Term Workforce",
                        "value": health_data["label"],
                        "caption": "outlook",
                        "show_bar": False,
                    },
                ]
            )

    with chart2:
        department_metrics = get_department_overview_metrics(filtered_df, selected_department)
        dept_overtime = department_metrics["dept_overtime"]
        dept_retention = department_metrics["dept_retention"]
        dept_engagement = department_metrics["dept_engagement"]
        overtime_data = classify_overtime_risk(dept_overtime)

        with glass_card():
            card_title("Workforce Instability Distribution")

            stat_rows(
                [
                    {
                        "icon": "◎",
                        "color": STATUS_CRITICAL,
                        "title": "Overtime Burnout",
                        "subtitle": selected_department,
                        "value": f"{dept_overtime}%",
                        "caption": "risk",
                        "show_bar": True,
                        "bar_pct": dept_overtime,
                    },
                    {
                        "icon": "◈",
                        "color": "#60A5FA",
                        "title": "Retention Strength",
                        "subtitle": "Stability score",
                        "value": f"{dept_retention}%",
                        "caption": "retained",
                        "show_bar": True,
                        "bar_pct": dept_retention,
                    },
                    {
                        "icon": "◉",
                        "color": "#A7F3D0",
                        "title": "Engagement Index",
                        "subtitle": "Workforce sentiment",
                        "value": f"{dept_engagement}%",
                        "caption": "engagement",
                        "show_bar": True,
                        "bar_pct": dept_engagement,
                    },
                    {
                        "icon": "◌",
                        "color": overtime_data["color"],
                        "title": "Overtime Exposure",
                        "subtitle": "Department pressure level",
                        "value": overtime_data["label"],
                        "caption": "",
                        "show_bar": False,
                    },
                ]
            )
