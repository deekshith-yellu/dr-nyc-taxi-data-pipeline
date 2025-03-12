import pandas as pd

# Read processed Parquet files from S3
df = pd.read_parquet("s3://nyc-taxi-processed/")

# Check for null values
print("Null values:\n", df.isnull().sum())

# Check data types
print("Data types:\n", df.dtypes)