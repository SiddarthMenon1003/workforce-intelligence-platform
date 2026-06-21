# =========================================================
# WORKFORCE RISK ENGINE
# =========================================================

def classify_risk(score):
    """
    Classify workforce risk level
    based on standardized thresholds.
    """

    if score < 30:

        return {
            "label":
            "Low Risk",

            "color":
            "#34D399",

            "status":
            "🟢 Low Workforce Risk"
        }

    elif score < 50:

        return {
            "label":
            "Moderate Risk",

            "color":
            "#C6A15B",

            "status":
            "🟡 Moderate Workforce Risk"
        }

    return {
        "label":
        "High Risk",

        "color":
        "#D97777",

        "status":
        "🔴 High Workforce Risk"
    }


# =========================================================
# WORKFORCE RISK SEVERITY
# =========================================================

def get_risk_severity(score):
    """
    Generate workforce
    severity messaging.
    """

    if score < 30:

        return (
            "success",
            "🟢 LOW RISK — Workforce stability remains strong."
        )

    elif score < 50:

        return (
            "warning",
            "🟡 MODERATE RISK — Burnout indicators increasing."
        )

    elif score < 70:

        return (
            "error",
            "🟠 HIGH RISK — Overtime pressure significantly impacting retention."
        )

    return (
        "error",
        "🔴 CRITICAL RISK — Severe workforce instability detected."
    )

# =========================================================
# RISK METER POSITION
# =========================================================

def get_meter_position(
    risk_percentage
):

    risk_label = (
        classify_risk(
            risk_percentage
        )["label"]
    )

    if risk_label == "Low Risk":

        return 18

    elif risk_label == "Moderate Risk":

        return 42

    return 76

# =========================================================
# WORKFORCE HEALTH ENGINE
# =========================================================

def classify_workforce_health(
    retention_percent
):

    if retention_percent >= 85:

        return {
            "label":
            "Excellent Stability",

            "color":
            "#22C55E"
        }

    elif retention_percent >= 75:

        return {
            "label":
            "Healthy Workforce",

            "color":
            "#60A5FA"
        }

    elif retention_percent >= 65:

        return {
            "label":
            "Moderate Stability",

            "color":
            "#FBBF24"
        }

    return {
        "label":
        "Retention Risk",

        "color":
        "#EF4444"
    }

def classify_overtime_risk(overtime_percent):
    """Classify overtime pressure level."""

    if overtime_percent >= 60:
        return {
            "label": "High",
            "color": "#EF4444",
            "severity": "critical"
        }

    elif overtime_percent >= 30:
        return {
            "label": "Moderate",
            "color": "#FBBF24",
            "severity": "warning"
        }

    return {
        "label": "Low",
        "color": "#22C55E",
        "severity": "healthy"
    }

def get_primary_driver(
    attrition_rate,
    overtime_percentage,
    engagement_score
):
    """Determine dominant workforce driver."""

    drivers = {
        "Overtime Exposure": overtime_percentage,
        "Attrition Risk": attrition_rate,
        "Employee Engagement": engagement_score
    }

    top_driver = max(
        drivers,
        key=drivers.get
    )

    return {
        "driver": top_driver,
        "score": round(drivers[top_driver], 1)
    }


def generate_risk_scores(
    dataframe
):
    """Generate employee risk scores."""

    risk_df = dataframe.copy()

    risk_score = (

        (risk_df["OverTime"] == "Yes")
        .astype(int) * 30 +

        (risk_df["JobSatisfaction"] <= 2)
        .astype(int) * 25 +

        (risk_df["WorkLifeBalance"] <= 2)
        .astype(int) * 20 +

        (risk_df["YearsAtCompany"] <= 2)
        .astype(int) * 15 +

        (
            risk_df["MonthlyIncome"]
            <
            risk_df["MonthlyIncome"].median()
        )
        .astype(int) * 10
    )

    risk_df["RiskScore"] = (
        risk_score
    )

    risk_df["RiskLevel"] = (
        risk_df["RiskScore"]
        .apply(
            lambda x:
            classify_risk(x)["label"]
        )
    )

    return risk_df

def calculate_live_attrition_risk(
    overtime,
    job_satisfaction,
    worklife,
    years_company,
    monthly_income
):
    """Live employee attrition risk estimation."""

    return round(
        (
            (overtime == "Yes") * 40 +
            (job_satisfaction <= 2) * 25 +
            (worklife <= 2) * 20 +
            (years_company <= 2) * 10 +
            (monthly_income < 4000) * 5
        ),
        1
    )



