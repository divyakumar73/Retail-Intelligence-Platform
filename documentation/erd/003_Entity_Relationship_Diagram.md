# Retail Intelligence Platform

# Enterprise Entity Relationship Diagram (ERD)

**Version:** 1.0

**Project:** Retail Intelligence Platform

**Prepared By:** Divya Kumar

**Status:** Draft

---

# Purpose

The Entity Relationship Diagram (ERD) defines how datasets within the Retail Intelligence Platform relate to one another.

It serves as the architectural blueprint for:

* SQL development
* Python data merging
* Power BI data modeling
* KPI calculation
* Dashboard development
* Business reporting

A well-designed ERD ensures consistent relationships, preserves referential integrity, and reduces ambiguity when performing analysis.

---

# Objectives

The ERD has the following objectives:

* Identify relationships between all datasets.
* Define Primary Keys and Foreign Keys.
* Specify relationship cardinality.
* Support SQL JOIN operations.
* Simplify Power BI model creation.
* Document data flow across the analytics pipeline.

---

# Dataset Classification

The Retail Intelligence Platform contains three categories of tables.

## Fact Tables

Fact tables store measurable business events.

* Orders
* Order Items
* Payments
* Reviews

---

## Dimension Tables

Dimension tables describe business entities.

* Customers
* Products
* Sellers

---

## Reference Tables

Reference tables enrich analytical data.

* Geolocation
* Product Category Translation

---

# Enterprise Data Model

```text
                     Customers
                         │
                         │ customer_id
                         │
                         ▼
                     Orders
                         │
     ┌───────────────────┼────────────────────┐
     │                   │                    │
     ▼                   ▼                    ▼
Order Items          Payments             Reviews
     │
     ├──────────────┐
     │              │
     ▼              ▼
 Products        Sellers
     │              │
     ▼              ▼
Category      Geolocation
Translation

Customers
     │
     ▼
Geolocation
```

---

# Relationship Overview

The Orders table acts as the central transaction table.

All analytical workflows originate from Orders and extend into:

* Customer Analytics
* Product Analytics
* Seller Analytics
* Payment Analytics
* Review Analytics
* Geographic Analytics

This design follows a star-schema-inspired analytical model optimized for reporting and dashboarding.

---

# Relationship Types

| Parent    | Child                | Relationship                     |
| --------- | -------------------- | -------------------------------- |
| Customers | Orders               | One-to-Many (1:N)                |
| Orders    | Order Items          | One-to-Many (1:N)                |
| Orders    | Payments             | One-to-Many (1:N)                |
| Orders    | Reviews              | One-to-One / One-to-Many*        |
| Products  | Order Items          | One-to-Many (1:N)                |
| Sellers   | Order Items          | One-to-Many (1:N)                |
| Products  | Category Translation | Many-to-One (N:1)                |
| Customers | Geolocation          | Many-to-One (N:1) via ZIP Prefix |
| Sellers   | Geolocation          | Many-to-One (N:1) via ZIP Prefix |

> *Although most orders have one review, the dataset allows multiple review records to share an order identifier in some situations, so analysts should validate this assumption during data quality checks.

---

# Primary Keys

| Table                | Primary Key                    |
| -------------------- | ------------------------------ |
| Customers            | customer_id                    |
| Orders               | order_id                       |
| Order Items          | (order_id, order_item_id)      |
| Payments             | (order_id, payment_sequential) |
| Reviews              | review_id                      |
| Products             | product_id                     |
| Sellers              | seller_id                      |
| Category Translation | product_category_name          |
| Geolocation          | No Primary Key                 |

---

# Foreign Keys

| Child Table | Foreign Key           | Parent Table         |
| ----------- | --------------------- | -------------------- |
| Orders      | customer_id           | Customers            |
| Order Items | order_id              | Orders               |
| Order Items | product_id            | Products             |
| Order Items | seller_id             | Sellers              |
| Payments    | order_id              | Orders               |
| Reviews     | order_id              | Orders               |
| Products    | product_category_name | Category Translation |

---

# Join Reference Guide

| Business Question     | Tables Required                               |
| --------------------- | --------------------------------------------- |
| Total Orders          | Orders                                        |
| Revenue               | Orders + Order Items                          |
| Customer Analysis     | Customers + Orders                            |
| Product Analysis      | Products + Order Items                        |
| Seller Performance    | Sellers + Order Items                         |
| Payment Analysis      | Orders + Payments                             |
| Customer Satisfaction | Orders + Reviews                              |
| Category Analysis     | Products + Category Translation + Order Items |
| Geographic Analysis   | Customers/Sellers + Geolocation               |
---

# Relationship Cardinality

Relationship cardinality defines how records in one table relate to records in another table.

---

## Customers → Orders

```text
One Customer
      │
      ├────────► Many Orders
```

**Cardinality**

1 : N

Reason

One customer can place multiple orders over time.

---

## Orders → Order Items

```text
One Order
      │
      ├────────► Many Order Items
```

**Cardinality**

1 : N

Reason

A single order may contain multiple products.

---

## Orders → Payments

```text
One Order
      │
      ├────────► Many Payment Records
```

**Cardinality**

1 : N

Reason

Customers may split a payment across multiple payment methods.

---

## Orders → Reviews

```text
One Order
      │
      ├────────► One Review (typically)
```

**Cardinality**

1 : 1 (Business Perspective)

Although the dataset may contain edge cases, analytical reporting generally treats one order as having one customer review.

---

## Products → Order Items

```text
One Product
      │
      ├────────► Many Order Items
```

**Cardinality**

1 : N

A product may be purchased many times.

---

## Sellers → Order Items

```text
One Seller
      │
      ├────────► Many Order Items
```

**Cardinality**

1 : N

A seller fulfills many order items.

---

# SQL JOIN Strategy

The following joins will be used throughout the project.

## Customer Analysis

```sql
Customers
INNER JOIN
Orders
ON customer_id
```

---

## Revenue Analysis

```sql
Orders
INNER JOIN
Order Items
ON order_id
```

---

## Product Analysis

```sql
Order Items
INNER JOIN
Products
ON product_id
```

---

## Seller Analysis

```sql
Order Items
INNER JOIN
Sellers
ON seller_id
```

---

## Payment Analysis

```sql
Orders
INNER JOIN
Payments
ON order_id
```

---

## Review Analysis

```sql
Orders
INNER JOIN
Reviews
ON order_id
```

---

## Geographic Analysis

```sql
Customers
LEFT JOIN
Geolocation
ON customer_zip_code_prefix =
geolocation_zip_code_prefix
```

---

# Power BI Relationship Model

The Power BI semantic model should follow a star-schema design.

Fact tables should remain at the center of the model, while dimension tables should provide filtering and grouping. Avoid connecting dimension tables directly to each other whenever possible. This approach improves model performance and simplifies DAX calculations. Microsoft recommends this modeling pattern for analytical reporting.

Recommended relationships:

| From                 | To          | Cardinality              | Cross Filter |
| -------------------- | ----------- | ------------------------ | ------------ |
| Customers            | Orders      | One-to-Many              | Single       |
| Orders               | Order Items | One-to-Many              | Single       |
| Orders               | Payments    | One-to-Many              | Single       |
| Orders               | Reviews     | One-to-One / One-to-Many | Single       |
| Products             | Order Items | One-to-Many              | Single       |
| Sellers              | Order Items | One-to-Many              | Single       |
| Category Translation | Products    | One-to-Many              | Single       |

---

# Recommended Star Schema

```text
                 Customers
                      │
                      │
                      ▼
                 Orders (Fact)
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 Order Items      Payments      Reviews
      │
 ┌────┴─────┐
 ▼          ▼
Products   Sellers

     │
     ▼
Category Translation
```

---

# Data Flow Architecture

```text
Raw CSV Files

        │

        ▼

Data Validation

        │

        ▼

Data Cleaning

        │

        ▼

Processed Data

        │

        ▼

SQL Analytics

        │

        ▼

Python Analytics

        │

        ▼

Power BI Semantic Model

        │

        ▼

Executive Dashboard

        │

        ▼

Business Insights
```

---

# Modeling Best Practices

The following standards will be followed throughout the project.

* Preserve referential integrity between related tables.
* Never modify the original datasets stored in the `data/raw` directory.
* Use Primary Keys and Foreign Keys consistently.
* Keep transactional (fact) and descriptive (dimension) data separate.
* Create reusable joins instead of duplicating transformation logic.
* Document every calculated KPI.
* Validate row counts after every merge or join operation.
* Avoid many-to-many relationships unless explicitly required.

---

# Common Modeling Mistakes

Avoid the following:

* Joining on descriptive fields instead of key columns.
* Counting rows from the Payments table to calculate total orders.
* Using `customer_id` instead of `customer_unique_id` for repeat customer analysis.
* Ignoring duplicate ZIP code prefixes in the Geolocation table.
* Creating bidirectional relationships in Power BI without a business requirement.
* Mixing raw and cleaned datasets in the same workflow.

---

# ERD Validation Checklist

Before beginning SQL or Python analysis, verify:

* All primary keys are unique.
* Foreign key relationships are valid.
* Duplicate records have been investigated.
* Date columns use appropriate datetime data types.
* Monetary fields use numeric data types.
* Required relationships are established.
* Fact and dimension tables are clearly identified.

---

# Enterprise Architecture Summary

The Retail Intelligence Platform follows a dimensional modeling approach designed for business intelligence and reporting.

The model is centered on transactional fact tables, supported by descriptive dimension tables and lightweight reference tables.

This architecture enables:

* Efficient SQL queries
* Clean Power BI relationships
* Reliable KPI calculations
* Scalable dashboard development
* Consistent business reporting

The ERD documented here serves as the architectural foundation for every subsequent phase of the Retail Intelligence Platform.

---

**End of Entity Relationship Diagram Documentation**
