"""Workforce KPI and aggregation calculations.

Every function here is a pure transformation of a pandas DataFrame into the
metrics the dashboard pages render — no Streamlit calls and no presentation
logic live in this module, so it can be unit-tested independently of the UI.
"""

import pandas as pd

from backend.risk_engine import classify_risk, generate_risk_scores

REQUIRED_COLUMNS = [
    "Age",
    "Attrition",
    "Department",
    "JobSatisfaction",
    "MonthlyIncome",
    "OverTime",
    "WorkLifeBalance",
    "YearsAtCompany",
]


def validate_dataset(dataframe, required_columns):
    """Return the subset of `required_columns` missing from `dataframe`."""

    return [col for col in required_columns if col not in dataframe.columns]


def filter_department(dataframe, selected_department):
    """Return rows for `selected_department`, or the full frame for "All"."""

    if selected_department == "All":
        return dataframe.copy()

    return dataframe[dataframe["Department"] == selected_department]


def _attrition_rate(dataframe):
    return round((dataframe["Attrition"] == "Yes").mean() * 100, 1)


def _overtime_rate(dataframe):
    return round((dataframe["OverTime"] == "Yes").mean() * 100, 1)


def get_overview_metrics(filtered_df):
    """Top-level KPI tile values for the Overview page."""

    attrition_rate = _attrition_rate(filtered_df)
    overtime_percentage = _overtime_rate(filtered_df)
    retention_percent = round(100 - attrition_rate, 1)

    return {
        "total_employees": len(filtered_df),
        "attrition_rate": attrition_rate,
        "high_risk_employees": int((filtered_df["OverTime"] == "Yes").sum()),
        "overtime_percentage": overtime_percentage,
        "retention_percent": retention_percent,
        "engagement_score": round(
            (retention_percent + (100 - overtime_percentage)) / 2, 1
        ),
    }


def get_department_intelligence(dataframe):
    """Identify the departments with the highest and lowest attrition."""

    dept_attrition = dataframe.groupby("Department")["Attrition"].apply(
        lambda x: (x == "Yes").mean()
    )

    return {
        "highest_attrition_dept": dept_attrition.idxmax(),
        "stable_dept": dept_attrition.idxmin(),
    }


def get_department_overview_metrics(filtered_df, selected_department):
    """Department-scoped attrition/retention/overtime/engagement metrics."""

    dept_df = (
        filtered_df
        if selected_department == "All"
        else filtered_df[filtered_df["Department"] == selected_department]
    )

    dept_attrition = _attrition_rate(dept_df)
    dept_retention = round(100 - dept_attrition, 1)
    dept_overtime = _overtime_rate(dept_df)

    return {
        "dept_attrition": dept_attrition,
        "dept_retention": dept_retention,
        "dept_overtime": dept_overtime,
        "dept_engagement": round((dept_retention + (100 - dept_overtime)) / 2, 1),
    }


def get_workforce_metrics(filtered_df):
    """Core workforce analytics used on the Workforce Analytics page."""

    overtime_pct = _overtime_rate(filtered_df)
    dept_attrition = _attrition_rate(filtered_df)

    # Composite stability score: attrition and overtime pressure combined,
    # clamped to a readable 35-95 band for the KPI ring.
    stability_score = round(100 - (dept_attrition * 0.55 + overtime_pct * 0.45), 0)
    stability_score = max(35, min(stability_score, 95))

    overtime_attrition_rate = round(
        (filtered_df[filtered_df["OverTime"] == "Yes"]["Attrition"] == "Yes").mean() * 100,
        1,
    )

    no_overtime_attrition_rate = round(
        (filtered_df[filtered_df["OverTime"] == "No"]["Attrition"] == "Yes").mean() * 100,
        1,
    )

    return {
        "avg_income": round(filtered_df["MonthlyIncome"].mean(), 0),
        "dept_attrition": dept_attrition,
        "stability_score": stability_score,
        "overtime_percentage": overtime_pct,
        "overtime_attrition_rate": overtime_attrition_rate,
        "no_overtime_attrition_rate": no_overtime_attrition_rate,
        # Overtime-specific stability: the inverse of overtime attrition risk.
        "workforce_stability_score": round(100 - overtime_attrition_rate, 1),
    }


def get_workforce_department_stats(filtered_df):
    """Department-level aggregations for attrition, income, and satisfaction."""

    department_attrition = (
        filtered_df.groupby("Department")["Attrition"]
        .apply(lambda x: (x == "Yes").mean() * 100)
        .reset_index()
    )
    department_attrition.columns = ["Department", "AttritionRate"]

    return {
        "department_attrition": department_attrition,
        "department_income": (
            filtered_df.groupby("Department")["MonthlyIncome"].mean().reset_index()
        ),
        "department_satisfaction": (
            filtered_df.groupby("Department")["JobSatisfaction"].mean().reset_index()
        ),
        "overtime_distribution": filtered_df["OverTime"].value_counts(),
    }


def get_satisfaction_metrics(filtered_df):
    """Satisfaction, work-life balance, tenure, and income lifecycle cuts."""

    return {
        "job_satisfaction": (
            filtered_df.groupby("JobSatisfaction")["Attrition"]
            .apply(lambda x: (x == "Yes").mean())
            .reset_index()
        ),
        "worklife_balance": (
            filtered_df.groupby("WorkLifeBalance")["Attrition"]
            .apply(lambda x: (x == "Yes").mean())
            .reset_index()
        ),
        "tenure_attrition": (
            filtered_df.groupby("YearsAtCompany")["Attrition"]
            .apply(lambda x: (x == "Yes").mean())
            .reset_index()
        ),
        "attrition_yes_income": filtered_df[filtered_df["Attrition"] == "Yes"]["MonthlyIncome"],
        "attrition_no_income": filtered_df[filtered_df["Attrition"] == "No"]["MonthlyIncome"],
    }


def get_risk_metrics(filtered_df):
    """Employee-level risk scores plus the executive risk roll-up."""

    risk_df = generate_risk_scores(filtered_df)

    high_risk_count = int((risk_df["RiskScore"] >= 50).sum())
    high_risk_percentage = round(high_risk_count / len(risk_df) * 100, 1)
    simulated_risk_reduction = round(high_risk_percentage * 0.18, 1)

    heatmap_data = risk_df.pivot_table(
        values="RiskScore",
        index="OverTime",
        columns="JobSatisfaction",
        aggfunc="mean",
        fill_value=0,
    )

    return {
        "risk_df": risk_df,
        "high_risk_count": high_risk_count,
        "avg_risk_score": round(risk_df["RiskScore"].mean(), 1),
        "high_risk_percentage": high_risk_percentage,
        "retention_probability": round(100 - high_risk_percentage, 1),
        "projected_attrition_impact": high_risk_count * 15000,
        "optimization_gain": simulated_risk_reduction,
        "simulated_risk_reduction": simulated_risk_reduction,
        "projected_risk": round(high_risk_percentage - simulated_risk_reduction, 1),
        "heatmap_data": heatmap_data,
    }


def get_strategic_metrics(filtered_df):
    """Executive-level strategic KPIs, health index, and risk classification."""

    attrition_rate = _attrition_rate(filtered_df)
    overtime_percentage = _overtime_rate(filtered_df)
    retention_score = round(100 - attrition_rate, 1)

    risk_df = generate_risk_scores(filtered_df)
    high_risk_count = int((risk_df["RiskLevel"] == "High Risk").sum())

    strategic_risk_score = round(risk_df["RiskScore"].mean(), 1)
    strategic_retention_score = round(100 - strategic_risk_score, 1)
    optimization_gain = round(strategic_retention_score * 0.12, 1)
    projected_stability = round(min(strategic_retention_score + optimization_gain, 100), 1)

    avg_job_satisfaction = round(filtered_df["JobSatisfaction"].mean() * 20, 1)
    avg_worklife_balance = round(filtered_df["WorkLifeBalance"].mean() * 20, 1)
    overtime_penalty = round(overtime_percentage * 0.35, 1)
    attrition_penalty = round(attrition_rate * 0.45, 1)

    health_index = round(
        (avg_job_satisfaction + avg_worklife_balance + strategic_retention_score) / 3
        - overtime_penalty
        - attrition_penalty,
        1,
    )
    health_index = max(0, min(100, health_index))

    risk_data = classify_risk(strategic_risk_score)

    return {
        "high_risk_count": high_risk_count,
        "strategic_risk_score": strategic_risk_score,
        "strategic_retention_score": strategic_retention_score,
        "projected_attrition_impact": high_risk_count * 15000,
        "optimization_gain": optimization_gain,
        "forecast_improvement": optimization_gain,
        "projected_stability": projected_stability,
        "health_index": health_index,
        "risk_label": risk_data["label"],
        "signal_color": risk_data["color"],
        "total_employees": len(filtered_df),
        "attrition_rate": attrition_rate,
        "overtime_percentage": overtime_percentage,
        "avg_income": round(filtered_df["MonthlyIncome"].mean(), 0),
        "avg_tenure": round(filtered_df["YearsAtCompany"].mean(), 1),
        "retention_score": retention_score,
        "workforce_stability": round((retention_score + (100 - overtime_percentage)) / 2, 1),
    }


def get_department_risk_ranking(df):
    """Composite department risk ranking, highest risk first."""

    dept_risk = df.groupby("Department").apply(
        lambda x: (
            (x["OverTime"] == "Yes").mean() * 30
            + (x["JobSatisfaction"] <= 2).mean() * 25
            + (x["WorkLifeBalance"] <= 2).mean() * 20
        )
    ).sort_values(ascending=False)

    return pd.DataFrame(
        {"Department": dept_risk.index, "Risk Score": dept_risk.values.round(1)}
    )


def get_impact_simulation(projected_attrition_impact, optimization_gain):
    """Executive savings/retention projections from a risk-reduction scenario."""

    return {
        "projected_savings": round(projected_attrition_impact * 0.22, 0),
        "projected_retention_gain": round(optimization_gain * 1.4, 1),
    }


def get_overtime_distribution_metrics(filtered_df):
    """Share of the workforce working overtime vs. not."""

    overtime_counts = filtered_df["OverTime"].value_counts()
    total = overtime_counts.sum()

    return {
        "overtime_pct": round(overtime_counts.get("Yes", 0) / total * 100, 1),
        "non_overtime_pct": round(overtime_counts.get("No", 0) / total * 100, 1),
    }
