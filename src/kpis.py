import pandas as pd
import numpy as np

from src.constants import (
    REPORTS_DIR,
    RFM_FILE,
    REPEAT_FILE,
    COHORT_FILE,
    RULES_FILE,
    BASKET_FILE,
    TOP_CATEGORIES_FILE,
    SELLER_PERF_FILE,
    SELLER_REVIEW_FILE,
    SELLER_CATEGORY_FILE,
    FORECAST_FILE,
)

# ======================================================
# Basic File Helpers
# ======================================================
def safe_read_csv(file_name: str):
    """
    Safely read a CSV from the reports directory.
    Returns a DataFrame if found and readable, otherwise None.
    """
    try:
        file_path = REPORTS_DIR / file_name
        if file_path.exists() and file_path.is_file():
            return pd.read_csv(file_path)
    except Exception:
        pass
    return None


def file_available(df) -> bool:
    """
    Returns True if a dataframe exists and is not empty.
    """
    return df is not None and isinstance(df, pd.DataFrame) and not df.empty


def file_row_count(df):
    """
    Returns row count for a dataframe, else None.
    """
    if file_available(df):
        return len(df)
    return None


# ======================================================
# Formatting Helpers
# ======================================================
def format_number(x):
    """
    Format integer-like numbers with commas.
    """
    try:
        if x is None or pd.isna(x):
            return "N/A"
        return f"{int(round(float(x))):,}"
    except Exception:
        return "N/A"


def format_decimal(x, digits=2):
    """
    Format decimal values safely.
    """
    try:
        if x is None or pd.isna(x):
            return "N/A"
        return f"{float(x):,.{digits}f}"
    except Exception:
        return "N/A"


def format_percent(x, digits=2):
    """
    Format percent values safely.
    Expects values already in percentage form (e.g. 42.35 -> '42.35%').
    """
    try:
        if x is None or pd.isna(x):
            return "N/A"
        return f"{float(x):,.{digits}f}%"
    except Exception:
        return "N/A"


def format_currency(x, symbol="₹"):
    """
    Format currency safely.
    """
    try:
        if x is None or pd.isna(x):
            return "N/A"
        return f"{symbol} {float(x):,.0f}"
    except Exception:
        return "N/A"


# ======================================================
# Column Detection Helpers
# ======================================================
def normalize_col_name(col_name: str) -> str:
    """
    Normalize column names for flexible matching.
    """
    return str(col_name).strip().lower().replace(" ", "_")


def find_col(df: pd.DataFrame, candidate_names):
    """
    Find the first matching column in a dataframe using
    case-insensitive normalized comparison.
    Returns the real dataframe column name or None.
    """
    if not file_available(df):
        return None

    normalized_map = {normalize_col_name(c): c for c in df.columns}

    for candidate in candidate_names:
        candidate_norm = normalize_col_name(candidate)
        if candidate_norm in normalized_map:
            return normalized_map[candidate_norm]

    return None


# ======================================================
# Generic Data Helpers
# ======================================================
def top_n(df, sort_col, n=10, ascending=False):
    """
    Return top N rows by a sort column if available.
    """
    if not file_available(df):
        return None
    if sort_col not in df.columns:
        return None

    return df.sort_values(sort_col, ascending=ascending).head(n).copy()


def add_missing_columns(df, required_cols, fill_value=np.nan):
    """
    Ensure required columns exist in a dataframe.
    """
    if df is None:
        return None

    df = df.copy()
    for col in required_cols:
        if col not in df.columns:
            df[col] = fill_value
    return df


# ======================================================
# Generic Customer KPI Helpers
# ======================================================
def get_total_customers(df):
    if not file_available(df):
        return None
    customer_col = find_col(df, ["customer_unique_id", "customer_id"])
    if customer_col:
        return df[customer_col].nunique()
    return len(df)


def get_repeat_customers(df):
    if not file_available(df):
        return None
    repeat_flag_col = find_col(df, ["is_repeat_customer", "repeat_customer"])
    total_orders_col = find_col(df, ["total_orders", "orders", "order_count", "frequency"])

    if repeat_flag_col:
        return df[df[repeat_flag_col] == True].shape[0]
    if total_orders_col:
        return df[df[total_orders_col] > 1].shape[0]
    return None


def get_repeat_rate(total_customers, repeat_customers):
    if total_customers is None or repeat_customers is None or total_customers == 0:
        return None
    return (repeat_customers / total_customers) * 100


def get_avg_customer_spend(df):
    if not file_available(df):
        return None
    spend_col = find_col(df, ["total_spent", "revenue", "sales", "monetary", "monetary_value"])
    if spend_col:
        return df[spend_col].mean()
    return None


def get_segment_distribution(rfm_df):
    if not file_available(rfm_df):
        return None

    segment_col = find_col(rfm_df, ["segment"])
    if not segment_col:
        return None

    out = (
        rfm_df[segment_col]
        .value_counts(dropna=False)
        .reset_index()
    )
    out.columns = ["segment", "customer_count"]
    return out


def get_segment_revenue(rfm_df):
    if not file_available(rfm_df):
        return None

    segment_col = find_col(rfm_df, ["segment"])
    monetary_col = find_col(rfm_df, ["monetary_value", "monetary", "revenue", "total_spent"])

    if not segment_col or not monetary_col:
        return None

    out = (
        rfm_df.groupby(segment_col, dropna=False)[monetary_col]
        .sum()
        .reset_index()
    )
    out.columns = ["segment", "monetary_value"]
    return out.sort_values("monetary_value", ascending=False)


# ======================================================
# Homepage KPI Logic
# ======================================================
def get_homepage_kpis():
    """
    Derive homepage KPIs primarily from repeat_purchase_summary.csv.
    """
    repeat_df = safe_read_csv(REPEAT_FILE)

    total_customers = get_total_customers(repeat_df)
    repeat_customers = get_repeat_customers(repeat_df)
    repeat_rate = get_repeat_rate(total_customers, repeat_customers)
    avg_customer_spend = get_avg_customer_spend(repeat_df)

    return {
        "total_customers": total_customers,
        "repeat_customers": repeat_customers,
        "repeat_rate": repeat_rate,
        "avg_customer_spend": avg_customer_spend,
    }


# ======================================================
# Customer Segmentation KPIs
# ======================================================
def get_customer_segmentation_kpis():
    """
    KPIs for customer segmentation page from RFM + repeat purchase files.
    """
    rfm_df = safe_read_csv(RFM_FILE)
    repeat_df = safe_read_csv(REPEAT_FILE)

    total_customers = get_total_customers(rfm_df)
    repeat_customers = get_repeat_customers(repeat_df)
    repeat_rate = get_repeat_rate(total_customers, repeat_customers)
    avg_customer_spend = get_avg_customer_spend(rfm_df)

    return {
        "total_customers": total_customers,
        "repeat_customers": repeat_customers,
        "repeat_rate": repeat_rate,
        "avg_customer_spend": avg_customer_spend,
    }


# ======================================================
# Cohort / Retention KPIs
# ======================================================
def get_cohort_kpis():
    """
    KPIs for cohort retention page.
    """
    repeat_df = safe_read_csv(REPEAT_FILE)
    cohort_df = safe_read_csv(COHORT_FILE)

    repeat_customers = get_repeat_customers(repeat_df)

    avg_orders_per_customer = None
    avg_customer_spend = get_avg_customer_spend(repeat_df)
    cohort_rows = file_row_count(cohort_df)

    if file_available(repeat_df):
        total_orders_col = find_col(repeat_df, ["total_orders", "orders", "order_count"])
        if total_orders_col:
            avg_orders_per_customer = repeat_df[total_orders_col].mean()

    return {
        "repeat_customers": repeat_customers,
        "avg_orders_per_customer": avg_orders_per_customer,
        "avg_customer_spend": avg_customer_spend,
        "cohort_rows": cohort_rows,
    }


# ======================================================
# Market Basket KPIs
# ======================================================
def get_market_basket_kpis():
    """
    KPIs for market basket analysis page.
    """
    rules_df = safe_read_csv(RULES_FILE)
    basket_df = safe_read_csv(BASKET_FILE)

    total_rules = file_row_count(rules_df)
    basket_rows = file_row_count(basket_df)
    avg_confidence = None
    avg_lift = None

    if file_available(rules_df):
        confidence_col = find_col(rules_df, ["confidence"])
        lift_col = find_col(rules_df, ["lift"])

        if confidence_col:
            avg_confidence = rules_df[confidence_col].mean()

        if lift_col:
            avg_lift = rules_df[lift_col].mean()

    return {
        "total_rules": total_rules,
        "basket_rows": basket_rows,
        "avg_confidence": avg_confidence,
        "avg_lift": avg_lift,
    }


# ======================================================
# Seller Analytics KPIs
# ======================================================
def get_seller_kpis():
    """
    KPIs for seller / marketplace analytics page.
    """
    seller_perf_df = safe_read_csv(SELLER_PERF_FILE)
    seller_review_df = safe_read_csv(SELLER_REVIEW_FILE)

    total_sellers = None
    top_seller_revenue = None
    avg_seller_orders = None
    avg_seller_review = None

    if file_available(seller_perf_df):
        seller_col = find_col(seller_perf_df, ["seller_id"])
        revenue_col = find_col(seller_perf_df, ["seller_revenue", "revenue"])
        orders_col = find_col(seller_perf_df, ["total_orders", "orders"])

        if seller_col:
            total_sellers = seller_perf_df[seller_col].nunique()

        if revenue_col:
            top_seller_revenue = seller_perf_df[revenue_col].max()

        if orders_col:
            avg_seller_orders = seller_perf_df[orders_col].mean()

    if file_available(seller_review_df):
        review_col = find_col(
            seller_review_df,
            ["avg_review_score", "avg_review", "review_score"]
        )
        if review_col:
            avg_seller_review = seller_review_df[review_col].mean()

    return {
        "total_sellers": total_sellers,
        "top_seller_revenue": top_seller_revenue,
        "avg_seller_orders": avg_seller_orders,
        "avg_seller_review": avg_seller_review,
    }