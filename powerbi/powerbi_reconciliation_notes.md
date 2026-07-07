# Power BI Reconciliation Notes – SQL vs Streamlit vs Power BI

## 1. Purpose
This document explains how the **Power BI dashboard layer** was reconciled against the **SQL analytics layer** and the **Streamlit analytics layer** in the Retail Intelligence Platform project.

The project was built across three analytical environments:

1. **SQL**
2. **Streamlit**
3. **Power BI**

Because each layer serves a different purpose, not every visual or KPI was implemented in exactly the same way. This file documents:
- the reconciliation approach used
- the final KPI alignment logic
- where Power BI matches SQL / Streamlit exactly
- where Power BI intentionally uses a business-equivalent alternative

---

# 2. Why Reconciliation Was Needed
The same Olist retail dataset was used in:
- SQL notebooks and reporting outputs
- Streamlit dashboards and Python analytics
- Power BI executive reporting

However, differences emerged because:
- SQL used PostgreSQL summary logic and notebook outputs
- Streamlit used Python / pandas transformations and app-specific metrics
- Power BI used DAX measures, relationships, and report visuals
- some Power BI visuals behaved differently under filter context, especially seller- and customer-level visuals

As a result, the Power BI layer was iteratively adjusted to align with the other two layers while keeping the dashboard stable and readable.

---

# 3. Final Reconciliation Principle
The final approach used in this project was:

## 3.1 SQL and Streamlit as the analytical reference layer
SQL and Streamlit were treated as the deeper analytical implementations because they:
- expose raw and transformed data more directly
- support notebook-level debugging and export validation
- allow detailed customer, seller, and product summaries
- are easier to reconcile at table / CSV level

## 3.2 Power BI as the executive reporting layer
Power BI was treated as the presentation and KPI dashboard layer.  
This means Power BI was aligned to SQL / Streamlit wherever possible, but when a visual did not behave reliably or did not add enough business value, it was replaced with a stronger business-equivalent visual.

---

# 4. KPI Reconciliation Logic

## Revenue
Final Power BI revenue logic uses:

- `Fact Sales[price] + Fact Sales[freight_value]`
- primarily filtered to **delivered orders**

This aligns the dashboard with the delivered-sales logic used in the SQL and Streamlit reporting layers.

## Orders
- **Total Orders** = distinct count of `order_id`
- **Delivered Orders** = distinct count of orders where status = delivered
- **Cancelled Orders** = distinct count of orders where status = canceled

## Customers
- **Total Customers** uses distinct `customer_unique_id`
- **Repeat Customers** uses customers with more than one order
- **Repeat Customer Rate** = repeat customers / total customers

## Products
- **Total Products** = distinct count of products
- **Revenue Per Product** = total revenue / total products
- **Category Revenue** uses delivered revenue logic

## Sellers
- seller KPI cards use seller-level aggregates
- the final seller page ranking visual was simplified because the original seller-state comparison visual was unstable under Power BI filter context

## Reviews and Delivery
- review metrics are based on `olist_order_reviews_dataset`
- delivery KPIs use delivered / cancelled order logic from `olist_orders_dataset`

---

# 5. Visual-Level Reconciliation Decisions

## 5.1 Executive Overview
### Final alignment
- Revenue, orders, customers, average review score, and average order value were aligned to the delivered-order business logic used across the project.
- The donut chart was finalized as **Total Orders by order_status**.

### Notes
This page is intended as a summary layer and broadly aligns well with SQL and Streamlit KPI totals.

---

## 5.2 Sales Performance
### Final alignment
- Revenue visuals use delivered revenue
- Freight cost and freight % use delivered-order sales logic
- The page includes month-wise revenue trend and previous-month comparison visuals
- Order-status donut uses total orders by status

### Notes
This page is one of the closest Power BI matches to the SQL / Streamlit outputs.

---

## 5.3 Customer Analysis
### Original issue
The original customer page included a cancellation-rate trend visual that was not especially useful and was harder to stabilize under the Power BI model.

### Final decision
The cancellation-rate visual was replaced with:

- **Top Customers by Revenue**

This was chosen because:
- it is easier to validate against SQL / Streamlit customer summaries
- it tells a stronger customer-value story
- it avoids weak or noisy trend behavior

### Final page logic
Customer page now focuses on:
- total customers
- revenue per customer
- repeat customers
- repeat rate
- average orders per customer
- top customers by revenue
- customer state distribution

---

## 5.4 Product & Category Analysis
### Final alignment
This page was kept close to the original design because the product-level KPIs and category visuals aligned well with the broader analytics outputs.

### Final page logic
- total products
- average item price
- revenue per product
- category revenue
- category revenue treemap
- average item price by category

---

## 5.5 Seller Analysis
### Original issue
The original seller-state visual repeatedly produced unstable or misleading outputs under Power BI filter context, including repeated grand-total behavior.

### Final decision
The seller-state visual was replaced with a seller ranking visual.

### Final page logic
Seller page now focuses on:
- total sellers
- seller revenue metrics
- revenue per seller metrics
- seller ranking visual

This keeps the page business-relevant while avoiding a weak or misleading state comparison chart.

---

## 5.6 Reviews & Delivery
### Final alignment
This page was successfully aligned around:
- review score averages
- customer satisfaction score
- delivered order rate
- 1-star and 5-star review percentages
- delivered orders
- cancellation rate
- net successful orders
- cancelled orders
- monthly review trend
- review score distribution

This page now functions as the quality and delivery performance summary layer of the dashboard.

---

# 6. Metrics That Match Closely Across Layers
The following metrics were explicitly aligned and are expected to match closely across SQL, Streamlit, and Power BI, subject to rounding and filter context:

- Total Revenue
- Total Orders
- Delivered Orders
- Total Customers
- Average Review Score
- Delivered Order Rate %
- Cancelled Orders
- Cancellation Rate %
- Total Products
- Total Sellers
- Revenue Per Customer
- Revenue Per Product

---

# 7. Metrics / Visuals That Use Power BI-Specific Simplification
The following areas were simplified or adapted in Power BI for report stability or business storytelling:

## Customer page
- cancellation-rate trend removed
- replaced with top customer ranking visual

## Seller page
- seller-state comparison removed
- replaced with seller ranking visual

These changes were intentional and do not reduce the business value of the report.  
They improve clarity and make the dashboard more robust as a portfolio project.

---

# 8. Final Interpretation of the Three Layers

## SQL Layer
Best for:
- detailed KPI validation
- exports and summary tables
- notebook-based analytics
- reconciliation and debugging

## Streamlit Layer
Best for:
- interactive business exploration
- customer segmentation
- cohort retention
- market basket analysis
- seller marketplace analysis

## Power BI Layer
Best for:
- executive storytelling
- high-level KPI monitoring
- presentation-ready dashboards
- recruiter / stakeholder-facing visual reporting

---

# 9. Final Conclusion
The final Power BI report should be interpreted as a **business-facing executive reporting layer** that sits on top of the deeper SQL and Streamlit analytics layers.

The reconciliation process in this project was not about forcing every chart to be identical across all tools.  
Instead, the goal was to make sure:

- the KPI logic is consistent
- the business story remains aligned
- Power BI presents a clean, stable, and credible executive dashboard
- SQL and Streamlit remain the detailed analytical backbone of the project