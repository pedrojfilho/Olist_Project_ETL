import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

tables = [
    "category_csv",
    "customers_csv",
    "geolocation_csv",
    "items_csv",
    "orders_csv",
    "payments_csv",
    "products_csv",
    "reviews_csv",
    "sellers_csv"
]

for table in tables:
    dyf = glueContext.create_dynamic_frame.from_catalog(
        database="owlist-raw-db",
        table_name=table
    )
    
    df = dyf.toDF()
    
    output = "s3://pedro-datalake-project/bronze/" + table.replace("_csv", "") + "/"
    
    df.write.mode("overwrite").parquet(output)
job.commit()