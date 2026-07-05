# dax_measures_notes.md

# DAX Measures Notes – Retail Intelligence Dashboard

## 1. Purpose
This file contains the core DAX measures used in the **Retail Intelligence Dashboard** Power BI project.  
The measures are grouped by business area so they are easy to maintain, explain in interviews, and reuse across report pages.

The measure design supports analysis across:
- Sales and revenue performance
- Orders and cancellations
- Customer behavior
- Product and category performance
- Seller performance
- Review and delivery quality
- Time-based trend analysis

---

# 2. Measure Organization Recommendation

Create a dedicated **Measures Table** in Power BI called:

- `Measures`

Inside it, organize measures in folders such as:
- Sales
- Orders
- Customers
- Products
- Sellers
- Reviews
- Delivery
- Time Intelligence

This makes the Power BI model cleaner and easier to navigate.

---

# 3. Base Assumptions
These DAX measures assume the main fact table is called:

- `fact_orders`

And the model includes:
- `dim_date`
- `dim_customer`
- `dim_product`
- `dim_seller`

Key columns assumed in `fact_orders`:
- `order_id`
- `customer_id`
- `seller_id`
- `product_id`
- `payment_value`
- `price`
- `freight_value`
- `review_score`
- `order_status`
- `order_purchase_timestamp`
- `order_delivered_customer_date`
- `order_estimated_delivery_date`

---

# 4. Sales Measures

## 4.1 Total Revenue
**Purpose:** Calculates the total payment value generated from all orders.

```DAX
Total Revenue =
SUM(fact_orders[payment_value])