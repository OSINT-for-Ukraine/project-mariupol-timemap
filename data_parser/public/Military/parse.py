import os
import shutil
from datetime import datetime, timedelta

def generate_date_list(start_date, end_date):
    delta = end_date - start_date  # timedelta
    return [start_date + timedelta(days=i) for i in range(delta.days + 1)]

def check_and_create_files(start_date, end_date):
    date_list = generate_date_list(start_date, end_date)
    previous_file = None
    for date in date_list:
        file_name = date.strftime("%d-%m-%Y") # Assuming text files, adjust extension if needed
        if not os.path.exists(file_name):
            if previous_file:
                shutil.copy(previous_file, file_name)
                print(f"Missing file for {date.strftime('%d-%m-%Y')} created, copying data from {previous_file}.")
            else:
                print(f"No file to copy from for the first date {date.strftime('%d-%m-%Y')}.")
        else:
            previous_file = file_name

# Example usage
start_date = datetime.strptime("19-02-2022", "%d-%m-%Y")
end_date = datetime.today()
check_and_create_files(start_date, end_date)