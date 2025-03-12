import json
import boto3
from datetime import datetime
import random
import uuid

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Simulate taxi trip data
    trip_data = {
        "trip_id": str(uuid.uuid4()),  # Unique ID for each trip
        "pickup_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "pickup_location": random.choice(["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]),
        "dropoff_location": random.choice(["Manhattan", "Brooklyn", "Queens", "Bronx", "Staten Island"]),
        "passenger_count": random.randint(1, 4),
        "trip_distance": round(random.uniform(1, 20), 2),  # Distance in miles
        "fare": round(random.uniform(10, 50), 2)  # Fare in USD
    }
    
    # Upload to S3
    s3.put_object(
        Bucket="dr-nyc-taxi-raw",  # Raw bucket name
        Key=f"trip_{trip_data['trip_id']}.json",
        Body=json.dumps(trip_data))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data ingested successfully!')
    }