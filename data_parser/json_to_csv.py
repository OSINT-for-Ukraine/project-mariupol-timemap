import json
import pandas as pd

# Load JSON data
with open('list_of_events.json', 'r') as file:
    data = json.load(file)

# Extracting associations and creating a mapping for filter_paths to events
associations = {assoc['id']: assoc['filter_paths'] for assoc in data['Associations']}
events = data['Events']

# Create a DataFrame for events
events_df = pd.DataFrame(events)

# Convert 'date' column to datetime
events_df['date'] = pd.to_datetime(events_df['date'], format='%m/%d/%Y')

# Prepare Excel writer
writer = pd.ExcelWriter('output.xlsx', engine='openpyxl')

# Dictionary to hold dataframes for each filter path
dfs = {}

# Process each association
for assoc_id, filter_paths in associations.items():
    # Filter events based on association id
    filtered_events = events_df[events_df['associations'].apply(lambda x: assoc_id in x)]

    # Append events to corresponding filter path
    for path in filter_paths:
        sheet_name = path.replace('/', '_')  # Replace '/' with '_' to avoid Excel naming issues
        if sheet_name not in dfs:
            dfs[sheet_name] = filtered_events
        else:
            dfs[sheet_name] = pd.concat([dfs[sheet_name], filtered_events])

# Write each dataframe to a separate sheet in the Excel file
for sheet_name, df in dfs.items():
    # Write to Excel with date formatting
    df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Apply date format to the 'date' column
    for column in df:
        if column == 'date':
            worksheet = writer.sheets[sheet_name]
            for row in range(2, len(df) + 2):  # Adjusting rows for Excel's 1-based indexing and header row
                worksheet.cell(row=row, column=df.columns.get_loc(column) + 1).number_format = 'yyyy-mm-dd'

# Save the Excel file
writer._save()
