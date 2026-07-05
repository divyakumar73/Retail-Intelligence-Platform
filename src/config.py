from pathlib import Path

# ======================================================
# Project Root
# ======================================================
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# ======================================================
# Core Folders
# ======================================================
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

REPORTS_DIR = PROJECT_ROOT / "reports"
POWERBI_DIR = PROJECT_ROOT / "powerbi"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"
DOCUMENTATION_DIR = PROJECT_ROOT / "documentation"

APP_DIR = PROJECT_ROOT / "app"
SRC_DIR = PROJECT_ROOT / "src"

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
# Raw Olist Source Files
# ======================================================
ORDERS_FILE = RAW_DATA_DIR / "olist_orders_dataset.csv"
ORDER_ITEMS_FILE = RAW_DATA_DIR / "olist_order_items_dataset.csv"
PRODUCTS_FILE = RAW_DATA_DIR / "olist_products_dataset.csv"
CUSTOMERS_FILE = RAW_DATA_DIR / "olist_customers_dataset.csv"
PAYMENTS_FILE = RAW_DATA_DIR / "olist_order_payments_dataset.csv"
SELLERS_FILE = RAW_DATA_DIR / "olist_sellers_dataset.csv"
REVIEWS_FILE = RAW_DATA_DIR / "olist_order_reviews_dataset.csv"
CATEGORY_TRANSLATION_FILE = RAW_DATA_DIR / "product_category_name_translation.csv"

# Optional raw supporting file if present
GEOLOCATION_FILE = RAW_DATA_DIR / "olist_geolocation_dataset.csv"

# ======================================================
# Streamlit Report File Names
# Keep these as FILE NAMES only.
# safe_read_csv() should join them with REPORTS_DIR.
# ======================================================
RFM_FILE = "rfm_customer_segments.csv"
REPEAT_FILE = "repeat_purchase_summary.csv"
COHORT_FILE = "cohort_business_summary.csv"

RULES_FILE = "association_rules.csv"
BASKET_FILE = "basket_summary.csv"
TOP_CATEGORIES_FILE = "top_categories_by_order_presence.csv"

SELLER_PERF_FILE = "seller_performance_summary.csv"
SELLER_REVIEW_FILE = "seller_review_summary.csv"
SELLER_CATEGORY_FILE = "seller_category_summary.csv"

# Optional / future module
FORECAST_FILE = "forecast_results.csv"

# ======================================================
# Optional Full Report Paths
# Use these only if you need explicit Path objects somewhere
# outside safe_read_csv().
# ======================================================
RFM_REPORT_PATH = REPORTS_DIR / RFM_FILE
REPEAT_REPORT_PATH = REPORTS_DIR / REPEAT_FILE
COHORT_REPORT_PATH = REPORTS_DIR / COHORT_FILE

RULES_REPORT_PATH = REPORTS_DIR / RULES_FILE
BASKET_REPORT_PATH = REPORTS_DIR / BASKET_FILE
TOP_CATEGORIES_REPORT_PATH = REPORTS_DIR / TOP_CATEGORIES_FILE

SELLER_PERF_REPORT_PATH = REPORTS_DIR / SELLER_PERF_FILE
SELLER_REVIEW_REPORT_PATH = REPORTS_DIR / SELLER_REVIEW_FILE
SELLER_CATEGORY_REPORT_PATH = REPORTS_DIR / SELLER_CATEGORY_FILE

FORECAST_REPORT_PATH = REPORTS_DIR / FORECAST_FILE