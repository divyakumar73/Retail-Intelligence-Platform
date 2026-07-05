# Retail Intelligence Platform

# 000 - Sprint 2 Data Understanding Plan

**Version:** 1.0  
**Sprint Number:** 2  
**Sprint Name:** Data Understanding  
**Methodology:** CRISP-DM  
**Status:** In Progress  
**Prepared By:** Divya Kumar  

---

# 1. Sprint Goal

The goal of **Sprint 2 - Data Understanding** is to build a complete understanding of the Olist dataset before any cleaning, transformation, SQL modeling, or dashboard development begins.

This sprint focuses on **understanding the data exactly as received**, not modifying it.

The work in this sprint will establish a structured foundation for the rest of the Retail Intelligence Platform by answering core questions about:

- dataset availability
- table structure and grain
- column-level data quality
- missing values and duplicates
- key integrity
- relationships across datasets
- business meaning of each table
- readiness for downstream analysis

---

# 2. Sprint Objective

The objective of Sprint 2 is to profile and document every dataset used in the Retail Intelligence Platform.

This phase is strictly focused on **inspection, profiling, and validation**.  
No records will be deleted, updated, cleaned, transformed, or engineered during this sprint.

Instead, the sprint will produce a structured understanding of:

- what datasets exist
- how each dataset fits into the business model
- what quality issues are present
- what relationships need validation
- what assumptions must be confirmed before data cleaning begins

The findings from this sprint will directly guide **Sprint 3 - Data Cleaning and Preparation**.

---

# 3. Why This Sprint Matters

The Retail Intelligence Platform depends on multiple related datasets from the Olist e-commerce data model, including orders, customers, products, sellers, payments, and reviews.

Before any KPI calculation, dashboard design, or advanced analytics can be trusted, the project must first answer foundational questions such as:

- Is each table at the expected grain?
- Are primary keys unique?
- Are foreign-key relationships valid?
- Which columns contain missing values?
- Are timestamps logically sequenced?
- Are business categories and statuses consistent?
- Which data-quality issues must be handled before analysis?

Sprint 2 exists to answer those questions systematically.

---

# 4. Sprint Scope

## Included in Sprint 2

This sprint includes:

- dataset inventory creation
- table-level profiling
- column-level profiling
- row and column statistics
- data-type validation
- missing-value assessment
- duplicate-record analysis
- primary-key validation
- foreign-key validation
- relationship validation
- business interpretation of tables
- initial data-quality observations
- documentation of findings

---

## Excluded from Sprint 2

This sprint does **not** include:

- data cleaning
- feature engineering
- SQL analytics and business KPI development
- dashboard development
- machine learning or forecasting
- final business reporting

These activities belong to later sprints in the project lifecycle.

---

# 5. Sprint Deliverables

At the end of Sprint 2, the project should contain the following deliverables.

## Core deliverables
- Dataset Inventory Report
- table profiling reports
- table-level statistics
- column-level statistics
- data-type validation findings
- missing-value analysis
- duplicate analysis
- primary-key validation notes
- foreign-key validation notes
- relationship validation summary
- initial business observations
- data-quality assessment notes
- Sprint 2 summary documentation

## Expected project documents
Examples of Sprint 2 documentation include:

- `001_Dataset_Inventory_Report.md`
- `002_Orders_Table_Profiling_Report.md`
- additional profiling reports for Customers, Order Items, Payments, Reviews, Products, Sellers, Geolocation, and Category Translation
- final Sprint 2 summary report

---

# 6. Datasets Included in Sprint 2

The following Olist datasets are included in the Data Understanding phase.

| Dataset | Purpose |
|---|---|
| `olist_orders_dataset.csv` | Order lifecycle and order-level fact data |
| `olist_customers_dataset.csv` | Customer master / customer identity data |
| `olist_order_items_dataset.csv` | Product-level order transaction lines |
| `olist_order_payments_dataset.csv` | Payment information for orders |
| `olist_order_reviews_dataset.csv` | Customer review and satisfaction data |
| `olist_products_dataset.csv` | Product master information |
| `olist_sellers_dataset.csv` | Seller master information |
| `olist_geolocation_dataset.csv` | Geographic / zip-prefix reference data |
| `product_category_name_translation.csv` | Category translation lookup table |

---

# 7. Sprint Workflow

Sprint 2 follows a structured data-understanding workflow.

```text
Acquire Dataset
      │
      ▼
Inspect Files
      │
      ▼
Inventory Tables
      │
      ▼
Profile Tables
      │
      ▼
Validate Data Types
      │
      ▼
Assess Missing Values
      │
      ▼
Check Duplicate Records
      │
      ▼
Validate Primary Keys
      │
      ▼
Validate Foreign Keys
      │
      ▼
Understand Relationships
      │
      ▼
Document Findings
      │
      ▼
Prepare for Data Cleaning