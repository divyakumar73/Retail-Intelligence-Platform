import streamlit as st
import pandas as pd
import plotly.express as px

from src.kpis import (
    safe_read_csv,
    file_available,
    find_col,
    format_number,
    format_currency,
    get_seller_kpis
)

# ======================================================
# Page Config
# ======================================================
st.set_page_config(
    page_title="Seller / Marketplace Analytics",
    page_icon="🏪",
    layout="wide"
)

st.title("Seller / Marketplace Analytics")
st.markdown(
    """
    Analyze seller performance across revenue, order volume, product categories, and review quality
    to understand marketplace concentration and identify top-performing sellers.
    """
)

st.markdown("---")

# ======================================================
# Load Report Files
# ======================================================
seller_perf_df = safe_read_csv("seller_performance_summary.csv")
seller_reviews_df = safe_read_csv("seller_review_summary.csv")
seller_category_df = safe_read_csv("seller_category_summary.csv")

# ======================================================
# Detect Columns Dynamically
# ======================================================
seller_id_col = None
seller_revenue_col = None
seller_orders_col = None
seller_review_col = None
seller_category_col = None
category_revenue_col = None

if file_available(seller_perf_df):
    seller_id_col = find_col(
        seller_perf_df,
        ["seller_id", "seller", "SellerID"]
    )

    seller_revenue_col = find_col(
        seller_perf_df,
        ["seller_revenue", "revenue", "Revenue", "total_revenue", "TotalRevenue"]
    )

    seller_orders_col = find_col(
        seller_perf_df,
        ["total_orders", "orders", "order_count", "OrderCount", "num_orders"]
    )

if file_available(seller_reviews_df):
    seller_review_col = find_col(
        seller_reviews_df,
        [
            "avg_review_score",
            "review_score",
            "avg_score",
            "average_review_score",
            "avg_review",
            "review_mean",
            "seller_review_avg",
            "mean_review_score",
            "avg seller review score",
            "review_avg"
        ]
    )

if file_available(seller_category_df):
    seller_category_col = find_col(
        seller_category_df,
        [
            "product_category_name_english",
            "category",
            "product_category",
            "Category",
            "category_final"
        ]
    )

    category_revenue_col = find_col(
        seller_category_df,
        [
            "category_revenue",
            "revenue",
            "Revenue",
            "total_revenue"
        ]
    )

# ======================================================
# KPI Snapshot
# ======================================================
kpis = get_seller_kpis()

total_sellers = kpis.get("total_sellers")
top_seller_revenue = kpis.get("top_seller_revenue")
avg_seller_orders = kpis.get("avg_seller_orders")
avg_seller_review = kpis.get("avg_seller_review")

st.subheader("Marketplace Snapshot")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Sellers",
        format_number(total_sellers) if total_sellers is not None else "N/A"
    )

with col2:
    st.metric(
        "Top Seller Revenue",
        format_currency(top_seller_revenue) if top_seller_revenue is not None else "N/A"
    )

with col3:
    st.metric(
        "Avg Orders per Seller",
        f"{avg_seller_orders:.2f}" if avg_seller_orders is not None else "N/A"
    )

with col4:
    st.metric(
        "Avg Seller Review Score",
        f"{avg_seller_review:.2f}" if avg_seller_review is not None else "N/A"
    )

st.markdown("---")

# ======================================================
# Seller Performance Summary Table
# ======================================================
st.subheader("Seller Performance Summary")

if file_available(seller_perf_df):
    st.dataframe(seller_perf_df.head(20), use_container_width=True, hide_index=True)
else:
    st.info("seller_performance_summary.csv is not available.")

st.markdown("---")

# ======================================================
# Top Sellers by Revenue
# ======================================================
st.subheader("Top Sellers by Revenue")

if file_available(seller_perf_df):
    if seller_id_col and seller_revenue_col:
        top_rev = seller_perf_df.copy()
        top_rev[seller_revenue_col] = pd.to_numeric(top_rev[seller_revenue_col], errors="coerce")
        top_rev = (
            top_rev.sort_values(seller_revenue_col, ascending=False)
            .head(15)
            .copy()
        )

        fig = px.bar(
            top_rev,
            x=seller_revenue_col,
            y=seller_id_col,
            orientation="h",
            title="Top 15 Sellers by Revenue"
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Could not detect seller id / revenue columns in seller_performance_summary.csv.")
else:
    st.info("Top seller revenue chart unavailable because seller_performance_summary.csv is missing.")

st.markdown("---")

# ======================================================
# Top Sellers by Order Volume
# ======================================================
st.subheader("Top Sellers by Order Volume")

if file_available(seller_perf_df):
    if seller_id_col and seller_orders_col:
        top_orders = seller_perf_df.copy()
        top_orders[seller_orders_col] = pd.to_numeric(top_orders[seller_orders_col], errors="coerce")
        top_orders = (
            top_orders.sort_values(seller_orders_col, ascending=False)
            .head(15)
            .copy()
        )

        fig = px.bar(
            top_orders,
            x=seller_orders_col,
            y=seller_id_col,
            orientation="h",
            title="Top 15 Sellers by Order Count"
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Could not detect seller id / order columns in seller_performance_summary.csv.")
else:
    st.info("Top seller order chart unavailable because seller_performance_summary.csv is missing.")

st.markdown("---")

# ======================================================
# Seller Review Summary
# ======================================================
st.subheader("Seller Review Summary")

if file_available(seller_reviews_df):
    st.dataframe(seller_reviews_df.head(20), use_container_width=True, hide_index=True)

    review_seller_col = find_col(seller_reviews_df, ["seller_id", "seller", "SellerID"])

    if review_seller_col and seller_review_col:
        top_review = seller_reviews_df.copy()
        top_review[seller_review_col] = pd.to_numeric(top_review[seller_review_col], errors="coerce")
        top_review = (
            top_review.sort_values(seller_review_col, ascending=False)
            .head(15)
            .copy()
        )

        fig = px.bar(
            top_review,
            x=seller_review_col,
            y=review_seller_col,
            orientation="h",
            title="Top Sellers by Average Review Score"
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Could not detect seller id / review score columns in seller_review_summary.csv.")
else:
    st.info("seller_review_summary.csv is not available.")

st.markdown("---")

# ======================================================
# Seller Category Summary
# ======================================================
st.subheader("Top Categories by Seller Revenue")

if file_available(seller_category_df):
    st.dataframe(seller_category_df.head(20), use_container_width=True, hide_index=True)

    if seller_category_col and category_revenue_col:
        top_cat = seller_category_df.copy()
        top_cat[category_revenue_col] = pd.to_numeric(top_cat[category_revenue_col], errors="coerce")
        top_cat = (
            top_cat.sort_values(category_revenue_col, ascending=False)
            .head(15)
            .copy()
        )

        fig = px.bar(
            top_cat,
            x=category_revenue_col,
            y=seller_category_col,
            orientation="h",
            title="Top Product Categories by Seller Revenue"
        )
        fig.update_layout(yaxis={"categoryorder": "total ascending"})
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Could not detect category / revenue columns in seller_category_summary.csv.")
else:
    st.info("seller_category_summary.csv is not available.")

st.markdown("---")

# ======================================================
# Data Asset Status
# ======================================================
st.subheader("Seller Analytics Data Assets")

status_rows = [
    {
        "File": "seller_performance_summary.csv",
        "Status": "Loaded" if file_available(seller_perf_df) else "Missing"
    },
    {
        "File": "seller_review_summary.csv",
        "Status": "Loaded" if file_available(seller_reviews_df) else "Missing"
    },
    {
        "File": "seller_category_summary.csv",
        "Status": "Loaded" if file_available(seller_category_df) else "Missing"
    },
]

status_df = pd.DataFrame(status_rows)
st.dataframe(status_df, use_container_width=True, hide_index=True)

st.markdown("---")

# ======================================================
# Business Interpretation
# ======================================================
st.subheader("Business Interpretation")
st.markdown(
    """
    - **Seller revenue concentration** shows whether a small number of sellers dominate the marketplace.
    - **Order volume by seller** highlights operationally important sellers and fulfillment-heavy accounts.
    - **Review score by seller** helps identify seller quality, service consistency, and potential customer experience risks.
    - **Category-level seller revenue** shows which product families contribute most to marketplace sales and where the seller ecosystem is strongest.
    """
)