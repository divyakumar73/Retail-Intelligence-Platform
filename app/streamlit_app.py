import streamlit as st
from pathlib import Path
import sys

# ======================================================
# Make project root importable
# ======================================================
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.constants import APP_TITLE, APP_SUBTITLE

# ======================================================
# App Config
# ======================================================
st.set_page_config(
    page_title=APP_TITLE,
    page_icon="📊",
    layout="wide"
)

# ======================================================
# Landing Page
# ======================================================
st.title(APP_TITLE)
st.markdown(f"### {APP_SUBTITLE}")

st.markdown(
    """
    Welcome to the **Retail Intelligence Platform** — a multi-page analytics dashboard built on the
    **Olist Brazilian E-commerce dataset**.

    This project brings together **customer analytics, retention analysis, seller performance,
    and market basket insights** into a single business-facing dashboard experience.
    """
)

st.markdown("---")

st.subheader("Available Dashboard Modules")
st.markdown(
    """
    Use the **left sidebar** to navigate across the project pages:

    - **Home** — project overview, data asset readiness, and business summary
    - **Executive Dashboard** — customer KPIs, repeat behavior, and segment-level overview
    - **Customer Segmentation** — RFM segmentation and repeat purchase analytics
    - **Cohort Retention Analysis** — repeat customers, cohort-style summaries, and retention insights
    - **Market Basket Analysis** — association rules, basket summaries, and category co-purchase trends
    - **Seller / Marketplace Analytics** — seller revenue, review performance, and category contribution
    """
)

st.markdown("---")

st.info("Select a page from the sidebar to start exploring the dashboard.")