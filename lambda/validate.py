import json
import boto3

def validate_data(data):
    required_fields = ["trip_id", "pickup_time", "pickup_location", "fare"]
    return all(field in data for field in required_fields)

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        response = s3.get_object(Bucket=bucket, Key=key)
        data = json.loads(response['Body'].read())
        if validate_data(data):
            s3.put_object(Bucket='dr-nyc-taxi-staged', Key=key, Body=json.dumps(data))
        else:
            s3.put_object(Bucket='dr-nyc-taxi-errors', Key=key, Body=json.dumps(data))