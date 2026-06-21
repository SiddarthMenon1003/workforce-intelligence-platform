import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

from frontend.styles import load_css

from frontend.sidebar import (
    render_sidebar,
    render_navigation
)

from frontend.overview import render_overview

from frontend.risk_intelligence import (
    render_risk_intelligence
)

from frontend.strategic_insights import (
    render_strategic_insights
)

from frontend.workforce_analytics import (
    render_workforce_analytics
)

from backend.analytics import (
    validate_dataset,
    filter_department,
    REQUIRED_COLUMNS
)

plt.style.use("dark_background")

plt.rcParams.update({

    "figure.facecolor": "#0B1120",
    "axes.facecolor": "#111827",

    "axes.edgecolor": "#111827",

    "axes.labelcolor": "white",

    "xtick.color": "#CBD5E1",
    "ytick.color": "#CBD5E1",

    "text.color": "white",

    "axes.titleweight": "bold",
    "axes.titlepad": 20,

    "font.size": 13,

    "grid.color": "white",
    "grid.alpha": 0.10,
    "grid.linestyle": "--",

    "axes.grid": True,

    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.spines.left": False,
    "axes.spines.bottom": False
})

from backend.model import (
    train_workforce_model
)

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title=
    "Workforce Intelligence Dashboard",

    page_icon="🧠",

    layout="wide"
)

load_css()


# ======================================================
# LOAD DATA
# ======================================================

uploaded_file = render_sidebar()

if uploaded_file is not None:

    df = pd.read_csv(
        uploaded_file
    )

else:

    df = pd.read_csv(
        "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    )


# ======================================================
# DATA VALIDATION
# ======================================================

missing_columns = (
    validate_dataset(
        df,
        REQUIRED_COLUMNS
    )
)

if missing_columns:

    st.error(
        f"""
        Missing required columns:
        {missing_columns}
        """
    )

    st.stop()


# ======================================================
# NAVIGATION
# ======================================================

section, selected_department = (
    render_navigation()
)

# ======================================================
# TRAIN MODEL
# ======================================================

with st.spinner(
    "Initializing Workforce Intelligence Systems..."
):

    model_data = (
        train_workforce_model(df)
    )

    rf_model = (
        model_data["model"]
    )

    model_accuracy = (
        model_data["accuracy"]
    )

    X = (
        model_data["X"]
    )


# ======================================================
# APPLY FILTER
# ======================================================

filtered_df = filter_department(
    df,
    selected_department
)

if filtered_df.empty:

    st.warning(
        "No workforce records match current filters."
    )

    st.stop()


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


# =========================
# OVERVIEW SECTION
# =========================

if section == "📊 Overview":

    render_overview(
    filtered_df=filtered_df,
    df=df,
    selected_department=selected_department,
    model_accuracy=model_accuracy
)

# =========================
# WORKFORCE ANALYTICS SECTION
# =========================

elif section == "👥 Workforce Analytics":

    render_workforce_analytics(
        filtered_df=filtered_df,
        selected_department=selected_department
)

# =========================================================
# RISK INTELLIGENCE SECTION
# =========================================================

elif section == "⚠️ Risk Intelligence":

    render_risk_intelligence(
    filtered_df=filtered_df,
    selected_department=selected_department
)
        
# =========================================================
# STRATEGIC INSIGHTS SECTION
# =========================================================

elif section == "🧠 Strategic Insights":

    render_strategic_insights(
    filtered_df=filtered_df,
    df=df,
    selected_department=selected_department,
    X=X,
    rf_model=rf_model
)