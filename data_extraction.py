import pandas as pd
import os

def extract_employee_data(input_file_path):
    """Extracts employee data from a CSV file."""
    if not os.path.exists(input_file_path):
        raise FileNotFoundError(f"File not found: {input_file_path}")
    return pd.read_csv(input_file_path)

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, 'employee_data.csv')
    employee_df = extract_employee_data(csv_path)
    print(employee_df.head())
