# =========================================================
# WORKFORCE INSIGHTS ENGINE
# =========================================================

def get_department_recommendation(
    selected_department
):
    """
    Generate department-level
    workforce recommendations.
    """

    recommendations = {

        "All":
        """
Recommended organizational initiatives:

• Implement enterprise-wide burnout monitoring

• Reduce sustained overtime dependency

• Strengthen retention-focused HR policies

• Improve workforce allocation strategies

• Increase employee wellness engagement
""",

        "Sales":
        """
Recommended Sales department initiatives:

• Reduce aggressive overtime exposure

• Improve incentive structures

• Strengthen employee engagement

• Introduce workload balancing

• Enhance managerial monitoring
""",

        "Research & Development":
        """
Recommended R&D department initiatives:

• Improve long-term engagement programs

• Reduce project burnout exposure

• Strengthen workforce development

• Improve career progression visibility

• Enhance collaborative workload distribution
""",

        "Human Resources":
        """
Recommended HR department initiatives:

• Improve workload distribution

• Strengthen support resources

• Reduce administrative pressure

• Enhance wellness monitoring

• Improve staffing support mechanisms
"""
    }

    return recommendations[
        selected_department
    ]

# =========================================================
# STRATEGIC OUTLOOK ENGINE
# =========================================================

def get_strategic_outlook(
    risk_label,
    selected_department
):
    """
    Generate strategic workforce
    outlook messaging.
    """

    if risk_label == "Low Risk":

        return {

            "heading":
            "Strong workforce sustainability outlook",

            "text":
            f"The {selected_department if selected_department != 'All' else 'organization'} currently demonstrates healthy workforce sustainability with manageable attrition exposure."
        }

    elif risk_label == "Moderate Risk":

        return {

            "heading":
            "Emerging workforce instability indicators",

            "text":
            "Emerging workforce instability indicators require leadership attention and proactive retention planning."
        }

    return {

        "heading":
        "Immediate workforce intervention required",

        "text":
        "Significant workforce instability signals require immediate operational and retention intervention."
    }

# =========================================================
# WORKFORCE OPTIMIZATION ENGINE
# =========================================================

def get_optimization_projection(
    selected_department,
    projected_retention_gain,
    projected_savings
):
    """
    Generate workforce
    optimization projection.
    """

    if selected_department == "All":

        return f"""
### Strategic Workforce Optimization Projection

If current workforce recommendations are implemented:

• Predicted retention improvement:
**+{projected_retention_gain}%**

• Estimated annual organizational savings:
**${projected_savings:,.0f}**

• Reduced workforce instability exposure

• Improved workforce sustainability

• Increased operational continuity
"""

    return f"""
### {selected_department} Optimization Projection

If department-level workforce initiatives are implemented:

• Predicted department retention improvement:
**+{projected_retention_gain}%**

• Estimated department workforce savings:
**${projected_savings:,.0f}**
"""

# =========================================================
# DEPARTMENT INTELLIGENCE ENGINE
# =========================================================

def get_department_content(
    selected_department,
    optimization_gain
):

    department_messages = {

        "All": {
            "narrative": f"""
AI workforce intelligence predicts that the organization
currently faces moderate workforce sustainability pressure
driven primarily by overtime exposure, declining engagement,
and emerging retention instability.

Predictive workforce simulations indicate that proactive
burnout reduction initiatives and workforce balancing
strategies could improve long-term workforce stability
by approximately **{optimization_gain}%**.
""",

            "decision": """
### Recommended Immediate Executive Action

Prioritize organization-wide overtime reduction and
predictive workforce monitoring initiatives to stabilize
high-risk employee segments and improve long-term
workforce sustainability outcomes.
""",

            "summary": """
The organization currently demonstrates moderate
predictive workforce instability driven primarily
by overtime exposure, burnout pressure, and
employee engagement decline.

Strategic workforce optimization initiatives
present strong opportunities to improve retention,
reduce operational instability, and strengthen
long-term organizational sustainability.
"""
        },

        "Sales": {
            "narrative": """
AI workforce intelligence identifies the Sales department
as experiencing elevated performance-related operational
pressure and workforce fatigue exposure.
""",

            "decision": """
### Recommended Sales Leadership Action

Reduce sustained performance workload exposure and
improve employee engagement reinforcement mechanisms.
""",

            "summary": """
The Sales department demonstrates elevated workforce
pressure associated with operational workload and
workforce sustainability challenges.
"""
        },

        "Research & Development": {
            "narrative": """
AI workforce intelligence identifies long-term project
fatigue and workforce engagement sustainability as
primary retention challenges within R&D.
""",

            "decision": """
### Recommended R&D Leadership Action

Improve collaborative workload balancing and strengthen
long-term workforce engagement initiatives.
""",

            "summary": """
The R&D department demonstrates workforce sustainability
pressure linked to long-term engagement and burnout risk.
"""
        },

        "Human Resources": {
            "narrative": """
AI workforce intelligence identifies workforce coordination
pressure and administrative workload exposure as primary
drivers of operational fatigue within HR.
""",

            "decision": """
### Recommended HR Leadership Action

Reduce administrative workforce pressure and improve
employee support sustainability mechanisms.
""",

            "summary": """
The HR department demonstrates elevated operational
pressure associated with coordination and support demands.
"""
        }
    }

    return department_messages[
        selected_department
    ]

# =========================================================
# EXECUTIVE POSITION ENGINE
# =========================================================

def get_executive_position(
    risk_label
):

    if risk_label == "Low Risk":

        return {

            "title":
            "Strong Workforce Stability",

            "text":
            "Current workforce intelligence indicates strong sustainability with healthy retention conditions and stable workforce performance."
        }

    elif risk_label == "Moderate Risk":

        return {

            "title":
            "Moderate Workforce Stability",

            "text":
            "Current workforce intelligence indicates moderate sustainability with emerging retention pressure areas requiring leadership intervention and operational optimization strategies."
        }

    return {

        "title":
        "Critical Workforce Risk",

        "text":
        "Current workforce intelligence indicates significant workforce instability requiring immediate executive intervention and workforce stabilization measures."
    }

# =========================================================
# EXECUTIVE PRIORITY ENGINE
# =========================================================

def get_executive_priority(
    selected_department
):

    priorities = {

        "All": {

            "title":
            "Reduce Overtime Exposure",

            "text":
            "Target workload balancing and burnout reduction to improve workforce stability."
        },

        "Sales": {

            "title":
            "Reduce Performance Pressure",

            "text":
            "Focus on workload balancing and sustainable performance management."
        },

        "Research & Development": {

            "title":
            "Improve Long-Term Engagement",

            "text":
            "Strengthen workforce engagement and reduce project fatigue exposure."
        },

        "Human Resources": {

            "title":
            "Reduce Administrative Load",

            "text":
            "Improve workforce support processes and reduce coordination pressure."
        }
    }

    return priorities[
        selected_department
    ]

# =========================================================
# HEALTH ASSESSMENT ENGINE
# =========================================================

def get_health_assessment(
    health_index,
    selected_department
):

    entity = (
        selected_department
        if selected_department != "All"
        else "organization"
    )

    if health_index >= 75:

        return {

            "title":
            "Healthy Workforce",

            "text":
            f"The {entity} currently demonstrates strong workforce sustainability with healthy engagement indicators and stable operational retention conditions."
        }

    elif health_index >= 50:

        return {

            "title":
            "Moderate Stability",

            "text":
            f"The {entity} demonstrates moderate workforce sustainability with emerging burnout and retention pressure indicators."
        }

    return {

        "title":
        "High Workforce Instability",

        "text":
        f"The {entity} demonstrates elevated workforce instability driven by burnout exposure and operational workload imbalance."
    }

# =========================================================
# WORKFORCE ANALYTICS DEPARTMENT ENGINE
# =========================================================

def get_workforce_department_content(
    selected_department
):

    department_content = {

        "All": {
            "signal_title":
            "Organizational Workforce Signal",

            "signal_text":
            "Enterprise workforce analytics indicate moderate operational stability with department-specific workforce variation."
        },

        "Sales": {
            "signal_title":
            "High Workforce Pressure",

            "signal_text":
            "Sales operations show elevated overtime exposure and stronger attrition sensitivity, indicating higher workforce pressure and retention risk."
        },

        "Research & Development": {
            "signal_title":
            "Stable Workforce Environment",

            "signal_text":
            "R&D demonstrates stronger workforce stability, lower attrition sensitivity, and healthier organizational continuity."
        },

        "Human Resources": {
            "signal_title":
            "Balanced Workforce Activity",

            "signal_text":
            "HR operations reflect balanced workforce allocation with controlled overtime exposure and moderate organizational stability."
        }
    }

    return department_content[
        selected_department
    ]

# =========================================================
# WORKFORCE VULNERABILITY ENGINE
# =========================================================

def get_workforce_vulnerability(
    selected_department
):

    if selected_department == "All":

        return """
### Workforce Vulnerability

The organization demonstrates elevated overtime-related
workforce instability indicators.
"""

    return f"""
### Workforce Vulnerability

The {selected_department} department demonstrates elevated
overtime-related workforce instability indicators.
"""

# =========================================================
# WORKFORCE RISK DRIVER ENGINE
# =========================================================

def get_primary_risk_driver():

    return """
### Primary Workforce Risk Driver

Operational workload pressure and overtime
exposure remain major workforce retention
challenges.
"""

# =========================================================
# RISK DRIVER ENGINE
# =========================================================

def get_risk_driver(
    selected_department
):

    risk_driver_map = {

        "Sales": (
            "Travel Fatigue",
            "Field Workforce Burnout"
        ),

        "Research & Development": (
            "Overtime Exposure",
            "Workforce Burnout Signal"
        ),

        "Human Resources": (
            "Retention Pressure",
            "Talent Stability Concern"
        )
    }

    return risk_driver_map.get(
        selected_department,
        (
            "Overtime Exposure",
            "Cross-Department Burnout"
        )
    )

# =========================================================
# RISK PERSONA ENGINE
# =========================================================

def get_risk_personas(
    selected_department
):

    personas = {

        "All": (
            """
### High-Risk Persona 1

Early-career employees experiencing:
- Sustained overtime exposure
- Low work-life balance
- High workload pressure
- Reduced engagement levels
""",

            """
### High-Risk Persona 2

Employees demonstrating:
- Low job satisfaction
- Operational burnout indicators
- Short organizational tenure
- Elevated workforce instability risk
"""
        ),

        "Sales": (
            """
### Sales Performance Burnout Persona

Employees experiencing:
- Aggressive performance targets
- Sustained overtime exposure
- High client-facing workload
- Reduced engagement stability
""",

            """
### Sales Retention Risk Persona

Employees demonstrating:
- Reduced incentive satisfaction
- Elevated operational fatigue
- High performance pressure
- Increased workforce instability
"""
        ),

        "Research & Development": (
            """
### R&D Burnout Persona

Employees experiencing:
- Long project cycles
- Cognitive workload pressure
- Reduced work-life balance
- Engagement fatigue
""",

            """
### Innovation Retention Risk Persona

Employees demonstrating:
- Career stagnation concerns
- Reduced collaborative engagement
- Long-term workload fatigue
- Elevated attrition vulnerability
"""
        ),

        "Human Resources": (
            """
### HR Operational Pressure Persona

Employees experiencing:
- Administrative overload
- Workforce support fatigue
- Sustained operational pressure
- Reduced wellness balance
""",

            """
### HR Workforce Fatigue Persona

Employees demonstrating:
- Employee support burnout
- Workforce coordination pressure
- Reduced engagement sustainability
- Elevated retention vulnerability
"""
        )
    }

    return personas[selected_department]

# =========================================================
# RISK SIMULATION ENGINE
# =========================================================

def get_risk_simulation(
    selected_department,
    simulated_risk_reduction,
    projected_risk
):

    if selected_department == "All":

        return f"""
### Workforce Optimization Simulation

If overtime exposure is reduced by approximately 20%:

• Estimated high-risk workforce reduces by **{simulated_risk_reduction}%**

• Projected workforce risk exposure drops to **{projected_risk}%**

• Workforce stability and retention probability improve significantly

• Organizational burnout exposure decreases across critical employee groups
"""

    return f"""
### {selected_department} Workforce Optimization Simulation

If overtime exposure and workload imbalance are reduced
within the {selected_department} department:

• Estimated department risk exposure reduces by **{simulated_risk_reduction}%**

• Projected department instability decreases to **{projected_risk}%**

• Employee engagement and retention stability improve

• Department workforce sustainability strengthens significantly
"""

# =========================================================
# PREDICTIVE INTELLIGENCE ENGINE
# =========================================================

def get_predictive_intelligence(
    selected_department,
    high_risk_count,
    high_risk_percentage
):

    if selected_department == "All":

        return f"""
### Organization-Wide Predictive Intelligence

Predictive workforce analytics indicate that
employees exposed to sustained overtime pressure,
low satisfaction, and burnout indicators demonstrate
significantly elevated attrition risk.

Current analysis identifies **{high_risk_count}**
employees within the high-risk workforce category,
representing approximately **{high_risk_percentage}%**
of the workforce population.
"""

    elif selected_department == "Sales":

        return """
### Sales Department Predictive Intelligence

The Sales department demonstrates elevated workforce
instability associated with sustained performance pressure,
high overtime exposure, and engagement fatigue.
"""

    elif selected_department == "Research & Development":

        return """
### R&D Department Predictive Intelligence

The Research & Development department demonstrates
workforce instability patterns associated with long-term
project fatigue and engagement sustainability challenges.
"""

    return """
### Human Resources Predictive Intelligence

The Human Resources department demonstrates workforce
pressure associated with operational coordination demands,
employee support fatigue, and sustained administrative load.
"""

# =========================================================
# COST EXPOSURE ENGINE
# =========================================================

def get_cost_exposure(
    selected_department,
    projected_attrition_impact
):

    if selected_department == "All":

        return f"""
### Estimated Attrition Exposure: ${projected_attrition_impact:,.0f}

Projected workforce instability impact includes:

• Recruitment costs
• Onboarding expenses
• Productivity disruption
• Workforce transition instability
• Operational performance decline
"""

    return f"""
### Estimated {selected_department} Department Exposure:
${projected_attrition_impact:,.0f}

Projected department instability impact includes:

• Workforce replacement costs
• Operational productivity disruption
• Team performance instability
• Increased workforce transition exposure
"""

# =========================================================
# STRATEGIC PRIORITY ENGINE
# =========================================================

def get_risk_action_priorities(
    selected_department
):

    priorities = {

        "All": """
1. Reduce sustained overtime dependency
2. Improve employee engagement initiatives
3. Strengthen workforce wellness monitoring
4. Increase retention-focused HR interventions
5. Improve workforce allocation efficiency
6. Develop predictive workforce monitoring systems
""",

        "Sales": """
1. Reduce aggressive performance workload pressure
2. Improve employee incentive sustainability
3. Strengthen sales engagement initiatives
4. Improve workforce balancing strategies
5. Enhance retention-focused managerial oversight
6. Reduce sustained overtime dependency
""",

        "Research & Development": """
1. Improve long-term workforce engagement
2. Reduce project-related burnout exposure
3. Strengthen workforce innovation pathways
4. Improve collaborative workload balancing
5. Enhance career growth visibility
6. Improve retention-focused development planning
""",

        "Human Resources": """
1. Reduce administrative workload pressure
2. Improve workforce support sustainability
3. Strengthen employee wellness initiatives
4. Improve operational staffing balance
5. Enhance workforce coordination support
6. Reduce burnout exposure across HR operations
"""
    }

    return priorities[selected_department]

# =========================================================
# EXECUTIVE RISK POSITION ENGINE
# =========================================================

def get_risk_executive_position(
    risk_label
):

    if risk_label == "Low Risk":

        return {

            "title":
            "Strong Workforce Stability",

            "text":
            "Current workforce intelligence indicates strong workforce sustainability with healthy retention conditions and stable organizational performance."
        }

    elif risk_label == "Moderate Risk":

        return {

            "title":
            "Moderate Workforce Stability",

            "text":
            "Current workforce intelligence indicates a moderate workforce sustainability profile with measurable retention opportunity and emerging organizational pressure areas requiring leadership attention."
        }

    return {

        "title":
        "Critical Workforce Exposure",

        "text":
        "Current workforce intelligence indicates elevated workforce instability requiring immediate intervention and proactive workforce stabilization initiatives."
    }

# =========================================================
# EXECUTIVE RISK SUMMARY ENGINE
# =========================================================

def get_risk_summary(
    selected_department,
    high_risk_percentage,
    risk_level
):

    if selected_department == "All":

        return (
            f"Workforce intelligence indicates "
            f"{high_risk_percentage}% high-risk workforce "
            f"concentration across organizational segments, "
            f"requiring proactive workforce monitoring."
        )

    return (
        f"{selected_department} demonstrates "
        f"{risk_level.lower()} with "
        f"{high_risk_percentage}% predictive workforce "
        f"exposure requiring targeted intervention."
    )

# =========================================================
# OVERVIEW EXECUTIVE BRIEF ENGINE
# =========================================================

def get_overview_executive_brief(
    risk_label
):

    if risk_label == "Low Risk":

        return (
            "Healthy Workforce Environment",
            "Operational Workforce Stability"
        )

    elif risk_label == "Moderate Risk":

        return (
            "Moderate Attrition Exposure",
            "Overtime Workforce Burnout"
        )

    return (
        "Elevated Attrition Exposure",
        "Critical Workforce Burnout"
    )

# =========================================================
# OVERVIEW INSIGHTS ENGINE
# =========================================================

def get_overview_insights(
    selected_department,
    highest_attrition_dept,
    stable_dept,
    department_attrition=None,
    overtime_percentage=None
):

    if selected_department == "All":

        return f"""
### Organizational Workforce Intelligence

• Highest workforce instability detected in **{highest_attrition_dept}**

• Strongest workforce stability observed in **{stable_dept}**

• Overtime exposure remains the primary workforce risk driver

• Workforce optimization initiatives present significant retention opportunities

• Predictive workforce intelligence indicates moderate organizational sustainability pressure
"""

    return f"""
### {selected_department} Workforce Intelligence

• Department attrition rate: **{department_attrition:.1f}%**

• Overtime exposure: **{overtime_percentage:.1f}%**

• Workforce sustainability requires continued monitoring

• Employee engagement and workload balance remain key retention drivers

• Predictive workforce analytics indicate moderate optimization opportunity
"""

def get_strategy_maturity(
    health_index
):
    """Workforce strategy maturity classification."""

    if health_index >= 80:

        return {
            "level":
            "Optimized Workforce Strategy",

            "icon":
            "🟢"
        }

    elif health_index >= 60:

        return {
            "level":
            "Maturing Workforce Strategy",

            "icon":
            "🟡"
        }

    elif health_index >= 40:

        return {
            "level":
            "Developing Workforce Strategy",

            "icon":
            "🟠"
        }

    return {
        "level":
        "Reactive Workforce Strategy",

        "icon":
        "🔴"
    }