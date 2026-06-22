from datetime import datetime
import streamlit as st

from backend.insights_engine import (
    get_overview_executive_brief,
    get_overview_insights,
)

from backend.risk_engine import (
    classify_risk,
    classify_workforce_health,
    classify_overtime_risk,
    get_primary_driver
)

from backend.analytics import (
    get_overview_metrics,
    get_department_intelligence,
    get_department_overview_metrics
)

def render_overview(
    filtered_df,
    df,
    selected_department,
    model_accuracy
):
    """Render workforce overview dashboard."""

    # ======================================================
    # AI CARDS
    # ======================================================

    st.markdown("""
    <div style="
    display:flex;
    flex-direction:column;
    align-items:center;
    margin-top:10px;
    margin-bottom:36px;
    ">

    <div style="
    display:flex;
    justify-content:center;
    gap:14px;
    flex-wrap:wrap;
    ">

    <div style="
    background:rgba(59,130,246,0.12);
    border:1px solid rgba(59,130,246,0.20);
    padding:12px 20px;
    border-radius:999px;
    color:#93C5FD;
    font-weight:600;
    backdrop-filter:blur(12px);
    box-shadow:0 4px 18px rgba(59,130,246,0.10);
    ">
    🤖 AI Workforce Intelligence
    </div>

    <div style="
    background:rgba(16,185,129,0.12);
    border:1px solid rgba(16,185,129,0.20);
    padding:12px 20px;
    border-radius:999px;
    color:#6EE7B7;
    font-weight:600;
    backdrop-filter:blur(12px);
    box-shadow:0 4px 18px rgba(16,185,129,0.10);
    ">
    ⚡ Real-Time Risk Scoring
    </div>

    <div style="
    background:rgba(168,85,247,0.12);
    border:1px solid rgba(168,85,247,0.20);
    padding:12px 20px;
    border-radius:999px;
    color:#D8B4FE;
    font-weight:600;
    backdrop-filter:blur(12px);
    box-shadow:0 4px 18px rgba(168,85,247,0.10);
    ">
    📈 Predictive Analytics Engine
    </div>

    </div>

    <div style="
    margin-top:18px;
    font-size:14px;
    color:#94A3B8;
    text-align:center;
    line-height:1.8;
    max-width:720px;
    ">
    AI-powered workforce intelligence platform delivering
    predictive attrition analytics, workforce risk detection,
    and executive-level organizational insights in real time.
    </div>

    </div>
    """, unsafe_allow_html=True)

    # ======================================================
    # SYSTEM STATUS
    # ======================================================

    st.sidebar.markdown("""
    <div style='
    background:rgba(255,255,255,0.05);
    padding:18px;
    border-radius:16px;
    border:1px solid rgba(255,255,255,0.08);
    margin-top:18px;
    '>

    <h4 style='color:white;margin-bottom:12px;'>
    System Status
    </h4>

    <p style='
    color:#D1D5DB;
    line-height:1.8;
    font-size:14px;
    '>

    🟢 Real-Time Workforce Monitoring<br>
    🟢 Predictive Risk Scoring<br>
    🟢 Department Intelligence Active<br>
    🟢 Workforce Forecasting Enabled<br>
    🟢 Executive Decision Support Online

    </p>

    </div>
    """, unsafe_allow_html=True)

    # ============================================
    # EXECUTIVE STATUS BAR
    # ============================================

    st.markdown("""
    <div style="
    background: linear-gradient(
    90deg,
    rgba(37,99,235,0.15),
    rgba(59,130,246,0.05)
    );
    padding: 12px 18px;
    border-radius: 12px;
    margin-bottom: 20px;
    border: 1px solid rgba(59,130,246,0.2);
    ">

    <span style="color:#93C5FD;font-weight:600;">
    SYSTEM STATUS:
    </span>

    <span style="color:white;">
    Workforce Intelligence Systems Operational
    </span>

    </div>
    """, unsafe_allow_html=True)

    current_time = datetime.now().strftime(
        "%d %b %Y • %H:%M"
    )

    st.caption(
        f"Last Intelligence Refresh: {current_time}"
    )

    st.markdown("---")
    

    st.header("Workforce Overview")

    # =========================
    # KPI CALCULATIONS
    # =========================

    overview_metrics = (
        get_overview_metrics(
            filtered_df
        )
    )

    total_employees = (
        overview_metrics[
            "total_employees"
        ]
    )

    attrition_rate = (
        overview_metrics[
            "attrition_rate"
        ]
    )

    high_risk_employees = (
        overview_metrics[
            "high_risk_employees"
        ]
    )

    overtime_percentage = (
        overview_metrics[
            "overtime_percentage"
        ]
    )

    retention_percent = (
        overview_metrics[
            "retention_percent"
        ]
    )

    engagement_score = (
        overview_metrics[
            "engagement_score"
        ]
    )

    risk_data = classify_risk(
        attrition_rate
    )

    risk_status = (
        risk_data["status"]
    )

    overview_title, attention_area = (
        get_overview_executive_brief(
            risk_data["label"]
        )
    )

    st.markdown(f"""
    <div style='
    background: linear-gradient(135deg, rgba(15,23,42,0.95), rgba(30,41,59,0.88));
    border:1px solid rgba(255,255,255,0.08);
    border-radius:32px;
    padding:28px 34px;
    margin-top:18px;
    margin-bottom:28px;
    backdrop-filter: blur(18px);
    box-shadow:0 14px 35px rgba(0,0,0,0.24), inset 0 1px 0 rgba(255,255,255,0.04);
    '>

    <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom:20px;'>

    <div>

    <div style='
    font-size:13px;
    letter-spacing:1.5px;
    color:#60A5FA;
    font-weight:700;
    text-transform:uppercase;
    margin-bottom:6px;
    '>
    EXECUTIVE INTELLIGENCE BRIEF
    </div>

    <div style='
    font-size:28px;
    font-weight:750;
    color:white;
    letter-spacing:-1px;
    '>
    Organizational Workforce Snapshot
    </div>

    </div>

    <div style='
    padding:10px 18px;
    border-radius:999px;
    background:rgba(16,185,129,0.12);
    border:1px solid rgba(16,185,129,0.18);
    color:#6EE7B7;
    font-weight:600;
    font-size:14px;
    '>
    ● Live Analysis Active
    </div>

    </div>

    <div style='
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:18px;
    '>

    <div>
    <div style='color:#64748B;font-size:13px;'>
    Primary Workforce Risk
    </div>

    <div style='font-size:22px;font-weight:700;color:white;margin-top:8px;'>
    {overview_title}
    </div>
    </div>

    <div>
    <div style='color:#64748B;font-size:13px;'>
    Highest Attention Area
    </div>

    <div style='font-size:22px;font-weight:700;color:white;margin-top:8px;'>
    {attention_area}
    </div>
    </div>

    <div>
    <div style='color:#64748B;font-size:13px;'>
    ML Workforce Confidence
    </div>

    <div style='font-size:22px;font-weight:700;color:white;margin-top:8px;'>
    {model_accuracy * 100:.1f}% Prediction Confidence
    </div>
    </div>

    </div>

    </div>
    """, unsafe_allow_html=True)

       # =========================
    # KPI DISPLAY
    # =========================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Employees",
        total_employees
    )

    col2.metric(
        "Attrition Rate",
        f"{attrition_rate}%"
    )

    col3.metric(
        "High-Risk Employees",
        high_risk_employees
    )

    col4.metric(
        "ML Prediction Accuracy",
        f"{model_accuracy * 100:.1f}%"
    )

    # =========================
    # ORGANIZATIONAL RISK STATUS
    # =========================

    st.subheader("Organizational Risk Status")


    st.info(f"Current Organizational Risk Level: {risk_status}")

    # =========================
    # KEY BUSINESS INSIGHTS
    # =========================

    st.subheader("Key Workforce Insights")

    department_data = (
        get_department_intelligence(
            df
        )
    )

    highest_attrition_dept = (
        department_data[
            "highest_attrition_dept"
        ]
    )

    stable_dept = (
        department_data[
            "stable_dept"
        ]
    )

    department_attrition = (
        attrition_rate
    )   

    st.markdown(
            get_overview_insights(
                selected_department,
                highest_attrition_dept,
                stable_dept,
                department_attrition,
                overtime_percentage
            )
        )
        
    st.markdown("---")

    # =========================
    # VISUAL ANALYTICS
    # =========================

    st.subheader("Workforce Analytics Overview")

    chart1, chart2 = st.columns(2)

    # =========================
    # ATTRITION OVERVIEW CHART
    # =========================

    with chart1:

        retention_percent = round(
            100 - attrition_rate,
            1
        )

        health_data = classify_workforce_health(
            retention_percent
        )

        health_color = health_data["color"]
        health_label = health_data["label"]

        engagement_score = round(
            (
                (100 - attrition_rate) +
                (100 - overtime_percentage)
            ) / 2,
            1
        )

        driver_data = get_primary_driver(
            attrition_rate,
            overtime_percentage,
            engagement_score
        )

        primary_driver = driver_data["driver"]
        driver_score = driver_data["score"]

        driver_score = round(
            overtime_percentage
            if overtime_percentage > 30
            else engagement_score
        )

        chart_html = rf"""
        <div style="
        padding-right:28px;
        border-right:1px solid rgba(255,255,255,0.08);
        min-height:860px;
        display:flex;
        flex-direction:column;
        ">

            <!-- TITLE -->
            <div style="
            color:white;
            font-size:34px;
            font-weight:800;
            margin-bottom:12px;
            ">
            Workforce Health Intelligence
            </div>

            <div style="
            color:#94A3B8;
            font-size:15px;
            margin-bottom:44px;
            ">
            Executive workforce sustainability snapshot
            </div>


            <!-- WORKFORCE HEALTH -->
            <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin-bottom:20px;
            ">

                <div style="
                display:flex;
                align-items:center;
                gap:20px;
                ">

                    <div style="
                    width:92px;
                    height:92px;
                    border-radius:50%;
                    border:2px solid rgba(96,165,250,0.55);
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    font-size:42px;
                    color:#60A5FA;
                    ">
                    ◉
                    </div>

                    <div>
                        <div style="
                        color:white;
                        font-size:22px;
                        font-weight:800;
                        margin-bottom:4px;
                        ">
                        Workforce Health
                        </div>

                        <div style="
                        color:#A5B4FC;
                        font-size:16px;
                        ">
                        {health_label}
                        </div>
                    </div>
                </div>

                <div style="text-align:right;">
                    <div style="
                    color:#60A5FA;
                    font-size:64px;
                    font-weight:900;
                    line-height:1;
                    ">
                    {retention_percent}%
                    </div>

                    <div style="
                    color:#CBD5E1;
                    font-size:14px;
                    ">
                    score
                    </div>
                </div>
            </div>

            <div style="
            width:100%;
            height:12px;
            background:rgba(255,255,255,0.10);
            border-radius:999px;
            overflow:hidden;
            margin-bottom:38px;
            ">
                <div style="
                width:{retention_percent}%;
                height:100%;
                background:#60A5FA;
                border-radius:999px;
                ">
                </div>
            </div>

            <div style="
            border-top:1px solid rgba(255,255,255,0.08);
            margin-bottom:38px;
            ">
            </div>


            <!-- ATTRITION -->
            <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin-bottom:20px;
            ">

                <div style="
                display:flex;
                align-items:center;
                gap:20px;
                ">

                    <div style="
                    width:92px;
                    height:92px;
                    border-radius:50%;
                    border:2px solid rgba(248,113,113,0.50);
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    font-size:42px;
                    color:#F87171;
                    ">
                    ◈
                    </div>

                    <div>
                        <div style="
                        color:white;
                        font-size:22px;
                        font-weight:800;
                        margin-bottom:4px;
                        ">
                        Attrition Risk
                        </div>

                        <div style="
                        color:#CBD5E1;
                        font-size:16px;
                        ">
                        Organizational Risk
                        </div>
                    </div>
                </div>

                <div style="text-align:right;">
                    <div style="
                    color:#F87171;
                    font-size:56px;
                    font-weight:900;
                    line-height:1;
                    ">
                    {attrition_rate}%
                    </div>

                    <div style="
                    color:#CBD5E1;
                    font-size:14px;
                    ">
                    risk
                    </div>
                </div>
            </div>

            <div style="
            width:100%;
            height:12px;
            background:rgba(255,255,255,0.10);
            border-radius:999px;
            overflow:hidden;
            margin-bottom:38px;
            ">
                <div style="
                width:{attrition_rate}%;
                height:100%;
                background:#F87171;
                border-radius:999px;
                ">
                </div>
            </div>

            <div style="
            border-top:1px solid rgba(255,255,255,0.08);
            margin-bottom:38px;
            ">
            </div>


            <!-- DRIVER -->
            <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin-bottom:20px;
            ">

                <div style="
                display:flex;
                align-items:center;
                gap:20px;
                ">

                    <div style="
                    width:92px;
                    height:92px;
                    border-radius:50%;
                    border:2px solid rgba(251,146,60,0.55);
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    font-size:42px;
                    color:#FB923C;
                    ">
                    ⚡
                    </div>

                    <div>
                        <div style="
                        color:white;
                        font-size:22px;
                        font-weight:800;
                        margin-bottom:4px;
                        ">
                        Primary Workforce Driver
                        </div>

                        <div style="
                        color:#CBD5E1;
                        font-size:16px;
                        ">
                        {primary_driver}
                        </div>
                    </div>
                </div>

                <div style="text-align:right;">
                    <div style="
                    color:#FB923C;
                    font-size:56px;
                    font-weight:900;
                    line-height:1;
                    ">
                    {driver_score}%
                    </div>

                    <div style="
                    color:#CBD5E1;
                    font-size:14px;
                    ">
                    influence
                    </div>
                </div>

            </div>

            <div style="
            width:100%;
            height:12px;
            background:rgba(255,255,255,0.10);
            border-radius:999px;
            overflow:hidden;
            margin-bottom:38px;
            ">
                <div style="
                width:{driver_score}%;
                height:100%;
                background:#FB923C;
                border-radius:999px;
                ">
                </div>
            </div>

            <div style="
            border-top:1px solid rgba(255,255,255,0.08);
            margin-bottom:38px;
            ">
            </div>


            <!-- OUTLOOK -->
            <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            ">

                <div style="
                display:flex;
                align-items:center;
                gap:20px;
                ">

                <div style="
                width:92px;
                min-width:92px;
                max-width:92px;
                height:92px;
                min-height:92px;
                border-radius:50%;
                border:2px solid {health_color}55;
                display:flex;
                justify-content:center;
                align-items:center;
                font-size:42px;
                color:{health_color};
                flex-shrink:0;
                aspect-ratio:1/1;
                box-sizing:border-box;
                ">
                ↗
                </div>

                    <div>
                        <div style="
                        color:white;
                        font-size:22px;
                        font-weight:800;
                        margin-bottom:4px;
                        ">
                        Stability Outlook
                        </div>

                        <div style="
                        color:#CBD5E1;
                        font-size:16px;
                        ">
                        Long-Term Workforce
                        </div>
                    </div>
                </div>

                <div style="text-align:right;">
                    <div style="
                    color:{health_color};
                    font-size:56px;
                    font-weight:900;
                    line-height:1;
                    ">
                    {health_label}
                    </div>

                    <div style="
                    color:#CBD5E1;
                    font-size:14px;
                    ">
                    outlook
                    </div>
                </div>
            </div>

        </div>
        """

        st.html(chart_html)

    # ============================
    # DEPARTMENT RISK BREAKDOWN
    # ============================

    with chart2:

    # ==================================
    # DYNAMIC DEPARTMENT ANALYTICS
    # ==================================

        department_metrics = (
            get_department_overview_metrics(
                filtered_df,
                selected_department
            )
        )

        dept_attrition = (
            department_metrics[
                "dept_attrition"
            ]
        )

        dept_retention = (
            department_metrics[
                "dept_retention"
            ]
        )

        dept_overtime = (
            department_metrics[
                "dept_overtime"
            ]
        )

        dept_engagement = (
            department_metrics[
                "dept_engagement"
            ]
        )

        overtime_data = classify_overtime_risk(
            dept_overtime
        )

        overtime_level = overtime_data["label"]
        

        selected = {
            "burnout": dept_overtime,
            "retention": dept_retention,
            "engagement": dept_engagement,
            "overtime": overtime_level
        }

        chart2_html = f"""
        <div style="
        padding-left:48px;
        border-left:1px solid rgba(255,255,255,0.08);
        min-height:860px;   
        display:flex;
        flex-direction:column;
        box-sizing:border-box;
        ">

            <!-- TITLE -->
            <div style="
            color:white;
            font-size:34px;
            font-weight:800;
            margin-bottom:12px;
            ">
            Workforce Instability Distribution
            </div>

            <div style="
            color:#94A3B8;
            font-size:15px;
            margin-bottom:44px;
            ">
            Department instability analysis
            </div>
        """

        metrics = [
            (
                "◎",
                "#F87171",
                "Overtime Burnout",
                selected_department,
                selected['burnout'],
                "risk",
                True
            ),
            (
                "◈",
                "#60A5FA",
                "Retention Strength",
                "Stability score",
                selected['retention'],
                "retained",
                True
            ),
            (
                "◉",
                "#A7F3D0",
                "Engagement Index",
                "Workforce sentiment",
                selected['engagement'],
                "engagement",
                True
            ),
            (
                "◌",
                overtime_data["color"],
                "Overtime Exposure",
                "Department pressure level",
                selected['overtime'],
                "",
                False
            )
        ]

        for idx, (
            icon,
            color,
            title,
            subtitle,
            value,
            label,
            show_bar
        ) in enumerate(metrics):

            chart2_html += f"""
            <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
            margin-bottom:20px;
            ">

                <div style="
                display:flex;
                align-items:center;
                gap:20px;
                ">

                    <div style="
                    width:92px;
                    height:92px;
                    border-radius:50%;
                    border:2px solid {color}55;
                    display:flex;
                    justify-content:center;
                    align-items:center;
                    font-size:42px;
                    color:{color};
                    ">
                    {icon}
                    </div>

                    <div>
                        <div style="
                        color:white;
                        font-size:22px;
                        font-weight:800;
                        margin-bottom:4px;
                        ">
                        {title}
                        </div>

                        <div style="
                        color:#CBD5E1;
                        font-size:16px;
                        ">
                        {subtitle}
                        </div>
                    </div>
                </div>

                    <div style="
                    text-align:right;
                    min-width:255px;
                    width:255px;
                    flex-shrink:0;
                    ">

                        <div style="
                        color:{color};
                        font-size:58px;
                        font-weight:900;
                        line-height:1;
                        letter-spacing:-1px;
                        ">
                        {value if title == "Overtime Exposure" else f"{value}%"}
                        </div>

                        <div style="
                        color:#CBD5E1;
                        font-size:14px;
                        margin-top:6px;
                        ">
                        {label}
                        </div>

                    </div>

            </div>
            """

            # MATCH CHART 1 PROGRESS BARS
            if show_bar:

                # numeric width for progress bar
                if title == "Overtime Exposure":
                    bar_width = dept_overtime
                else:
                    bar_width = value

                chart2_html += f"""
                <div style="
                width:100%;
                height:12px;
                background:rgba(255,255,255,0.10);
                border-radius:999px;
                overflow:hidden;
                margin-bottom:38px;
                ">
                    <div style="
                    width:{bar_width}%;
                    height:100%;
                    background:{color};
                    border-radius:999px;
                    ">
                    </div>
                </div>
                """

            # DON'T SHOW DIVIDER AFTER LAST ROW
            if idx < len(metrics) - 1:
                chart2_html += """
                <div style="
                border-top:1px solid rgba(255,255,255,0.08);
                margin-bottom:38px;
                ">
                </div>
                """

        chart2_html += "</div>"

        st.html(chart2_html)

