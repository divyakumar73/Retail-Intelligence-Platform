import streamlit as st
import pandas as pd
import plotly.express as px

from src.kpis import (
    safe_read_csv,
    file_available,
    find_col,
    format_number,
    format_percent,
    get_market_basket_kpis
)

# ======================================================
# Page Config
# ======================================================
st.set_page_config(
    page_title="Market Basket Analysis",
    page_icon="🛒",
    layout="wide"
)

# ======================================================
# Page Header
# ======================================================
st.title("Market Basket Analysis")
st.markdown(
    """
    Analyze **product co-purchase behavior** and **association rules** to identify bundling,
    cross-sell, and recommendation opportunities from transaction baskets.
    """
)

st.markdown("---")

# ======================================================
# Load Basket Report Files
# ======================================================
rules_df = safe_read_csv("association_rules.csv")
basket_summary_df = safe_read_csv("basket_summary.csv")
top_categories_df = safe_read_csv("top_categories_by_order_presence.csv")

if not file_available(rules_df) and not file_available(basket_summary_df) and not file_available(top_categories_df):
    st.error(
        "No market basket report files found in `reports/`. Expected one or more of: "
        "`association_rules.csv`, `basket_summary.csv`, `top_categories_by_order_presence.csv`."
    )
    st.stop()

# ======================================================
# KPI Snapshot
# ======================================================
st.subheader("Basket Analytics Snapshot")

kpis = get_market_basket_kpis()

num_rules = kpis.get("total_rules")
num_basket_rows = kpis.get("basket_rows")
avg_confidence = kpis.get("avg_confidence")
avg_lift = kpis.get("avg_lift")

k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Association Rules",
        format_number(num_rules) if num_rules is not None else "N/A"
    )

with k2:
    st.metric(
        "Basket Summary Rows",
        format_number(num_basket_rows) if num_basket_rows is not None else "N/A"
    )

with k3:
    st.metric(
        "Average Confidence",
        format_percent(avg_confidence * 100) if avg_confidence is not None else "N/A"
    )

with k4:
    st.metric(
        "Average Lift",
        f"{avg_lift:.2f}" if avg_lift is not None else "N/A"
    )

st.markdown("---")

# ======================================================
# Association Rules Section
# ======================================================
st.subheader("Association Rules")

if file_available(rules_df):
    antecedents_col = find_col(rules_df, ["antecedents", "lhs"])
    consequents_col = find_col(rules_df, ["consequents", "rhs"])
    support_col = find_col(rules_df, ["support"])
    confidence_col = find_col(rules_df, ["confidence"])
    lift_col = find_col(rules_df, ["lift"])

    rules_display = rules_df.copy()

    if lift_col is not None:
        rules_display[lift_col] = pd.to_numeric(rules_display[lift_col], errors="coerce")
        rules_display = rules_display.sort_values(lift_col, ascending=False)

    display_cols = [
        c for c in [
            antecedents_col,
            consequents_col,
            support_col,
            confidence_col,
            lift_col
        ]
        if c is not None
    ]

    if display_cols:
        st.dataframe(
            rules_display[display_cols].head(50),
            use_container_width=True,
            hide_index=True
        )
    else:
        st.dataframe(
            rules_display.head(50),
            use_container_width=True,
            hide_index=True
        )
else:
    st.info("`association_rules.csv` not available.")

st.markdown("---")

# ======================================================
# Rule Strength Chart
# ======================================================
st.subheader("Top Rule Strength by Lift")

if file_available(rules_df):
    antecedents_col = find_col(rules_df, ["antecedents", "lhs"])
    consequents_col = find_col(rules_df, ["consequents", "rhs"])
    lift_col = find_col(rules_df, ["lift"])

    if antecedents_col and consequents_col and lift_col:
        chart_df = rules_df.copy()
        chart_df[lift_col] = pd.to_numeric(chart_df[lift_col], errors="coerce")

        chart_df["rule_label"] = (
            chart_df[antecedents_col].astype(str) + " → " + chart_df[consequents_col].astype(str)
        )

        top_rules = (
            chart_df.sort_values(lift_col, ascending=False)
            .head(15)
            .copy()
        )

        fig_lift = px.bar(
            top_rules,
            x=lift_col,
            y="rule_label",
            orientation="h",
            title="Top 15 Association Rules by Lift",
            text=lift_col
        )
        fig_lift.update_layout(
            xaxis_title="Lift",
            yaxis_title="Association Rule"
        )
        st.plotly_chart(fig_lift, use_container_width=True)
    else:
        st.info("Association rule columns not sufficient for lift chart.")
else:
    st.info("Association rules data not available for charting.")

st.markdown("---")

# ======================================================
# Top Categories by Order Presence
# ======================================================
st.subheader("Top Categories by Order Presence")

if file_available(top_categories_df):
    category_col = find_col(
        top_categories_df,
        ["category", "category_final", "product_category", "Category"]
    )
    order_count_col = find_col(
        top_categories_df,
        ["ordercount", "order_count", "orders", "num_orders", "OrderCount"]
    )

    if category_col and order_count_col:
        cat_df = top_categories_df.copy()
        cat_df[order_count_col] = pd.to_numeric(cat_df[order_count_col], errors="coerce")

        top_cat = (
            cat_df.sort_values(order_count_col, ascending=False)
            .head(15)
            .copy()
        )

        fig_cat = px.bar(
            top_cat,
            x=order_count_col,
            y=category_col,
            orientation="h",
            title="Top 15 Categories by Order Presence",
            text=order_count_col
        )
        fig_cat.update_layout(
            xaxis_title="Number of Orders",
            yaxis_title="Category"
        )
        st.plotly_chart(fig_cat, use_container_width=True)

        st.dataframe(
            top_cat[[category_col, order_count_col]],
            use_container_width=True,
            hide_index=True
        )
    else:
        st.dataframe(
            top_categories_df.head(30),
            use_container_width=True,
            hide_index=True
        )
else:
    st.info("`top_categories_by_order_presence.csv` not available.")

st.markdown("---")

# ======================================================
# Basket Summary Section
# ======================================================
st.subheader("Basket Summary")

if file_available(basket_summary_df):
    st.dataframe(
        basket_summary_df.head(100),
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("`basket_summary.csv` not available.")

st.markdown("---")

# ======================================================
# Business Interpretation
# ======================================================
st.subheader("Business Interpretation")
st.markdown(
    """
    - **Association rules** help identify products or categories that are frequently purchased together.
    - **Confidence** estimates how often the consequent appears when the antecedent is purchased.
    - **Lift** shows whether the relationship is stronger than random chance; higher lift generally indicates stronger bundling potential.
    - **Top categories by order presence** highlight which product families dominate baskets and can influence recommendation strategy.
    - These insights can support:
      - product bundling
      - checkout recommendations
      - cross-sell campaigns
      - merchandising and assortment decisions
    """
)