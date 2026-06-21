import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from backend.risk_engine import (
    classify_risk,
    calculate_live_attrition_risk
)

from backend.insights_engine import (
    get_strategic_outlook,
    get_optimization_projection,
    get_department_content,
    get_executive_position,
    get_executive_priority,
    get_health_assessment,
    get_strategy_maturity,
)

from backend.analytics import (
    get_strategic_metrics,
    get_department_risk_ranking,
    get_impact_simulation
)

def render_strategic_insights(
    filtered_df,
    df,
    selected_department,
    X,
    rf_model
):
    """Render strategic workforce insights dashboard."""

    # =========================================================
    # STRATEGIC ANALYTICS
    # =========================================================

    metrics = get_strategic_metrics(
        filtered_df
    )

    high_risk_count = (
        metrics["high_risk_count"]
    )

    strategic_risk_score = (
        metrics["strategic_risk_score"]
    )

    strategic_retention_score = (
        metrics["strategic_retention_score"]
    )

    projected_attrition_impact = (
        metrics["projected_attrition_impact"]
    )

    optimization_gain = (
        metrics["optimization_gain"]
    )

    forecast_improvement = (
        metrics["forecast_improvement"]
    )

    projected_stability = (
        metrics["projected_stability"]
    )

    health_index = (
        metrics["health_index"]
    )

    risk_label = (
        metrics["risk_label"]
    )

    signal_color = (
        metrics["signal_color"]
    )

    overtime_percentage = (
        metrics["overtime_percentage"]
    )   

    # =========================================================
    # STRATEGIC OUTLOOK
    # =========================================================

    outlook_data = (
        get_strategic_outlook(
            risk_label,
            selected_department
        )
    )

    outlook_heading = (
        outlook_data["heading"]
    )

    outlook_text = (
        outlook_data["text"]
    )

    # =========================================================
    # SIGNAL GLOW
    # =========================================================

    signal_glow_map = {

        "#34D399":
        "rgba(52,211,153,0.18)",

        "#C6A15B":
        "rgba(198,161,91,0.18)",

        "#D97777":
        "rgba(217,119,119,0.18)"
    }

    signal_glow = (
        signal_glow_map[
            signal_color
        ]
    )

    maturity_data = (
        get_strategy_maturity(
            health_index
        )
    )

    maturity_level = (
        maturity_data["level"]
    )

    maturity_color = (
        maturity_data["icon"]
    )


    # =========================================================
    # DEPARTMENT CONTENT
    # =========================================================

    department_content = (
        get_department_content(
            selected_department,
            optimization_gain
        )
    )

    executive_position = (
        get_executive_position(
            risk_label
        )
    )

    executive_priority = (
        get_executive_priority(
            selected_department
        )
    )   

    health_assessment = (
        get_health_assessment(
            health_index,
            selected_department
        )
    )


    # =========================================================
    # PAGE HEADER
    # =========================================================

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
    color:#A78BFA;
    margin-bottom:10px;
    ">
    Strategic Workforce Intelligence
    </div>

    <div style="
    font-size:34px;
    font-weight:750;
    color:white;
    margin-bottom:12px;
    letter-spacing:-0.8px;
    ">
    Executive Workforce Strategy
    </div>

    <div style="
    font-size:16px;
    line-height:1.8;
    color:#CBD5E1;
    max-width:760px;
    ">
    Department-specific workforce intelligence transforming
    predictive analytics into executive workforce decisions,
    retention strategies, and organizational planning.
    </div>

    </div>

    <div style="
    padding:12px 18px;
    border-radius:999px;
    background:rgba(168,85,247,0.08);
    border:1px solid rgba(168,85,247,0.16);
    color:#C4B5FD;
    font-size:14px;
    font-weight:600;
    ">
    🧠 Strategic Intelligence Active
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)


    # ======================================================
    # EXECUTIVE COMMAND CENTER
    # ======================================================

    st.markdown(f"""
    <div style="
    background:linear-gradient(
    135deg,
    rgba(20,27,45,0.96),
    rgba(30,41,59,0.90)
    );
    border:1px solid rgba(255,255,255,0.06);
    border-radius:34px;
    padding:34px;
    margin-top:18px;
    margin-bottom:30px;
    box-shadow:0 12px 35px rgba(0,0,0,0.22);
    ">

    <!-- TOP EXECUTIVE STATUS BAR -->

    <div style="
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:18px;
    margin-bottom:30px;
    ">
                
    <div style="
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.05);
    padding:24px;
    min-height:150px;
    display:flex;
    flex-direction:column;
    justify-content:flex-start;
    border-radius:22px;
    ">
                
    <div style="
    width:56px;
    height:3px;
    border-radius:999px;
    margin-bottom:22px;
    background:linear-gradient(90deg,#38BDF8,#2563EB);
    opacity:0.9;
    ">
    </div>
                
    <div style="
    font-size:13px;
    color:#94A3B8;
    margin-bottom:12px;
    ">
    Workforce Posture
    </div>
                

    <div style="
    font-size:28px;
    font-weight:800;
    color:white;
    line-height:1.1;
    ">
    {executive_position["title"]}
    </div>
    </div>


    <div style="
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.05);
    padding:24px;
    min-height:150px;
    display:flex;
    flex-direction:column;
    justify-content:flex-start;
    border-radius:22px;
    ">
                
    <div style="
    width:56px;
    height:3px;
    border-radius:999px;
    margin-bottom:22px;
    background:linear-gradient(90deg,#C4B5FD,#8B5CF6);
    opacity:0.9;
    "></div>
                
    <div style="
    font-size:13px;
    color:#94A3B8;
    margin-bottom:12px;
    ">
    Risk Score
    </div>

    <div style="
    font-size:22px;
    font-weight:800;
    color:#C4B5FD;
    ">
    {strategic_risk_score}/100
    </div>
    </div>


    <div style="
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.05);
    padding:24px;
    min-height:150px;
    display:flex;
    flex-direction:column;
    justify-content:flex-start;
    border-radius:22px;
    ">

    <div style="
    width:56px;
    height:3px;
    border-radius:999px;
    margin-bottom:22px;
    background:linear-gradient(90deg,#A7F3D0,#34D399);
    opacity:0.9;
    "></div>

    <div style="
    font-size:13px;
    color:#94A3B8;
    margin-bottom:12px;
    ">
    Retention Strength
    </div>

    <div style="
    font-size:22px;
    font-weight:800;
    color:#86EFAC;
    ">
    {strategic_retention_score}%
    </div>
    </div>


    <div style="
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.05);
    padding:24px;
    min-height:150px;
    display:flex;
    flex-direction:column;
    justify-content:flex-start;
    border-radius:22px;
    ">

    <div style="
    width:56px;
    height:3px;
    border-radius:999px;
    margin-bottom:22px;
    background:linear-gradient(90deg,#93C5FD,#3B82F6);
    opacity:0.9;
    "></div>

    <div style="
    font-size:13px;
    color:#94A3B8;
    margin-bottom:12px;
    ">
    Optimization Gain
    </div>

    <div style="
    font-size:22px;
    font-weight:800;
    color:#60A5FA;
    ">
    +{optimization_gain}%
    </div>
    </div>

    </div>

    <div style="
    height:1px;
    background:linear-gradient(
    90deg,
    rgba(255,255,255,0),
    rgba(255,255,255,0.08),
    rgba(255,255,255,0)
    );
    margin-bottom:26px;
    "></div>


    <!-- MIDDLE EXECUTIVE GRID -->

    <div style="
    display:grid;
    grid-template-columns:1.25fr 0.9fr 0.9fr;
    gap:22px;
    ">

    <!-- LEFT BIG INSIGHT -->

    <div style="
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.06);
    border-radius:28px;
    padding:26px;
    ">

    <div style="
    font-size:13px;
    font-weight:700;
    letter-spacing:1.5px;
    text-transform:uppercase;
    color:#A78BFA;
    margin-bottom:18px;
    ">
    Executive Workforce Position
    </div>

    <div style="
    font-size:30px;
    font-weight:800;
    color:white;
    margin-bottom:18px;
    line-height:1.1;
    ">
    {executive_position["title"]}
    </div>

    <div style="
    font-size:16px;
    line-height:1.7;
    color:#CBD5E1;
    ">
    {executive_position["text"]}
    </div>

    <div style="
    display:flex;
    gap:12px;
    margin-top:26px;
    flex-wrap:wrap;
    ">

    <div style="
    padding:10px 18px;
    background:rgba(168,85,247,0.08);
    border:1px solid rgba(168,85,247,0.12);
    border-radius:999px;
    font-size:14px;
    font-weight:600;
    color:#C4B5FD;
    ">
    Risk Score: {strategic_risk_score}
    </div>

    <div style="
    padding:10px 18px;
    background:rgba(34,197,94,0.08);
    border:1px solid rgba(34,197,94,0.12);
    border-radius:999px;
    font-size:14px;
    font-weight:600;
    color:#86EFAC;
    ">
    Retention: {strategic_retention_score}%
    </div>

    </div>

    </div>


    <!-- COST EXPOSURE -->

    <div style="
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.06);
    border-radius:34px;
    padding:34px 36px;
    display:flex;
    flex-direction:column;
    justify-content:flex-start;
    min-height:300px;
    ">

    <div>

    <div style="
    font-size:18px;
    color:#A1A8BE;
    margin-bottom:36px;
    ">
    Financial Exposure
    </div>

    <div style="
    font-size:12px;
    font-weight:700;
    letter-spacing:2px;
    text-transform:uppercase;
    color:#F5C84C;
    margin-bottom:14px;
    ">
    Estimated Annual Impact
    </div>

    <div style="
    font-size:52px;
    font-weight:800;
    line-height:1;
    color:white;
    margin-bottom:22px;
    ">
    ${projected_attrition_impact:,.0f}
    </div>

    </div>

    <div>

    <div style="
    width:100%;
    height:1px;
    background:rgba(255,255,255,0.06);
    margin-bottom:18px;
    "></div>

    <div style="
    font-size:16px;
    color:#F5C84C;
    font-weight:600;
    line-height:1.5;
    ">
    Potential workforce cost risk
    </div>

    </div>

    </div>


    <!-- EXECUTIVE ACTION -->

    <div style="
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.05);
    border-radius:28px;
    padding:34px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    min-height:340px;
    position:relative;
    overflow:hidden;
    ">

    <!-- Accent line -->
    <div style="
    width:58px;
    height:3px;
    border-radius:999px;
    margin-bottom:28px;
    background:linear-gradient(90deg,#60A5FA,#2563EB);
    opacity:0.9;
    "></div>

    <!-- Label -->
    <div style="
    font-size:14px;
    color:#94A3B8;
    margin-bottom:18px;
    font-weight:500;
    ">
    Executive Priority
    </div>

    <!-- Main heading -->
    <div style="
    font-size:28px;
    font-weight:800;
    color:white;
    line-height:1.18;
    margin-bottom:24px;
    max-width:95%;
    ">
    {executive_priority["title"]}
    </div>

    <!-- Supporting text -->
    <div style="
    font-size:15px;
    line-height:1.9;
    color:#7FAAFF;
    max-width:92%;
    ">
    {executive_priority["text"]}
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # WORKFORCE HEALTH INDEX
    # =========================================================

    st.markdown("---")
    st.subheader("Workforce Health Index")  


    # =========================================================
    # WORKFORCE HEALTH COMMAND CENTER
    # =========================================================

    st.markdown(f"""
    <div style="
    background:linear-gradient(
    135deg,
    rgba(18,24,40,0.96),
    rgba(29,38,59,0.92)
    );
    border:1px solid rgba(255,255,255,0.05);
    border-radius:36px;
    padding:38px;
    margin-top:18px;
    margin-bottom:36px;
    position:relative;
    overflow:hidden;
    ">

    <!-- subtle glow -->
    <div style="
    position:absolute;
    top:-120px;
    right:-80px;
    width:300px;
    height:300px;
    background:radial-gradient(
    circle,
    rgba(96,165,250,0.10),
    transparent 70%
    );
    pointer-events:none;
    "></div>

    <div style="
    display:grid;
    grid-template-columns:0.9fr 1.3fr;
    gap:28px;
    align-items:stretch;
    ">

    <!-- LEFT CARD -->
    <div style="
    background:rgba(255,255,255,0.035);
    border:1px solid rgba(255,255,255,0.06);
    border-radius:30px;
    padding:34px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    position:relative;
    overflow:hidden;
    ">

    <!-- green glow -->
    <div style="
    position:absolute;
    top:-80px;
    right:-60px;
    width:180px;
    height:180px;
    background:radial-gradient(
    circle,
    rgba(34,197,94,0.14),
    transparent 70%
    );
    "></div>

    <div style="
    display:flex;
    align-items:center;
    gap:10px;
    margin-bottom:24px;
    ">

    <div style="
    width:10px;
    height:10px;
    border-radius:50%;
    background:#22C55E;
    box-shadow:0 0 18px rgba(34,197,94,0.55);
    "></div>

    <div style="
    font-size:13px;
    letter-spacing:1.2px;
    text-transform:uppercase;
    font-weight:700;
    color:#A78BFA;
    ">
    Workforce Health Score
    </div>

    </div>

    <div style="
    font-size:84px;
    font-weight:800;
    color:white;
    line-height:1;
    letter-spacing:-3px;
    margin-bottom:14px;
    ">
    {health_index}
    </div>

    <div style="
    font-size:18px;
    color:#94A3B8;
    margin-bottom:28px;
    ">
    Organizational Health Index
    </div>

    <div style="
    width:100%;
    height:10px;
    background:rgba(255,255,255,0.06);
    border-radius:999px;
    overflow:hidden;
    margin-bottom:20px;
    ">

    <div style="
    height:100%;
    width:{health_index}%;
    background:linear-gradient(
    90deg,
    #22C55E,
    #A3E635
    );
    border-radius:999px;
    box-shadow:0 0 25px rgba(163,230,53,0.35);
    "></div>

    </div>

    <div style="
    display:flex;
    justify-content:space-between;
    font-size:13px;
    color:#64748B;
    ">
    <span>Critical</span>
    <span>Healthy</span>
    </div>

    </div>


    <!-- RIGHT EXECUTIVE INSIGHT -->
    <div style="
    background:rgba(255,255,255,0.035);
    border:1px solid rgba(255,255,255,0.06);
    border-radius:30px;
    padding:42px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    position:relative;
    overflow:hidden;
    ">

    <!-- glow -->
    <div style="
    position:absolute;
    top:-120px;
    right:-100px;
    width:240px;
    height:240px;
    background:radial-gradient(
    circle,
    rgba(167,139,250,0.10),
    transparent 70%
    );
    "></div>

    <div style="
    display:inline-flex;
    align-items:center;
    gap:10px;
    padding:10px 16px;
    border-radius:999px;
    width:fit-content;
    background:rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.06);
    margin-bottom:26px;
    ">

    <div style="
    width:8px;
    height:8px;
    border-radius:50%;
    background:{'#22C55E' if health_index >= 75 else '#F59E0B' if health_index >= 50 else '#EF4444'};
    "></div>

    <div style="
    font-size:13px;
    font-weight:700;
    color:#CBD5E1;
    ">
    Executive Workforce Assessment
    </div>

    </div>

    <div style="
    font-size:40px;
    font-weight:800;
    color:white;
    line-height:1.12;
    margin-bottom:24px;
    max-width:90%;
    ">
    {health_assessment["title"]}
    </div>

    <div style="
    font-size:16px;
    line-height:2;
    color:#CBD5E1;
    max-width:92%;
    ">
    {health_assessment["text"]}
    </div>

    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # EXECUTIVE OUTLOOK
    # =========================================================

    st.markdown("---")
    st.subheader("Executive Workforce Outlook")


    st.markdown(f"""
    <div style="
    position:relative;
    margin-top:22px;
    margin-bottom:34px;
    padding:36px 24px 30px 24px;
    ">

    <!-- SIGNAL LINE -->
    <div style="
    position:absolute;
    top:0;
    left:0;
    height:2px;
    width:100%;
    background:linear-gradient(
    90deg,
    transparent,
    {signal_color},
    transparent
    );
    box-shadow:0 0 24px {signal_glow};
    opacity:0.9;
    ">
    </div>


    <div style="
    display:grid;
    grid-template-columns:0.9fr 2fr 1fr;
    gap:36px;
    align-items:center;
    ">

    <!-- LEFT -->
    <div>

    <div style="
    display:flex;
    align-items:center;
    gap:12px;
    margin-bottom:16px;
    ">

    <div style="
    width:14px;
    height:14px;
    border-radius:50%;
    background:{signal_color};
    box-shadow:0 0 18px {signal_glow};
    ">
    </div>

    <div style="
    font-size:13px;
    font-weight:700;
    letter-spacing:1.5px;
    text-transform:uppercase;
    color:{signal_color};
    ">
    Executive Signal
    </div>

    </div>

    <div style="
    font-size:40px;
    font-weight:800;
    line-height:1;
    color:white;
    ">
    {outlook_heading}
    </div>

    </div>


    <!-- CENTER -->
    <div>

    <div style="
    font-size:34px;
    font-weight:800;
    color:white;
    line-height:1.2;
    margin-bottom:16px;
    ">
    {outlook_heading}
    </div>

    <div style="
    font-size:17px;
    line-height:1.9;
    color:#CBD5E1;
    max-width:780px;
    ">
    {outlook_text}
    </div>

    </div>


    <!-- RIGHT -->
    <div style="
    display:flex;
    flex-direction:column;
    gap:14px;
    align-items:flex-start;
    ">

    <div style="
    padding:10px 18px;
    border-radius:999px;
    background:rgba(255,255,255,0.04);
    color:#93C5FD;
    font-size:14px;
    font-weight:600;
    ">
    Retention Focus
    </div>

    <div style="
    padding:10px 18px;
    border-radius:999px;
    background:rgba(255,255,255,0.04);
    color:#FBBF24;
    font-size:14px;
    font-weight:600;
    ">
    Burnout Monitoring
    </div>

    <div style="
    padding:10px 18px;
    border-radius:999px;
    background:rgba(255,255,255,0.04);
    color:#C4B5FD;
    font-size:14px;
    font-weight:600;
    ">
    Leadership Action
    </div>

    </div>

    </div>
    </div>
    """, unsafe_allow_html=True)

    # =========================================================
    # STRATEGIC PRIORITY MATRIX
    # =========================================================

    st.markdown("---")
    st.subheader("Strategic Priority Matrix")

    priority_df = pd.DataFrame({

        "Strategic Initiative": [
            "Burnout Reduction",
            "Employee Engagement",
            "Workforce Planning",
            "Retention Optimization",
            "Leadership Monitoring"
        ],

        "Business Impact": [
            "High",
            "High",
            "Medium",
            "High",
            "Medium"
        ],

        "Urgency": [
            "High",
            "Medium",
            "Medium",
            "High",
            "Low"
        ]
    })

    st.dataframe(
        priority_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

    # =========================================================
    # STRATEGIC FORECAST VISUALS
    # =========================================================

    st.markdown("---")
    st.subheader("Strategic Workforce Forecast")


    forecast_col1, forecast_col2 = st.columns([1.05, 1])

    # ======================================================
    # LEFT — HERO VISUAL GAUGE
    # ======================================================

    st.markdown("""
    <style>

    /* Kill plot scrollbars */
    [data-testid="stPlotlyChart"] > div {
        overflow: hidden !important;
    }

    /* Remove scrollable iframe container */
    .js-plotly-plot .plot-container {
        overflow: hidden !important;
    }

    /* Remove streamlit scroll inside charts */
    .element-container iframe {
        overflow: hidden !important;
    }

    </style>
    """, unsafe_allow_html=True)

    with forecast_col1:

        fig_forecast = go.Figure()

        fig_forecast.add_trace(go.Indicator(
            mode="gauge+number",
            value=strategic_retention_score,

            number={
                "suffix": "%",
                "font": {
                    "size": 46,
                    "color": "white"
                }
            },

            title={
                "text": "Retention Stability",
                "font": {
                    "size": 18,
                    "color": "#E2E8F0"
                }
            },

            domain={
                "x": [0.12, 0.88],
                "y": [0.22, 0.82]
            },

            gauge={
                "shape": "angular",

                "axis": {
                    "range": [0, 100],
                    "tickwidth": 0,
                    "tickcolor": "rgba(0,0,0,0)"
                },

                "bar": {
                    "color": "#8ED973",
                    "thickness": 0.30
                },

                "bgcolor": "rgba(0,0,0,0)",

                "borderwidth": 0,

                "steps": [
                    {
                        "range": [0, 40],
                        "color": "rgba(239,68,68,0.15)"
                    },
                    {
                        "range": [40, 70],
                        "color": "rgba(245,158,11,0.12)"
                    },
                    {
                        "range": [70, 100],
                        "color": "rgba(34,197,94,0.12)"
                    }
                ]
            }
        ))

        fig_forecast.update_layout(
            template="plotly_dark",

            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",

            height=240,

            margin=dict(
                l=0,
                r=0,
                t=0,
                b=0
            )
        )

        st.plotly_chart(
            fig_forecast,
            use_container_width=True,
            config={
                "displayModeBar": False,
                "staticPlot": True
            }
        )

        st.markdown(f"""
        <div style="
        margin-top:-10px;
        padding:0 8px;
        ">

        <div style="
        font-size:13px;
        font-weight:700;
        letter-spacing:1.5px;
        text-transform:uppercase;
        color:#A5C4FF;
        margin-bottom:14px;
        ">
        WORKFORCE STABILITY FORECAST
        </div>

        <div style="
        font-size:15px;
        line-height:1.9;
        color:#CBD5E1;
        margin-bottom:24px;
        ">
        Workforce intelligence forecasts indicate
        retention performance can improve through
        targeted workforce optimization and burnout
        reduction strategies.
        </div>


        <!-- RISK DRIVER PANEL -->

        <div style="
        background:rgba(255,255,255,0.03);
        border:1px solid rgba(255,255,255,0.06);
        border-radius:20px;
        padding:20px;
        ">

        <div style="
        font-size:12px;
        font-weight:700;
        letter-spacing:1.4px;
        text-transform:uppercase;
        color:#FBBF24;
        margin-bottom:18px;
        ">
        Primary Workforce Risk Drivers
        </div>


        <!-- DRIVER 1 -->

        <div style="
        display:flex;
        justify-content:space-between;
        margin-bottom:14px;
        ">

        <span style="
        color:#CBD5E1;
        font-size:14px;
        font-weight:600;
        ">
        Overtime Exposure
        </span>

        <span style="
        color:#FCA5A5;
        font-size:14px;
        font-weight:700;
        ">
        {overtime_percentage}%
        </span>

        </div>

        <div style="
        width:100%;
        height:8px;
        background:rgba(255,255,255,0.06);
        border-radius:999px;
        overflow:hidden;
        margin-bottom:20px;
        ">

        <div style="
        width:{overtime_percentage}%;
        height:100%;
        background:linear-gradient(
        90deg,
        #F59E0B,
        #EF4444
        );
        border-radius:999px;
        "></div>

        </div>


        <!-- DRIVER 2 -->

        <div style="
        display:flex;
        justify-content:space-between;
        margin-bottom:14px;
        ">

        <span style="
        color:#CBD5E1;
        font-size:14px;
        font-weight:600;
        ">
        High Risk Employees
        </span>

        <span style="
        color:#FCA5A5;
        font-size:14px;
        font-weight:700;
        ">
        {high_risk_count}
        </span>

        </div>

        <div style="
        width:100%;
        height:8px;
        background:rgba(255,255,255,0.06);
        border-radius:999px;
        overflow:hidden;
        margin-bottom:20px;
        ">

        <div style="
        width:{min((high_risk_count / len(filtered_df)) * 100, 100)}%;
        height:100%;
        background:linear-gradient(
        90deg,
        #A855F7,
        #EC4899
        );
        border-radius:999px;
        "></div>

        </div>


        <!-- DRIVER 3 -->

        <div style="
        display:flex;
        justify-content:space-between;
        margin-bottom:14px;
        ">

        <span style="
        color:#CBD5E1;
        font-size:14px;
        font-weight:600;
        ">
        Workforce Health
        </span>

        <span style="
        color:#86EFAC;
        font-size:14px;
        font-weight:700;
        ">
        {health_index}/100
        </span>

        </div>

        <div style="
        width:100%;
        height:8px;
        background:rgba(255,255,255,0.06);
        border-radius:999px;
        overflow:hidden;
        ">

        <div style="
        width:{health_index}%;
        height:100%;
        background:linear-gradient(
        90deg,
        #22C55E,
        #84CC16
        );
        border-radius:999px;
        "></div>

        </div>

        </div>

        </div>
        """, unsafe_allow_html=True)

    # ======================================================
    # RIGHT — LIVE FORECAST RAIL
    # ======================================================

    with forecast_col2:

        st.markdown(f"""
        <div style="
        padding:22px 10px 0px 10px;
        ">

        <div style="
        font-size:13px;
        font-weight:700;
        letter-spacing:1.5px;
        text-transform:uppercase;
        color:#93C5FD;
        margin-bottom:34px;
        ">
        Stability Scenario Forecast
        </div>


        <!-- CURRENT -->

        <div style="
        margin-bottom:36px;
        ">

        <div style="
        display:flex;
        justify-content:space-between;
        margin-bottom:12px;
        ">
        <span style="
        color:#CBD5E1;
        font-size:16px;
        font-weight:600;
        ">
        Current Stability
        </span>

        <span style="
        color:white;
        font-size:24px;
        font-weight:800;
        ">
        {strategic_retention_score}%
        </span>
        </div>

        <div style="
        width:100%;
        height:14px;
        background:rgba(255,255,255,0.06);
        border-radius:999px;
        overflow:hidden;
        ">

        <div style="
        width:{strategic_retention_score}%;
        height:100%;
        background:linear-gradient(
        90deg,
        #64748B,
        #94A3B8
        );
        border-radius:999px;
        ">
        </div>

        </div>

        </div>


        <!-- PROJECTED -->

        <div style="
        margin-bottom:42px;
        ">

        <div style="
        display:flex;
        justify-content:space-between;
        margin-bottom:12px;
        ">
        <span style="
        color:#CBD5E1;
        font-size:16px;
        font-weight:600;
        ">
        Projected Stability
        </span>

        <span style="
        color:#22C55E;
        font-size:24px;
        font-weight:800;
        ">
        {projected_stability}%
        </span>
        </div>

        <div style="
        width:100%;
        height:14px;
        background:rgba(255,255,255,0.06);
        border-radius:999px;
        overflow:hidden;
        ">

        <div style="
        width:{projected_stability}%;
        height:100%;
        border-radius:999px;
        background:linear-gradient(
        90deg,
        #22C55E,
        #84CC16
        );
        box-shadow:0 0 18px rgba(34,197,94,0.30);
        ">
        </div>

        </div>

        </div>


        <!-- IMPACT SIGNAL -->

        <div style="
        border-left:2px solid rgba(34,197,94,0.35);
        padding-left:18px;
        ">

        <div style="
        font-size:13px;
        text-transform:uppercase;
        letter-spacing:1.3px;
        color:#86EFAC;
        font-weight:700;
        margin-bottom:12px;
        ">
        Forecasted Impact
        </div>

        <div style="
        font-size:48px;
        font-weight:800;
        color:white;
        line-height:1;
        margin-bottom:12px;
        ">
        +{forecast_improvement}%
        </div>

        <div style="
        font-size:15px;
        line-height:1.8;
        color:#CBD5E1;
        ">
        Estimated workforce stability improvement
        through targeted retention initiatives.
        </div>

        </div>

        <!-- EXECUTIVE SNAPSHOT -->

        <div style="
        margin-top:34px;
        padding:22px;
        border-radius:22px;
        background:rgba(255,255,255,0.03);
        border:1px solid rgba(255,255,255,0.05);
        ">

        <div style="
        font-size:13px;
        font-weight:700;
        letter-spacing:1.4px;
        text-transform:uppercase;
        color:#93C5FD;
        margin-bottom:18px;
        ">
        Executive Risk Snapshot
        </div>

        <div style="
        display:flex;
        flex-direction:column;
        gap:18px;
        ">

        <!-- Row 1 -->

        <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        ">

        <span style="
        color:#CBD5E1;
        font-size:15px;
        font-weight:500;
        ">
        Overtime Exposure
        </span>

        <span style="
        color:#FCA5A5;
        font-size:22px;
        font-weight:800;
        ">
        {overtime_percentage}%
        </span>

        </div>

        <!-- Row 2 -->

        <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        ">

        <span style="
        color:#CBD5E1;
        font-size:15px;
        font-weight:500;
        ">
        High Risk Employees
        </span>

        <span style="
        color:#C4B5FD;
        font-size:22px;
        font-weight:800;
        ">
        {high_risk_count}
        </span>

        </div>

        <!-- Row 3 -->

        <div style="
        display:flex;
        justify-content:space-between;
        align-items:center;
        ">

        <span style="
        color:#CBD5E1;
        font-size:15px;
        font-weight:500;
        ">
        Health Index
        </span>

        <span style="
        color:#86EFAC;
        font-size:22px;
        font-weight:800;
        ">
        {health_index}/100
        </span>

        </div>

        </div>

        </div>
        
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # =========================================================
    # AI EXECUTIVE NARRATIVE
    # =========================================================

    st.markdown("---")
    st.subheader("AI Executive Narrative")

    st.info(
    department_content["narrative"]
)
    # =========================================================
    # DEPARTMENT RISK RANKING
    # =========================================================

    st.markdown("---")
    st.subheader("Department Workforce Risk Ranking")

    ranking_df = get_department_risk_ranking(df)

    st.dataframe(
        ranking_df,
        use_container_width=True,
        hide_index=True
    )

    # =========================================================
    # EXECUTIVE DECISION SUPPORT
    # =========================================================

    st.markdown("---")
    st.subheader("Executive Decision Support")

    st.success(
    department_content["decision"]
)

    # =========================================================
    # EXECUTIVE IMPACT SIMULATION
    # =========================================================

    st.markdown("---")
    st.subheader("Executive Impact Simulation")

    impact_metrics = get_impact_simulation(
        projected_attrition_impact,
        optimization_gain
    )

    projected_savings = (
        impact_metrics["projected_savings"]
    )

    projected_retention_gain = (
        impact_metrics["projected_retention_gain"]
    )

    st.success(
        get_optimization_projection(
            selected_department,
            projected_retention_gain,
            projected_savings
        )
    )

    # =========================================================
    # WORKFORCE STRATEGY MATURITY
    # =========================================================

    st.markdown("---")
    st.subheader("Workforce Strategy Maturity")

    st.info(f"""
    ### {maturity_color} {maturity_level}

    The current workforce management environment reflects
    organizational maturity in managing:
    • Burnout exposure
    • Retention sustainability
    • Workforce engagement
    • Strategic workforce planning
    """)
    st.markdown("---")
    
    # ======================================================
    # FEATURE IMPORTANCE
    # ======================================================

    st.markdown("---")
    st.header("Attrition Driver Intelligence")

    importance_df = pd.DataFrame({

        'Feature': X.columns,

        'Importance': rf_model.feature_importances_

    })

    importance_df = importance_df.sort_values(
        by='Importance',
        ascending=False
    ).head(10)

    fig_ml = px.bar(
            importance_df,
            x='Importance',
            y='Feature',
            orientation='h',
            title='Top Workforce Attrition Drivers',
            color='Importance',
            color_continuous_scale='Blues'
        )

    fig_ml.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            title_font_size=22,
            height=600,
            yaxis=dict(categoryorder='total ascending')
        )

    st.plotly_chart(
            fig_ml,
            use_container_width=True
        )
    
    st.markdown("---")

    st.markdown("""
            <div style="
            height:1px;
            background: linear-gradient(
            90deg,
            rgba(239,68,68,0),
            rgba(239,68,68,0.9),
            rgba(239,68,68,0)
            );
            margin-top:35px;
            margin-bottom:35px;
            ">
            </div>
            """, unsafe_allow_html=True)

    # =========================================================
    # LIVE EMPLOYEE ATTRITION PREDICTION
    # =========================================================

    st.markdown("---")
    st.subheader("Live Employee Attrition Prediction")

    pred1, pred2 = st.columns(2)

    with pred1:

        age = st.slider(
            "Employee Age",
            18,
            60,
            30
        )

        monthly_income = st.slider(
            "Monthly Income",
            1000,
            20000,
            5000
        )

        years_company = st.slider(
            "Years At Company",
            0,
            40,
            5
         )

    with pred2:

        overtime = st.selectbox(
            "Overtime",
            ["Yes", "No"]
        )

        job_satisfaction = st.slider(
            "Job Satisfaction",
            1,
            4,
            2
        )

        worklife = st.slider(
            "Work-Life Balance",
            1,
            4,
            2
        )

    risk_probability = (
        calculate_live_attrition_risk(
            overtime,
            job_satisfaction,
            worklife,
            years_company,
            monthly_income
        )
    )

    prediction_risk = classify_risk(
        risk_probability
    )

    prediction_status = (
        prediction_risk["status"]
    )

    if prediction_risk["label"] == "Low Risk":

        st.success(
            f"{prediction_status}: {risk_probability}%"
        )

    elif prediction_risk["label"] == "Moderate Risk":

        st.warning(
            f"{prediction_status}: {risk_probability}%"
        )

    else:

        st.error(
            f"{prediction_status}: {risk_probability}%"
        )

    # =========================================================
    # FINAL EXECUTIVE SUMMARY
    # =========================================================

    st.markdown("---")
    st.subheader("Executive Strategic Summary")

    st.info(
        department_content["summary"]
    )

    # ============================================
    # FOOTER
    # ============================================

    st.markdown("---")

    st.markdown("""
    <div style='
    text-align:center;
    padding:20px;
    color:#94A3B8;
    font-size:14px;
    line-height:1.8;
    '>

    Workforce Intelligence Dashboard<br>

    Built with Streamlit • Predictive Analytics • Workforce Intelligence • HR Risk Modeling

    </div>
    """, unsafe_allow_html=True)