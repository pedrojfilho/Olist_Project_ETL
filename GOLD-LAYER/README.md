# 🥇 Gold Layer — Analytical Data Model

The **Gold layer** represents the **analytical and consumption-ready layer** of the data platform.  
It is designed following **dimensional modeling (Star Schema)** principles and serves as the
single source of truth for **BI tools, dashboards, KPIs, and analytical queries**.

All tables in this layer are built using **PySpark** and executed in **AWS Glue**, with
local notebooks used to reproduce logic and validate results for portfolio and development purposes.

---

## 🎯 Design Principles

The Gold layer follows these core principles:

- **Dimensional modeling (Star Schema)**
- **Clear separation of responsibilities**
  - Creation logic
  - Validation logic
  - Presentation (BI)
- **No data imputation or assumptions**
- **Full numeric precision preserved**
- **Business rules applied explicitly and documented**
- **Formatting and rounding handled only at the dashboard layer**

---

## 🧱 Gold Layer Structure

The Gold layer is composed of:

### ⭐ Dimensions
- `dim_date`
- `dim_customer`
- `dim_products`
- `dim_sellers`
- `dim_geolocation`

### 📊 Fact Tables
- `fact_orders` (base transactional fact)
- `fact_seller_performance` (aggregated KPI fact)
- `fact_product_performance` (aggregated KPI fact)

---

## ⭐ Dimensions Overview

### `dim_date`
A programmatically generated date dimension covering a fixed date range.

**Key attributes:**
- `date_key` (surrogate key)
- Year, month, day, quarter, week
- Weekday name
- Weekend flag

📌 Generated independently of source systems to ensure consistency.

---

### `dim_customer`
Customer dimension enriched with **purchase behavior metrics**.

**Key attributes:**
- Customer identifiers
- Location (city, state, region)
- First order date
- Last order date
- Total orders
- Recency (days since last purchase)

📌 Metrics are derived from historical orders and preserved without assumptions.

---

### `dim_products`
Product dimension enriched with **physical and logistical attributes**.

**Derived attributes:**
- Product volume (cm³)
- Density
- Bulky flag (`is_bulky`)

📌 If physical dimensions are missing in the Silver layer, derived attributes remain **NULL**.
This behavior is intentional and documented to preserve data integrity.

---

### `dim_sellers`
Seller dimension enriched with **regional classification**.

**Key attributes:**
- Seller identifiers
- City, state
- Region (Norte, Nordeste, Sudeste, Sul, Centro-Oeste)

---

### `dim_geolocation`
Geographical dimension aggregated by ZIP code prefix.

**Key attributes:**
- ZIP code prefix
- City
- State

📌 Ensures one row per ZIP prefix for analytical joins.

---

## 📊 Fact Tables Overview

### `fact_orders`
Base transactional fact table representing **orders**.

**Key features:**
- Integrates orders, order items, payments, sellers, and customers
- Stores surrogate keys where applicable
- Contains business metrics and flags

**Key metrics:**
- Total paid
- Delivery time (days)
- Delay flag (`is_delayed`)

📌 `is_delayed` is **NULL** for non-delivered or canceled orders, representing
*non-applicable* cases rather than false values.

---

### `fact_seller_performance`
Aggregated fact table providing **seller-level KPIs**.

**Granularity:** one row per seller

**Metrics include:**
- Total orders
- Total customers
- Total revenue
- Freight cost
- Average delivery time
- Late deliveries
- On-time delivery rate

📌 KPIs are pre-aggregated to optimize dashboard performance.

---

### `fact_product_performance`
Aggregated fact table providing **product-level KPIs**.

**Granularity:** one row per product

**Metrics include:**
- Total orders
- Total customers
- Revenue and freight metrics
- Average price and freight
- Late delivery count
- Percentage of late deliveries (`pct_late`)

📌 Products with zero orders have:
- `total_orders = 0`
- Percentage metrics set to **NULL**, indicating *non-applicable* values.

---

## ⚠️ Handling NULL Values

NULL values in the Gold layer are **intentional and meaningful**.

Examples:
- Products or sellers with no orders
- Orders without delivery dates
- Missing physical dimensions

📌 **NULL does not mean error** — it represents *unknown* or *not applicable* data.

No artificial defaults or assumptions are introduced at this layer.

---

## 🔢 Numeric Precision & Formatting

- All numeric values are stored with **full precision**
- No rounding is applied during Gold table creation
- This avoids cumulative rounding errors in analytical aggregations

📊 **Rounding and formatting are handled exclusively at the dashboard / BI layer**.

---

## 🧪 Validation Strategy

For each Gold table, two notebooks are maintained:

1. **Creation Notebook**
   - Demonstrates transformation logic
   - Does not write data
2. **Validation Notebook**
   - Reads data directly from S3
   - Validates:
     - Schema integrity
     - Granularity
     - Key uniqueness
     - Metric consistency
     - Business rules

---

## 🧠 Why This Matters

This Gold layer design:
- Mirrors real-world data warehouse architectures
- Follows industry best practices
- Separates engineering, governance, and presentation concerns
- Produces reliable, explainable, and scalable analytical data

---

## 🚀 Ready for Consumption

The Gold layer is ready to be consumed by:
- BI tools (Power BI, QuickSight, Tableau)
- Analytical queries
- KPI dashboards
- Data science workloads

---
