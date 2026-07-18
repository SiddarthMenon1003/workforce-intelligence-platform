"""Workforce Analytics page — operational overtime, burnout, and lifecycle cuts."""

import plotly.graph_objects as go
import streamlit as st

from backend.insights_engine import (
    get_department_recommendation,
    get_primary_risk_driver,
    get_workforce_department_content,
    get_workforce_vulnerability,
)
from backend.risk_engine import classify_risk, get_risk_severity
from backend.analytics import (
    get_overtime_distribution_metrics,
    get_satisfaction_metrics,
    get_workforce_metrics,
)
from frontend.components import badge, card_eyebrow, divider, glass_card, kpi_row, page_header, ring_metric, section_title
from frontend.theme import PLOTLY_AXIS, PLOTLY_LAYOUT, SERIES, STATUS_CRITICAL, STATUS_GOOD


def _styled_layout(**overrides):
    layout = dict(PLOTLY_LAYOUT)
    layout.update(overrides)
    return layout


def render_workforce_analytics(filtered_df, selected_department):
    """Render the Workforce Analytics page."""

    metrics = get_workforce_metrics(filtered_df)
    distribution_metrics = get_overtime_distribution_metrics(filtered_df)

    avg_income = metrics["avg_income"]
    dept_attrition = metrics["dept_attrition"]
    stability_score = metrics["stability_score"]
    overtime_percentage = metrics["overtime_percentage"]
    overtime_attrition_rate = metrics["overtime_attrition_rate"]
    no_overtime_attrition_rate = metrics["no_overtime_attrition_rate"]
    workforce_stability_score = metrics["workforce_stability_score"]

    department_content = get_workforce_department_content(selected_department)
    stability_risk = classify_risk(100 - stability_score)

    page_header(
        eyebrow="Operational Intelligence Layer",
        title="Workforce Performance Snapshot",
        description=(
            "Real-time operational metrics on overtime exposure, income, "
            "attrition, and department-level workforce distribution."
        ),
        badge_text="\U0001F4CA Workforce Analytics Active",
        badge_color="#60A5FA",
    )

    kpi_row(
        [
            {"icon": "⏱️", "label": "Overtime Workforce", "value": f"{distribution_metrics['overtime_pct']}%", "accent": STATUS_CRITICAL},
            {"icon": "\U0001F4B0", "label": "Average Monthly Income", "value": f"₹{avg_income:,.0f}", "accent": "#60A5FA"},
            {"icon": "\U0001F4C9", "label": "Attrition Rate", "value": f"{dept_attrition}%", "accent": "#A78BFA"},
        ]
    )

    divider()

    # =========================================================
    # OPERATIONAL SIGNAL + STABILITY INDEX + DEPARTMENT MIX
    # =========================================================

    signal_col, ring_col, dist_col = st.columns([1.1, 1, 1])

    with signal_col:
        with glass_card("height:100%;"):
            card_eyebrow("Operational Workforce Signal", color="#60A5FA")
            st.markdown(
                f'<div class="card-title" style="font-size:17px;">{department_content["signal_title"]}</div>'
                f'<div style="font-size:15px;line-height:1.7;color:#CBD5E1;">{department_content["signal_text"]}</div>'
                '<div style="height:18px;"></div>',
                unsafe_allow_html=True,
            )
            badge(stability_risk["status"], stability_risk["color"])

    with ring_col:
        with glass_card("height:100%; text-align:center;"):
            card_eyebrow("Workforce Stability Index", color="#94A3B8")
            ring_metric(
                "#60A5FA",
                f"{stability_score}",
                stability_risk["label"],
                size=150,
                inner_caption="Stability",
            )

    with dist_col:
        with glass_card("height:100%;"):
            card_eyebrow("Department Distribution", color="#94A3B8")

            dept_counts = filtered_df["Department"].value_counts()
            fig_dist = go.Figure(
                go.Bar(
                    x=dept_counts.index,
                    y=dept_counts.values,
                    marker_color=SERIES[: len(dept_counts)],
                    text=dept_counts.values,
                    textposition="outside",
                    hovertemplate="%{x}: %{y} employees<extra></extra>",
                )
            )
            fig_dist.update_layout(**_styled_layout(height=250, showlegend=False, margin=dict(l=10, r=10, t=45, b=10)))
            fig_dist.update_xaxes(**PLOTLY_AXIS, showgrid=False)
            fig_dist.update_yaxes(
                **PLOTLY_AXIS, showgrid=True, visible=False, range=[0, dept_counts.values.max() * 1.25]
            )

            st.plotly_chart(fig_dist, use_container_width=True, config={"displayModeBar": False})

    # =========================================================
    # OVERTIME & BURNOUT ANALYSIS
    # =========================================================

    divider()
    section_title("Overtime & Burnout Analysis")

    kpi_row(
        [
            {"icon": "⏱️", "label": "Employees Working Overtime", "value": f"{overtime_percentage}%", "accent": STATUS_CRITICAL},
            {"icon": "\U0001F525", "label": "Overtime Attrition Rate", "value": f"{overtime_attrition_rate}%", "accent": "#F59E0B"},
            {"icon": "\U0001F6E1️", "label": "Non-Overtime Attrition", "value": f"{no_overtime_attrition_rate}%", "accent": STATUS_GOOD},
            {"icon": "\U0001F4CA", "label": "Workforce Stability Score", "value": f"{workforce_stability_score}/100", "accent": "#60A5FA"},
        ]
    )

    section_title("Workforce Risk Severity")
    severity_type, severity_message = get_risk_severity(overtime_attrition_rate)

    if severity_type == "success":
        st.success(severity_message)
    else:
        st.error(severity_message)

    section_title("Strategic Workforce Intelligence")
    insight1, insight2 = st.columns(2)

    with insight1:
        st.info(get_workforce_vulnerability(selected_department))

    with insight2:
        st.info(get_primary_risk_driver())

    # =========================================================
    # VISUAL ANALYTICS
    # =========================================================

    chart1, chart2 = st.columns(2)

    with chart1:
        risk_score = overtime_attrition_rate
        risk_data = classify_risk(risk_score)

        fig_gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=risk_score,
                number={"suffix": "%", "font": {"size": 42, "color": "white"}},
                title={"text": "Overtime Attrition Risk", "font": {"size": 16}},
                gauge={
                    "shape": "angular",
                    "axis": {"range": [0, 100], "tickcolor": "rgba(0,0,0,0)"},
                    "bar": {"color": risk_data["color"], "thickness": 0.3},
                    "bgcolor": "rgba(0,0,0,0)",
                    "borderwidth": 0,
                    "steps": [
                        {"range": [0, 30], "color": "rgba(34,197,94,0.15)"},
                        {"range": [30, 50], "color": "rgba(245,158,11,0.12)"},
                        {"range": [50, 100], "color": "rgba(239,68,68,0.12)"},
                    ],
                },
            )
        )
        fig_gauge.update_layout(**_styled_layout(height=260))
        st.plotly_chart(fig_gauge, use_container_width=True, config={"displayModeBar": False})

        kpi_row(
            [
                {"label": "Overtime Employees", "value": f"{overtime_percentage}%", "accent": STATUS_CRITICAL},
                {"label": "Stability Score", "value": f"{workforce_stability_score}/100", "accent": "#60A5FA"},
                {"label": "Risk Category", "value": risk_data["label"], "accent": risk_data["color"]},
            ]
        )

    with chart2:
        overtime_pct = distribution_metrics["overtime_pct"]
        non_overtime_pct = distribution_metrics["non_overtime_pct"]

        fig_composition = go.Figure()
        fig_composition.add_trace(
            go.Bar(
                y=["Workforce"], x=[overtime_pct], name="Overtime", orientation="h",
                marker_color=STATUS_CRITICAL, text=[f"{overtime_pct}%"], textposition="inside",
                hovertemplate="Overtime: %{x}%<extra></extra>",
            )
        )
        fig_composition.add_trace(
            go.Bar(
                y=["Workforce"], x=[non_overtime_pct], name="Non-Overtime", orientation="h",
                marker_color="#60A5FA", text=[f"{non_overtime_pct}%"], textposition="inside",
                hovertemplate="Non-Overtime: %{x}%<extra></extra>",
            )
        )
        fig_composition.update_layout(
            **_styled_layout(height=240, barmode="stack", title="Workforce Composition")
        )
        fig_composition.update_xaxes(visible=False)
        fig_composition.update_yaxes(visible=False)

        st.plotly_chart(fig_composition, use_container_width=True, config={"displayModeBar": False})

        kpi_row(
            [
                {"label": "Overtime Employees", "value": f"{overtime_pct}%", "accent": STATUS_CRITICAL},
                {"label": "Non-Overtime Employees", "value": f"{non_overtime_pct}%", "accent": "#60A5FA"},
            ]
        )

    # =========================================================
    # STRATEGIC RECOMMENDATION & FINDINGS
    # =========================================================

    divider()
    section_title("Strategic Recommendation")
    st.success(get_department_recommendation(selected_department))

    section_title("Key Workforce Findings")

    if selected_department == "All":
        st.markdown(
            f"""
- Employees working overtime demonstrate substantially higher attrition vulnerability across the organization.
- Overtime employees currently show an attrition rate of **{overtime_attrition_rate}%**.
- Workforce instability appears strongly linked to overtime exposure and operational workload imbalance.
- Workforce stability score currently stands at **{workforce_stability_score}/100**.
"""
        )
    else:
        st.markdown(
            f"""
- The **{selected_department}** department currently demonstrates an attrition rate of **{dept_attrition}%**.
- Workforce pressure and operational workload appear strongly associated with retention challenges.
- Overtime exposure remains a major workforce risk factor within the selected department.
- Workforce stability score currently stands at **{workforce_stability_score}/100**.
"""
        )

    # =========================================================
    # SATISFACTION & ENGAGEMENT ANALYSIS
    # =========================================================

    satisfaction_data = get_satisfaction_metrics(filtered_df)
    job_sat = satisfaction_data["job_satisfaction"]
    worklife = satisfaction_data["worklife_balance"]
    tenure = satisfaction_data["tenure_attrition"]
    attrition_yes = satisfaction_data["attrition_yes_income"]
    attrition_no = satisfaction_data["attrition_no_income"]

    divider()
    section_title("Satisfaction & Engagement Analysis")

    sat1, sat2 = st.columns(2)

    with sat1:
        fig = go.Figure(
            go.Scatter(
                x=job_sat["JobSatisfaction"], y=job_sat["Attrition"],
                mode="lines+markers", line=dict(color=SERIES[1], width=2),
                marker=dict(size=9), fill="tozeroy",
                fillcolor="rgba(167,139,250,0.12)",
                hovertemplate="Satisfaction %{x}: %{y:.1%} attrition<extra></extra>",
            )
        )
        fig.update_layout(**_styled_layout(height=380, title="Attrition by Job Satisfaction", showlegend=False))
        fig.update_xaxes(title="Job Satisfaction Level", **PLOTLY_AXIS)
        fig.update_yaxes(title="Attrition Rate", tickformat=".0%", **PLOTLY_AXIS)
        st.plotly_chart(fig, use_container_width=True)

    with sat2:
        fig = go.Figure(
            go.Bar(
                x=worklife["WorkLifeBalance"], y=worklife["Attrition"],
                marker_color=SERIES[2],
                hovertemplate="Balance %{x}: %{y:.1%} attrition<extra></extra>",
            )
        )
        fig.update_layout(**_styled_layout(height=380, title="Work-Life Balance Impact", showlegend=False))
        fig.update_xaxes(title="Work-Life Balance Rating", **PLOTLY_AXIS)
        fig.update_yaxes(title="Attrition Rate", tickformat=".0%", **PLOTLY_AXIS)
        st.plotly_chart(fig, use_container_width=True)

    # =========================================================
    # WORKFORCE LIFECYCLE ANALYSIS
    # =========================================================

    divider()
    section_title("Workforce Lifecycle Analysis")

    lifecycle1, lifecycle2 = st.columns(2)

    with lifecycle1:
        fig = go.Figure(
            go.Scatter(
                x=tenure["YearsAtCompany"], y=tenure["Attrition"],
                mode="lines", line=dict(color=SERIES[3], width=2),
                fill="tozeroy", fillcolor="rgba(251,191,36,0.12)",
                hovertemplate="Year %{x}: %{y:.1%} attrition<extra></extra>",
            )
        )
        fig.update_layout(**_styled_layout(height=380, title="Attrition by Employee Tenure", showlegend=False))
        fig.update_xaxes(title="Years at Company", **PLOTLY_AXIS)
        fig.update_yaxes(title="Attrition Rate", tickformat=".0%", **PLOTLY_AXIS)
        st.plotly_chart(fig, use_container_width=True)

    with lifecycle2:
        fig = go.Figure()
        fig.add_trace(go.Histogram(x=attrition_yes, name="Attrition", marker_color=STATUS_CRITICAL, opacity=0.85))
        fig.add_trace(go.Histogram(x=attrition_no, name="Retention", marker_color="#60A5FA", opacity=0.85))
        fig.update_layout(
            **_styled_layout(height=380, title="Income Distribution & Attrition", barmode="stack")
        )
        fig.update_xaxes(title="Monthly Income", **PLOTLY_AXIS)
        fig.update_yaxes(title="Employees", **PLOTLY_AXIS)
        st.plotly_chart(fig, use_container_width=True)

    divider()
