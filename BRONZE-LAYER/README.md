# 🟤 Bronze Layer — AWS Olist ETL Project

The **Bronze Layer** represents the first stage of the Medallion Architecture.  
In this layer, data is **ingested from RAW** (CSV stored in S3) and written in **Parquet format**, without applying any cleaning or transformations.  
This ensures:

- Fidelity to the original source data  
- Improved performance through Parquet compression  
- Schema consistency for downstream layers  
- Standardized storage for Silver and Gold processing  

---

## 🚀 1. Glue Job — RAW → Bronze

The file:

GLUE-JOB/job-raw-to-bronze.py


Performs:

- Reading RAW CSV files via **AWS Glue Data Catalog**
- Converting DynamicFrame → Spark DataFrame
- Writing all tables into the Bronze Layer at:

s3://pedro-datalake-project/bronze/<table>/


📌 **No data cleaning or transformation is performed in this stage.**  
The purpose of the Bronze Layer is to preserve raw data while standardizing file format and structure.

---

## 🧪 2. Notebook — Sample Generation

The notebook:

Notebooks/create-samples-bronze.ipynb


Was used to:

- Read all Parquet files from the Bronze Layer  
- Generate **local Parquet samples** (10–30 rows each)  
- Document schemas and test transformations without relying on S3  

Samples are saved in:

SAMPLES-PARQUET/<table>_sample.parquet


These files allow:

- Fast local testing (`df.show()`, `df.printSchema()`)  
- Lightweight sample datasets for validation  
- Avoiding large data in the Git repository  

---

## 📁 3. Parquet Samples Included

The following sample datasets are included:

- `category_sample.parquet`
- `customers_sample.parquet`
- `geolocation_sample.parquet`
- `items_sample.parquet`
- `orders_sample.parquet`
- `payments_sample.parquet`
- `products_sample.parquet`
- `sellers_sample.parquet`

Each sample contains:

- The exact schema from the Bronze Layer  
- A subset of rows for local analysis  

---

## 🔜 Next Stage — Silver Layer

The **Silver Layer** will introduce:

- Data cleaning and standardization  
- Type conversions  
- Null handling  
- Date normalization  
- Column renaming and structuring  
- Referential integrity checks  
- Prep for analytical modeling (Gold Layer)  

This is where the majority of data quality logic will reside.

---

## 📚 References

- AWS Glue ETL Best Practices  
- Medallion Architecture (Databricks)  
- Apache Parquet Format  
- PySpark Structured API Documentation  

---
