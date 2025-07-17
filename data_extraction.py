import csv
import random
import string
from faker import Faker
from google.cloud import storage

# Configuration
NUM_EMPLOYEES = 100
CSV_FILE_NAME = 'yeshwanth_employee_data.csv'
GCS_BUCKET_NAME = 'yeshwanth-employee-bucket'
GCS_BLOB_NAME = 'data/yeshwanth_employee_data.csv'

# Initialize Faker and character set
fake = Faker()
PASSWORD_CHAR_SET = string.ascii_letters + string.digits + 'm'

def generate_employee_data(filename: str, num_records: int) -> None:
    """Generate fake employee data and save it to a CSV file."""
    with open(filename, mode='w', newline='') as file:
        fieldnames = ['first_name', 'last_name', 'job_title', 'department', 'email',
                      'address', 'phone_number', 'salary', 'password']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_records):
            writer.writerow({
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "job_title": fake.job(),
                "department": fake.job(),
                "email": fake.email(),
                "address": fake.city(),
                "phone_number": fake.phone_number(),
                "salary": fake.random_number(digits=5),
                "password": ''.join(random.choice(PASSWORD_CHAR_SET) for _ in range(8))
            })

    print(f"{num_records} employee records written to {filename}")

def upload_to_gcs(bucket_name: str, source_file: str, blob_name: str) -> None:
    """Upload a local file to Google Cloud Storage."""
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    blob.upload_from_filename(source_file)
    print(f"File '{source_file}' uploaded to '{blob_name}' in bucket '{bucket_name}'")

if __name__ == "__main__":
    generate_employee_data(CSV_FILE_NAME, NUM_EMPLOYEES)
    upload_to_gcs(GCS_BUCKET_NAME, CSV_FILE_NAME, GCS_BLOB_NAME)
