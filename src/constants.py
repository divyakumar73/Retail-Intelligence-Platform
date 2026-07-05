from pathlib import Path

# ======================================================
# Project Paths
# ======================================================
PROJECT_ROOT = Path(__file__).resolve().parents[1]
REPORTS_DIR = PROJECT_ROOT / "reports"

# ======================================================
# App Metadata
# ======================================================
APP_TITLE = "Retail Intelligence Platform"
APP_SUBTITLE = "End-to-End E-commerce Analytics Dashboard"

# ======================================================
# Theme / Styling
# ======================================================
PRIMARY_COLOR = "#005072"
SECONDARY_COLOR = "#1B9AAA"
ACCENT_COLOR = "#F4A261"
BACKGROUND_LIGHT = "#F8F9FA"

# ======================================================
# Core Report Files
# ======================================================
RFM_FILE = "rfm_customer_segments.csv"
REPEAT_FILE = "repeat_purchase_summary.csv"
COHORT_FILE = "cohort_business_summary.csv"
FORECAST_FILE = "sales_forecast_summary.csv"

# ======================================================
# Market Basket Report Files
# ======================================================
RULES_FILE = "association_rules.csv"
BASKET_FILE = "basket_summary.csv"
TOP_CATEGORIES_FILE = "top_categories_by_order_presence.csv"

# ======================================================
# Seller / Marketplace Report Files
# ======================================================
SELLER_PERF_FILE = "seller_performance_summary.csv"
SELLER_REVIEW_FILE = "seller_review_summary.csv"
SELLER_CATEGORY_FILE = "seller_category_summary.csv"

# ======================================================
# All Report Files Registry
# Useful for status tables / validation / future checks
# ======================================================
ALL_REPORT_FILES = [
    RFM_FILE,
    REPEAT_FILE,
    COHORT_FILE,
    FORECAST_FILE,
    RULES_FILE,
    BASKET_FILE,
    TOP_CATEGORIES_FILE,
    SELLER_PERF_FILE,
    SELLER_REVIEW_FILE,
    SELLER_CATEGORY_FILE,
]