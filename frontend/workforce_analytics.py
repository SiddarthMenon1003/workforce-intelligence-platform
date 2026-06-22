import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

from backend.risk_engine import (
    classify_risk,
    get_risk_severity
)

from backend.insights_engine import (
    get_department_recommendation,
    get_workforce_department_content,
    get_workforce_vulnerability,
    get_primary_risk_driver
)

from backend.analytics import (
    get_workforce_metrics,
    get_workforce_department_stats,
    get_satisfaction_metrics,
    get_overtime_distribution_metrics
)

def render_workforce_analytics(
    filtered_df,
    selected_department
):
    """Render workforce analytics dashboard."""

    # =========================================================
    # WORKFORCE ANALYTICS CALCULATIONS
    # =========================================================

    metrics = get_workforce_metrics(
        filtered_df
    )

    distribution_metrics = (
        get_overtime_distribution_metrics(
            filtered_df
        )
    )

    overtime_pct = (
        distribution_metrics["overtime_pct"]
    )

    non_overtime_pct = (
        distribution_metrics["non_overtime_pct"]
    )

    avg_income = (
        metrics["avg_income"]
    )

    dept_attrition = (
        metrics["dept_attrition"]
    )

    stability_score = (
        metrics["stability_score"]
    )

    overtime_percentage = (
        metrics["overtime_percentage"]
    )

    overtime_attrition_rate = (
        metrics["overtime_attrition_rate"]
    )

    no_overtime_attrition_rate = (
        metrics["no_overtime_attrition_rate"]
    )

    workforce_stability_score = (
        metrics["workforce_stability_score"]
    )

    # =========================
    # DEPARTMENT SIGNAL
    # =========================

    department_data = (
        get_workforce_department_content(
            selected_department
        )
    )

    stability_risk = (
        classify_risk(
            100 - stability_score
        )
    )

    stability_status = (
        stability_risk["status"]
    )

    signal_title = (
        department_data["signal_title"]
    )

    signal_text = (
        department_data["signal_text"]
    )

    st.markdown(f"""
        <div style="background:linear-gradient(135deg, rgba(15,23,42,0.95), rgba(30,41,59,0.88)); border:1px solid rgba(96,165,250,0.12); border-radius:30px; padding:26px 30px; margin-top:16px; margin-bottom:30px; box-shadow:0 12px 30px rgba(0,0,0,0.20);">

        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;">

        <div>

        <div style="font-size:13px; font-weight:700; letter-spacing:1.3px; text-transform:uppercase; color:#60A5FA; margin-bottom:8px;">
        OPERATIONAL INTELLIGENCE LAYER
        </div>

        <div style="font-size:28px; font-weight:700; color:white;">
        Workforce Performance Snapshot
        </div>

        </div>

        <div style="padding:10px 18px; border-radius:999px; background:rgba(59,130,246,0.10); border:1px solid rgba(59,130,246,0.18); color:#93C5FD; font-size:14px; font-weight:600;">
        📊 Workforce Analytics Active
        </div>

        </div>

        <div style="display:grid; grid-template-columns:repeat(3,1fr); gap:18px;">

        <div style="background:rgba(255,255,255,0.03); padding:18px; border-radius:22px;">
        <div style="font-size:13px; color:#64748B;">
        Overtime Workforce
        </div>

        <div style="font-size:30px; font-weight:750; color:white; margin-top:10px;">
        {overtime_pct}%
        </div>
        </div>

        <div style="background:rgba(255,255,255,0.03); padding:18px; border-radius:22px;">
        <div style="font-size:13px; color:#64748B;">
        Average Monthly Income
        </div>

        <div style="font-size:30px; font-weight:750; color:white; margin-top:10px;">
        ₹{avg_income:,.0f}
        </div>
        </div>

        <div style="background:rgba(255,255,255,0.03); padding:18px; border-radius:22px;">
        <div style="font-size:13px; color:#64748B;">
        Attrition Risk
        </div>

        <div style="font-size:30px; font-weight:750; color:white; margin-top:10px;">
        {dept_attrition}%
        </div>
        </div>

        </div>

        <div style="
        margin-top:26px;
        padding-top:22px;
        border-top:1px solid rgba(255,255,255,0.06);
        display:grid;
        grid-template-columns:1.2fr 1fr 1fr;
        gap:28px;
        align-items:stretch;
        ">

        <!-- LEFT SIGNAL -->
        <div style="
        display:flex;
        flex-direction:column;
        justify-content:center;
        ">

        <div style="
        font-size:12px;
        text-transform:uppercase;
        letter-spacing:1.5px;
        color:#60A5FA;
        font-weight:700;
        margin-bottom:16px;
        ">
        Operational Workforce Signal
        </div>

        <div style="
        font-size:17px;
        line-height:1.8;
        color:#CBD5E1;
        margin-top:10px;
        max-width:520px;
        ">

        <strong style="color:white;">
        {signal_title}
        </strong>

        <div style="height:12px;"></div>

        {signal_text}

        </div>

        <div style="
        margin-top:24px;
        display:inline-flex;
        align-items:center;
        gap:10px;
        padding:12px 18px;
        border-radius:999px;
        background:rgba(16,185,129,0.08);
        border:1px solid rgba(16,185,129,0.18);
        width:fit-content;
        ">

        <div style="
        width:10px;
        height:10px;
        border-radius:50%;
        background:#6EE7B7;
        box-shadow:0 0 12px #6EE7B7;
        "></div>

        <div style="
        font-size:14px;
        font-weight:600;
        color:#6EE7B7;
        ">
        {stability_status}
        </div>

        </div>

        </div>


        <!-- CENTER DONUT -->
        <div style="
        padding:24px;
        border-radius:26px;
        background:rgba(59,130,246,0.06);
        border:1px solid rgba(59,130,246,0.12);
        display:flex;
        flex-direction:column;
        align-items:center;
        justify-content:center;
        ">

        <div style="
        font-size:13px;
        color:#64748B;
        margin-bottom:40px;
        align-self:flex-start;
        ">
        Workforce Stability Index
        </div>

        <div style="
        width:170px;
        height:170px;
        border-radius:50%;
        background:
        conic-gradient(
        #60A5FA 0% {stability_score}%,
        rgba(255,255,255,0.08) {stability_score}% 100%
        );
        display:flex;
        align-items:center;
        justify-content:center;
        ">

        <div style="
        width:125px;
        height:125px;
        border-radius:50%;
        background:#0F172A;
        display:flex;
        flex-direction:column;
        align-items:center;
        justify-content:center;
        ">

        <div style="
        font-size:38px;
        font-weight:800;
        color:white;
        ">
        {stability_score}
        </div>

        <div style="
        font-size:12px;
        letter-spacing:1px;
        text-transform:uppercase;
        color:#93C5FD;
        margin-top:4px;
        ">
        Stability
        </div>

        </div>

        </div>

        <div style="
        margin-top:20px;
        font-size:15px;
        font-weight:700;
        color:#93C5FD;
        text-align:center;
        ">
        {stability_risk["label"]}
        </div>

        <div style="
        margin-top:8px;
        font-size:13px;
        color:#94A3B8;
        line-height:1.6;
        text-align:center;
        ">
        Balanced workforce structure with moderate overtime exposure.
        </div>

        </div>


        <!-- RIGHT VISUAL -->
        <div style="
        padding:24px;
        border-radius:26px;
        background:rgba(168,85,247,0.06);
        border:1px solid rgba(168,85,247,0.12);
        display:flex;
        flex-direction:column;
        justify-content:center;
        ">

        <div style="
        font-size:13px;
        color:#64748B;
        margin-bottom:20px;
        ">
        Department Distribution
        </div>

        <div style="
        display:flex;
        align-items:flex-end;
        justify-content:center;
        gap:18px;
        height:150px;
        ">

        <div style="
        width:52px;
        height:70px;
        border-radius:16px 16px 6px 6px;
        background:#60A5FA;
        "></div>

        <div style="
        width:52px;
        height:115px;
        border-radius:16px 16px 6px 6px;
        background:#34D399;
        "></div>

        <div style="
        width:52px;
        height:90px;
        border-radius:16px 16px 6px 6px;
        background:#A78BFA;
        "></div>

        </div>

        <div style="
        display:flex;
        justify-content:space-around;
        font-size:13px;
        color:#94A3B8;
        margin-top:12px;
        ">
        <span>HR</span>
        <span>R&D</span>
        <span>Sales</span>
        </div>

        <div style="
        margin-top:18px;
        padding-top:14px;
        border-top:1px solid rgba(255,255,255,0.06);
        font-size:14px;
        line-height:1.7;
        color:#CBD5E1;
        text-align:center;
        ">

        Balanced workforce allocation across core departments.

        </div>

        </div>

        </div>

        </div>

        </div>

        </div>

        </div>
        """, unsafe_allow_html=True)

    # =========================================================
    # OVERTIME & BURNOUT ANALYSIS
    # =========================================================

    st.markdown("---")
    st.subheader("Overtime & Burnout Analysis")

    # KPI Cards
    card1, card2, card3, card4 = st.columns(4)

    card1.metric(
        "Employees Working Overtime",
        f"{overtime_percentage}%"
    )

    card2.metric(
        "Overtime Attrition Rate",
        f"{overtime_attrition_rate}%"
    )

    card3.metric(
        "Non-Overtime Attrition",
        f"{no_overtime_attrition_rate}%"
    )

    card4.metric(
        "Workforce Stability Score",
        f"{workforce_stability_score}/100"
    )

    # Risk Meter
    st.subheader("Workforce Risk Severity")

    severity_type, severity_message = (
        get_risk_severity(
            overtime_attrition_rate
        )
    )

    if severity_type == "success":

        st.success(
            severity_message
        )

    else:

        st.error(
            severity_message
        )

    # Smart Insights
    st.subheader("Strategic Workforce Intelligence")

    insight1, insight2 = st.columns(2)

    with insight1:

        st.info(
            get_workforce_vulnerability(
                selected_department
            )
        )

    with insight2:

        st.info(
            get_primary_risk_driver(
            )
        )
        
    # Visual Analytics
    chart1, chart2 = st.columns(2)

    with chart1:

        risk_score = overtime_attrition_rate

        risk_data = classify_risk(
            risk_score
        )

        risk_label = (
            risk_data["label"]
        )

        risk_color = (
            risk_data["color"]
        )

        st.markdown(f"""
        <div style="
        background:linear-gradient(
            135deg,
            rgba(17,24,39,0.96),
            rgba(30,41,59,0.92)
        );
        border:1px solid rgba(255,255,255,0.06);
        border-radius:28px;
        padding:36px;
        height:520px;
        ">

        <div style="
        font-size:26px;
        font-weight:800;
        color:white;
        margin-bottom:10px;
        ">
        Overtime Attrition Risk
        </div>

        <div style="
        color:#94A3B8;
        font-size:15px;
        margin-bottom:36px;
        ">
        Likelihood of employee attrition among overtime workforce.
        </div>

        <div style="
        display:grid;
        grid-template-columns:1.4fr 1fr;
        gap:24px;
        align-items:center;
        ">

        <!-- LEFT SIDE -->

        <div style="
        display:flex;
        align-items:center;
        gap:28px;
        ">

        <!-- THERMOMETER -->

        <div style="
        position:relative;
        width:62px;
        height:220px;
        border-radius:999px;
        background:rgba(255,255,255,0.06);
        overflow:hidden;
        flex-shrink:0;
        ">

        <div style="
        position:absolute;
        bottom:0;
        width:100%;
        height:{risk_score}%;
        background:linear-gradient(
            180deg,
            {risk_color},
            rgba(255,255,255,0.95)
        );
        border-radius:999px;
        box-shadow:0 0 25px {risk_color};
        ">
        </div>

        </div>

        <!-- MAIN METRIC -->

        <div>

        <div style="
        font-size:74px;
        font-weight:900;
        color:{risk_color};
        line-height:1;
        margin-bottom:10px;
        ">
        {risk_score}%
        </div>

        <div style="
        font-size:18px;
        font-weight:700;
        color:{risk_color};
        line-height:1.2;
        ">
        {risk_label}
        </div>

        <div style="
        display:inline-flex;
        margin-top:18px;
        align-items:center;
        gap:10px;
        padding:16px 22px;
        border-radius:999px;
        background:rgba(255,255,255,0.025);
        border:1px solid rgba(255,255,255,0.045);
        backdrop-filter:blur(18px);
        ">

        <div style="
        width:10px;
        height:10px;
        border-radius:50%;
        background:{risk_color};
        box-shadow:0 0 8px rgba(198,161,91,0.28);
        ">
        </div>

        <div style="
        color:#CBD5E1;
        font-size:14px;
        font-weight:600;
        ">
        Overtime-linked workforce instability
        </div>

        </div>

        </div>

        </div>

        <!-- RIGHT CARDS -->

        <div style="
        display:flex;
        flex-direction:column;
        gap:10px;
        justify-content:center;
        ">

        <div style="
        padding:14px;
        border-radius:18px;
        background:rgba(239,68,68,0.08);
        border:1px solid rgba(239,68,68,0.14);
        ">

        <div style="
        font-size:13px;
        color:#94A3B8;
        margin-bottom:6px;
        ">
        Overtime Employees
        </div>

        <div style="
        font-size:26px;
        font-weight:800;
        color:#F87171;
        ">
        {overtime_percentage}%
        </div>

        </div>

        <div style="
        padding:14px;
        border-radius:18px;
        background:rgba(59,130,246,0.08);
        border:1px solid rgba(59,130,246,0.14);
        ">

        <div style="
        font-size:13px;
        color:#94A3B8;
        margin-bottom:6px;
        ">
        Stability Score
        </div>

        <div style="
        font-size:26px;
        font-weight:800;
        color:#60A5FA;
        ">
        {workforce_stability_score}/100
        </div>

        </div>

        <div style="
        padding:14px;
        border-radius:18px;
        background:rgba(251,191,36,0.08);
        border:1px solid rgba(251,191,36,0.14);
        ">

        <div style="
        font-size:13px;
        color:#94A3B8;
        margin-bottom:6px;
        ">
        Risk Category
        </div>

        <div style="
        font-size:20px;
        font-weight:700;
        color:{risk_color};
        ">
        {risk_label}
        </div>

        </div>

        </div>

        </div>

        </div>
        """, unsafe_allow_html=True)

    with chart2:

        distribution_metrics = (
            get_overtime_distribution_metrics(
                filtered_df
            )
        )

        overtime_pct = (
            distribution_metrics[
                "overtime_pct"
            ]
        )

        non_overtime_pct = (
            distribution_metrics[
                "non_overtime_pct"
            ]
        )

        st.markdown(f"""
        <div style="
        background:linear-gradient(
            135deg,
            rgba(17,24,39,0.96),
            rgba(30,41,59,0.92)
        );
        border:1px solid rgba(255,255,255,0.06);
        border-radius:28px;
        padding:32px;
        height:420px;
        ">

        <div style="
        font-size:26px;
        font-weight:800;
        color:white;
        margin-bottom:10px;
        ">
        Workforce Composition
        </div>

        <div style="
        color:#94A3B8;
        font-size:15px;
        margin-bottom:36px;
        ">
        Distribution of workforce based on overtime exposure.
        </div>

        <!-- SPLIT BAR -->

        <div style="
        display:flex;
        width:100%;
        height:58px;
        border-radius:999px;
        overflow:hidden;
        background:rgba(255,255,255,0.06);
        margin-bottom:34px;
        ">

        <div style="
        width:{overtime_pct}%;
        background:linear-gradient(90deg, #EF4444, #F87171);
        display:flex;
        align-items:center;
        justify-content:center;
        color:white;
        font-size:18px;
        font-weight:700;
        ">
        {overtime_pct}%
        </div>

        <div style="
        width:{non_overtime_pct}%;
        background:linear-gradient(90deg, #3B82F6, #60A5FA);
        display:flex;
        align-items:center;
        justify-content:center;
        color:white;
        font-size:18px;
        font-weight:700;
        ">
        {non_overtime_pct}%
        </div>

        </div>

        <!-- METRIC CARDS -->

        <div style="
        display:flex;
        gap:20px;
        ">

        <div style="
        flex:1;
        padding:24px;
        border-radius:22px;
        background:rgba(239,68,68,0.08);
        border:1px solid rgba(239,68,68,0.14);
        ">

        <div style="
        font-size:14px;
        color:#94A3B8;
        ">
        Overtime Employees
        </div>

        <div style="
        font-size:42px;
        font-weight:900;
        color:#F87171;
        margin-top:10px;
        ">
        {overtime_pct}%
        </div>

        </div>

        <div style="
        flex:1;
        padding:24px;
        border-radius:22px;
        background:rgba(59,130,246,0.08);
        border:1px solid rgba(59,130,246,0.14);
        ">

        <div style="
        font-size:14px;
        color:#94A3B8;
        ">
        Non-Overtime Employees
        </div>

        <div style="
        font-size:42px;
        font-weight:900;
        color:#60A5FA;
        margin-top:10px;
        ">
        {non_overtime_pct}%
        </div>

        </div>

        </div>

        </div>
        """, unsafe_allow_html=True)


    #--------------------------------------------------------
    # STRATEGIC RECOMMENDATION
    #--------------------------------------------------------

    st.subheader("Strategic Recommendation")

    st.success(
        get_department_recommendation(
            selected_department
        )
    )

    # Key Findings
    st.subheader("Key Workforce Findings")

    if selected_department == "All":

        st.markdown(f"""
    - Employees working overtime demonstrate substantially higher attrition vulnerability across the organization.
    - Overtime employees currently show an attrition rate of **{overtime_attrition_rate}%**.
    - Workforce instability appears strongly linked to overtime exposure and operational workload imbalance.
    - Workforce stability score currently stands at **{workforce_stability_score}/100**.
    """)

    else:

        st.markdown(f"""
    - The **{selected_department}** department currently demonstrates an attrition rate of **{dept_attrition}%**.
    - Workforce pressure and operational workload appear strongly associated with retention challenges.
    - Overtime exposure remains a major workforce risk factor within the selected department.
    - Workforce stability score currently stands at **{workforce_stability_score}/100**.
    """)

    # =========================================================
    # SATISFACTION & ENGAGEMENT ANALYSIS
    # =========================================================

    satisfaction_data = (
    get_satisfaction_metrics(
        filtered_df
    )
    )

    job_sat = (
        satisfaction_data[
            "job_satisfaction"
        ]
    )

    worklife = (
        satisfaction_data[
            "worklife_balance"
        ]
    )

    tenure = (
        satisfaction_data[
            "tenure_attrition"
        ]
    )

    attrition_yes = (
        satisfaction_data[
            "attrition_yes_income"
        ]
    )

    attrition_no = (
        satisfaction_data[
            "attrition_no_income"
        ]
    )

    st.markdown("---")
    st.subheader("Satisfaction & Engagement Analysis")

    sat1, sat2 = st.columns(2)

    # Job Satisfaction
    with sat1:

        fig5, ax5 = plt.subplots(figsize=(7,5))

        ax5.plot(
            job_sat['JobSatisfaction'],
            job_sat['Attrition'],
            marker='o',
            linewidth=4,
            markersize=10,
            color='#9B59B6'
        )

        ax5.fill_between(
            job_sat['JobSatisfaction'],
            job_sat['Attrition'],
            alpha=0.2,
            color='#9B59B6'
        )

        ax5.set_title(
            "Attrition by Job Satisfaction",
            fontsize=18,
            fontweight='bold'
        )

        ax5.set_xlabel("Job Satisfaction Level")
        ax5.set_ylabel("Attrition Rate")

        ax5.grid(alpha=0.3, linestyle='--')

        st.pyplot(fig5)

    # Work-Life Balance
    with sat2:

        fig6, ax6 = plt.subplots(figsize=(7,5))

        ax6.bar(
            worklife['WorkLifeBalance'],
            worklife['Attrition'],
            color='#2ECC71',
            width=0.6
        )

        ax6.set_title(
            "Work-Life Balance Impact",
            fontsize=18,
            fontweight='bold'
        )

        ax6.set_xlabel("Work-Life Balance Rating")
        ax6.set_ylabel("Attrition Rate")

        ax6.grid(axis='y', linestyle='--', alpha=0.3)

        st.pyplot(fig6)

    # =========================================================
    # WORKFORCE LIFECYCLE ANALYSIS
    # =========================================================

    st.markdown("---")
    st.subheader("Workforce Lifecycle Analysis")

    lifecycle1, lifecycle2 = st.columns(2)

    # Years at Company
    with lifecycle1:

        fig7, ax7 = plt.subplots(figsize=(7,5))

        ax7.plot(
            tenure['YearsAtCompany'],
            tenure['Attrition'],
            linewidth=3,
            color='#F39C12'
        )

        ax7.fill_between(
            tenure['YearsAtCompany'],
            tenure['Attrition'],
            alpha=0.2,
            color='#F39C12'
        )

        ax7.set_title(
            "Attrition by Employee Tenure",
            fontsize=18,
            fontweight='bold'
        )

        ax7.set_xlabel("Years at Company")
        ax7.set_ylabel("Attrition Rate")

        ax7.grid(alpha=0.3, linestyle='--')

        st.pyplot(fig7)

    # Monthly Income
    with lifecycle2:

        fig8, ax8 = plt.subplots(figsize=(7,5))

        ax8.hist(
            [attrition_yes, attrition_no],
            bins=15,
            label=['Attrition', 'Retention'],
            stacked=True
        )

        ax8.set_title(
            "Income Distribution & Attrition",
            fontsize=18,
            fontweight='bold'
        )

        ax8.set_xlabel("Monthly Income")
        ax8.set_ylabel("Employees")

        ax8.legend()

        st.pyplot(fig8)

    st.markdown("""
            <div style="
            height:1px;
            background: linear-gradient(
            90deg,
            rgba(59,130,246,0),
            rgba(59,130,246,0.7),
            rgba(59,130,246,0)
            );
            margin-top:30px;
            margin-bottom:30px;
            ">
            </div>
            """, unsafe_allow_html=True)
