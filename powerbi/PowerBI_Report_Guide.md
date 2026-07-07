
# Power BI Report Guide – Retail Intelligence Dashboard

## 1. Purpose
This guide explains the structure, page logic, KPI design, and visual choices used in the **Retail Intelligence Dashboard** Power BI report.

The dashboard is part of the larger **Retail Intelligence Platform**, which includes:
- a SQL analytics layer
- a Streamlit analytics application
- a Power BI executive dashboard layer

The Power BI report is designed as the **executive-facing visual reporting layer** of the project.

---

# 2. Dashboard Pages

The report contains six main pages:

1. **Executive Overview**
2. **Sales Performance**
3. **Customer Analysis**
4. **Product & Category Analysis**
5. **Seller Analysis**
6. **Reviews & Delivery Executive Overview**

---

# 3. Page-by-Page Summary

## 3.1 Executive Overview
**Purpose**  
Provide a high-level business snapshot of revenue, orders, customers, reviews, delivery rate, and revenue trends.

**Key KPIs**
- Total Revenue
- Total Orders
- Total Customers
- Average Review Score
- Average Order Value
- Delivered Order Rate %
- Revenue YTD
- Revenue MTD

**Key visuals**
- Total Orders by `order_status`
- Total Revenue by Month Year

---

## 3.2 Sales Performance
**Purpose**  
Focus on delivered sales, freight cost, monthly revenue movement, and revenue trend comparisons.

**Key KPIs**
- Total Revenue
- Total Delivered Orders
- Average Order Value
- Delivered Orders
- Freight % of Revenue

**Key visuals**
- Total Revenue by Month Year
- Total Revenue and Total Freight Cost by Month Year
- Total Revenue and Previous Month Revenue by Month Year
- Total Orders by `order_status`

---

## 3.3 Customer Analysis
**Purpose**  
Analyze customer scale, repeat purchasing behavior, average customer value, and top customer contribution.

**Key KPIs**
- Total Customers
- Revenue Per Customer
- Repeat Customers
- Repeat Customer Rate
- Average Orders Per Customer

**Key visuals**
- Top Customers by Revenue
- Total Customers by `customer_state`

**Note**  
An earlier cancellation-rate visual was replaced with a customer ranking visual to improve clarity and avoid weak business storytelling on the customer page.

---

## 3.4 Product & Category Analysis
**Purpose**  
Analyze product scale, category-level revenue, and price behavior across product categories.

**Key KPIs**
- Total Products
- Average Item Price
- Revenue Per Product
- Category Revenue

**Key visuals**
- Category Revenue by `product_category_name_english`
- Average Item Price by `product_category_name_english`

---

## 3.5 Seller Analysis
**Purpose**  
Analyze seller scale, seller revenue performance, and seller ranking.

**Key KPIs**
- Total Sellers
- Total Revenue Per Seller
- Seller Revenue
- Average Revenue Per Seller

**Key visuals**
- Seller ranking visual based on seller performance / seller orders

**Note**  
The original seller-state comparison visual was replaced because it was not reliable under the Power BI model context. A seller ranking visual provides stronger business value and a more stable report output.

---

## 3.6 Reviews & Delivery Executive Overview
**Purpose**  
Monitor review quality, customer satisfaction, delivery success, and cancellation behavior.

**Key KPIs**
- Average Review Score
- Customer Satisfaction Score
- Delivered Order Rate %
- 1-Star Review %
- 5-Star Review %
- Delivered Orders
- Cancellation Rate %
- Net Successful Orders
- Cancelled Orders

**Key visuals**
- Average Review Score by Month Year
- 1-Star Review Count vs 5-Star Review Count
- Total Review Count by `review_score`

---

# 4. Alignment with SQL and Streamlit
This project includes three reporting / analytics layers:

## SQL Layer
Used for:
- KPI reconciliation
- summary reporting tables
- seller, customer, review, and product analysis exports
- notebook-driven analytics

## Streamlit Layer
Used for:
- interactive analytics
- customer segmentation
- cohort retention
- market basket analysis
- seller marketplace exploration
- business-facing navigation

## Power BI Layer
Used for:
- executive reporting
- visual KPI storytelling
- stakeholder-friendly dashboarding
- presentation-ready summary views

Power BI KPIs were aligned to the SQL and Streamlit outputs wherever possible.  
Where a visual was not stable or meaningful in Power BI, a business-equivalent visual was used instead.

---

# 5. Important Modeling Notes
- `Fact Sales` is the primary transactional table used for sales-related measures.
- `olist_orders_dataset` is used for order status, order-level counts, and date logic.
- Review measures are driven by `olist_order_reviews_dataset`.
- Date slicing is driven by the `Date` table.
- Delivered-order logic is used for most sales-focused KPIs.

---

# 6. Filters and Slicers
The report uses a consistent slicer pattern across pages to support cross-page analysis.

Common slicers include:
- Year
- Month Name
- Order Status
- Customer State (customer page)
- Seller State (seller page)

These slicers allow the report to be used as a business-facing dashboard for trend, customer, seller, and review analysis.

---

# 7. Design Notes
The report uses a dark executive dashboard layout with:
- page-level KPI cards
- category-specific analytical visuals
- shared date filtering logic
- high-level summary views rather than notebook-style detail

The goal of the dashboard is not to replace SQL or Streamlit analysis, but to present the most decision-relevant metrics in a concise and visually accessible way.

---

# 8. Final Interpretation
This Power BI report should be read as the **executive summary layer** of the Retail Intelligence Platform.

- **SQL** = deeper analytical and tabular reporting layer
- **Streamlit** = interactive business analytics application
- **Power BI** = presentation and KPI dashboard layer

Power BI is the final visual storytelling layer built on top of the broader analytics pipeline.