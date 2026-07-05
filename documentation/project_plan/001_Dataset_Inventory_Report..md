# Retail Intelligence Platform

# 001 - Dataset Inventory & Initial Data Understanding

**Version:** 1.0  
**Sprint:** 2  
**Phase:** Data Understanding  
**Prepared By:** Divya Kumar  

---

# 1. Purpose

This document provides the **dataset inventory and initial data understanding** for the **Retail Intelligence Platform** project.

The goal of this report is to formally document every dataset used in the project before any cleaning, transformation, feature engineering, SQL development, Python analytics, or dashboard modeling begins.

This report establishes the foundation for all downstream work by answering the following questions:

- What datasets are available in the project?
- What business process does each dataset represent?
- Which datasets behave like fact tables, dimension tables, or reference tables?
- What is the likely grain of each dataset?
- Which columns are expected to act as keys or relationship links?
- What data-quality checks and profiling steps must be performed before analysis?

Rather than making assumptions about the data, this report records the datasets **as received** and defines the structure for the profiling and cleaning work that follows.

---

# 2. Dataset Source

| Attribute | Details |
|---|---|
| **Dataset Name** | Brazilian E-Commerce Public Dataset by Olist |
| **Dataset Provider** | Olist |
| **Source Platform** | Kaggle |
| **Data Period** | September 2016 – October 2018 |
| **Dataset Type** | Historical Transactional E-Commerce Data |
| **Country** | Brazil |
| **Primary Language** | Portuguese |
| **Translation Support** | Product category translation dataset available |

---

# 3. Why This Dataset Matters to the Project

The Retail Intelligence Platform is designed to deliver analytics across multiple business themes, including:

- customer segmentation and repeat purchase behavior
- cohort-style retention analysis
- seller and marketplace performance monitoring
- market basket and association-rule analysis
- executive KPI reporting through Streamlit dashboards

Because these use cases depend on multiple related source tables, it is important to first document the available datasets, their purpose, their expected business relationships, and their analytical role before any transformation or modeling begins.

This dataset inventory acts as the **foundation layer** for the entire project.

---

# 4. Dataset Inventory

The Olist dataset is composed of transactional, dimensional, and reference datasets.  
The table below captures the **initial business interpretation** of each dataset before profiling.

| Dataset | Business Domain | Expected Role | Likely Grain | Primary / Join Keys |
|---|---|---|---|---|
| `olist_orders_dataset.csv` | Sales | Fact Table | One row per order | `order_id`, `customer_id` |
| `olist_order_items_dataset.csv` | Sales | Fact Table | One row per order item | `order_id`, `product_id`, `seller_id` |
| `olist_order_payments_dataset.csv` | Finance | Fact Table | One row per payment transaction | `order_id` |
| `olist_order_reviews_dataset.csv` | Customer Experience | Fact Table | One row per order review | `review_id`, `order_id` |
| `olist_customers_dataset.csv` | Customer | Dimension | One row per customer record | `customer_id`, `customer_unique_id` |
| `olist_products_dataset.csv` | Product | Dimension | One row per product | `product_id` |
| `olist_sellers_dataset.csv` | Seller | Dimension | One row per seller | `seller_id` |
| `olist_geolocation_dataset.csv` | Geography | Reference | One row per geolocation / zip prefix record | `geolocation_zip_code_prefix` |
| `product_category_name_translation.csv` | Reference | Lookup | One row per category translation | `product_category_name` |

---

# 5. Initial Dataset Classification

Based on the business purpose of each table, the datasets can be classified into the following groups.

---

## 5.1 Fact Tables

These tables record **business events / transactions** and will likely drive most analytical calculations.

### Fact tables in this project
- **Orders** → overall order lifecycle and timestamps
- **Order Items** → product-level order lines, prices, freight values, seller relationships
- **Payments** → payment types, installments, payment value
- **Reviews** → customer review score and review timing

---

## 5.2 Dimension Tables

These tables describe **business entities** and enrich fact tables with descriptive attributes.

### Dimension tables in this project
- **Customers**
- **Products**
- **Sellers**

---

## 5.3 Reference / Lookup Tables

These tables provide **supporting metadata** used for enrichment, translation, or geographic mapping.

### Reference tables in this project
- **Geolocation**
- **Category Translation**

---

# 6. Expected Business Relationships

At a high level, the Olist dataset is expected to behave like a relational commerce model in which customers place orders, orders contain items, items connect to products and sellers, and orders also have associated payment and review records.

## Expected relationship map

```text
Customers
      │
      ▼
Orders
      │
 ┌────┼─────┐
 ▼    ▼     ▼
Items Payments Reviews
 │
 ├──────┐
 ▼      ▼
Products Sellers

Products
     │
     ▼
Category Translation

Customers
     │
     ▼
Geolocation

Sellers
     │
     ▼
Geolocation