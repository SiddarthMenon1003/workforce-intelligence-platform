from backend.risk_engine import (
    classify_risk,
    generate_risk_scores
)

REQUIRED_COLUMNS = [

    "Age",
    "Attrition",
    "Department",
    "JobSatisfaction",
    "MonthlyIncome",
    "OverTime",
    "WorkLifeBalance",
    "YearsAtCompany"
]

def validate_dataset(
    dataframe,
    required_columns
):
    """Validate uploaded dataset schema."""

    missing_columns = [
        col for col in required_columns
        if col not in dataframe.columns
    ]

    return missing_columns


def filter_department(
    dataframe,
    selected_department
):
    """Apply department filter."""

    if selected_department != "All":

        return dataframe[
            dataframe["Department"]
            == selected_department
        ]

    return dataframe.copy()

def get_overview_metrics(
    filtered_df
):
    """Overview KPI calculations."""

    total_employees = len(
        filtered_df
    )

    attrition_rate = round(
        (
            filtered_df[
                "Attrition"
            ] == "Yes"
        ).mean() * 100,
        1
    )

    high_risk_employees = len(
        filtered_df[
            filtered_df[
                "OverTime"
            ] == "Yes"
        ]
    )

    overtime_percentage = round(
        (
            filtered_df[
                "OverTime"
            ] == "Yes"
        ).mean() * 100,
        1
    )

    retention_percent = round(
        100 - attrition_rate,
        1
    )

    engagement_score = round(
        (
            retention_percent +
            (
                100 -
                overtime_percentage
            )
        ) / 2,
        1
    )

    return {
        "total_employees":
        total_employees,

        "attrition_rate":
        attrition_rate,

        "high_risk_employees":
        high_risk_employees,

        "overtime_percentage":
        overtime_percentage,

        "retention_percent":
        retention_percent,

        "engagement_score":
        engagement_score
    }

def get_department_intelligence(
    dataframe
):
    
    
    """Department attrition intelligence."""

    dept_attrition_calc = (
        dataframe
        .groupby("Department")
        ["Attrition"]
        .apply(
            lambda x:
            (x == "Yes").mean()
        )
    )

    highest_attrition_dept = (
        dept_attrition_calc.idxmax()
    )

    stable_dept = (
        dept_attrition_calc.idxmin()
    )

    return {
        "highest_attrition_dept":
        highest_attrition_dept,

        "stable_dept":
        stable_dept
    }

def get_department_overview_metrics(
    filtered_df,
    selected_department
):
    """Department overview metrics."""

    dept_df = (
        filtered_df
        if selected_department == "All"
        else filtered_df[
            filtered_df["Department"]
            == selected_department
        ]
    )

    dept_attrition = round(
        (
            dept_df["Attrition"]
            == "Yes"
        ).mean() * 100,
        1
    )

    dept_retention = round(
        100 - dept_attrition,
        1
    )

    dept_overtime = round(
        (
            dept_df["OverTime"]
            == "Yes"
        ).mean() * 100,
        1
    )

    dept_engagement = round(
        (
            dept_retention +
            (
                100 - dept_overtime
            )
        ) / 2,
        1
    )

    return {

        "dept_attrition":
            dept_attrition,

        "dept_retention":
            dept_retention,

        "dept_overtime":
            dept_overtime,

        "dept_engagement":
            dept_engagement
    }

def get_workforce_metrics(filtered_df):
    """Core workforce analytics calculations."""

    overtime_pct = round(
        (filtered_df['OverTime'] == 'Yes').mean() * 100,
        1
    )

    avg_income = round(
        filtered_df['MonthlyIncome'].mean(),
        0
    )

    dept_attrition = round(
        (filtered_df['Attrition'] == 'Yes').mean() * 100,
        1
    )

    # Workforce Stability Score
    stability_score = round(
        100 - (
            dept_attrition * 0.55 +
            overtime_pct * 0.45
        ),
        0
    )

    stability_score = max(
        35,
        min(stability_score, 95)
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

    return {
        "overtime_pct": overtime_pct,
        "avg_income": avg_income,
        "dept_attrition": dept_attrition,
        "stability_score": stability_score,
        "overtime_percentage": overtime_pct,
        "overtime_attrition_rate":
            overtime_attrition_rate,
        "no_overtime_attrition_rate":
            no_overtime_attrition_rate,
        "workforce_stability_score":
            workforce_stability_score
    }

def get_workforce_department_stats(
    filtered_df
):
    """Department workforce aggregations."""

    department_attrition = (
        filtered_df
        .groupby("Department")
        ["Attrition"]
        .apply(
            lambda x:
            (x == "Yes").mean() * 100
        )
        .reset_index()
    )

    department_attrition.columns = [
        "Department",
        "AttritionRate"
    ]

    department_income = (
        filtered_df
        .groupby("Department")
        ["MonthlyIncome"]
        .mean()
        .reset_index()
    )

    department_satisfaction = (
        filtered_df
        .groupby("Department")
        ["JobSatisfaction"]
        .mean()
        .reset_index()
    )

    overtime_distribution = (
        filtered_df
        ["OverTime"]
        .value_counts()
    )

    return {
        "department_attrition":
            department_attrition,

        "department_income":
            department_income,

        "department_satisfaction":
            department_satisfaction,

        "overtime_distribution":
            overtime_distribution
    }

def get_satisfaction_metrics(filtered_df):
    """Satisfaction & lifecycle analytics."""

    job_satisfaction = (
        filtered_df
        .groupby("JobSatisfaction")["Attrition"]
        .apply(lambda x: (x == "Yes").mean())
        .reset_index()
    )

    worklife_balance = (
        filtered_df
        .groupby("WorkLifeBalance")["Attrition"]
        .apply(lambda x: (x == "Yes").mean())
        .reset_index()
    )

    tenure_attrition = (
        filtered_df
        .groupby("YearsAtCompany")["Attrition"]
        .apply(lambda x: (x == "Yes").mean())
        .reset_index()
    )

    attrition_yes_income = filtered_df[
        filtered_df["Attrition"] == "Yes"
    ]["MonthlyIncome"]

    attrition_no_income = filtered_df[
        filtered_df["Attrition"] == "No"
    ]["MonthlyIncome"]

    return {
        "job_satisfaction": job_satisfaction,
        "worklife_balance": worklife_balance,
        "tenure_attrition": tenure_attrition,
        "attrition_yes_income": attrition_yes_income,
        "attrition_no_income": attrition_no_income
    }

import pandas as pd


def get_risk_metrics(filtered_df):
    """Generate workforce risk intelligence metrics."""

    risk_df = generate_risk_scores(
    filtered_df
    )

    # ==================================
    # RISK LEVELS
    # ==================================

    high_risk_mask = (
        risk_df['RiskScore'] >= 50
    )

    high_risk_count = len(
        risk_df[high_risk_mask]
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

    # ==================================
    # HEATMAP DATA
    # ==================================

    heatmap_data = risk_df.pivot_table(
        values='RiskScore',
        index='OverTime',
        columns='JobSatisfaction',
        aggfunc='mean',
        fill_value=0
    )

    return {
        "risk_df": risk_df,
        "high_risk_count": high_risk_count,
        "avg_risk_score": avg_risk_score,
        "high_risk_percentage": high_risk_percentage,
        "retention_probability": retention_probability,
        "projected_attrition_impact":
            projected_attrition_impact,
        "optimization_gain":
            optimization_gain,
        "simulated_risk_reduction":
            simulated_risk_reduction,
        "projected_risk":
            projected_risk,
        "heatmap_data":
            heatmap_data
    }


def get_strategic_metrics(filtered_df):
    """Generate strategic workforce metrics."""

    # ==================================
    # CORE WORKFORCE METRICS
    # ==================================

    total_employees = len(
        filtered_df
    )

    attrition_rate = round(
        (
            filtered_df["Attrition"]
            == "Yes"
        ).mean() * 100,
        1
    )

    overtime_percentage = round(
        (
            filtered_df["OverTime"]
            == "Yes"
        ).mean() * 100,
        1
    )

    avg_income = round(
        filtered_df[
            "MonthlyIncome"
        ].mean(),
        0
    )

    avg_tenure = round(
        filtered_df[
            "YearsAtCompany"
        ].mean(),
        1
    )

    retention_score = round(
        100 - attrition_rate,
        1
    )

    workforce_stability = round(
        (
            retention_score +
            (
                100 -
                overtime_percentage
            )
        ) / 2,
        1
    )

    # ==================================
    # RISK SCORE GENERATION
    # ==================================

    risk_df = generate_risk_scores(
        filtered_df
    )

    high_risk_count = len(
        risk_df[
            risk_df["RiskLevel"]
            == "High Risk"
        ]
    )

    # ==================================
    # STRATEGIC EXECUTIVE METRICS
    # ==================================

    strategic_risk_score = round(
        risk_df["RiskScore"].mean(),
        1
    )
    

    strategic_retention_score = round(
        100 - strategic_risk_score,
        1
    )

    projected_attrition_impact = (
        high_risk_count * 15000
    )

    optimization_gain = round(
        strategic_retention_score * 0.12,
        1
    )

    forecast_improvement = round(
        optimization_gain,
        1
    )

    projected_stability = round(
        min(
            strategic_retention_score +
            forecast_improvement,
            100
        ),
        1
    )

    # ==================================
    # WORKFORCE HEALTH INDEX
    # ==================================

    avg_job_satisfaction = round(
        filtered_df[
            "JobSatisfaction"
        ].mean() * 20,
        1
    )

    avg_worklife_balance = round(
        filtered_df[
            "WorkLifeBalance"
        ].mean() * 20,
        1
    )

    overtime_penalty = round(
        overtime_percentage * 0.35,
        1
    )

    attrition_penalty = round(
        attrition_rate * 0.45,
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

    health_index = max(
        0,
        min(100, health_index)
    )

    # ==================================
    # RISK SIGNALS
    # ==================================

    risk_data = classify_risk(
        strategic_risk_score
    )

    risk_label = (
        risk_data["label"]
    )

    signal_color = (
        risk_data["color"]
    )

    # ==================================
    # RETURN
    # ==================================

    return {

        "high_risk_count":
            high_risk_count,

        "strategic_risk_score":
            strategic_risk_score,

        "strategic_retention_score":
            strategic_retention_score,

        "projected_attrition_impact":
            projected_attrition_impact,

        "optimization_gain":
            optimization_gain,

        "forecast_improvement":
            forecast_improvement,

        "projected_stability":
            projected_stability,

        "health_index":
            health_index,

        "risk_label":
            risk_label,

        "signal_color":
            signal_color,

        "total_employees":
            total_employees,

        "attrition_rate":
            attrition_rate,

        "overtime_percentage":
            overtime_percentage,

        "avg_income":
            avg_income,

        "avg_tenure":
            avg_tenure,

        "retention_score":
            retention_score,

        "workforce_stability":
            workforce_stability
    }

def get_department_risk_ranking(df):
    """Department workforce risk ranking."""

    dept_risk = df.groupby("Department").apply(
        lambda x: (
            (
                (x["OverTime"] == "Yes").mean() * 30
            ) +
            (
                (x["JobSatisfaction"] <= 2).mean() * 25
            ) +
            (
                (x["WorkLifeBalance"] <= 2).mean() * 20
            )
        )
    ).sort_values(ascending=False)

    ranking_df = pd.DataFrame({
        "Department": dept_risk.index,
        "Risk Score": dept_risk.values.round(1)
    })

    return ranking_df

def get_impact_simulation(
    projected_attrition_impact,
    optimization_gain
):
    """Executive impact simulation metrics."""

    projected_savings = round(
        projected_attrition_impact * 0.22,
        0
    )

    projected_retention_gain = round(
        optimization_gain * 1.4,
        1
    )

    return {
        "projected_savings":
            projected_savings,

        "projected_retention_gain":
            projected_retention_gain
    }

def get_overtime_distribution_metrics(
    filtered_df
):
    """Overtime workforce distribution."""

    overtime_counts = (
        filtered_df["OverTime"]
        .value_counts()
    )

    total = overtime_counts.sum()

    overtime_pct = round(
        overtime_counts.get("Yes", 0)
        / total * 100,
        1
    )

    non_overtime_pct = round(
        overtime_counts.get("No", 0)
        / total * 100,
        1
    )

    return {
        "overtime_pct":
            overtime_pct,

        "non_overtime_pct":
            non_overtime_pct
    }
