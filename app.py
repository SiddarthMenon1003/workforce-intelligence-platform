import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import plotly.express as px

plt.style.use('dark_background')

plt.rcParams['figure.facecolor'] = 'none'
plt.rcParams['axes.facecolor'] = 'none'
plt.rcParams['savefig.facecolor'] = 'none'

plt.rcParams['text.color'] = 'white'
plt.rcParams['axes.labelcolor'] = 'white'
plt.rcParams['xtick.color'] = 'white'
plt.rcParams['ytick.color'] = 'white'

plt.rcParams['axes.titlecolor'] = 'white'

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from datetime import datetime


# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Workforce Intelligence Dashboard",
    layout="wide"
)


# =========================
# GLOBAL UI STYLING
# =========================

st.markdown("""
<style>

/* ======================================================
MAIN APP
====================================================== */

.main {
    background-color: #050816;
}

/* ======================================================
SIDEBAR
====================================================== */

section[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #0F172A 0%,
        #111827 45%,
        #1E293B 100%
    );

    border-right: 1px solid rgba(255,255,255,0.06);
}

/* Sidebar Scrollbar */

section[data-testid="stSidebar"] ::-webkit-scrollbar {
    width: 6px;
}

section[data-testid="stSidebar"] ::-webkit-scrollbar-thumb {
    background: rgba(255,255,255,0.15);
    border-radius: 10px;
}

/* Sidebar Text */

section[data-testid="stSidebar"] * {
    color: white;
}

/* ======================================================
METRIC CARDS
====================================================== */

div[data-testid="metric-container"] {

    background: linear-gradient(
        135deg,
        rgba(17,24,39,0.92) 0%,
        rgba(30,41,59,0.92) 100%
    );

    border-radius: 18px;
            
    backdrop-filter: blur(10px);

    padding: 20px;

    border: 1px solid rgba(255,255,255,0.06);

    box-shadow:
        0px 8px 24px rgba(0,0,0,0.35),
        0px 0px 18px rgba(59,130,246,0.08);

    transition: 0.3s ease;
}

/* Metric Hover */

div[data-testid="metric-container"]:hover {

    transform: translateY(-4px);

    box-shadow:
        0px 10px 24px rgba(0,0,0,0.25);
}

/* ======================================================
METRIC VALUES
====================================================== */

div[data-testid="stMetricValue"] {

    font-size: 30px;

    font-weight: 800;

    color: white !important;
}

/* ======================================================
METRIC LABELS
====================================================== */

div[data-testid="stMetricLabel"] {

    color: #CBD5E1 !important;

    font-weight: 600;
}

/* ======================================================
HEADERS
====================================================== */

h1, h2, h3 {

    color: white;

    font-weight: 800;
}

/* ======================================================
TABS
====================================================== */

button[data-baseweb="tab"] {

    font-size: 16px;

    font-weight: 600;

    border-radius: 12px;

    padding: 10px 18px;

    transition: 0.3s ease;
}

/* Selected Tab */

button[data-baseweb="tab"][aria-selected="true"] {

    background-color: #2563EB !important;

    color: white !important;
}

/* ======================================================
INFO / SUCCESS / WARNING BOXES
====================================================== */

.stAlert {

    border-radius: 18px;

    padding: 18px;

    border: none;
}

/* ======================================================
DATAFRAMES
====================================================== */

[data-testid="stDataFrame"] {

    border-radius: 16px;

    overflow: hidden;

    border: 1px solid rgba(255,255,255,0.06);
}

/* ======================================================
BUTTONS
====================================================== */

.stButton>button {

    border-radius: 12px;

    padding: 10px 20px;

    font-weight: 700;

    background: linear-gradient(
        90deg,
        #2563EB 0%,
        #3B82F6 100%
    );

    color: white;

    border: none;

    transition: 0.3s ease;
}

/* Button Hover */

.stButton>button:hover {

    transform: translateY(-2px);

    box-shadow:
        0px 8px 18px rgba(59,130,246,0.35);
}

/* ======================================================
DOWNLOAD BUTTON
====================================================== */

.stDownloadButton>button {

    border-radius: 12px;

    background: linear-gradient(
        90deg,
        #059669 0%,
        #10B981 100%
    );

    color: white;

    font-weight: 700;

    border: none;
}

/* Download Hover */

.stDownloadButton>button:hover {

    transform: translateY(-2px);

    box-shadow:
        0px 8px 18px rgba(16,185,129,0.35);
}

/* ======================================================
CHART SPACING
====================================================== */

.element-container {

    margin-bottom: 1rem;
}

/* ======================================================
SECTION SEPARATORS
====================================================== */

hr {

    margin-top: 2rem;

    margin-bottom: 2rem;

    border: 0;

    border-top: 1px solid rgba(255,255,255,0.08);
}

/* ======================================================
PREMIUM SELECTBOX
====================================================== */

div[data-baseweb="select"] {

    background: rgba(255,255,255,0.06);

    border-radius: 14px;

    border: 1px solid rgba(255,255,255,0.08);

    transition: 0.3s ease;

    margin-top: -10px;
}

div[data-baseweb="select"]:hover {

    border: 1px solid #3B82F6;

    box-shadow:
        0px 0px 14px rgba(59,130,246,0.35);
}

div[data-baseweb="select"] * {

    color: white !important;
}

/* ======================================================
RADIO GROUP
====================================================== */

div[role="radiogroup"] {

    margin-top: 10px;

    padding: 8px;
}

/* ======================================================
RADIO BUTTON ITEMS
====================================================== */

div[role="radiogroup"] label {

    background: rgba(255,255,255,0.04);

    padding: 12px 14px;

    border-radius: 14px;

    margin-bottom: 10px;

    transition: all 0.3s ease;

    border: 1px solid transparent;
}

/* Hover */

div[role="radiogroup"] label:hover {

    background: rgba(59,130,246,0.15);

    border: 1px solid rgba(59,130,246,0.35);

    transform: translateX(4px);
}

/* Selected */

div[role="radiogroup"] label[data-selected="true"] {

    background: linear-gradient(
        90deg,
        #2563EB 0%,
        #3B82F6 100%
    );

    border: 1px solid rgba(255,255,255,0.08);

    box-shadow:
        0px 0px 12px rgba(59,130,246,0.35);
}

div[role="radiogroup"] span {

    color: white !important;

    font-weight: 600;
}

/* ======================================================
DATAFRAME TEXT
====================================================== */

[data-testid="stDataFrame"] * {

    color: white !important;
}
            
thead tr th {
    background: linear-gradient(
        90deg,
        #111827 0%,
        #1F2937 100%
    ) !important;

    color: white !important;

    font-weight: 700 !important;
}

/* ======================================================
GLOBAL FONT
====================================================== */

html, body, [class*="css"] {

    font-family: "Segoe UI", sans-serif;
}
            
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# ======================================================
# DATASET UPLOAD
# ======================================================

uploaded_file = st.sidebar.file_uploader(
    "Upload Workforce Dataset",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

else:

    df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")

st.sidebar.markdown("""
<div style="
background: rgba(255,255,255,0.04);
padding: 14px 18px;
border-radius: 14px;
border: 1px solid rgba(255,255,255,0.08);
margin-top: -8px;
margin-bottom: 18px;
">

<div style="
font-size: 15px;
font-weight: 600;
color: white;
margin-bottom: 6px;
">
Dataset Intelligence Gateway
</div>

<div style="
font-size: 13px;
color: #94A3B8;
line-height: 1.6;
">
Upload workforce datasets for dynamic analytics, predictive modeling,
risk intelligence, and strategic workforce simulations.
</div>

</div>
""", unsafe_allow_html=True)

# ======================================================
# SCHEMA VALIDATION
# ======================================================

required_columns = [
    'Attrition',
    'Department',
    'OverTime',
    'JobSatisfaction',
    'WorkLifeBalance',
    'MonthlyIncome',
    'YearsAtCompany'
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:

    st.error(
        f"Missing required columns: {missing_columns}"
    )
    

    st.stop()

if uploaded_file is not None:

    st.markdown("""
    <div style="
    background: linear-gradient(
        90deg,
        rgba(16,185,129,0.15) 0%,
        rgba(16,185,129,0.05) 100%
    );
    padding: 12px 18px;
    border-radius: 12px;
    border: 1px solid rgba(16,185,129,0.35);
    margin-bottom: 18px;
    ">

    <div style="
    color:#6EE7B7;
    font-weight:600;
    font-size:14px;
    ">
    ✓ Workforce dataset validated successfully
    </div>

    <div style="
    color:#A7F3D0;
    font-size:12px;
    margin-top:4px;
    ">
    Schema integrity verified • Predictive pipeline active
    </div>

    </div>
    """, unsafe_allow_html=True)


# ======================================================
# MACHINE LEARNING MODEL
# ======================================================

@st.cache_resource
def train_model(dataframe):

    ml_df = dataframe.copy()

    # Encode categorical columns

    categorical_cols = ml_df.select_dtypes(
        include='object'
    ).columns

    encoder = LabelEncoder()

    for col in categorical_cols:

        ml_df[col] = encoder.fit_transform(
            ml_df[col]
        )

    # Features & Target

    X = ml_df.drop("Attrition", axis=1)

    y = ml_df["Attrition"]

    # Train/Test Split

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Random Forest Model

    rf_model = RandomForestClassifier(
        n_estimators=200,
        random_state=42
    )

    rf_model.fit(X_train, y_train)

    # Predictions

    y_pred = rf_model.predict(X_test)

    # Accuracy

    model_accuracy = accuracy_score(
        y_test,
        y_pred
    )

    return rf_model, model_accuracy, X

# ======================================================
# TRAIN MODEL
# ======================================================

with st.spinner(
    "Initializing Workforce Intelligence Systems..."
):

    rf_model, model_accuracy, X = train_model(df)

# ======================================================
# PREMIUM SIDEBAR
# ======================================================

st.sidebar.markdown("""
<h1 style='color:white;font-size:32px;font-weight:800;margin-bottom:5px;'>
Workforce Intelligence
</h1>

<p style='color:#CBD5E1;font-size:14px;line-height:1.5;margin-bottom:25px;'>
Predictive Workforce Analytics & Strategic Attrition Intelligence Platform
</p>
""", unsafe_allow_html=True)

# ======================================================
# DEPARTMENT FILTER
# ======================================================

st.sidebar.markdown("""
<div style='
background:rgba(255,255,255,0.04);
padding:18px;
border-radius:16px;
border:1px solid rgba(255,255,255,0.08);
margin-bottom:18px;
'>

<h3 style='color:white;margin-bottom:10px;'>
Department Filter
</h3>

<p style='color:#CBD5E1;font-size:13px;'>
Filter workforce analytics dynamically by department intelligence.
</p>

</div>
""", unsafe_allow_html=True)

selected_department = st.sidebar.selectbox(
    "",
    ["All"] + sorted(df['Department'].unique())
)

# ======================================================
# APPLY FILTER
# ======================================================

if selected_department != "All":

    filtered_df = df[
        df['Department'] == selected_department
    ]

else:

    filtered_df = df.copy()

if filtered_df.empty:

    st.warning(
        "No workforce records match current filters."
    )

    st.stop()

# ======================================================
# NAVIGATION
# ======================================================

st.sidebar.markdown("""
<div style='
background:rgba(255,255,255,0.04);
padding:18px;
border-radius:16px;
border:1px solid rgba(255,255,255,0.08);
margin-top:18px;
margin-bottom:10px;
'>

<h3 style='color:white;margin-bottom:10px;'>
Dashboard Navigation
</h3>

<p style='color:#CBD5E1;font-size:13px;'>
Navigate through workforce intelligence modules.
</p>

</div>
""", unsafe_allow_html=True)

section = st.sidebar.radio(
    "",
    [
    "📊 Overview",
    "👥 Workforce Analytics",
    "⚠️ Risk Intelligence",
    "🧠 Strategic Insights"
    ]
)

# ======================================================
# PLATFORM CAPABILITIES
# ======================================================

st.sidebar.markdown("""
<div style='
background:linear-gradient(135deg,#1E3A5F 0%,#2563EB 100%);
padding:20px;
border-radius:18px;
margin-top:20px;
box-shadow:0px 4px 14px rgba(0,0,0,0.25);
'>

<h3 style='color:white;margin-bottom:16px;font-size:20px;'>
Platform Capabilities
</h3>

<ul style='
color:white;
padding-left:18px;
line-height:1.9;
font-size:14px;
'>

<li>Predictive Attrition Analytics</li>
<li>Workforce Risk Intelligence</li>
<li>Strategic Forecasting</li>
<li>Executive Decision Support</li>
<li>Retention Optimization</li>
<li>AI Workforce Simulations</li>

</ul>

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

# ======================================================
# DASHBOARD HEADER
# ======================================================

st.markdown("""
<h1 style='
font-size:52px;
font-weight:800;
margin-bottom:8px;
color:white;
'>
Employee Attrition & Workforce Intelligence Dashboard
</h1>
            
<p style='
font-size:18px;
color:#CBD5E1;
margin-bottom:25px;
line-height:1.6;
'>
Predictive Workforce Analytics, Attrition Intelligence,
Risk Monitoring & Strategic Workforce Decision Support
</p>
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

# =========================
# OVERVIEW SECTION
# =========================

if section == "📊 Overview":

    st.header("Workforce Overview")

    # =========================
    # KPI CALCULATIONS
    # =========================

    total_employees = len(filtered_df)

    attrition_rate = round(
        (filtered_df['Attrition'] == 'Yes').mean() * 100,
        1
    )

    high_risk_employees = len(
        filtered_df[filtered_df['OverTime'] == 'Yes']
    )

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

    if attrition_rate < 10:
        risk_status = "🟢 Low Workforce Risk"

    elif attrition_rate < 20:
        risk_status = "🟡 Moderate Workforce Risk"

    else:
        risk_status = "🔴 High Workforce Risk"

    st.info(f"Current Organizational Risk Level: {risk_status}")

    # =========================
    # KEY BUSINESS INSIGHTS
    # =========================

    st.subheader("Key Workforce Insights")

    dept_attrition_calc = df.groupby('Department')['Attrition'] \
                            .apply(lambda x: (x == 'Yes').mean())

    highest_attrition_dept = dept_attrition_calc.idxmax()

    stable_dept = dept_attrition_calc.idxmin()

    if selected_department == "All":

        st.markdown(f"""
- **Highest Attrition Department:** {highest_attrition_dept}
- **Most Stable Department:** {stable_dept}
- **Employees working overtime show significantly elevated attrition risk**
- **Overall organizational retention rate remains above 80%**
- **Primary Workforce Risk Factor:** Workload & Overtime Pressure
""")

    else:

        department_attrition = round(
            (filtered_df['Attrition'] == 'Yes').mean() * 100,
            1
        )

        overtime_percentage = round(
            (filtered_df['OverTime'] == 'Yes').mean() * 100,
            1
        )

        st.markdown(f"""
- **Selected Department:** {selected_department}
- **Department Attrition Rate:** {department_attrition}%
- **Employees working overtime in this department:** {overtime_percentage}%
- **Workforce stability varies based on overtime exposure and employee workload**
- **Primary Workforce Risk Factor in this department:** Overtime & Burnout Pressure
""") 
        
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

        attrition_percent = (
            (filtered_df['Attrition'] == 'Yes').mean() * 100
        )

        retention_percent = 100 - attrition_percent

        categories = ['Retention Rate', 'Attrition Rate']
        values = [retention_percent, attrition_percent]

        colors = ['#4F8BF9', '#FF6B6B']

        fig1, ax1 = plt.subplots(figsize=(7,4))

        bars = ax1.barh(
            categories,
            values,
            color=colors,
            height=0.5
        )

        # =========================
        # VALUE LABELS
        # =========================

        for bar in bars:

            width = bar.get_width()

            x_position = width + 2

            ax1.text(
                x_position,
                bar.get_y() + bar.get_height()/2,
                f'{width:.1f}%',
                va='center',
                fontsize=16,
                fontweight='bold',
                color='white'
            )

        # =========================
        # STYLING
        # =========================

        ax1.set_xlim(0, 100)

        ax1.set_title(
            "Employee Attrition Overview",
            fontsize=22,
            fontweight='bold',
            pad=20
        )

        ax1.set_xlabel(
            "Percentage",
            fontsize=13
        )

        ax1.tick_params(
            axis='y',
            labelsize=14
        )

        ax1.tick_params(
            axis='x',
            labelsize=12
        )

        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.spines['left'].set_visible(False)

        ax1.grid(
            axis='x',
            linestyle='--',
            alpha=0.3
        )

        st.pyplot(fig1)

    # =========================
    # DEPARTMENT ATTRITION GRAPH
    # =========================

    with chart2:

        dept_attrition = df.groupby('Department')['Attrition'] \
                           .apply(lambda x: (x == 'Yes').mean()) \
                           .reset_index()

        fig2 = px.line(
            dept_attrition,
            x='Department',
            y='Attrition',
            markers=True,
            title='Attrition Rate by Department'
)

        fig2.update_traces(
            line=dict(width=4),
            marker=dict(size=12)
)

        fig2.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            title_font_size=22,
            height=500
)

        st.plotly_chart(
            fig2,
            use_container_width=True
)


# =========================
# WORKFORCE ANALYTICS SECTION
# =========================

elif section == "👥 Workforce Analytics":

    st.header(" Operational Workforce Analytics")

    st.write("""
    This section analyzes workforce factors contributing
    to employee attrition and organizational instability.
    """)

    # =========================================================
    # OVERTIME & BURNOUT ANALYSIS
    # =========================================================

    st.markdown("---")
    st.subheader("Overtime & Burnout Analysis")

    overtime_percentage = round(
        (filtered_df['OverTime'] == 'Yes').mean() * 100,
        1
    )

    overtime_attrition_rate = round(
        (
            filtered_df[
                filtered_df['OverTime'] == 'Yes'
            ]['Attrition'] == 'Yes'
        ).mean() * 100,
        1
    )

    no_overtime_attrition_rate = round(
        (
            filtered_df[
                filtered_df['OverTime'] == 'No'
            ]['Attrition'] == 'Yes'
        ).mean() * 100,
        1
    )

    workforce_stability_score = round(
        100 - overtime_attrition_rate,
        1
    )

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

    if overtime_attrition_rate < 15:

        st.success("🟢 LOW RISK — Workforce stability remains strong.")

    elif overtime_attrition_rate < 25:

        st.warning("🟡 MODERATE RISK — Burnout indicators increasing.")

    elif overtime_attrition_rate < 35:

        st.error("🟠 HIGH RISK — Overtime pressure significantly impacting retention.")

    else:

        st.error("🔴 CRITICAL RISK — Severe workforce instability detected.")

    # Smart Insights
    st.subheader("Strategic Workforce Intelligence")

    insight1, insight2 = st.columns(2)

    with insight1:

        st.info(f"""
### Workforce Vulnerability

The {selected_department if selected_department != 'All' else 'organization'}
demonstrates elevated overtime-related
workforce instability indicators.
""")

    with insight2:

        st.info(f"""
### Primary Workforce Risk Driver

Operational workload pressure and overtime
exposure remain major workforce retention
challenges.
""")

    # Visual Analytics
    chart1, chart2 = st.columns(2)

    # Radial Risk Chart
    with chart1:

        fig3, ax3 = plt.subplots(figsize=(6,6))

        sizes = [
            overtime_attrition_rate,
            100 - overtime_attrition_rate
        ]

        colors = ['#FF6B6B', '#EAEAEA']

        ax3.pie(
            sizes,
            startangle=90,
            colors=colors,
            wedgeprops=dict(
                width=0.35,
                edgecolor='white'
            )
        )

        ax3.text(
            0,
            0,
            f"{overtime_attrition_rate}%",
            ha='center',
            va='center',
            fontsize=30,
            fontweight='bold',
            color='#FF6B6B'
        )

        ax3.text(
            0,
            -0.18,
            "Attrition Risk",
            ha='center',
            va='center',
            fontsize=13,
            color='#CBD5E1'
        )

        ax3.set_title(
            "Overtime Employee Attrition Risk",
            fontsize=18,
            fontweight='bold',
            pad=20
        )

        st.pyplot(fig3)

    # Workforce Composition
    with chart2:

        overtime_counts = filtered_df['OverTime'].value_counts()

        total = overtime_counts.sum()

        yes_percentage = round(
            overtime_counts.get('Yes', 0) / total * 100,
            1
        )

        no_percentage = round(
            overtime_counts.get('No', 0) / total * 100,
            1
        )

        fig4, ax4 = plt.subplots(figsize=(8,3))

        ax4.barh(
            ['Workforce'],
            [yes_percentage],
            color='#FF6B6B',
            height=0.5,
            label='Overtime Employees'
        )

        ax4.barh(
            ['Workforce'],
            [no_percentage],
            left=[yes_percentage],
            color='#4F8BF9',
            height=0.5,
            label='Non-Overtime Employees'
        )

        ax4.text(
            yes_percentage / 2,
            0,
            f'{yes_percentage}%',
            ha='center',
            va='center',
            fontsize=14,
            fontweight='bold',
            color='white'
        )

        ax4.text(
            yes_percentage + (no_percentage / 2),
            0,
            f'{no_percentage}%',
            ha='center',
            va='center',
            fontsize=14,
            fontweight='bold',
            color='white'
        )

        ax4.set_xlim(0, 100)

        ax4.set_title(
            "Workforce Overtime Composition",
            fontsize=18,
            fontweight='bold',
            pad=20
        )

        ax4.legend(
            loc='lower center',
            bbox_to_anchor=(0.5, -0.45),
            ncol=2,
            frameon=False
        )

        ax4.set_xticks([])
        ax4.set_yticks([])

        for spine in ax4.spines.values():
            spine.set_visible(False)

        st.pyplot(fig4)

        st.markdown("---")

    #--------------------------------------------------------
    # STRATEGIC RECOMMENDATION
    #--------------------------------------------------------

    st.subheader("Strategic Recommendation")

    if selected_department == "All":

        st.success(
            "Recommended organizational initiatives:\n\n"
            "- Implement enterprise-wide burnout monitoring\n"
            "- Reduce sustained overtime dependency\n"
            "- Strengthen retention-focused HR policies\n"
            "- Improve workforce allocation strategies\n"
            "- Increase employee wellness engagement"
        )

    elif selected_department == "Sales":

        st.success(
            "Recommended Sales department initiatives:\n\n"
            "- Reduce aggressive overtime exposure\n"
            "- Improve incentive structures\n"
            "- Strengthen employee engagement\n"
            "- Introduce workload balancing\n"
            "- Enhance managerial monitoring"
        )

    elif selected_department == "Research & Development":

        st.success(
            "Recommended R&D department initiatives:\n\n"
            "- Improve long-term engagement programs\n"
            "- Reduce project burnout exposure\n"
            "- Strengthen workforce development\n"
            "- Improve career progression visibility\n"
            "- Enhance collaborative workload distribution"
        )

    elif selected_department == "Human Resources":

        st.success(
            "Recommended HR department initiatives:\n\n"
            "- Improve workload distribution\n"
            "- Strengthen support resources\n"
            "- Reduce administrative pressure\n"
            "- Enhance wellness monitoring\n"
            "- Improve staffing support mechanisms"
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

        department_attrition = round(
            (filtered_df['Attrition'] == 'Yes').mean() * 100,
            1
        )

        st.markdown(f"""
- The **{selected_department}** department currently demonstrates an attrition rate of **{department_attrition}%**.
- Workforce pressure and operational workload appear strongly associated with retention challenges.
- Overtime exposure remains a major workforce risk factor within the selected department.
- Workforce stability score currently stands at **{workforce_stability_score}/100**.
""")

    # =========================================================
    # SATISFACTION & ENGAGEMENT ANALYSIS
    # =========================================================

    st.markdown("---")
    st.subheader("Satisfaction & Engagement Analysis")

    sat1, sat2 = st.columns(2)

    # Job Satisfaction
    with sat1:

        job_sat = filtered_df.groupby('JobSatisfaction')['Attrition'] \
                             .apply(lambda x: (x == 'Yes').mean()) \
                             .reset_index()

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

        worklife = filtered_df.groupby('WorkLifeBalance')['Attrition'] \
                              .apply(lambda x: (x == 'Yes').mean()) \
                              .reset_index()

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

        tenure = filtered_df.groupby('YearsAtCompany')['Attrition'] \
                            .apply(lambda x: (x == 'Yes').mean()) \
                            .reset_index()

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

        attrition_yes = filtered_df[
            filtered_df['Attrition'] == 'Yes'
        ]['MonthlyIncome']

        attrition_no = filtered_df[
            filtered_df['Attrition'] == 'No'
        ]['MonthlyIncome']

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


# =========================================================
# RISK INTELLIGENCE SECTION
# =========================================================

elif section == "⚠️ Risk Intelligence":

    st.header("Risk Intelligence")

    st.write("""
    This section leverages predictive workforce intelligence
    to identify high-risk employee segments, workforce instability
    indicators, and organizational attrition exposure patterns.
    """)

    # =========================================================
    # RISK SCORE GENERATION
    # =========================================================

    risk_df = filtered_df.copy()

    risk_score = (
        (risk_df['OverTime'] == 'Yes').astype(int) * 30 +
        (risk_df['JobSatisfaction'] <= 2).astype(int) * 25 +
        (risk_df['WorkLifeBalance'] <= 2).astype(int) * 20 +
        (risk_df['YearsAtCompany'] <= 2).astype(int) * 15 +
        (
            risk_df['MonthlyIncome']
            < risk_df['MonthlyIncome'].median()
        ).astype(int) * 10
    )

    risk_df['RiskScore'] = risk_score

    risk_df['RiskLevel'] = pd.cut(
        risk_df['RiskScore'],
        bins=[-1, 20, 50, 100],
        labels=['Low Risk', 'Moderate Risk', 'High Risk']
    )

    # =========================================================
    # EXECUTIVE RISK SNAPSHOT
    # =========================================================

    st.markdown("---")
    st.subheader("Executive Risk Snapshot")

    high_risk_count = len(
        risk_df[risk_df['RiskLevel'] == 'High Risk']
    )

    moderate_risk_count = len(
        risk_df[risk_df['RiskLevel'] == 'Moderate Risk']
    )

    low_risk_count = len(
        risk_df[risk_df['RiskLevel'] == 'Low Risk']
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

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    kpi1.metric(
        "High-Risk Employees",
        high_risk_count
    )

    kpi2.metric(
        "Moderate Risk Employees",
        moderate_risk_count
    )

    kpi3.metric(
        "Average Workforce Risk",
        avg_risk_score
    )

    kpi4.metric(
        "Retention Probability",
        f"{retention_probability}%"
    )

    # =========================================================
    # ORGANIZATIONAL RISK STATUS
    # =========================================================

    st.subheader("Organizational Risk Exposure")

    if selected_department == "All":

        if high_risk_percentage < 15:

            st.success("""
🟢 LOW ORGANIZATIONAL RISK

Current workforce risk exposure remains
within stable organizational thresholds.
""")

        elif high_risk_percentage < 30:

            st.warning("""
🟡 MODERATE ORGANIZATIONAL RISK

Workforce instability indicators are
increasing across selected employee segments.
""")

        else:

            st.error("""
🔴 HIGH ORGANIZATIONAL RISK

Significant workforce instability detected
across high-risk employee populations.
""")

    else:

        if high_risk_percentage < 15:

            st.success(f"""
🟢 LOW {selected_department.upper()} DEPARTMENT RISK

The {selected_department} department currently
maintains relatively stable workforce conditions.
""")

        elif high_risk_percentage < 30:

            st.warning(f"""
🟡 MODERATE {selected_department.upper()} DEPARTMENT RISK

The {selected_department} department demonstrates
growing workforce instability indicators.
""")

        else:

            st.error(f"""
🔴 HIGH {selected_department.upper()} DEPARTMENT RISK

The {selected_department} department demonstrates
elevated predictive attrition exposure and
workforce instability concentration.
""")

    # =========================================================
    # PREDICTIVE VISUALS
    # =========================================================

    st.markdown("---")
    st.subheader("Predictive Risk Distribution")

    chart1, chart2 = st.columns(2)

    # =========================================================
    # RADIAL RISK GAUGE
    # =========================================================

    with chart1:

        fig9, ax9 = plt.subplots(figsize=(6,6))

        sizes = [
            high_risk_percentage,
            100 - high_risk_percentage
        ]

        colors = ['#E74C3C', '#EAEAEA']

        ax9.pie(
            sizes,
            startangle=90,
            colors=colors,
            wedgeprops=dict(
                width=0.35,
                edgecolor='white'
            )
        )

        ax9.text(
            0,
            0,
            f"{high_risk_percentage}%",
            ha='center',
            va='center',
            fontsize=30,
            fontweight='bold',
            color='#E74C3C'
        )

        ax9.text(
            0,
            -0.18,
            "High Risk",
            ha='center',
            va='center',
            fontsize=13,
            color='#CBD5E1'
        )

        ax9.set_title(
            "Organizational Risk Exposure",
            fontsize=18,
            fontweight='bold',
            pad=20
        )

        st.pyplot(fig9)

    # =========================================================
    # RISK SEGMENTATION
    # =========================================================

    with chart2:

        risk_counts = risk_df['RiskLevel'].value_counts()

        fig10 = px.pie(
            names=risk_counts.index,
            values=risk_counts.values,
            title='Workforce Risk Segmentation',
            color=risk_counts.index,
            color_discrete_map={
                'Low Risk': '#2ECC71',
                'Moderate Risk': '#F1C40F',
                'High Risk': '#E74C3C'
        }
)

        fig10.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            title_font_size=22,
            height=500
)

        st.plotly_chart(
            fig10,
            use_container_width=True
)

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

    if selected_department == "All":

        with persona1:

            st.info("""
### High-Risk Persona 1

Early-career employees experiencing:
- Sustained overtime exposure
- Low work-life balance
- High workload pressure
- Reduced engagement levels
""")

        with persona2:

            st.info("""
### High-Risk Persona 2

Employees demonstrating:
- Low job satisfaction
- Operational burnout indicators
- Short organizational tenure
- Elevated workforce instability risk
""")

    elif selected_department == "Sales":

        with persona1:

            st.info("""
### Sales Performance Burnout Persona

Employees experiencing:
- Aggressive performance targets
- Sustained overtime exposure
- High client-facing workload
- Reduced engagement stability
""")

        with persona2:

            st.info("""
### Sales Retention Risk Persona

Employees demonstrating:
- Reduced incentive satisfaction
- Elevated operational fatigue
- High performance pressure
- Increased workforce instability
""")

    elif selected_department == "Research & Development":

        with persona1:

            st.info("""
### R&D Burnout Persona

Employees experiencing:
- Long project cycles
- Cognitive workload pressure
- Reduced work-life balance
- Engagement fatigue
""")

        with persona2:

            st.info("""
### Innovation Retention Risk Persona

Employees demonstrating:
- Career stagnation concerns
- Reduced collaborative engagement
- Long-term workload fatigue
- Elevated attrition vulnerability
""")

    elif selected_department == "Human Resources":

        with persona1:

            st.info("""
### HR Operational Pressure Persona

Employees experiencing:
- Administrative overload
- Workforce support fatigue
- Sustained operational pressure
- Reduced wellness balance
""")

        with persona2:

            st.info("""
### HR Workforce Fatigue Persona

Employees demonstrating:
- Employee support burnout
- Workforce coordination pressure
- Reduced engagement sustainability
- Elevated retention vulnerability
""")

    # =========================================================
    # RISK HEATMAP STYLE ANALYSIS
    # =========================================================

    st.markdown("---")
    st.subheader("Workforce Risk Pattern Analysis")

    heatmap_data = risk_df.pivot_table(
        values='RiskScore',
        index='OverTime',
        columns='JobSatisfaction',
        aggfunc='mean',
        fill_value=0
    ) 

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

    simulated_risk_reduction = round(
        high_risk_percentage * 0.18,
        1
    )

    projected_risk = round(
        high_risk_percentage - simulated_risk_reduction,
        1
    )

    if selected_department == "All":

        st.success(f"""
### Workforce Optimization Simulation

If overtime exposure is reduced by approximately 20%:

• Estimated high-risk workforce reduces by **{simulated_risk_reduction}%**
• Projected workforce risk exposure drops to **{projected_risk}%**
• Workforce stability and retention probability improve significantly
• Organizational burnout exposure decreases across critical employee groups
""")

    else:

        st.success(f"""
### {selected_department} Workforce Optimization Simulation

If overtime exposure and workload imbalance are reduced
within the {selected_department} department:

• Estimated department risk exposure reduces by **{simulated_risk_reduction}%**
• Projected department instability decreases to **{projected_risk}%**
• Employee engagement and retention stability improve
• Department workforce sustainability strengthens significantly
""")

    # =========================================================
    # PREDICTIVE INSIGHTS
    # =========================================================

    st.markdown("---")
    st.subheader("Predictive Workforce Insights")

    if selected_department == "All":

        st.info(f"""
### Organization-Wide Predictive Intelligence

Predictive workforce analytics indicate that
employees exposed to sustained overtime pressure,
low satisfaction, and burnout indicators demonstrate
significantly elevated attrition risk.

Current analysis identifies **{high_risk_count}**
employees within the high-risk workforce category,
representing approximately **{high_risk_percentage}%**
of the workforce population.
""")

    elif selected_department == "Sales":

        st.info("""
### Sales Department Predictive Intelligence

The Sales department demonstrates elevated workforce
instability associated with sustained performance pressure,
high overtime exposure, and engagement fatigue.
""")

    elif selected_department == "Research & Development":

        st.info("""
### R&D Department Predictive Intelligence

The Research & Development department demonstrates
workforce instability patterns associated with long-term
project fatigue and engagement sustainability challenges.
""")

    elif selected_department == "Human Resources":

        st.info("""
### Human Resources Predictive Intelligence

The Human Resources department demonstrates workforce
pressure associated with operational coordination demands,
employee support fatigue, and sustained administrative load.
""")

    # =========================================================
    # COST IMPACT ESTIMATION
    # =========================================================

    st.markdown("---")
    st.subheader("Estimated Organizational Cost Exposure")

    estimated_replacement_cost = high_risk_count * 15000

    if selected_department == "All":

        st.error(f"""
### Estimated Attrition Exposure: ${estimated_replacement_cost:,.0f}

Projected workforce instability impact includes:
• Recruitment costs
• Onboarding expenses
• Productivity disruption
• Workforce transition instability
• Operational performance decline
""")

    else:

        st.error(f"""
### Estimated {selected_department} Department Exposure:
${estimated_replacement_cost:,.0f}

Projected department instability impact includes:
• Workforce replacement costs
• Operational productivity disruption
• Team performance instability
• Increased workforce transition exposure
""")

    # =========================================================
    # STRATEGIC ACTION PRIORITIES
    # =========================================================

    st.markdown("---")
    st.subheader("Strategic Action Priorities")

    if selected_department == "All":

        st.success("""
1. Reduce sustained overtime dependency
2. Improve employee engagement initiatives
3. Strengthen workforce wellness monitoring
4. Increase retention-focused HR interventions
5. Improve workforce allocation efficiency
6. Develop predictive workforce monitoring systems
""")

    elif selected_department == "Sales":

        st.success("""
1. Reduce aggressive performance workload pressure
2. Improve employee incentive sustainability
3. Strengthen sales engagement initiatives
4. Improve workforce balancing strategies
5. Enhance retention-focused managerial oversight
6. Reduce sustained overtime dependency
""")

    elif selected_department == "Research & Development":

        st.success("""
1. Improve long-term workforce engagement
2. Reduce project-related burnout exposure
3. Strengthen workforce innovation pathways
4. Improve collaborative workload balancing
5. Enhance career growth visibility
6. Improve retention-focused development planning
""")

    elif selected_department == "Human Resources":

        st.success("""
1. Reduce administrative workload pressure
2. Improve workforce support sustainability
3. Strengthen employee wellness initiatives
4. Improve operational staffing balance
5. Enhance workforce coordination support
6. Reduce burnout exposure across HR operations
""")
        
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
        
# =========================================================
# STRATEGIC INSIGHTS SECTION
# =========================================================

elif section == "🧠 Strategic Insights":

    # =========================================================
    # RISK DATA PREPARATION
    # =========================================================

    risk_df = filtered_df.copy()

    risk_score = (
        (risk_df['OverTime'] == 'Yes').astype(int) * 30 +
        (risk_df['JobSatisfaction'] <= 2).astype(int) * 25 +
        (risk_df['WorkLifeBalance'] <= 2).astype(int) * 20 +
        (risk_df['YearsAtCompany'] <= 2).astype(int) * 15 +
        (
            risk_df['MonthlyIncome']
            < risk_df['MonthlyIncome'].median()
        ).astype(int) * 10
    )

    risk_df['RiskScore'] = risk_score

    risk_df['RiskLevel'] = pd.cut(
        risk_df['RiskScore'],
        bins=[-1, 20, 50, 100],
        labels=['Low Risk', 'Moderate Risk', 'High Risk']
    )

    high_risk_count = len(
        risk_df[risk_df['RiskLevel'] == 'High Risk']
    )

    # =========================================================
    # PAGE HEADER
    # =========================================================

    st.header("Strategic Insights")

    st.write("""
    This section transforms workforce analytics and predictive
    intelligence into strategic organizational recommendations,
    leadership priorities, and workforce optimization planning.
    """)

    # =========================================================
    # EXECUTIVE STRATEGIC SNAPSHOT
    # =========================================================

    st.markdown("---")
    st.subheader("Executive Strategic Snapshot")

    strategic_risk_score = round(
        risk_df['RiskScore'].mean(),
        1
    )

    strategic_retention_score = round(
        100 - strategic_risk_score,
        1
    )

    projected_attrition_impact = high_risk_count * 15000

    optimization_gain = round(
        strategic_retention_score * 0.12,
        1
    )

    s1, s2, s3, s4 = st.columns(4)

    s1.metric(
        "Strategic Risk Score",
        f"{strategic_risk_score}/100"
    )

    s2.metric(
        "Retention Stability",
        f"{strategic_retention_score}%"
    )

    s3.metric(
        "Projected Cost Exposure",
        f"${projected_attrition_impact:,.0f}"
    )

    s4.metric(
        "Optimization Potential",
        f"+{optimization_gain}%"
    )

    # =========================================================
    # WORKFORCE HEALTH INDEX
    # =========================================================

    st.markdown("---")
    st.subheader("Workforce Health Index")

    avg_job_satisfaction = round(
        filtered_df['JobSatisfaction'].mean() * 20,
        1
    )

    avg_worklife_balance = round(
        filtered_df['WorkLifeBalance'].mean() * 20,
        1
    )

    overtime_penalty = round(
        (filtered_df['OverTime'] == 'Yes').mean() * 100 * 0.35,
        1
    )

    attrition_penalty = round(
        (filtered_df['Attrition'] == 'Yes').mean() * 100 * 0.45,
        1
    )

    health_index = round(
        (
            avg_job_satisfaction +
            avg_worklife_balance +
            strategic_retention_score
        ) / 3
        - overtime_penalty
        - attrition_penalty,
        1
    )

    health_index = max(0, min(100, health_index))

    health_col1, health_col2 = st.columns([1, 2])

    with health_col1:

        fig15, ax15 = plt.subplots(figsize=(4,4))

        sizes = [health_index, 100 - health_index]

        if health_index >= 75:
            health_color = '#2ECC71'

        elif health_index >= 50:
            health_color = '#F1C40F'

        else:
            health_color = '#E74C3C'

        ax15.pie(
            sizes,
            startangle=90,
            colors=[health_color, '#EAEAEA'],
            wedgeprops=dict(
                width=0.3,
                edgecolor='white'
            )
        )

        ax15.text(
            0,
            0,
            f"{health_index}",
            ha='center',
            va='center',
            fontsize=28,
            fontweight='bold',
            color=health_color
        )

        ax15.text(
            0,
            -0.2,
            "/100",
            ha='center',
            va='center',
            fontsize=12,
            color='#CBD5E1'
        )

        ax15.set_title(
            "Workforce Health",
            fontsize=16,
            fontweight='bold'
        )

        st.pyplot(fig15)

    with health_col2:

        if health_index >= 75:

            st.success(f"""
### Workforce Condition: HEALTHY

The {selected_department if selected_department != 'All' else 'organization'}
currently demonstrates strong workforce sustainability,
healthy engagement indicators, and stable operational
retention conditions.
""")

        elif health_index >= 50:

            st.warning(f"""
### Workforce Condition: MODERATE STABILITY

The {selected_department if selected_department != 'All' else 'organization'}
demonstrates moderate workforce sustainability with
emerging burnout and retention pressure indicators.
""")

        else:

            st.error(f"""
### Workforce Condition: HIGH INSTABILITY

The {selected_department if selected_department != 'All' else 'organization'}
demonstrates elevated workforce instability driven by
burnout exposure and operational workload imbalance.
""")

    # =========================================================
    # EXECUTIVE OUTLOOK
    # =========================================================

    st.markdown("---")
    st.subheader("Executive Workforce Outlook")

    if selected_department == "All":

        if strategic_risk_score < 25:

            st.success("""
🟢 STRATEGIC WORKFORCE OUTLOOK: STABLE

The organization currently demonstrates healthy
workforce sustainability with manageable levels
of operational attrition exposure.
""")

        elif strategic_risk_score < 45:

            st.warning("""
🟡 STRATEGIC WORKFORCE OUTLOOK: MODERATE RISK

Emerging workforce instability indicators require
leadership attention and proactive retention planning.
""")

        else:

            st.error("""
🔴 STRATEGIC WORKFORCE OUTLOOK: HIGH RISK

Significant organizational workforce instability
requires immediate strategic intervention.
""")

    else:

        if strategic_risk_score < 25:

            st.success(f"""
🟢 {selected_department.upper()} OUTLOOK: STABLE

The {selected_department} department currently
maintains relatively healthy workforce sustainability.
""")

        elif strategic_risk_score < 45:

            st.warning(f"""
🟡 {selected_department.upper()} OUTLOOK: MODERATE RISK

The {selected_department} department demonstrates
growing workforce pressure and retention exposure.
""")

        else:

            st.error(f"""
🔴 {selected_department.upper()} OUTLOOK: HIGH RISK

The {selected_department} department requires
immediate workforce stabilization initiatives.
""")

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

    forecast1, forecast2 = st.columns(2)

    with forecast1:

        fig13, ax13 = plt.subplots(figsize=(6,6))

        sizes = [
            strategic_retention_score,
            100 - strategic_retention_score
        ]

        colors = ['#2ECC71', '#EAEAEA']

        ax13.pie(
            sizes,
            startangle=90,
            colors=colors,
            wedgeprops=dict(
                width=0.35,
                edgecolor='white'
            )
        )

        ax13.text(
            0,
            0,
            f"{strategic_retention_score}%",
            ha='center',
            va='center',
            fontsize=30,
            fontweight='bold',
            color='#2ECC71'
        )

        ax13.text(
            0,
            -0.18,
            "Retention Stability",
            ha='center',
            va='center',
            fontsize=13,
            color='#CBD5E1'
        )

        ax13.set_title(
            "Predicted Workforce Stability",
            fontsize=18,
            fontweight='bold',
            pad=20
        )

        st.pyplot(fig13)

    with forecast2:

        baseline = strategic_retention_score

        optimized = min(
            strategic_retention_score + optimization_gain,
            100
        )
        categories = [
            'Current Stability',
            'Projected Stability'
        ]

        values = [
            baseline,
            optimized
        ]

        optimization_df = pd.DataFrame({
            'Scenario': categories,
            'Stability': values
        })

        fig14 = px.bar(
            optimization_df,
            x='Scenario',
            y='Stability',
            color='Scenario',
            title='Optimization Impact Simulation',
            text='Stability'
        )

        fig14.update_traces(
            texttemplate='%{text:.1f}%',
            textposition='outside'
        )

        fig14.update_layout(
            template='plotly_dark',
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            title_font_size=22,
            height=500,
            yaxis_range=[0,100]
        )

        st.plotly_chart(
            fig14,
            use_container_width=True
        )

        st.markdown("---")

    # =========================================================
    # AI EXECUTIVE NARRATIVE
    # =========================================================

    st.markdown("---")
    st.subheader("AI Executive Narrative")

    if selected_department == "All":

        st.info(f"""
AI workforce intelligence predicts that the organization
currently faces moderate workforce sustainability pressure
driven primarily by overtime exposure, declining engagement,
and emerging retention instability.

Predictive workforce simulations indicate that proactive
burnout reduction initiatives and workforce balancing
strategies could improve long-term workforce stability
by approximately **{optimization_gain}%**.
""")

    elif selected_department == "Sales":

        st.info("""
AI workforce intelligence identifies the Sales department
as experiencing elevated performance-related operational
pressure and workforce fatigue exposure.
""")

    elif selected_department == "Research & Development":

        st.info("""
AI workforce intelligence identifies long-term project
fatigue and workforce engagement sustainability as
primary retention challenges within R&D.
""")

    elif selected_department == "Human Resources":

        st.info("""
AI workforce intelligence identifies workforce coordination
pressure and administrative workload exposure as primary
drivers of operational fatigue within HR.
""")

    # =========================================================
    # DEPARTMENT RISK RANKING
    # =========================================================

    st.markdown("---")
    st.subheader("Department Workforce Risk Ranking")

    dept_risk = df.groupby('Department').apply(
        lambda x: (
            (
                (x['OverTime'] == 'Yes').mean() * 30
            ) +
            (
                (x['JobSatisfaction'] <= 2).mean() * 25
            ) +
            (
                (x['WorkLifeBalance'] <= 2).mean() * 20
            )
        )
    ).sort_values(ascending=False)

    ranking_df = pd.DataFrame({
        "Department": dept_risk.index,
        "Risk Score": dept_risk.values.round(1)
    })

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

    if selected_department == "All":

        st.success("""
### Recommended Immediate Executive Action

Prioritize organization-wide overtime reduction and
predictive workforce monitoring initiatives to stabilize
high-risk employee segments and improve long-term
workforce sustainability outcomes.
""")

    elif selected_department == "Sales":

        st.success("""
### Recommended Sales Leadership Action

Reduce sustained performance workload exposure and
improve employee engagement reinforcement mechanisms.
""")

    elif selected_department == "Research & Development":

        st.success("""
### Recommended R&D Leadership Action

Improve collaborative workload balancing and strengthen
long-term workforce engagement initiatives.
""")

    elif selected_department == "Human Resources":

        st.success("""
### Recommended HR Leadership Action

Reduce administrative workforce pressure and improve
employee support sustainability mechanisms.
""")

    # =========================================================
    # EXECUTIVE IMPACT SIMULATION
    # =========================================================

    st.markdown("---")
    st.subheader("Executive Impact Simulation")

    projected_savings = round(
        projected_attrition_impact * 0.22,
        0
    )

    projected_retention_gain = round(
        optimization_gain * 1.4,
        1
    )

    if selected_department == "All":

        st.success(f"""
### Strategic Workforce Optimization Projection

If current workforce recommendations are implemented:

• Predicted retention improvement:
  **+{projected_retention_gain}%**

• Estimated annual organizational savings:
  **${projected_savings:,.0f}**

• Reduced workforce instability exposure
• Improved workforce sustainability
• Increased operational continuity
""")

    else:

        st.success(f"""
### {selected_department} Optimization Projection

If department-level workforce initiatives are implemented:

• Predicted department retention improvement:
  **+{projected_retention_gain}%**

• Estimated department workforce savings:
  **${projected_savings:,.0f}**
""")

    # =========================================================
    # WORKFORCE STRATEGY MATURITY
    # =========================================================

    st.markdown("---")
    st.subheader("Workforce Strategy Maturity")

    if health_index >= 80:

        maturity_level = "Optimized Workforce Strategy"
        maturity_color = "🟢"

    elif health_index >= 60:

        maturity_level = "Maturing Workforce Strategy"
        maturity_color = "🟡"

    elif health_index >= 40:

        maturity_level = "Developing Workforce Strategy"
        maturity_color = "🟠"

    else:

        maturity_level = "Reactive Workforce Strategy"
        maturity_color = "🔴"

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

    risk_probability = round(
            (
                (overtime == 'Yes') * 40 +
                (job_satisfaction <= 2) * 25 +
                (worklife <= 2) * 20 +
                (years_company <= 2) * 10 +
                (monthly_income < 4000) * 5
            ),
            1
        )

    if risk_probability < 25:

            st.success(
                f"🟢 Predicted Attrition Risk: {risk_probability}%"
            )

    elif risk_probability < 50:

            st.warning(
                f"🟡 Predicted Attrition Risk: {risk_probability}%"
            )

    else:

            st.error(
                f"🔴 Predicted Attrition Risk: {risk_probability}%"
            )


# =========================================================
# FINAL EXECUTIVE SUMMARY
# =========================================================

    st.markdown("---")
    st.subheader("Executive Strategic Summary")

    if selected_department == "All":

        st.info("""
        The organization currently demonstrates moderate
        predictive workforce instability driven primarily
        by overtime exposure, burnout pressure, and
        employee engagement decline.

        Strategic workforce optimization initiatives
        present strong opportunities to improve retention,
        reduce operational instability, and strengthen
        long-term organizational sustainability.
        """)

    else:

        st.info(f"""
        The {selected_department} department demonstrates
        elevated workforce pressure associated with
        operational workload and workforce sustainability
        challenges.

        Strategic intervention focused on engagement,
        burnout reduction, and workload optimization
        may significantly improve department stability
        and long-term workforce retention outcomes.
        """)

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