# 🛒 Retail Intelligence Platform

### End-to-End E-Commerce Analytics using Python, PostgreSQL, SQL, Pandas, Streamlit, Forecasting, Customer Segmentation, Market Basket Analysis, and Power BI

**Retail Intelligence Platform** is an end-to-end e-commerce analytics project built on the **Olist Brazilian E-Commerce Public Dataset**. It transforms raw multi-table marketplace data into a **business-ready retail analytics solution** covering customer behavior, repeat purchase analysis, retention, seller performance, product insights, forecasting, executive reporting, and interactive dashboard exploration.

This project was designed to simulate the work of a **Data Analyst / Business Analyst / BI Analyst** working on a retail marketplace use case. It combines **Python-based analytics**, **PostgreSQL SQL analysis**, **Power BI reporting**, and a **Streamlit analytics application** into a single portfolio project.

---

# 🚀 Project Highlights

- End-to-end analytics project using a real multi-table e-commerce dataset
- Data cleaning, EDA, feature engineering, and business KPI development
- Customer segmentation using **RFM**
- **Cohort / retention analysis**
- **Sales forecasting**
- **Market basket analysis**
- **Seller / marketplace analytics**
- **PostgreSQL SQL analytics layer**
- **Power BI executive dashboard**
- **Streamlit analytics application**

---

# 📊 Power BI Dashboard Preview

The **Power BI layer** provides executive reporting across sales, customers, products, sellers, and delivery / review quality.

## Executive Overview
![Executive Overview](./powerbi/dashboard_screenshots/executive_overview.png)

## Sales Performance
![Sales Performance](./powerbi/dashboard_screenshots/sales_performance.png)

## Customer Analysis
![Customer Analysis](./powerbi/dashboard_screenshots/customer_analysis.png)

## Product and Category Analysis
![Product and Category Analysis](./powerbi/dashboard_screenshots/product_category_analysis.png)

## Seller Analysis
![Seller Analysis](./powerbi/dashboard_screenshots/seller_analysis.png)

## Reviews and Delivery
![Reviews and Delivery](./powerbi/dashboard_screenshots/reviews_delivery.png)

---

# 🖥️ Streamlit Application Preview

The **Streamlit application** acts as the interactive analytics layer of the project, allowing business users to explore KPIs, customer segments, retention trends, seller analytics, and market basket insights through an app-based interface.

## Home
![Home](./app/app_screenshots/Home.png)

## Executive Dashboard
![Executive Dashboard](./app/app_screenshots/Executive_Dashboard.png)

## Customer Segmentation
![Customer Segmentation](./app/app_screenshots/Customer_Segmentation.png)

## Cohort Retention
![Cohort Retention](./app/app_screenshots/Cohort_Retention.png)

## Market Basket Analysis
![Market Basket Analysis](./app/app_screenshots/Market_Basket_Analysis.png)

## Seller Marketplace Analytics
![Seller Marketplace Analytics](./app/app_screenshots/Seller_Marketplace_Analytics.png)

## Retail Intelligence Platform App View
![Retail Intelligence Platform](./app/app_screenshots/Retail_Intelligence_Platform.png)

---

# 1. Business Problem

E-commerce businesses generate large volumes of data across customers, orders, products, sellers, reviews, and payments. However, raw transactional data is not directly useful for decision-makers unless it is transformed into business metrics, trend reporting, and analytical views.

This project was built to answer business questions such as:

- Who are the most valuable customers and how can they be segmented?
- How many customers make repeat purchases and what does retention behavior look like?
- What future sales trend can be expected from historical order data?
- Which product categories or items are frequently purchased together?
- Which sellers drive the most revenue and how does seller quality vary?
- How do delivery timelines and review scores impact customer experience?
- Which KPIs should leadership monitor through executive dashboards?
- How can retail stakeholders explore insights interactively through a self-service analytics app?

---

# 2. Dataset

This project uses the **Olist Brazilian E-Commerce Public Dataset**, a publicly available multi-table marketplace dataset containing approximately **100,000 orders** placed between **2016 and 2018**.

### Core tables used
- `olist_orders_dataset`
- `olist_order_items_dataset`
- `olist_order_payments_dataset`
- `olist_order_reviews_dataset`
- `olist_customers_dataset`
- `olist_products_dataset`
- `olist_sellers_dataset`
- `product_category_name_translation`
- `olist_geolocation_dataset`

### Main business domains covered
- Customers
- Orders
- Products
- Sellers
- Payments
- Reviews
- Product categories
- Delivery / order lifecycle

---

# 3. Project Objectives

The main objectives of the Retail Intelligence Platform are to:

- build a production-style analytics project around a real retail dataset
- clean and prepare multi-table marketplace data for analysis
- create business KPIs across customers, sellers, products, and orders
- perform customer segmentation using **RFM logic**
- analyze repeat purchase and retention behavior
- forecast sales / order trends using time-series techniques
- identify product co-purchase patterns through market basket analysis
- evaluate seller performance, delivery experience, and review quality
- build executive dashboards in **Power BI**
- deliver a business-facing analytics application using **Streamlit**
- create a **PostgreSQL SQL analytics layer** for KPI reporting and analytical exports

---

# 4. Project Architecture

```text
Raw Olist CSV Data
      │
      ▼
Python Data Understanding / Cleaning / Feature Engineering
      │
      ▼
Analytical Notebooks
      │
      ├── Exploratory Data Analysis
      ├── Customer Segmentation (RFM)
      ├── Cohort / Repeat Purchase Analysis
      ├── Sales Forecasting
      ├── Market Basket Analysis
      ├── Seller / Marketplace Analytics
      ├── Power BI Data Modeling
      └── PostgreSQL SQL Analytics
      │
      ▼
Exported Business Reporting Files / Analytical Outputs
      │
      ├── Streamlit App Data Layer
      ├── Power BI Dashboard Layer
      └── SQL Reporting Layer
      │
      ▼
Business Dashboards, KPIs, and Insights