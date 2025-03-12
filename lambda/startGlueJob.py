import boto3
import json

def lambda_handler(event, context):
    glue = boto3.client('glue')
    job_name = 'dr-nyc-taxi-etl-job'  # Replace with your actual Glue job name

    try:
        response = glue.start_job_run(JobName=job_name)
        print(f"Successfully started Glue job: {response['JobRunId']}")
        return {
            'statusCode': 200,
            'body': json.dumps('Glue job started successfully')
        }
    except Exception as e:
        print(f"Error starting Glue job: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error starting Glue job: {str(e)}')
        }