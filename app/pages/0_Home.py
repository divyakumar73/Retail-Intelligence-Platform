from pathlib import Path
import sys

# ======================================================
# Make project root importable
# ======================================================
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st
import pandas as pd

from src.constants import (
    APP_TITLE,
    APP_SUBTITLE,
    RFM_FILE,
    REPEAT_FILE,
    COHORT_FILE,
    RULES_FILE,
    BASKET_FILE,
    SELLER_PERF_FILE,
    SELLER_REVIEW_FILE,
    SELLER_CATEGORY_FILE,
    TOP_CATEGORIES_FILE,
)
from src.kpis import (
    safe_read_csv,
    get_homepage_kpis,
    format_number,
    format_currency
)

# ======================================================
# Page Config
# ======================================================
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📊",
    layout="wide"
)

# ======================================================
# Load Core Files
# ======================================================
rfm_df = safe_read_csv(RFM_FILE)
repeat_df = safe_read_csv(REPEAT_FILE)
cohort_df = safe_read_csv(COHORT_FILE)

rules_df = safe_read_csv(RULES_FILE)
basket_df = safe_read_csv(BASKET_FILE)
top_categories_df = safe_read_csv(TOP_CATEGORIES_FILE)

seller_perf_df = safe_read_csv(SELLER_PERF_FILE)
seller_review_df = safe_read_csv(SELLER_REVIEW_FILE)
seller_category_df = safe_read_csv(SELLER_CATEGORY_FILE)

# ======================================================
# Helpers
# ======================================================
def status_label(df):
    return "Loaded" if df is not None and not df.empty else "Missing"


def file_rows(df):
    if df is not None and not df.empty:
        return len(df)
    return None


# ======================================================
# Homepage KPIs
# ======================================================
home_kpis = get_homepage_kpis()

total_customers = home_kpis.get("total_customers")
repeat_customers = home_kpis.get("repeat_customers")
repeat_rate = home_kpis.get("repeat_rate")
avg_customer_spend = home_kpis.get("avg_customer_spend")

# ======================================================
# Header
# ======================================================
st.title(APP_TITLE)
st.markdown(f"### {APP_SUBTITLE}")

st.markdown(
    """
    The **Retail Intelligence Platform** is a portfolio-grade e-commerce analytics solution built on the
    **Olist Brazilian E-Commerce dataset**.

    It combines **customer analytics, retention analysis, seller performance monitoring, and market basket insights**
    into a single Streamlit application designed for business-facing reporting and decision support.
    """
)

st.markdown("---")

# ======================================================
# Quick Business Snapshot
# ======================================================
st.subheader("Quick Business Snapshot")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Customers",
        format_number(total_customers) if total_customers is not None else "N/A"
    )

with col2:
    st.metric(
        "Repeat Customers",
        format_number(repeat_customers) if repeat_customers is not None else "N/A"
    )

with col3:
    st.metric(
        "Repeat Rate",
        f"{repeat_rate:.2f}%" if repeat_rate is not None else "N/A"
    )

with col4:
    st.metric(
        "Avg Customer Spend",
        format_currency(avg_customer_spend) if avg_customer_spend is not None else "N/A"
    )

st.markdown("---")

# ======================================================
# Project Overview
# ======================================================
st.subheader("Project Overview")
st.markdown(
    """
    This platform was designed to convert raw e-commerce marketplace data into a structured analytics layer
    that supports business questions across customers, retention, seller performance, and basket behavior.

    The project brings together:
    - **customer segmentation and repeat-purchase analysis**
    - **cohort-style retention summaries**
    - **seller / marketplace performance analytics**
    - **association-rule and basket analytics**
    - **dashboard-ready reporting outputs for business consumption**
    """
)

st.markdown("---")

# ======================================================
# Dashboard Modules
# ======================================================
st.subheader("Dashboard Modules")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        ### 1. Executive Dashboard
        High-level business summary focused on:
        - total customers and repeat customers
        - repeat rate and average customer spend
        - segment distribution and segment revenue contribution

        ### 2. Customer Segmentation
        Customer value and repeat-purchase analysis using RFM:
        - customer segments
        - segment distribution
        - revenue by segment
        - repeat customer summary

        ### 3. Cohort Retention Analysis
        Retention and repeat-order monitoring:
        - cohort business summary
        - repeat purchase summary
        - repeat purchase distribution
        """
    )

with col2:
    st.markdown(
        """
        ### 4. Market Basket Analysis
        Product co-purchase behavior and association rules:
        - basket summary and diagnostics
        - top categories by order presence
        - association rules for bundling and recommendation

        ### 5. Seller / Marketplace Analytics
        Seller-side marketplace performance monitoring:
        - seller revenue and order volume
        - seller review quality
        - category-level seller contribution
        """
    )

st.markdown("---")

# ======================================================
# Business Questions This Dashboard Answers
# ======================================================
st.subheader("Business Questions Answered")

st.markdown(
    """
    This platform is designed to support decision-making across multiple retail and marketplace functions:

    - **Customer Analytics** → Who are the highest-value customers and how can they be segmented?
    - **Retention & Lifecycle** → What share of customers come back and how frequently do they reorder?
    - **Basket Intelligence** → Which categories are frequently purchased together and where are bundling opportunities visible?
    - **Seller Performance** → Which sellers drive revenue and order volume, and how does seller quality compare?
    - **Marketplace Monitoring** → Which data assets are currently available to support dashboard reporting?
    """
)

st.markdown("---")

# ======================================================
# Data Assets Status
# ======================================================
st.subheader("Data Assets Status")

status_rows = [
    {"File": RFM_FILE, "Status": status_label(rfm_df), "Rows": file_rows(rfm_df)},
    {"File": REPEAT_FILE, "Status": status_label(repeat_df), "Rows": file_rows(repeat_df)},
    {"File": COHORT_FILE, "Status": status_label(cohort_df), "Rows": file_rows(cohort_df)},
    {"File": RULES_FILE, "Status": status_label(rules_df), "Rows": file_rows(rules_df)},
    {"File": BASKET_FILE, "Status": status_label(basket_df), "Rows": file_rows(basket_df)},
    {"File": TOP_CATEGORIES_FILE, "Status": status_label(top_categories_df), "Rows": file_rows(top_categories_df)},
    {"File": SELLER_PERF_FILE, "Status": status_label(seller_perf_df), "Rows": file_rows(seller_perf_df)},
    {"File": SELLER_REVIEW_FILE, "Status": status_label(seller_review_df), "Rows": file_rows(seller_review_df)},
    {"File": SELLER_CATEGORY_FILE, "Status": status_label(seller_category_df), "Rows": file_rows(seller_category_df)},
]

status_df = pd.DataFrame(status_rows)
st.dataframe(status_df, use_container_width=True, hide_index=True)

st.markdown("---")

# ======================================================
# Notebook-to-Dashboard Pipeline
# ======================================================
st.subheader("Notebook to Dashboard Pipeline")

pipeline_rows = [
    {
        "Notebook": "Notebook 07",
        "Purpose": "Customer Segmentation (RFM)",
        "Key Outputs": "rfm_customer_segments.csv"
    },
    {
        "Notebook": "Notebook 08",
        "Purpose": "Cohort / Repeat Purchase Analysis",
        "Key Outputs": "repeat_purchase_summary.csv, cohort_business_summary.csv"
    },
    {
        "Notebook": "Notebook 09",
        "Purpose": "Market Basket Analysis",
        "Key Outputs": "association_rules.csv, basket_summary.csv, top_categories_by_order_presence.csv"
    },
    {
        "Notebook": "Notebook 10",
        "Purpose": "Seller / Marketplace Analytics",
        "Key Outputs": "seller_performance_summary.csv, seller_review_summary.csv, seller_category_summary.csv"
    },
]

pipeline_df = pd.DataFrame(pipeline_rows)
st.dataframe(pipeline_df, use_container_width=True, hide_index=True)

st.markdown("---")

# ======================================================
# Tech Stack
# ======================================================
st.subheader("Tech Stack")

st.markdown(
    """
    **Core stack used in this project:**

    - **Python** for data cleaning, transformation, KPI generation, and analytics workflows
    - **Pandas / NumPy** for data manipulation and aggregation
    - **Matplotlib / Seaborn / Plotly** for visual analytics
    - **mlxtend** for association-rule mining and market basket analysis
    - **Streamlit** for multi-page dashboard development
    - **Jupyter Notebooks** for modular analysis and report generation
    """
)

st.markdown("---")

# ======================================================
# Business Value Delivered
# ======================================================
st.subheader("Business Value Delivered")

st.markdown(
    """
    This dashboard is designed to move beyond descriptive reporting and support **actionable business decisions**:

    - identify **high-value customer segments** and repeat-purchase opportunities
    - monitor **retention and reorder behavior**
    - surface **cross-sell and bundling opportunities** from market basket analysis
    - track **seller concentration, revenue contribution, and review quality**
    - consolidate multiple retail analytics workflows into **one portfolio-grade BI interface**
    """
)

st.markdown("---")

# ======================================================
# Footer
# ======================================================
st.caption(
    "Retail Intelligence Platform | Olist E-Commerce Analytics Project | Streamlit Portfolio Dashboard"
)