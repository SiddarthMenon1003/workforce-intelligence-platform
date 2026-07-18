"""Workforce Intelligence Dashboard — Streamlit entry point.

This module only orchestrates the page: load data, validate it, train the
model, apply filters, and dispatch to the selected page renderer. All
business logic lives in `backend/`, all layout lives in `frontend/`.
"""

import pandas as pd
import streamlit as st

from backend.analytics import REQUIRED_COLUMNS, filter_department, validate_dataset
from backend.model import train_workforce_model
from frontend.components import footer
from frontend.overview import render_overview
from frontend.risk_intelligence import render_risk_intelligence
from frontend.sidebar import (
    NAVIGATION_ITEMS,
    render_capabilities_panel,
    render_navigation,
    render_sidebar,
    render_system_status,
)
from frontend.strategic_insights import render_strategic_insights
from frontend.styles import load_css
from frontend.workforce_analytics import render_workforce_analytics

DEFAULT_DATASET_PATH = "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"


@st.cache_data(show_spinner=False)
def load_dataset(uploaded_file):
    """Load the uploaded CSV, or fall back to the bundled sample dataset."""

    if uploaded_file is not None:
        return pd.read_csv(uploaded_file)

    return pd.read_csv(DEFAULT_DATASET_PATH)


def main():
    st.set_page_config(
        page_title="Workforce Intelligence Dashboard",
        page_icon="\U0001F9E0",
        layout="wide",
    )

    load_css()

    uploaded_file = render_sidebar()
    df = load_dataset(uploaded_file)

    missing_columns = validate_dataset(df, REQUIRED_COLUMNS)

    if missing_columns:
        st.error(f"Missing required columns: {missing_columns}")
        st.stop()

    section, selected_department = render_navigation()
    render_system_status()
    render_capabilities_panel()

    with st.spinner("Initializing Workforce Intelligence Systems..."):
        model_data = train_workforce_model(df)

    rf_model = model_data["model"]
    model_accuracy = model_data["accuracy"]
    X = model_data["X"]

    filtered_df = filter_department(df, selected_department)

    if filtered_df.empty:
        st.warning("No workforce records match current filters.")
        st.stop()

    renderers = [
        lambda: render_overview(
            filtered_df=filtered_df,
            df=df,
            selected_department=selected_department,
            model_accuracy=model_accuracy,
        ),
        lambda: render_workforce_analytics(
            filtered_df=filtered_df,
            selected_department=selected_department,
        ),
        lambda: render_risk_intelligence(
            filtered_df=filtered_df,
            selected_department=selected_department,
        ),
        lambda: render_strategic_insights(
            filtered_df=filtered_df,
            df=df,
            selected_department=selected_department,
            X=X,
            rf_model=rf_model,
        ),
    ]

    # Zipped positionally against NAVIGATION_ITEMS so the routing table can
    # never drift out of sync with the sidebar's radio options.
    dict(zip(NAVIGATION_ITEMS, renderers))[section]()

    footer()


if __name__ == "__main__":
    main()
