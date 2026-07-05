import pandas as pd
from pathlib import Path

from src.constants import (
    REPORTS_DIR,
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
)


def safe_read_csv(file_name: str) -> pd.DataFrame:
    """
    Safely read a CSV from the reports directory.
    Returns an empty DataFrame if the file does not exist.
    """
    file_path = REPORTS_DIR / file_name
    if file_path.exists():
        return pd.read_csv(file_path)
    return pd.DataFrame()


# ======================================================
# Report Data Loaders
# ======================================================
def load_rfm_segments() -> pd.DataFrame:
    return safe_read_csv(RFM_FILE)


def load_repeat_purchase_summary() -> pd.DataFrame:
    return safe_read_csv(REPEAT_FILE)


def load_cohort_summary() -> pd.DataFrame:
    return safe_read_csv(COHORT_FILE)


def load_forecast_results() -> pd.DataFrame:
    return safe_read_csv(FORECAST_FILE)


def load_basket_rules() -> pd.DataFrame:
    return safe_read_csv(RULES_FILE)


def load_basket_summary() -> pd.DataFrame:
    return safe_read_csv(BASKET_FILE)


def load_top_categories() -> pd.DataFrame:
    return safe_read_csv(TOP_CATEGORIES_FILE)


def load_seller_performance() -> pd.DataFrame:
    return safe_read_csv(SELLER_PERF_FILE)


def load_seller_reviews() -> pd.DataFrame:
    return safe_read_csv(SELLER_REVIEW_FILE)


def load_seller_categories() -> pd.DataFrame:
    return safe_read_csv(SELLER_CATEGORY_FILE)