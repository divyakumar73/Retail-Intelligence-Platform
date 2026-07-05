import streamlit as st
import pandas as pd
import plotly.express as px

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
    page_title="Customer Segmentation",
    page_icon="👥",
    layout="wide"
)

# ======================================================
# Page Title
# ======================================================
st.title("Customer Segmentation")
st.markdown(
    """
    Analyze customer value and repeat purchase behavior using **RFM segmentation**
    and repeat-customer metrics derived from the retail customer base.
    """
)

st.markdown("---")

# ======================================================
# Load Data
# ======================================================
rfm_df = safe_read_csv("rfm_customer_segments.csv")
repeat_df = safe_read_csv("repeat_purchase_summary.csv")

if not file_available(rfm_df):
    st.error("Missing file: `rfm_customer_segments.csv`")
    st.stop()

if not file_available(repeat_df):
    st.warning("`repeat_purchase_summary.csv` not found. Repeat KPIs will be limited.")

# ======================================================
# Standardize / Detect RFM Columns
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

# ======================================================
# KPI Cards
# ======================================================
st.subheader("Customer KPIs")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Customers", format_number(total_customers))

with col2:
    st.metric(
        "Repeat Customers",
        format_number(repeat_customers) if repeat_customers is not None else "N/A"
    )

with col3:
    st.metric(
        "Repeat Customer Rate",
        format_percent(repeat_rate) if repeat_rate is not None else "N/A"
    )

with col4:
    st.metric(
        "Average Customer Spend",
        format_currency(avg_customer_spend) if avg_customer_spend is not None else "N/A"
    )

st.markdown("---")

# ======================================================
# Segment Distribution
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
        st.info("Segment column not found in RFM file.")

with seg_col2:
    st.subheader("Top Segments by Revenue")

    if segment_col and monetary_col:
        segment_revenue = (
            rfm_df.groupby(segment_col, dropna=False)[monetary_col]
            .sum()
            .reset_index()
            .sort_values(monetary_col, ascending=False)
            .head(10)
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
        st.info("Segment revenue data not available.")

st.markdown("---")

# ======================================================
# Repeat Purchase Summary Table
# ======================================================
st.subheader("Repeat Purchase Summary")

if file_available(repeat_df):
    repeat_customer_col = find_col(repeat_df, ["customer_unique_id", "customer_id"])
    repeat_orders_col = find_col(repeat_df, ["total_orders", "orders", "order_count", "frequency"])
    repeat_spent_col = find_col(repeat_df, ["total_spent", "revenue", "monetary", "sales"])
    repeat_flag_col = find_col(repeat_df, ["is_repeat_customer", "repeat_customer"])

    display_cols = [
        c for c in [
            repeat_customer_col,
            repeat_orders_col,
            repeat_spent_col,
            repeat_flag_col
        ]
        if c is not None
    ]

    if display_cols:
        st.dataframe(
            repeat_df[display_cols].head(50),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("Repeat purchase summary columns not found.")
else:
    st.info("Repeat purchase summary file not available.")

st.markdown("---")

# ======================================================
# RFM Segment Sample
# ======================================================
st.subheader("RFM Segment Sample")

rfm_sample_cols = [
    c for c in [
        customer_col,
        recency_col,
        frequency_col,
        monetary_col,
        segment_col
    ]
    if c is not None
]

if rfm_sample_cols:
    st.dataframe(
        rfm_df[rfm_sample_cols].head(50),
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("RFM sample columns not available.")

st.markdown("---")

# ======================================================
# Business Interpretation
# ======================================================
st.subheader("Business Interpretation")
st.markdown(
    """
    - **High-value / loyal segments** typically show high frequency and high monetary value.
    - **At-risk or low-engagement segments** often show higher recency and lower purchase frequency.
    - Segment revenue contribution helps identify where retention and upsell efforts should be focused.
    - Repeat customer analysis provides an early signal of customer stickiness and lifecycle quality.
    """
)