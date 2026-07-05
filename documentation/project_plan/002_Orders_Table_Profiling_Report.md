# Retail Intelligence Platform

# 002 - Orders Table Profiling Report

**Version:** 1.0  
**Sprint:** 2  
**Phase:** Data Understanding  
**Table:** `olist_orders_dataset.csv`  
**Business Entity:** Orders  
**Prepared By:** Divya Kumar  
**Status:** Pending Profiling  

---

# 1. Purpose

This report documents the **profiling framework, business interpretation, and quality-validation plan** for the **Orders** table in the Retail Intelligence Platform project.

The Orders table is the central transactional dataset of the Olist e-commerce data model and acts as the **core order-level fact table** for downstream analytics. It links customers to order lifecycle events and provides the foundation for customer analytics, delivery performance analysis, repeat purchase tracking, and revenue-oriented modeling.

This document captures the expected structure and validation logic for the Orders dataset **before any cleaning, transformation, or feature engineering is performed**.

---

# 2. Business Purpose of the Orders Table

The Orders table records the lifecycle of every customer order placed on the marketplace.

It contains the key order identifier, the customer reference, the current order status, and multiple timestamps representing major stages of the fulfillment journey, such as:

- order purchase
- order approval
- carrier handoff
- final customer delivery
- estimated delivery expectation

Because it sits at the center of the transactional model, this table is expected to connect directly or indirectly to:

- customers
- order items
- payments
- reviews
- delivery performance analysis
- customer behavior and retention analysis

---

# 3. Table Classification

| Property | Value |
|---|---|
| **Business Domain** | Sales |
| **Table Type** | Fact Table |
| **Expected Grain** | One row per order |
| **Primary Key** | `order_id` |
| **Foreign Key** | `customer_id` |
| **Analytical Role** | Core order-level transactional fact |

---

# 4. Expected Columns

The Orders table is expected to contain the following columns.

| Column | Description |
|---|---|
| `order_id` | Unique order identifier |
| `customer_id` | Customer identifier linked to the customer table |
| `order_status` | Current status of the order |
| `order_purchase_timestamp` | Timestamp when the order was placed |
| `order_approved_at` | Timestamp when the order was approved |
| `order_delivered_carrier_date` | Timestamp when the order was handed to the carrier |
| `order_delivered_customer_date` | Timestamp when the order was delivered to the customer |
| `order_estimated_delivery_date` | Estimated delivery date promised to the customer |

---

# 5. Expected Business Role in the Data Model

The Orders table is the **central anchor table** in the commerce model.

## Expected relationships

| Related Table | Join Key | Relationship Expectation |
|---|---|---|
| `olist_customers_dataset.csv` | `customer_id` | Many orders belong to one customer |
| `olist_order_items_dataset.csv` | `order_id` | One order can have multiple order-item rows |
| `olist_order_payments_dataset.csv` | `order_id` | One order can have one or more payment rows |
| `olist_order_reviews_dataset.csv` | `order_id` | One order may have a review record |
| Downstream RFM / retention outputs | derived from order history | Used for customer-level behavior modeling |

---

# 6. Profiling Objectives

The profiling of the Orders table will answer the following questions:

1. Is the table truly at **one row per order** grain?
2. Is `order_id` unique and complete?
3. Are there missing or invalid `customer_id` references?
4. Are timestamp columns properly typed and logically sequenced?
5. What are the dominant order statuses and how are they distributed?
6. Are there missing values that reflect valid business process states or true data-quality issues?
7. Is the table ready to support downstream order, customer, and retention analysis?

---

# 7. Profiling Checklist

The following information will be collected directly from the dataset during profiling.

---

## 7.1 Dataset-Level Statistics

The following high-level statistics will be captured:

- total row count
- total column count
- file size
- memory usage
- count of duplicate rows
- count of duplicate primary keys
- date range covered by the table

---

## 7.2 Column-Level Statistics

For each column, the following attributes will be reviewed:

- data type
- null count
- null percentage
- distinct value count
- duplicate behavior where relevant
- minimum value
- maximum value
- sample values
- business interpretation / notes

---

# 8. Column Profiling Plan

Each column will be reviewed using the following logic.

| Column | Profiling Focus |
|---|---|
| `order_id` | uniqueness, nulls, duplicate detection |
| `customer_id` | nulls, foreign-key validation against Customers table |
| `order_status` | distinct values, frequency distribution, invalid categories |
| `order_purchase_timestamp` | min/max date, nulls, timestamp formatting |
| `order_approved_at` | missing values, timestamp sequence validation |
| `order_delivered_carrier_date` | missing values, carrier handoff timing logic |
| `order_delivered_customer_date` | missing values, delivery timing validation |
| `order_estimated_delivery_date` | date completeness, expected delivery comparison |

---

# 9. Business Validation Rules

The Orders table will be validated against expected business rules.

---

## 9.1 Primary Key Validation

### Questions to validate
- Is `order_id` unique?
- Are any duplicate order IDs present?
- Are any order IDs missing or blank?
- Does the table behave as one row per order?

### Expected rule
`order_id` should uniquely identify each order.

---

## 9.2 Foreign Key Validation

### Questions to validate
- Does every `customer_id` exist in the Customers table?
- Are any orphan order records present?
- Are any `customer_id` values missing?

### Expected rule
Every order should map to a valid customer record.

---

## 9.3 Timestamp Validation

### Questions to validate
- Are timestamp fields stored in valid datetime format?
- Is `order_purchase_timestamp` earlier than or equal to `order_approved_at`?
- Is `order_approved_at` earlier than carrier pickup / delivery events when present?
- Is `order_delivered_customer_date` logically after purchase date?
- Are estimated delivery dates reasonable relative to purchase and actual delivery?

### Expected sequence
Where values exist, the lifecycle should generally follow this order:

```text
purchase → approval → carrier handoff → customer delivery