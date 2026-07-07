# DAX Measures Notes – Retail Intelligence Dashboard

## 1. Purpose
This document contains the core DAX measures used in the **Retail Intelligence Dashboard** Power BI report for the **Retail Intelligence Platform** project.

The purpose of this file is to document:
- the KPI and business logic used in the Power BI layer
- the final DAX measures used across report pages
- how Power BI measures align with the SQL analytics layer and Streamlit application outputs
- page-specific measures created for sales, customers, products, sellers, reviews, and delivery analysis

This file is intended to make the Power BI layer easier to maintain, explain in interviews, and reconcile against the SQL and Streamlit implementations.

---

# 2. Power BI Model Used in This Project

The final Power BI report is built on the **Olist Brazilian E-Commerce dataset** using the following tables:

## Core tables used in the report
- `Fact Sales`
- `olist_orders_dataset`
- `olist_customers_dataset`
- `olist_products_dataset`
- `olist_sellers_dataset`
- `olist_order_reviews_dataset`
- `olist_order_payments_dataset`
- `product_category_name_translation`
- `Date`

---

# 3. Alignment with SQL and Streamlit
This project includes three analytics layers:

1. **SQL analytics layer**
   - PostgreSQL notebooks and exported CSV summaries
2. **Streamlit analytics layer**
   - interactive Python dashboard and business insights
3. **Power BI dashboard layer**
   - executive and visual reporting dashboard

The Power BI measures were adjusted to align as closely as possible with the SQL and Streamlit outputs.  
Where exact one-to-one parity was not practical in Power BI because of model context or visual behavior, the dashboard uses the closest business-equivalent measure while keeping the KPI meaning consistent.

## Alignment principles used
- Revenue measures are primarily based on delivered-order sales logic
- Delivered order metrics use `olist_orders_dataset[order_status] = "delivered"`
- Review metrics are based on `olist_order_reviews_dataset`
- Customer and seller visuals were adjusted to avoid filter-context issues in Power BI visuals
- Some visuals were replaced with stronger business alternatives when the original chart did not behave reliably in Power BI

---

# 4. Measure Organization Recommendation

Create a dedicated **Measures** table in Power BI and organize measures into folders such as:

- Sales
- Orders
- Customers
- Products
- Sellers
- Reviews
- Delivery
- Time Intelligence
- Visual-specific Measures

This keeps the model cleaner and makes the report easier to maintain.

---

# 5. Core Business Logic Assumptions

## Revenue logic
For dashboard reporting, revenue is treated as:

- `Fact Sales[price] + Fact Sales[freight_value]`

In most KPI measures, revenue is filtered to **delivered orders** using the order status from `olist_orders_dataset`.

## Order logic
- **Total Orders** = distinct count of orders
- **Delivered Orders** = distinct count of orders where order status = delivered
- **Cancelled Orders** = distinct count of orders where order status = canceled

## Customer logic
- Customer-level metrics use `customer_unique_id` for unique customer counting
- Repeat customer logic is based on customers having more than one distinct order

## Seller logic
- Seller counts use seller IDs from the seller / fact tables
- Seller visuals were simplified to avoid seller-state filter context issues in Power BI

---

# 6. Core Measures

## 6.1 Total Revenue
**Purpose:** Total delivered revenue used across executive and sales pages.

```DAX
Total Revenue =
CALCULATE(
    SUM('Fact Sales'[price]) + SUM('Fact Sales'[freight_value]),
    olist_orders_dataset[order_status] = "delivered"
)