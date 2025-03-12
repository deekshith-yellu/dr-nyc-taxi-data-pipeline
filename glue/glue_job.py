import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.context import SparkContext

# Initialize minimal context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

# Minimal parameters
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
job.init(args['JOB_NAME'], args)

# Read data - direct and efficient
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="nyc_taxi_db",
    table_name="staged_dr_nyc_taxi_staged",
    transformation_ctx="datasource0"
)

# Apply mapping in one step
mapped_frame = ApplyMapping.apply(
    frame=datasource,
    mappings=[
        ("trip_id", "string", "trip_id", "string"),
        ("pickup_time", "string", "pickup_time", "timestamp"),
        ("pickup_location", "string", "pickup_location", "string"),
        ("fare", "double", "fare", "double")
    ]
)

# Write directly to S3 with minimal options
glueContext.write_dynamic_frame.from_options(
    frame=mapped_frame,
    connection_type="s3",
    connection_options={"path": "s3://dr-nyc-taxi-processed/"},
    format="parquet"
)

# Finish
job.commit()