import matplotlib.pyplot as plt
import pandas as pd

# Read processed Parquet files from S3
df = pd.read_parquet("s3://nyc-taxi-processed/")

# Plot total trips by pickup location
df.groupby("pickup_location")["total_trips"].sum().plot(kind="bar")
plt.title("Total Trips by Pickup Location")
plt.xlabel("Pickup Location")
plt.ylabel("Total Trips")
plt.show()