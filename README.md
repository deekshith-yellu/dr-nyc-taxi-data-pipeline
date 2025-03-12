# NYC Taxi Data Pipeline

## Overview
This project implements a **real-time NYC Taxi data pipeline** using AWS services (Lambda, S3, Glue) and Power BI for visualization. The pipeline ingests, processes, validates, and visualizes taxi trip data in near real-time.

---

## Components

### 1. **Data Ingestion**
- **AWS Lambda**: Simulates real-time taxi trip data and uploads it to S3 (`nyc-taxi-raw`).
  - **Script**: `lambda/ingest.py`.
  - **Trigger**: CloudWatch Events (every 1 minute).
  - **Data Format**: JSON (e.g., `{"trip_id": "12345", "pickup_time": "2025-03-09 10:00:00", "fare": 15.50}`).

### 2. **Data Processing**
- **AWS Glue**: Processes the raw data and writes it to S3 (`nyc-taxi-processed`) in Parquet format.
  - **Script**: `glue/process_taxi_data.py`.
  - **Transformations**:
    - Convert `pickup_time` to timestamp.
    - Convert `fare` to double.
    - Aggregate data by `pickup_location`.

### 3. **Data Validation**
- **Python Scripts**: Validate and visualize the processed data.
  - **Validation**: `scripts/validate.py` (checks for null values and data types).
  - **Visualization**: `scripts/visualize.py` (creates plots using Matplotlib).

### 4. **Visualization**
- **Power BI**: Connects to the processed data in S3 (`nyc-taxi-processed`) for real-time dashboards.
  - **Dashboards**:
    - Total trips by pickup location.
    - Average fare trends over time.

---

## File Structure
nyc-taxi-data-pipeline/
├── README.md # Project documentation
├── lambda/ # Lambda function code
│ └── ingest.py # Lambda script for data ingestion
├── glue/ # Glue job code
│ └── process_taxi_data.py # Glue script for data processing
├── scripts/ # Python scripts for validation and visualization
│ ├── validate.py # Script to validate processed data
│ └── visualize.py # Script to visualize processed data
├── docs/ # Documentation and diagrams
│ └── architecture_diagram.png # Architecture diagram of the pipeline
└── .gitignore # Files to ignore in Git

2. Set Up AWS Services
S3 Buckets:

Create three buckets:

nyc-taxi-raw: For raw JSON data.

nyc-taxi-staged: For staging data before processing.

nyc-taxi-processed: For processed Parquet files.

Lambda Function:

Deploy lambda/ingest.py to AWS Lambda.

Set up a CloudWatch Events trigger to run the Lambda every 1 minute.

Glue Crawler:

Create a crawler to scan nyc-taxi-staged and infer the schema.

Output the schema to a Glue Data Catalog table (e.g., staged_nyc_taxi).

Glue Job:

Create a Glue job using glue/process_taxi_data.py.

Configure the job to read from staged_nyc_taxi and write to nyc-taxi-processed.

3. Run the Pipeline
Ingest Data:

The Lambda function will automatically upload JSON files to nyc-taxi-raw.

Process Data:

Manually or automatically trigger the Glue job to process data from nyc-taxi-staged to nyc-taxi-processed.

Validate Data:

Run scripts/validate.py to check for null values and data types.

Visualize Data:

Run scripts/visualize.py to generate plots.

Connect Power BI to nyc-taxi-processed for real-time dashboards.

Usage
Lambda Function
Script: lambda/ingest.py.

Trigger: CloudWatch Events (every 1 minute).

Output: JSON files in nyc-taxi-raw.

Glue Job
Script: glue/process_taxi_data.py.

Input: JSON files in nyc-taxi-staged.

Output: Parquet files in nyc-taxi-processed.