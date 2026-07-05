import streamlit as st
import pandas as pd
import plotly.express as px

from src.constants import APP_TITLE, RFM_FILE, REPEAT_FILE
from src.kpis import (
    safe_read_csv,
    file_available,
    find_col,
    format_number,
    format_currency,
    format_percent,
    get_customer_segmentation_kpis
)

# ======================================================
# Page Config
# ======================================================
st.set_page_config(
    page_title="Executive Dashboard",
    page_icon="📈",
    layout="wide"
)

# ======================================================
# Page Header
# ======================================================
st.title("Executive Dashboard")
st.markdown(
    """
    High-level business overview of the retail analytics platform.  
    This page summarizes customer scale, repeat behavior, segment contribution,
    and current data asset readiness.
    """
)

st.markdown("---")

# ======================================================
# Load Core Data
# ======================================================
rfm_df = safe_read_csv(RFM_FILE)
repeat_df = safe_read_csv(REPEAT_FILE)

if not file_available(rfm_df):
    st.error(f"Missing file: `reports/{RFM_FILE}`")
    st.stop()

# ======================================================
# Detect RFM Columns Dynamically
# ======================================================
customer_col = find_col(rfm_df, ["customer_unique_id", "customer_id"])
recency_col = find_col(rfm_df, ["recency"])
frequency_col = find_col(rfm_df, ["frequency"])
monetary_col = find_col(rfm_df, ["monetary_value", "monetary", "revenue", "total_spent"])
segment_col = find_col(rfm_df, ["segment", "Segment", "cluster", "Cluster"])

# ======================================================
# KPI Calculations
# ======================================================
kpis = get_customer_segmentation_kpis()

total_customers = kpis.get("total_customers")
repeat_customers = kpis.get("repeat_customers")
repeat_rate = kpis.get("repeat_rate")
avg_customer_spend = kpis.get("avg_customer_spend")

# Additional executive KPIs from RFM
avg_recency = None
avg_frequency = None
avg_monetary = None

if recency_col:
    avg_recency = pd.to_numeric(rfm_df[recency_col], errors="coerce").mean()

if frequency_col:
    avg_frequency = pd.to_numeric(rfm_df[frequency_col], errors="coerce").mean()

if monetary_col:
    avg_monetary = pd.to_numeric(rfm_df[monetary_col], errors="coerce").mean()

# ======================================================
# KPI Cards - Row 1
# ======================================================
st.subheader("Business Snapshot")

kpi1, kpi2, kpi3, kpi4 = st.columns(4)

with kpi1:
    st.metric("Total Customers", format_number(total_customers))

with kpi2:
    st.metric(
        "Repeat Customers",
        format_number(repeat_customers) if repeat_customers is not None else "N/A"
    )

with kpi3:
    st.metric(
        "Repeat Rate",
        format_percent(repeat_rate) if repeat_rate is not None else "N/A"
    )

with kpi4:
    st.metric(
        "Average Customer Spend",
        format_currency(avg_customer_spend) if avg_customer_spend is not None else "N/A"
    )

# ======================================================
# KPI Cards - Row 2
# ======================================================
kpi5, kpi6, kpi7 = st.columns(3)

with kpi5:
    st.metric(
        "Average Recency",
        f"{avg_recency:.2f}" if avg_recency is not None else "N/A"
    )

with kpi6:
    st.metric(
        "Average Frequency",
        f"{avg_frequency:.2f}" if avg_frequency is not None else "N/A"
    )

with kpi7:
    st.metric(
        "Average Monetary Value",
        format_currency(avg_monetary) if avg_monetary is not None else "N/A"
    )

st.markdown("---")

# ======================================================
# Segment Distribution + Revenue
# ======================================================
seg_col1, seg_col2 = st.columns(2)

with seg_col1:
    st.subheader("Customer Segment Distribution")

    if segment_col:
        segment_dist = (
            rfm_df.groupby(segment_col)
            .size()
            .reset_index(name="customer_count")
            .sort_values("customer_count", ascending=False)
        )

        fig_dist = px.bar(
            segment_dist,
            x=segment_col,
            y="customer_count",
            text="customer_count",
            title="Customers by Segment"
        )
        fig_dist.update_layout(
            xaxis_title="Segment",
            yaxis_title="Customer Count"
        )
        st.plotly_chart(fig_dist, use_container_width=True)
    else:
        st.info("Segment distribution data not available.")

with seg_col2:
    st.subheader("Revenue Contribution by Segment")

    if segment_col and monetary_col:
        segment_revenue = (
            rfm_df.groupby(segment_col, dropna=False)[monetary_col]
            .sum()
            .reset_index()
            .sort_values(monetary_col, ascending=False)
        )

        fig_rev = px.bar(
            segment_revenue,
            x=segment_col,
            y=monetary_col,
            text=monetary_col,
            title="Revenue by Segment"
        )
        fig_rev.update_layout(
            xaxis_title="Segment",
            yaxis_title="Revenue"
        )
        st.plotly_chart(fig_rev, use_container_width=True)
    else:
        segment_revenue = None
        st.info("Segment revenue data not available.")

st.markdown("---")

# ======================================================
# Top Segment Revenue Summary Table
# ======================================================
st.subheader("Top Segment Revenue Summary")

if segment_col and monetary_col:
    top_segment_table = (
        rfm_df.groupby(segment_col, dropna=False)[monetary_col]
        .sum()
        .reset_index()
        .sort_values(monetary_col, ascending=False)
        .copy()
    )

    top_segment_table[monetary_col] = pd.to_numeric(
        top_segment_table[monetary_col],
        errors="coerce"
    ).round(2)

    st.dataframe(
        top_segment_table.head(15),
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("Segment revenue summary not available.")

st.markdown("---")

# ======================================================
# Data Readiness / Asset Status
# ======================================================
st.subheader("Current Data Asset Readiness")

status_rows = [
    {
        "Asset": "RFM Customer Segments",
        "Status": "Loaded" if file_available(rfm_df) else "Missing"
    },
    {
        "Asset": "Repeat Purchase Summary",
        "Status": "Loaded" if file_available(repeat_df) else "Missing"
    }
]

status_df = pd.DataFrame(status_rows)
st.dataframe(status_df, use_container_width=True, hide_index=True)

st.markdown("---")

# ======================================================
# Executive Interpretation
# ======================================================
st.subheader("Executive Interpretation")
st.markdown(
    """
    - The dashboard currently uses **customer segmentation outputs** as the primary executive summary layer.
    - **Segment distribution** shows how customers are distributed across behavioral and value-based buckets.
    - **Revenue by segment** highlights which customer groups contribute the most to overall monetary value.
    - **Repeat-customer metrics** provide an early signal of retention strength and customer lifecycle quality.
    - As more summary exports are added, this page can be extended with order trends, state-wise revenue, top categories, and seller performance metrics.
    """
)