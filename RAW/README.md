# 🟫 RAW Layer — Olist Data Lake (AWS S3)

The **RAW layer** is the first zone of the Medallion Architecture and stores the Olist dataset **exactly as received**, in its original CSV format.  
No transformations, cleaning, or type adjustments are performed at this stage.  
This ensures full data lineage, traceability, and the ability to reprocess the dataset at any time.

---

## 📌 Purpose of the RAW Layer

- Preserve original source data  
- Enable auditing and full reproducibility  
- Serve as the input for the Bronze ingestion process  
- Maintain unmodified CSV files in AWS S3  
- Provide schemas for each dataset using JSON definitions  

---

## 📂 RAW Data Stored in S3

The following CSV files were uploaded to:

"s3://pedro-datalake-project/raw/"


**CSV Tables:**

- customers.csv  
- orders.csv  
- items.csv  
- products.csv  
- sellers.csv  
- payments.csv  
- geolocation.csv  
- category.csv  

Each CSV represents part of the Olist e-commerce dataset and serves as the raw source for downstream ETL processing.

---

## 🧾 Schema Extraction (JSON Files)

To improve documentation and data governance, the schema for each CSV file was extracted using PySpark and saved as structured **JSON schema files**.

Each schema file includes:

- Column names  
- Data types  
- Nullable attributes  
- Metadata for downstream validation  

These JSON files allow:

- Schema versioning  
- Comparison across layers (Bronze → Silver → Gold)  
- Automatic validation in future pipelines  

---

## 📁 Folder Structure

RAW/
│
├── Notebooks/
│ ├── check_schemas.ipynb # Notebook used to inspect CSV structure
│ └── sample_schemas/ # Extracted schemas in JSON
│ ├── category_schema.json
│ ├── customer_schema.json
│ ├── geolocation_schema.json
│ ├── items_schema.json
│ ├── orders_schema.json
│ ├── payments_schema.json
│ ├── products_schema.json
│ └── sellers_schema.json
│
└── README_RAW.md


---

## 🔍 Example Schema JSON Structure

Each schema file follows a similar pattern:

```json
{
  "table": "customers",
  "columns": [
    {"name": "customer_id", "type": "string", "nullable": true},
    {"name": "customer_unique_id", "type": "string", "nullable": true},
    {"name": "customer_zip_code_prefix", "type": "integer", "nullable": true},
    {"name": "customer_city", "type": "string", "nullable": true},
    {"name": "customer_state", "type": "string", "nullable": true}
  ]
}

🚀 Next Steps

Ingest these RAW CSVs into the Bronze layer

Convert to Parquet format

Enforce schemas using the JSON definitions

Begin cleaning and enrichment for the Silver layer

🧑‍💻 Author

Pedro Filho — Data Engineering Project (AWS + PySpark + Medallion Architecture)