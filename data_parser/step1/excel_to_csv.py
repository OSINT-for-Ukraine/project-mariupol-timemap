import pandas as pd


def excel_to_filtered_csv(excel_path, output_csv_path):
    """
    Reads an Excel file with multiple sheets (tables), adds an extra column to denote the name of the table,
    filters out rows where only the 'date' column is filled, combines all tables into a single DataFrame,
    and exports this combined DataFrame to a CSV file.

    Args:
    - excel_path: Path to the input Excel file.
    - output_csv_path: Path to the output CSV file.
    """
    # Load the Excel file
    xl = pd.ExcelFile(excel_path)

    # Initialize an empty DataFrame to hold all the combined data
    combined_df = pd.DataFrame()

    # Process each sheet in the Excel file
    for sheet_name in xl.sheet_names:
        # Read the current sheet
        df = pd.read_excel(excel_path, sheet_name=sheet_name)

        # Add an extra column for the table (sheet) name
        df['category'] = sheet_name

        # Filter out rows where only the 'date' column is filled and all other columns are empty
        relevant_columns = [col for col in df.columns if col not in ['date', 'category']]
        df = df.dropna(subset=relevant_columns, how='all')

        # Append the processed DataFrame to the combined DataFrame
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    # Save the combined DataFrame to a CSV file
    combined_df.to_csv(output_csv_path, index=False)

excel_file_path = 'ProjectMariupol.xlsx'
csv_file_path = 'ProjectMariupol.csv'
excel_to_filtered_csv(excel_file_path, csv_file_path)


# import pandas as pd
#
#
# def excel_to_csv_with_table_names(excel_file_path, csv_file_path):
#     # Read the entire Excel file
#     xl = pd.ExcelFile(excel_file_path)
#
#     # Assuming there's only one sheet, or you're interested in the first sheet
#     sheet_name = xl.sheet_names[0]
#     df = xl.parse(sheet_name)
#
#     # List to hold each chunk of the DataFrame with the table name added
#     dfs_with_table_names = []
#
#     # Variables to track the current table name and whether we're starting a new table
#     current_table_name = ""
#     start_new_table = True
#
#     # Temporary list to collect rows belonging to the current table
#     current_table_rows = []
#
#     for index, row in df.iterrows():
#         # Check if the row is empty (signifying the end of a table)
#         if row.isnull().all():
#             if current_table_rows:  # Check if there are any rows collected for the current table
#                 # Convert the list of rows to a DataFrame and append it to the list
#                 temp_df = pd.DataFrame(current_table_rows)
#                 temp_df['category'] = current_table_name  # Add the table name column
#                 dfs_with_table_names.append(temp_df)
#                 current_table_rows = []  # Reset the list for the next table
#             start_new_table = True
#             continue
#
#         if start_new_table:
#             # Assume the table name is in the first cell of the first row of each table
#             current_table_name = row.iloc[0]  # Changed to iloc for clarity
#             start_new_table = False
#             continue
#
#         # Collect the row for the current table
#         current_table_rows.append(row)
#
#     # Check if there are any remaining rows collected after the loop
#     if current_table_rows:
#         temp_df = pd.DataFrame(current_table_rows)
#         temp_df['category'] = current_table_name
#         dfs_with_table_names.append(temp_df)
#
#     # Concatenate all collected DataFrames
#     combined_df = pd.concat(dfs_with_table_names, ignore_index=True)
#
#     # Save the combined DataFrame to a CSV file
#     combined_df.to_csv(csv_file_path, index=False)
#
#
# # Example usage
# excel_file_path = 'ProjectMariupol.xlsx'
# csv_file_path = 'ProjectMariupol.csv'
# excel_to_csv_with_table_names(excel_file_path, csv_file_path)


