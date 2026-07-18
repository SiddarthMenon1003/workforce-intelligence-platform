"""Risk Intelligence page — predictive attrition risk scoring and simulation."""

import plotly.graph_objects as go
import streamlit as st

from backend.analytics import get_risk_metrics
from backend.insights_engine import (
    get_cost_exposure,
    get_predictive_intelligence,
    get_risk_action_priorities,
    get_risk_driver,
    get_risk_executive_position,
    get_risk_personas,
    get_risk_simulation,
    get_risk_summary,
)
from backend.risk_engine import classify_risk, get_meter_position
from frontend.components import card_eyebrow, divider, executive_card, glass_card, kpi_row, page_header, ring_metric, section_title
from frontend.theme import PLOTLY_AXIS, PLOTLY_LAYOUT, SEQUENTIAL_BLUE, STATUS_WARNING


def _styled_layout(**overrides):
    layout = dict(PLOTLY_LAYOUT)
    layout.update(overrides)
    return layout


def render_risk_intelligence(filtered_df, selected_department):
    """Render the Risk Intelligence page."""

    page_header(
        eyebrow="Risk Intelligence Layer",
        title="Workforce Risk Analysis",
        description=(
            "Department-specific predictive workforce analysis to identify "
            "attrition exposure, instability indicators, and burnout concentration."
        ),
        badge_text="⚠ Risk Monitoring Active",
        badge_color=STATUS_WARNING,
    )

    # =========================================================
    # RISK SCORE GENERATION
    # =========================================================

    metrics = get_risk_metrics(filtered_df)
    high_risk_count = metrics["high_risk_count"]
    avg_risk_score = metrics["avg_risk_score"]
    high_risk_percentage = metrics["high_risk_percentage"]
    retention_probability = metrics["retention_probability"]
    projected_attrition_impact = metrics["projected_attrition_impact"]
    optimization_gain = metrics["optimization_gain"]
    simulated_risk_reduction = metrics["simulated_risk_reduction"]
    projected_risk = metrics["projected_risk"]
    heatmap_data = metrics["heatmap_data"]

    risk_data = classify_risk(high_risk_percentage)
    risk_color = risk_data["color"]
    executive_position = get_risk_executive_position(risk_data["label"])

    risk_level_map = {
        "Low Risk": "Low Risk Exposure",
        "Moderate Risk": "Moderate Risk Exposure",
        "High Risk": "High Risk Exposure",
    }
    risk_level = risk_level_map[risk_data["label"]]

    # =========================================================
    # EXECUTIVE RISK SNAPSHOT
    # =========================================================

    divider()
    section_title("Executive Risk Snapshot")

    main_col, side_col = st.columns([2, 1])

    with main_col:
        executive_card(
            eyebrow="Executive Workforce Position",
            title=executive_position["title"],
            text=executive_position["text"],
            accent="#A78BFA",
            badges=[
                (f"Risk Score: {avg_risk_score}/100", "#A78BFA"),
                (f"Retention: {retention_probability}%", "#34D399"),
            ],
        )

    with side_col:
        kpi_row(
            [
                {
                    "icon": "\U0001F4B0",
                    "label": "Financial Exposure",
                    "value": f"${projected_attrition_impact:,.0f}",
                    "sub": "Potential workforce cost risk",
                    "accent": STATUS_WARNING,
                }
            ]
        )
        kpi_row(
            [
                {
                    "icon": "\U0001F4C8",
                    "label": "Optimization Opportunity",
                    "value": f"+{optimization_gain}%",
                    "sub": "Predicted retention improvement",
                    "accent": "#A78BFA",
                }
            ]
        )

    # =========================================================
    # ORGANIZATIONAL RISK STATUS
    # =========================================================

    divider()

    risk_summary = get_risk_summary(selected_department, high_risk_percentage, risk_level)

    executive_card(
        eyebrow="Executive Risk Signal",
        title=risk_level,
        text=risk_summary,
        accent=risk_color,
        tinted=True,
    )

    # =========================================================
    # PREDICTIVE RISK DISTRIBUTION
    # =========================================================

    divider()
    section_title("Predictive Risk Distribution")

    meter_col, snapshot_col = st.columns([1.2, 1])

    with meter_col:
        meter_position = get_meter_position(high_risk_percentage)
        overtime_share = round((filtered_df["OverTime"] == "Yes").mean() * 100)

        with glass_card():
            card_eyebrow("Workforce Risk Meter", color="#F59E0B")
            st.markdown(
                f'<div class="card-title" style="font-size:24px;">{risk_level}</div>'
                f'<div style="font-size:15px;line-height:1.8;color:#CBD5E1;margin-bottom:26px;">'
                f"Current workforce intelligence indicates {high_risk_percentage}% predictive workforce "
                f"exposure requiring monitoring and targeted intervention strategies.</div>"
                f'<div style="position:relative;">'
                f'<div style="height:12px;border-radius:999px;'
                f'background:linear-gradient(90deg,#34D399 0%,#FBBF24 50%,#F87171 100%);"></div>'
                f'<div style="position:absolute;top:50%;left:{meter_position}%;transform:translate(-50%,-50%);'
                f"width:26px;height:26px;border-radius:50%;background:white;border:4px solid {risk_color};"
                f'box-shadow:0 0 18px rgba(255,255,255,0.25);"></div>'
                f"</div>"
                f'<div style="display:flex;justify-content:space-between;margin-top:10px;color:#94A3B8;'
                f'font-size:13px;font-weight:600;"><span>LOW</span><span>MODERATE</span><span>HIGH</span></div>',
                unsafe_allow_html=True,
            )

            ring1, ring2, ring3 = st.columns(3)

            with ring1:
                ring_metric("#F59E0B", f"{overtime_share}%", "Burnout")
            with ring2:
                ring_metric("#22C55E", f"{100 - high_risk_percentage:.0f}%", "Retention")
            with ring3:
                ring_metric("#EF4444", f"{high_risk_percentage:.0f}%", "Attrition")

    with snapshot_col:
        risk_driver, risk_driver_signal = get_risk_driver(selected_department)

        kpi_row(
            [{
                "label": "High-Risk Workforce (%)",
                "value": f"{high_risk_percentage}%",
                "sub": "Attrition Vulnerability",
                "accent": "#F87171",
            }]
        )
        kpi_row(
            [{
                "label": "Primary Risk Driver",
                "value": risk_driver,
                "sub": risk_driver_signal,
                "accent": "#FBBF24",
            }]
        )
        kpi_row(
            [{
                "label": "Department Risk Status",
                "value": risk_level,
                "sub": "Predictive Workforce Intelligence",
                "accent": risk_color,
            }]
        )

    # =========================================================
    # PREDICTIVE RISK DRIVERS
    # =========================================================

    divider()
    section_title("Predictive Risk Drivers")

    feature_names = ["Overtime", "Job Satisfaction", "Work-Life Balance", "Employee Tenure", "Monthly Income"]
    feature_scores = [30, 25, 20, 15, 10]  # mirrors the risk-scoring weights in backend.risk_engine

    fig = go.Figure(
        go.Bar(
            x=feature_scores,
            y=feature_names,
            orientation="h",
            marker_color=SEQUENTIAL_BLUE[2:7][::-1],
            text=feature_scores,
            textposition="outside",
            hovertemplate="%{y}: %{x} pts<extra></extra>",
        )
    )
    fig.update_layout(**_styled_layout(height=380, title="Feature Importance Analysis", showlegend=False))
    fig.update_xaxes(title="Risk Contribution Score", **PLOTLY_AXIS)
    fig.update_yaxes(categoryorder="total ascending", **PLOTLY_AXIS)
    st.plotly_chart(fig, use_container_width=True)

    # =========================================================
    # HIGH-RISK PERSONAS
    # =========================================================

    divider()
    section_title("High-Risk Workforce Personas")

    persona_one, persona_two = get_risk_personas(selected_department)
    persona_col1, persona_col2 = st.columns(2)

    with persona_col1:
        st.info(persona_one)
    with persona_col2:
        st.info(persona_two)

    # =========================================================
    # RISK HEATMAP
    # =========================================================

    divider()
    section_title("Workforce Risk Pattern Analysis")

    fig = go.Figure(
        go.Heatmap(
            z=heatmap_data.values,
            x=[str(c) for c in heatmap_data.columns],
            y=[str(i) for i in heatmap_data.index],
            colorscale="Blues",
            hovertemplate="Overtime: %{y}<br>Satisfaction: %{x}<br>Avg Risk: %{z:.1f}<extra></extra>",
            colorbar=dict(title="Risk Score", tickfont=dict(color="#94A3B8")),
        )
    )
    fig.update_layout(**_styled_layout(height=380, title="Risk Heatmap: Overtime vs Satisfaction"))
    fig.update_xaxes(title="Job Satisfaction", **PLOTLY_AXIS)
    fig.update_yaxes(title="Overtime Status", **PLOTLY_AXIS)
    st.plotly_chart(fig, use_container_width=True)

    # =========================================================
    # SIMULATION, INSIGHTS, COST, PRIORITIES
    # =========================================================

    divider()
    section_title("Predictive Scenario Simulation")
    st.success(get_risk_simulation(selected_department, simulated_risk_reduction, projected_risk))

    section_title("Predictive Workforce Insights")
    st.info(get_predictive_intelligence(selected_department, high_risk_count, high_risk_percentage))

    section_title("Estimated Organizational Cost Exposure")
    st.error(get_cost_exposure(selected_department, projected_attrition_impact))

    section_title("Strategic Action Priorities")
    st.success(get_risk_action_priorities(selected_department))

    divider()
