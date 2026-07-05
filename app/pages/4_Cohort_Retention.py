import streamlit as st
import pandas as pd
import plotly.express as px

from src.kpis import (
    safe_read_csv,
    file_available,
    find_col,
    format_number,
    format_currency,
    get_cohort_kpis
)

# ======================================================
# Page Config
# ======================================================
st.set_page_config(
    page_title="Cohort Retention Analysis",
    page_icon="🔁",
    layout="wide"
)

# ======================================================
# Page Header
# ======================================================
st.title("Cohort Retention Analysis")
st.markdown(
    """
    Analyze customer retention and repeat purchase behavior over time using
    cohort-style business summaries and repeat-customer metrics.
    """
)

st.markdown("---")

# ======================================================
# Load Data
# ======================================================
cohort_df = safe_read_csv("cohort_business_summary.csv")
repeat_df = safe_read_csv("repeat_purchase_summary.csv")

if not file_available(cohort_df) and not file_available(repeat_df):
    st.error(
        "Missing both `cohort_business_summary.csv` and `repeat_purchase_summary.csv` in the reports folder."
    )
    st.stop()

# ======================================================
# KPI Section
# ======================================================
st.subheader("Retention Snapshot")

kpis = get_cohort_kpis()

total_repeat_customers = kpis.get("repeat_customers")
avg_orders_per_customer = kpis.get("avg_orders_per_customer")
avg_spend_per_customer = kpis.get("avg_customer_spend")
cohort_count = kpis.get("cohort_rows")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Repeat Customers",
        format_number(total_repeat_customers) if total_repeat_customers is not None else "N/A"
    )

with k2:
    st.metric(
        "Avg Orders per Customer",
        f"{avg_orders_per_customer:.2f}" if avg_orders_per_customer is not None else "N/A"
    )

with k3:
    st.metric(
        "Avg Customer Spend",
        format_currency(avg_spend_per_customer) if avg_spend_per_customer is not None else "N/A"
    )

with k4:
    st.metric(
        "Cohort Summary Rows",
        format_number(cohort_count) if cohort_count is not None else "N/A"
    )

st.markdown("---")

# ======================================================
# Cohort Business Summary Section
# ======================================================
st.subheader("Cohort Business Summary")

if file_available(cohort_df):
    st.dataframe(cohort_df, use_container_width=True, hide_index=True)
else:
    st.info("`cohort_business_summary.csv` is not available.")

st.markdown("---")

# ======================================================
# Repeat Purchase Summary Section
# ======================================================
st.subheader("Repeat Purchase Summary")

if file_available(repeat_df):
    repeat_customer_col = find_col(repeat_df, ["customer_unique_id", "customer_id"])
    repeat_orders_col = find_col(repeat_df, ["total_orders", "orders", "order_count", "frequency"])
    repeat_spent_col = find_col(repeat_df, ["total_spent", "revenue", "sales", "monetary"])
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
            repeat_df[display_cols].head(100),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.dataframe(
            repeat_df.head(100),
            use_container_width=True,
            hide_index=True
        )
else:
    st.info("`repeat_purchase_summary.csv` is not available.")

st.markdown("---")

# ======================================================
# Repeat Purchase Distribution Chart
# ======================================================
st.subheader("Repeat Purchase Distribution")

if file_available(repeat_df):
    orders_col = find_col(repeat_df, ["total_orders", "orders", "order_count", "frequency"])

    if orders_col is not None:
        repeat_chart_df = repeat_df.copy()
        repeat_chart_df[orders_col] = pd.to_numeric(repeat_chart_df[orders_col], errors="coerce")

        order_dist = (
            repeat_chart_df[orders_col]
            .dropna()
            .value_counts()
            .sort_index()
            .reset_index()
        )
        order_dist.columns = ["total_orders", "customer_count"]

        fig_orders = px.bar(
            order_dist,
            x="total_orders",
            y="customer_count",
            text="customer_count",
            title="Distribution of Orders per Customer"
        )
        fig_orders.update_layout(
            xaxis_title="Number of Orders",
            yaxis_title="Customer Count"
        )
        st.plotly_chart(fig_orders, use_container_width=True)
    else:
        st.info("Could not identify an orders column in repeat purchase summary.")
else:
    st.info("Repeat purchase summary not available for charting.")

st.markdown("---")

# ======================================================
# Retention / Cohort Notes
# ======================================================
st.subheader("Retention Insights")
st.markdown(
    """
    - **Repeat customers** are a leading signal of retention quality and customer stickiness.
    - **Average orders per customer** helps indicate whether the business is driving repeat engagement.
    - **Average customer spend** can be tracked alongside repeat behavior to understand whether retained customers are also higher-value customers.
    - As the project matures, this page can be extended with:
      - cohort retention heatmaps
      - month-on-month cohort curves
      - first-order month analysis
      - retention by state, category, or payment type
    """
)