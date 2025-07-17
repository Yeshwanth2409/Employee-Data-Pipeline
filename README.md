# Employee-Data-Pipeline
# 🚀 ETL Data Pipeline on Google Cloud using Cloud Data Fusion & Airflow

This project demonstrates how to build a complete **ETL (Extract, Transform, Load)** pipeline using **Google Cloud Platform (GCP)** services such as **Cloud Data Fusion**, **Cloud Storage**, **BigQuery**, and **Cloud Composer (Airflow)**, with final visualization in **Looker Studio**.

---

## 📌 Overview

This project walks through the end-to-end process of creating a real-time and scalable ETL pipeline. The workflow is automated with **Apache Airflow**, and includes the following steps:

1. **Extract** dummy employee data using Python and Faker.
2. **Store** the data in Google Cloud Storage (GCS).
3. **Transform & Load** the data into BigQuery using Cloud Data Fusion.
4. **Visualize** the final output using Looker Studio.

---

## 🛠️ Technologies Used

- **Google Cloud Platform (GCP)**
  - Cloud Storage
  - BigQuery
  - Cloud Data Fusion
  - Cloud Composer (Airflow)
- **Python** (for data generation)
- **Faker** library (mock data)
- **Apache Airflow** (workflow orchestration)
- **Looker Studio** (dashboard visualization)
- **Git, GitHub** (version control)

---

## 📁 Project Structure
etl-pipeline-datafusion-airflow/
│
├── dags/
│ └──etl_pipeline_dag.py # Airflow DAG definition
│
├── scripts/
│ └── data_extraction.py # Python script to generate & upload data to GCS
│
├── datafusion/
│ └── employee_pipeline.json # Data Fusion pipeline config
│
├── data/
│ └── employee_data.csv # Sample CSV file (auto-generated & uploaded to GCS)
│
├── looker/
│ └── dashboard_link.txt # (Optional) Link or description of dashboard
│
└── README.md # Project documentation


---

## 🔄 Workflow Breakdown

### ✅ Step 1: Data Extraction

- Generate **dummy employee records** using Python's `Faker` library.
- Save data into a CSV file (`employee_data.csv`).
- Upload the CSV to a **GCS bucket** using the Google Cloud Storage client.

```bash
python scripts/data_extraction.py
```
---
## 🔁 Step 2: Orchestration with Airflow (Cloud Composer)
Define an Airflow DAG in yeshwanth_employee_etl_dag.py.

Schedule the pipeline to:

Run the Python extraction script.

Trigger the Data Fusion pipeline.
extract_employee_data >> trigger_datafusion_pipeline

---
## 🔃 Step 3: ETL with Cloud Data Fusion
Create a pipeline that reads from GCS.

Apply transformations like masking and type casting.

Load clean data into BigQuery for analysis.
---
## 📊 Step 4: Visualization in Looker Studio
Use Looker Studio to connect with the BigQuery table.

## Create dashboards for:

Department-wise headcount

Salary distribution

Employee locations

Password strength masking
---
✅ How to Run This Project
Clone the repo

```bash
Copy
Edit
git clone https://github.com/yourusername/etl-pipeline-datafusion-airflow.git
cd etl-pipeline-datafusion-airflow
```
Configure GCP

Enable APIs: Cloud Data Fusion, Cloud Storage, BigQuery, and Composer.

Create and configure your:

Cloud Storage bucket

Data Fusion instance

BigQuery dataset

Composer (Airflow) environment

Upload DAG to Cloud Composer

Place yeshwanth_employee_etl_dag.py into the Composer environment’s dags/ folder.

Run the DAG

Trigger the DAG manually via Airflow UI or let it run on schedule.

🔍 Sample Output Locations
GCS Path: gs://yeshwanth-employee-data/employee_data.csv

BigQuery Table: your-project-id.dataset.employee_table

Looker Studio: [Insert link here once published]
---
🧠 Concepts Covered
Data Extraction using Python

Secure upload to Google Cloud Storage

Orchestration with Apache Airflow

ETL transformation using Cloud Data Fusion

Data warehousing with BigQuery

Dashboarding with Looker Studio

CI/CD-ready pipeline components
