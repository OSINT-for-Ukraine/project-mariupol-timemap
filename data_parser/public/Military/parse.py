# import os
#
# def remove_json_extension(directory):
#     # Iterate through all files in the specified directory
#     for filename in os.listdir(directory):
#         # Check if the current file has a .json extension
#         if filename.endswith('.json'):
#             # Construct the old file path
#             old_file = os.path.join(directory, filename)
#             # Construct the new file path without the .json extension
#             new_file = os.path.join(directory, filename[:-5])
#             # Rename the file
#             os.rename(old_file, new_file)
#             print(f'Renamed "{old_file}" to "{new_file}"')
#
# # Specify the directory you want to change file extensions in
# directory_path = '.'
# remove_json_extension(directory_path)
import os
import datetime
import shutil

def create_missing_files(base_path):
    # Calculate the date range for the last two years
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=2*365)

    current_date = start_date
    previous_file_path = None

    while current_date <= end_date:
        current_file_name = current_date.strftime("%d-%m-%Y")
        current_file_path = os.path.join(base_path, current_file_name)

        if not os.path.exists(current_file_path):
            if previous_file_path:
                # Copy the previous file to the current missing file
                shutil.copyfile(previous_file_path, current_file_path)
                print(f"Created missing file {current_file_name} by copying {previous_file_path}")
            else:
                print(f"No file to copy for the first date: {current_file_name}")
        else:
            previous_file_path = current_file_path

        current_date += datetime.timedelta(days=1)

# Replace '/path/to/your/files' with the actual path to your files
base_path = '.'
create_missing_files(base_path)