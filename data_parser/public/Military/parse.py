import os

def remove_json_extension(directory):
    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the current file has a .json extension
        if filename.endswith('.json'):
            # Construct the old file path
            old_file = os.path.join(directory, filename)
            # Construct the new file path without the .json extension
            new_file = os.path.join(directory, filename[:-5])
            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed "{old_file}" to "{new_file}"')

# Specify the directory you want to change file extensions in
directory_path = '.'
remove_json_extension(directory_path)
