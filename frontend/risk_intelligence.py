import streamlit as st
import matplotlib.pyplot as plt

from backend.risk_engine import (
    classify_risk,
    get_meter_position,
)

from backend.analytics import (
    get_risk_metrics
)

from backend.insights_engine import (
     get_risk_driver,
     get_risk_personas,
     get_risk_simulation,
     get_predictive_intelligence,
     get_cost_exposure,
     get_risk_action_priorities,
     get_risk_executive_position,
     get_risk_summary
)


def render_risk_intelligence(
    filtered_df,
    selected_department
):
    """Render workforce risk intelligence dashboard."""

    st.subheader("Risk Intelligence")

    st.markdown(f"""
    <div style="
    background:linear-gradient(
    135deg,
    rgba(15,23,42,0.95),
    rgba(30,41,59,0.88)
    );
    border:1px solid rgba(255,255,255,0.06);
    border-radius:30px;
    padding:28px 34px;
    margin-bottom:28px;
    box-shadow:0 10px 30px rgba(0,0,0,0.18);
    ">

    <div style="
    display:flex;
    justify-content:space-between;
    align-items:flex-start;
    flex-wrap:wrap;
    gap:20px;
    ">

    <div>

    <div style="
    font-size:13px;
    font-weight:700;
    letter-spacing:1.4px;
    text-transform:uppercase;
    color:#F59E0B;
    margin-bottom:10px;
    ">
    Risk Intelligence Layer
    </div>

    <div style="
    font-size:34px;
    font-weight:750;
    color:white;
    margin-bottom:12px;
    letter-spacing:-0.8px;
    ">
    Workforce Risk Analysis
    </div>

    <div style="
    font-size:16px;
    line-height:1.8;
    color:#CBD5E1;
    max-width:760px;
    ">
    Department-specific predictive workforce analysis to identify
    attrition exposure, employee instability indicators,
    burnout concentration, and organizational workforce risk.
    </div>

    </div>

    <div style="
    padding:12px 18px;
    border-radius:999px;
    background:rgba(245,158,11,0.08);
    border:1px solid rgba(245,158,11,0.16);
    color:#FBBF24;
    font-size:14px;
    font-weight:600;
    ">
    ⚠ Risk Monitoring Active
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)


    # =========================================================
    # RISK SCORE GENERATION
    # =========================================================

    metrics = get_risk_metrics(
        filtered_df
    )

    risk_df = (
        metrics["risk_df"]
    )

    high_risk_count = (
        metrics["high_risk_count"]
    )

    avg_risk_score = (
        metrics["avg_risk_score"]
    )

    high_risk_percentage = (
        metrics["high_risk_percentage"]
    )

    retention_probability = (
        metrics["retention_probability"]
    )

    projected_attrition_impact = (
        metrics["projected_attrition_impact"]
    )

    optimization_gain = (
        metrics["optimization_gain"]
    )

    simulated_risk_reduction = (
        metrics["simulated_risk_reduction"]
    )

    projected_risk = (
        metrics["projected_risk"]
    )

    heatmap_data = (
        metrics["heatmap_data"]
    )


    # =========================================================
    # EXECUTIVE RISK CALCULATIONS
    # =========================================================

    high_risk_count = len(
        risk_df[risk_df['RiskLevel'] == 'High Risk']
    )

    avg_risk_score = round(
        risk_df['RiskScore'].mean(),
        1
    )

    high_risk_percentage = round(
        high_risk_count / len(risk_df) * 100,
        1
    )

    retention_probability = round(
        100 - high_risk_percentage,
        1
    )

    projected_attrition_impact = (
        high_risk_count * 15000
    )

    optimization_gain = round(
        high_risk_percentage * 0.18,
        1
    )

    simulated_risk_reduction = round(
        high_risk_percentage * 0.18,
        1
    )

    projected_risk = round(
        high_risk_percentage -
        simulated_risk_reduction,
        1
    )

    risk_data = classify_risk(
        high_risk_percentage
    )

    risk_color = (
        risk_data["color"]
    )

    executive_position = (
        get_risk_executive_position(
            risk_data["label"]
        )
    )

    risk_level_map = {

        "Low Risk":
        "Low Risk Exposure",

        "Moderate Risk":
        "Moderate Risk Exposure",

        "High Risk":
        "High Risk Exposure"
    }

    risk_level = (
        risk_level_map[
            risk_data["label"]
        ]
    )


    # =========================================================
    # EXECUTIVE RISK SNAPSHOT
    # =========================================================

    st.markdown("---")
    st.subheader("Executive Risk Snapshot")


    # ======================================================
    # EXECUTIVE SNAPSHOT UI
    # ======================================================

    st.markdown(f"""
    <div style="
    display:grid;
    grid-template-columns:2.2fr 1fr;
    gap:22px;
    align-items:stretch;
    margin-top:22px;
    margin-bottom:40px;
    ">

    <!-- LEFT MAIN CARD -->
    <div style="
    background:linear-gradient(135deg,
    rgba(29,36,71,0.96),
    rgba(31,41,55,0.95));
    border:1px solid rgba(255,255,255,0.05);
    border-radius:34px;
    padding:42px 48px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    box-shadow:0 18px 40px rgba(0,0,0,0.22);
    ">

    <div style="
    font-size:14px;
    font-weight:700;
    letter-spacing:2px;
    text-transform:uppercase;
    color:#A78BFA;
    margin-bottom:28px;
    ">
    Executive Workforce Position
    </div>

    <div style="
    font-size:56px;
    font-weight:800;
    color:white;
    line-height:1.05;
    letter-spacing:-1.6px;
    margin-bottom:30px;
    ">
    {executive_position["title"]}
    </div>

    <div style="
    font-size:18px;
    line-height:2;
    color:#CBD5E1;
    max-width:900px;
    margin-bottom:34px;
    ">
    {executive_position["text"]}
    </div>

    <div style="
    display:flex;
    gap:18px;
    flex-wrap:wrap;
    ">

    <div style="
    padding:16px 24px;
    border-radius:999px;
    background:rgba(167,139,250,0.12);
    border:1px solid rgba(167,139,250,0.18);
    font-size:16px;
    font-weight:700;
    color:#C4B5FD;
    ">
    Risk Score: {avg_risk_score}/100
    </div>

    <div style="
    padding:16px 24px;
    border-radius:999px;
    background:rgba(52,211,153,0.10);
    border:1px solid rgba(52,211,153,0.15);
    font-size:16px;
    font-weight:700;
    color:#9AE6B4;
    ">
    Retention: {retention_probability}%
    </div>

    </div>

    </div>


    <!-- RIGHT STACK -->
    <div style="
    display:flex;
    flex-direction:column;
    gap:18px;
    ">

    <!-- FINANCIAL EXPOSURE -->
    <div style="
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.06);
    border-radius:28px;
    padding:28px 30px;
    height:190px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    box-shadow:0 8px 25px rgba(0,0,0,0.18);
    ">

    <div style="
    font-size:14px;
    color:#94A3B8;
    margin-bottom:12px;
    ">
    Financial Exposure
    </div>

    <div style="
    height:3px;
    width:90px;
    background:linear-gradient(
    90deg,
    rgba(245,158,11,0.85),
    rgba(245,158,11,0.15)
    );
    border-radius:999px;
    margin-bottom:26px;
    "></div>

    <div style="
    font-size:52px;
    font-weight:800;
    color:white;
    line-height:1;
    letter-spacing:-1px;
    margin-bottom:16px;
    ">
    ${projected_attrition_impact:,.0f}
    </div>

    <div style="
    font-size:16px;
    font-weight:600;
    color:#FBBF24;
    line-height:1.4;
    ">
    Potential workforce cost risk
    </div>

    </div>


    <!-- OPTIMIZATION -->
    <div style="
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.06);
    border-radius:28px;
    padding:28px 30px;
    height:190px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    box-shadow:0 8px 25px rgba(0,0,0,0.18);
    ">

    <div style="
    font-size:14px;
    color:#94A3B8;
    margin-bottom:12px;
    ">
    Optimization Opportunity
    </div>

    <div style="
    height:3px;
    width:90px;
    background:linear-gradient(
    90deg,
    rgba(168,85,247,0.85),
    rgba(168,85,247,0.15)
    );
    border-radius:999px;
    margin-bottom:26px;
    "></div>

    <div style="
    font-size:52px;
    font-weight:800;
    color:white;
    line-height:1;
    letter-spacing:-1px;
    margin-bottom:16px;
    ">
    +{optimization_gain}%
    </div>

    <div style="
    font-size:16px;
    font-weight:600;
    color:#60A5FA;
    line-height:1.4;
    ">
    Predicted retention improvement
    </div>

    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # ORGANIZATIONAL RISK STATUS
    # =========================================================

    risk_style_map = {

        "#34D399": {
            "bg":
            "rgba(52,211,153,0.08)",

            "border":
            "rgba(52,211,153,0.14)"
        },

        "#C6A15B": {
            "bg":
            "rgba(198,161,91,0.08)",

            "border":
            "rgba(198,161,91,0.14)"
        },

        "#D97777": {
            "bg":
            "rgba(217,119,119,0.08)",

            "border":
            "rgba(217,119,119,0.14)"
        }
    }

    risk_bg = (
        risk_style_map[
            risk_color
        ]["bg"]
    )

    risk_border = (
        risk_style_map[
            risk_color
        ]["border"]
)


    risk_summary = (
        get_risk_summary(
            selected_department,
            high_risk_percentage,
            risk_level
        )
    )


    st.markdown(f"""
    <div style="
    background:{risk_bg};
    border:1px solid {risk_border};
    border-radius:28px;
    padding:24px 32px;
    margin-top:18px;
    margin-bottom:28px;
    ">

    <div style="
    display:flex;
    justify-content:space-between;
    align-items:flex-start;
    gap:20px;
    flex-wrap:wrap;
    ">

    <div>

    <div style="
    font-size:13px;
    letter-spacing:1.5px;
    text-transform:uppercase;
    font-weight:700;
    color:{risk_color};
    margin-bottom:10px;
    ">
    Executive Risk Signal
    </div>

    <div style="
    font-size:32px;
    font-weight:750;
    color:white;
    margin-bottom:14px;
    ">
    {risk_level}
    </div>

    <div style="
    width:80px;
    height:4px;
    border-radius:999px;
    background:{risk_color};
    margin-bottom:20px;
    opacity:0.9;
    ">
    </div>

    <div style="
    font-size:17px;
    line-height:1.9;
    color:#CBD5E1;
    max-width:620px;
    font-family: 'Inter', sans-serif;
    ">
    {risk_summary}
    </div>

    </div>

    <div style="
    padding:14px 20px;
    border-radius:999px;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.06);
    font-size:15px;
    font-weight:700;
    color:{risk_color};
    ">
    ● Active Risk Monitoring
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # EXECUTIVE RISK DISTRIBUTION
    # =========================================================

    st.markdown("---")
    st.subheader("Predictive Risk Distribution")

    risk_col1, risk_col2 = st.columns([1.2, 1])

    # =========================================================
    # EXECUTIVE RISK METER
    # =========================================================

    with risk_col1:

        meter_position = (
            get_meter_position(
                high_risk_percentage
            )
        )

        st.markdown(f"""
        <div style="
        background:linear-gradient(
        135deg,
        rgba(15,23,42,0.95),
        rgba(30,41,59,0.88)
        );
        border:1px solid rgba(255,255,255,0.06);
        border-radius:28px;
        padding:30px;
        min-height:280px;
        ">

        <div style="
        font-size:13px;
        letter-spacing:1.4px;
        text-transform:uppercase;
        font-weight:700;
        color:#F59E0B;
        margin-bottom:10px;
        ">
        Workforce Risk Meter
        </div>

        <div style="
        font-size:30px;
        font-weight:750;
        color:white;
        margin-bottom:10px;
        ">
        {risk_level}
        </div>

        <div style="
        font-size:16px;
        line-height:1.8;
        color:#CBD5E1;
        margin-bottom:34px;
        max-width:550px;
        ">
        Current workforce intelligence indicates
        {high_risk_percentage}% predictive workforce
        exposure requiring monitoring and targeted
        intervention strategies.
        </div>

        <div style="
        position:relative;
        margin-top:30px;
        ">

        <div style="
        height:12px;
        border-radius:999px;
        background:linear-gradient(
        90deg,
        #34D399 0%,
        #FBBF24 50%,
        #F87171 100%
        );
        ">
        </div>

        <div style="
        position:absolute;
        top:-12px;
        left:{meter_position}%;
        top:50%;
        transform:translate(-50%, -45%);
        width:28px;
        height:28px;
        border-radius:50%;
        background:white;
        box-shadow:
        0 0 18px rgba(255,255,255,0.22);
        border:4px solid {risk_color};
        ">
        </div>

        </div>

        <div style="
        display:flex;
        justify-content:space-between;
        margin-top:12px;
        color:#94A3B8;
        font-size:13px;
        font-weight:600;
        ">
        <span>LOW</span>
        <span>MODERATE</span>
        <span>HIGH</span>
        </div>

        <!-- EXECUTIVE SIGNALS -->

        <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        margin-top:36px;
        padding-top:28px;
        border-top:1px solid rgba(255,255,255,0.06);
        ">

        <!-- BURNOUT -->

        <div style="
        display:flex;
        flex-direction:column;
        align-items:center;
        gap:14px;
        ">

        <div style="
        width:92px;
        height:92px;
        border-radius:50%;
        background:
        conic-gradient(
        #F59E0B {(filtered_df['OverTime'] == 'Yes').mean()*100}%,
        rgba(255,255,255,0.08) 0
        );
        display:flex;
        justify-content:center;
        align-items:center;
        box-shadow:0 0 24px rgba(245,158,11,0.10);
        ">

        <div style="
        width:68px;
        height:68px;
        border-radius:50%;
        background:#0B1120;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:20px;
        font-weight:800;
        color:white;
        ">
        {round((filtered_df['OverTime'] == 'Yes').mean()*100)}
        %
        </div>

        </div>

        <div style="
        font-size:13px;
        font-weight:700;
        color:#94A3B8;
        text-transform:uppercase;
        letter-spacing:1px;
        ">
        Burnout
        </div>

        </div>


        <!-- RETENTION -->

        <div style="
        display:flex;
        flex-direction:column;
        align-items:center;
        gap:14px;
        ">

        <div style="
        width:92px;
        height:92px;
        border-radius:50%;
        background:
        conic-gradient(
        #22C55E {(100 - high_risk_percentage)}%,
        rgba(255,255,255,0.08) 0
        );
        display:flex;
        justify-content:center;
        align-items:center;
        box-shadow:0 0 24px rgba(34,197,94,0.10);
        ">

        <div style="
        width:68px;
        height:68px;
        border-radius:50%;
        background:#0B1120;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:20px;
        font-weight:800;
        color:white;
        ">
        {100 - high_risk_percentage:.0f}%
        </div>

        </div>

        <div style="
        font-size:13px;
        font-weight:700;
        color:#94A3B8;
        text-transform:uppercase;
        letter-spacing:1px;
        ">
        Retention
        </div>

        </div>


        <!-- ATTRITION -->

        <div style="
        display:flex;
        flex-direction:column;
        align-items:center;
        gap:14px;
        ">

        <div style="
        width:92px;
        height:92px;
        border-radius:50%;
        background:
        conic-gradient(
        #EF4444 {high_risk_percentage}%,
        rgba(255,255,255,0.08) 0
        );
        display:flex;
        justify-content:center;
        align-items:center;
        box-shadow:0 0 24px rgba(239,68,68,0.10);
        ">

        <div style="
        width:68px;
        height:68px;
        border-radius:50%;
        background:#0B1120;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:20px;
        font-weight:800;
        color:white;
        ">
        {high_risk_percentage:.0f}%
        </div>

        </div>

        <div style="
        font-size:13px;
        font-weight:700;
        color:#94A3B8;
        text-transform:uppercase;
        letter-spacing:1px;
        ">
        Attrition
        </div>

        </div>

        </div>

        </div>
        """, unsafe_allow_html=True)

    # =========================================================
    # EXECUTIVE SNAPSHOT
    # =========================================================

    with risk_col2:

        risk_driver, risk_driver_signal = (
            get_risk_driver(
                selected_department
            )
        )
        st.markdown(f"""
        <div style="
        display:flex;
        flex-direction:column;
        gap:18px;
        ">

        <!-- CARD 1 -->
        <div style="
        background:linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
        border:1px solid rgba(255,255,255,0.06);
        border-radius:24px;
        padding:22px 24px 34px 24px;
        min-height:120px;
        display:flex;
        flex-direction:column;
        justify-content:center;
        box-shadow:0 8px 25px rgba(0,0,0,0.18), inset 0 1px 0 rgba(255,255,255,0.03);
        ">

        <div style="
        font-size:13px;
        color:#94A3B8;
        margin-bottom:14px;
        ">
        High Risk Population
        </div>

        <div style="
        height:2px;
        background:rgba(245,158,11,0.20);
        margin-bottom:26px;
        border-radius:999px;
        "></div>

        <div style="
        font-size:32px;
        font-weight:800;
        color:white;
        line-height:1.1;
        ">
        {high_risk_percentage}%
        </div>

        <div style="
        color:#F87171;
        font-size:14px;
        margin-top:12px;
        font-weight:600;
        ">
        Attrition Vulnerability
        </div>

        </div>


        <!-- CARD 2 -->
        <div style="
        background:linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
        border:1px solid rgba(255,255,255,0.06);
        border-radius:24px;
        padding:22px 24px 34px 24px;
        min-height:120px;
        display:flex;
        flex-direction:column;
        justify-content:center;
        box-shadow:0 8px 25px rgba(0,0,0,0.18), inset 0 1px 0 rgba(255,255,255,0.03);
        ">

        <div style="
        font-size:13px;
        color:#94A3B8;
        margin-bottom:14px;
        ">
        Primary Risk Driver
        </div>

        <div style="
        height:2px;
        background:rgba(245,158,11,0.20);
        margin-bottom:26px;
        border-radius:999px;
        "></div>

        <div style="
        font-size:32px;
        font-weight:800;
        color:white;
        line-height:1.1;
        ">
        {risk_driver}
        </div>

        <div style="
        color:#FBBF24;
        font-size:14px;
        margin-top:12px;
        font-weight:600;
        ">
        {risk_driver_signal}
        </div>

        </div>


        <!-- CARD 3 -->
        <div style="
        background:linear-gradient(180deg, rgba(255,255,255,0.04), rgba(255,255,255,0.02));
        border:1px solid rgba(255,255,255,0.06);
        border-radius:24px;
        padding:22px 24px 34px 24px;
        min-height:120px;
        display:flex;
        flex-direction:column;
        justify-content:center;
        box-shadow:0 8px 25px rgba(0,0,0,0.18), inset 0 1px 0 rgba(255,255,255,0.03);
        ">

        <div style="
        font-size:13px;
        color:#94A3B8;
        margin-bottom:14px;
        ">
        Department Risk Status
        </div>

        <div style="
        height:2px;
        background:rgba(245,158,11,0.20);
        margin-bottom:26px;
        border-radius:999px;
        "></div>

        <div style="
        font-size:32px;
        font-weight:800;
        color:white;
        line-height:1.1;
        ">
        {risk_level}
        </div>

        <div style="
        color:{risk_color};
        font-size:14px;
        margin-top:12px;
        font-weight:600;
        ">
        Predictive Workforce Intelligence
        </div>

        </div>

        </div>
        """, unsafe_allow_html=True)

    # ======================================================
    # FEATURE IMPORTANCE
    # ======================================================

    st.markdown("---")
    st.subheader("Predictive Risk Drivers")

    feature_names = [
        'Overtime',
        'Job Satisfaction',
        'Work-Life Balance',
        'Employee Tenure',
        'Monthly Income'
    ]

    feature_scores = [30, 25, 20, 15, 10]

    fig11, ax11 = plt.subplots(figsize=(9,5))

    bars = ax11.barh(
        feature_names,
        feature_scores,
        color=[
            '#E74C3C',
            '#F39C12',
            '#F1C40F',
            '#3498DB',
            '#2ECC71'
        ]
    )

    for bar in bars:

        width = bar.get_width()

        ax11.text(
            width + 1,
            bar.get_y() + bar.get_height()/2,
            f'{width}',
            va='center',
            fontsize=12,
            fontweight='bold'
        )

    ax11.set_title(
        "Feature Importance Analysis",
        fontsize=18,
        fontweight='bold',
        pad=20
    )

    ax11.set_xlabel("Risk Contribution Score")

    ax11.grid(
        axis='x',
        linestyle='--',
        alpha=0.3
    )

    ax11.spines['top'].set_visible(False)
    ax11.spines['right'].set_visible(False)

    st.pyplot(fig11)

    # =========================================================
    # HIGH-RISK PERSONAS
    # =========================================================

    st.markdown("---")
    st.subheader("High-Risk Workforce Personas")

    persona1, persona2 = st.columns(2)

    persona_one, persona_two = (
        get_risk_personas(
            selected_department
        )
    )

    with persona1:

        st.info(persona_one)

    with persona2:

        st.info(persona_two)

    # =========================================================
    # RISK HEATMAP STYLE ANALYSIS
    # =========================================================

    st.markdown("---")
    st.subheader("Workforce Risk Pattern Analysis")

    fig12, ax12 = plt.subplots(figsize=(7,5))

    im = ax12.imshow(
        heatmap_data,
        aspect='auto',
        cmap='coolwarm'
    )

    ax12.set_xticks(range(len(heatmap_data.columns)))
    ax12.set_xticklabels(heatmap_data.columns)

    ax12.set_yticks(range(len(heatmap_data.index)))
    ax12.set_yticklabels(heatmap_data.index)

    ax12.set_title(
        "Risk Heatmap: Overtime vs Satisfaction",
        fontsize=18,
        fontweight='bold',
        pad=20
    )

    ax12.set_xlabel("Job Satisfaction")
    ax12.set_ylabel("Overtime Status")

    fig12.colorbar(im)

    st.pyplot(fig12)

    # =========================================================
    # PREDICTIVE SCENARIO SIMULATION
    # =========================================================

    st.markdown("---")
    st.subheader("Predictive Scenario Simulation")

    st.success(
        get_risk_simulation(
            selected_department,
            simulated_risk_reduction,
            projected_risk
        )
    )

    # =========================================================
    # PREDICTIVE INSIGHTS
    # =========================================================

    st.markdown("---")
    st.subheader("Predictive Workforce Insights")

    st.info(
        get_predictive_intelligence(
            selected_department,
            high_risk_count,
            high_risk_percentage
        )
    )

    # =========================================================
    # COST IMPACT ESTIMATION
    # =========================================================

    st.markdown("---")
    st.subheader("Estimated Organizational Cost Exposure")

    st.error(
        get_cost_exposure(
            selected_department,
            projected_attrition_impact
        )
    )
    # =========================================================
    # STRATEGIC ACTION PRIORITIES
    # =========================================================

    st.markdown("---")
    st.subheader("Strategic Action Priorities")

    st.success(
        get_risk_action_priorities(
            selected_department
        )
    )
        
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
