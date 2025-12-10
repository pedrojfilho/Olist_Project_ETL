# 🏛️ Medallion Architecture Overview

The **Medallion Architecture** is a modern data engineering design pattern that organizes a Data Lake into structured layers with increasing levels of quality, refinement, and business value.  
This project applies the Medallion Architecture to transform the **Olist Dataset** into optimized analytical datasets.

---

## 🟫 Raw Layer (Landing Zone)

The **Raw Layer** stores data exactly as it arrives from the source, without any transformations or cleaning.  
It preserves the original structure and is essential for:

- Full lineage tracking  
- Auditing  
- Reprocessing in case of downstream failures  
- Ensuring data immutability  

**Examples of Raw assets in this project:**

- `customers.csv`  
- `orders.csv`  
- `items.csv`  
- `products.csv`  
- `payments.csv`  
- `sellers.csv`  
- `geolocation.csv`  
- `category.csv`

**Purpose:** Serve as the single source of truth for unmodified data.

---

## 🟧 Bronze Layer (Ingested / Parsed)

The **Bronze Layer** introduces the first structured form of data.  
Here, the pipeline performs:

- CSV → Parquet conversion  
- Basic normalization of column names  
- Type standardization  
- Removal of corrupt or malformed records  
- Efficient columnar storage  

**Purpose:**  
Provide consistent, performant, and query-friendly datasets while staying close to the original source.

**Benefits:**

- Better Spark and Athena performance  
- Enforced schemas  
- Efficient storage through Parquet  

---

## ⚪ Silver Layer (Clean / Enriched)

The **Silver Layer** applies business-level cleaning and enrichment.  
This is where data becomes *trusted* and ready for analytics.

Typical operations:

- Missing value handling  
- Date/time normalization  
- Standardization of states, cities, categories  
- Joins for contextual enrichment (e.g., Orders ↔ Customers ↔ Geolocation)  
- Calculated/derived fields  
- Deduplication  

**Purpose:**  
Deliver **clean, reliable, analytics-ready data**.

---

## 🟨 Gold Layer (Business / Analytics)

The **Gold Layer** contains the datasets consumed by BI tools, dashboards, ML models, and business applications.

Gold delivers:

- **Fact tables**  
- **Dimension tables**  
- **Business metrics**  
- **Star Schema Models**  
- **Optimized aggregates**  

Examples of Gold entities:

- Fact Sales  
- Dim Customer  
- Dim Product  
- Dim Date  
- Revenue KPIs, order performance, fulfillment metrics  

**Purpose:**  
Provide high-value analytical datasets with maximum usability and performance.

---

# 📊 End-to-End Pipeline Flow

```mermaid
flowchart TD
    A[Raw Layer] --> B[Bronze Layer]
    B --> C[Silver Layer]
    C --> D[Gold Layer]
