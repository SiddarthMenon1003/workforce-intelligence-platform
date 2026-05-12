
# Employee Attrition Prediction & Workforce Strategy Optimization

## Overview

This project focuses on predicting employee attrition and generating business-driven workforce strategies using machine learning and analytics.

The objective is not only to identify employees likely to leave the organization, but also to understand the underlying drivers of attrition and recommend actionable retention strategies.

The project combines:
- Predictive analytics
- Workforce segmentation
- Business strategy
- Risk scoring
- HR decision support

---

# Business Problem

Employee attrition creates significant costs for organizations through:
- Recruitment expenses
- Training costs
- Productivity loss
- Team disruption

This project aims to answer:

"How can organizations proactively identify high-risk employees and reduce attrition using data-driven insights?"

---

# Dataset

Dataset Used:
- IBM HR Analytics Employee Attrition Dataset

File:
WA_Fn-UseC_-HR-Employee-Attrition.csv

---

# Project Workflow

## 1. Data Preprocessing
- Data cleaning
- Feature engineering
- Encoding categorical variables
- Tenure segmentation
- Income-based feature creation

---

## 2. Exploratory Data Analysis
Analysis performed on:
- Attrition distribution
- Overtime impact
- Salary trends
- Satisfaction metrics
- Tenure patterns
- Correlation analysis

---

## 3. Machine Learning Models

The following models were implemented and compared:

### Logistic Regression
- Baseline interpretable model
- Feature coefficient analysis

### Random Forest
- Non-linear ensemble model
- Feature importance analysis

### Gradient Boosting
- Final high-performance predictive model
- Risk scoring implementation

---

## 4. Model Evaluation

Models were evaluated using:
- Accuracy
- ROC-AUC
- Cross-validation
- ROC Curves
- Feature Importance
- Hyperparameter tuning

---

## 5. Business Analytics Layer

The project extends beyond prediction into strategic workforce analysis.

### Key Business Insights
- Overtime is the strongest attrition driver
- Early tenure employees are highly vulnerable
- Employees in first 2 years working overtime show the highest attrition risk
- Compensation and workplace satisfaction significantly impact retention

---

## 6. Risk Segmentation & Scoring

The project includes:
- Employee risk scoring
- High-risk employee identification
- Workforce segmentation
- Interaction analysis

This enables proactive HR intervention and workforce planning.

---

# Strategic Recommendations

Based on the analysis, the following actions are recommended:

1. Reduce overtime exposure for early-tenure employees
2. Strengthen onboarding and engagement programs
3. Implement targeted retention strategies
4. Monitor high-risk employees proactively
5. Optimize compensation structures

---

# Estimated Business Impact

Reducing attrition by even a small percentage can generate substantial savings through:
- Reduced hiring costs
- Lower training expenses
- Improved workforce stability

The project demonstrates how predictive analytics can support strategic HR decision-making.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

---

# Installation

Install required libraries using:

pip install -r requirements_clean_updated.txt

---

# Project Structure

├── Attrition Prediction Models.ipynb
├── WA_Fn-UseC_-HR-Employee-Attrition.csv
├── requirements_clean_updated.txt
├── requirements.txt
└── README.md

---

# Key Outcomes

- Built and compared multiple ML models
- Identified major attrition drivers
- Developed employee risk scoring system
- Generated business-oriented workforce insights
- Proposed actionable retention strategies

---

# Future Improvements

Potential future enhancements:
- Interactive dashboard using Streamlit or Power BI
- Real-time attrition monitoring
- SHAP explainability integration
- Deployment as HR analytics tool

---

# Author

Siddarth Menon

Master’s Student — Data Science & AI Strategy
emlyon business school
