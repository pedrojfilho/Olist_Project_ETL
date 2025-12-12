# 🥈 Silver Layer — AWS Olist ETL Project

This directory contains the **Silver layer** of the **AWS Olist ETL Project**, responsible for transforming raw Bronze data into **clean, standardized, and analytics-ready datasets**, while still preserving the original business meaning of the data.

The Silver layer follows **Medallion Architecture best practices** and serves as the trusted source for building the Gold (dimensional and fact) layer.

---

## 🎯 Purpose of the Silver Layer

The Silver layer is responsible for:

- Cleaning and standardizing data
- Enforcing consistent schemas and data types
- Removing obvious data quality issues (duplicates, invalid keys)
- Preserving nulls and business meaning (no data imputation)
- Adding audit metadata
- Preparing data for dimensional modeling (Gold)

> ⚠️ **Important principle**  
> The Silver layer **does NOT create surrogate keys, business rules, or aggregations**.  
> Those transformations are intentionally deferred to the Gold layer.

---

## 🧱 General Transformation Rules

All Silver tables follow the same core standards:

### 🔹 Text standardization
- `lower()` or `upper()` applied consistently
- `trim()` to remove extra spaces
- Accent removal where applicable (cities, categories)

### 🔹 Data types
- Numeric fields explicitly cast (`int`, `double`)
- Date/time fields converted to `timestamp`

### 🔹 Deduplication
- Applied using **natural keys**, when applicable
- Ensures uniqueness without altering business meaning

### 🔹 Data integrity
- Records with missing **critical identifiers** are removed
- Non-critical nulls are preserved

### 🔹 Audit
- All tables include:
  ```text
  audit_timestamp

## 📂 Silver Tables Overview

### 🧍 customers
- CEP formatted to 5 digits  
- City standardized  
- State in uppercase  
- Deduplicated by `customer_id`

### 🗂️ category
- Header row removed from Bronze  
- Uses only English category names  
- Lowercase + character normalization  
- Deduplicated by category name

### 🌍 geolocation
- City normalized (lowercase + accent removal)  
- State standardized  
- ZIP prefix formatted  
- Latitude/longitude removed  
- Deduplicated by ZIP prefix

### 📦 products
- Category name standardized and normalized  
- Product dimensions and attributes preserved  
- Null values maintained (no imputation)  
- Audit timestamp added

### 🏪 sellers
- City normalized with accent removal  
- State standardized  
- ZIP prefix formatted  
- Deduplicated by `seller_id`

### 🛒 orders
- Header row removed  
- All date fields converted to timestamps  
- Order status standardized  
- Deduplicated by `order_id`

### 🧾 items
- Numeric fields cast correctly  
- Shipping dates converted to timestamp  
- Deduplicated by (`order_id`, `order_item_id`)  
- Referential integrity preserved

### 💳 payments
- Payment type standardized  
- Numeric values cast  
- Deduplicated by (`order_id`, `payment_sequential`)  
- Undefined payment types preserved for Gold handling

---

## 🛠️ Technology Stack
- **AWS S3** — Data Lake storage  
- **AWS Glue** — ETL jobs  
- **Apache Spark (PySpark)** — Data transformations  
- **Parquet** — Columnar storage format  
- **Jupyter / VSCode Notebooks** — Bronze validation before Silver  

---

## 🚀 Next Step: Gold Layer

The Silver layer feeds the **Gold layer**, where the following will be created:
- Dimension tables (`dim_customers`, `dim_products`, `dim_sellers`, `dim_category`, `dim_date`)  
- Fact tables (`fact_orders`, `fact_order_items`, `fact_payments`)   

---

## 📌 Project Status
- ✅ Silver layer fully implemented  
- ✅ Data quality validated via notebooks  
- ✅ Ready for Gold modeling  
