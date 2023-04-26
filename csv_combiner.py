import os
import pandas as pd

# Define the directory containing the CSV files
data_dir = 'Data'

# Create a list to store the DataFrames from each CSV file
df_list = []

# Loop through all CSV files in the directory
for file in os.listdir(data_dir):
    if file.endswith('.csv'):
        # Read the CSV file into a DataFrame
        file_path = os.path.join(data_dir, file)
        df = pd.read_csv(file_path)

        # Append the DataFrame to the list
        df_list.append(df)

# Concatenate all DataFrames in the list into one DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

# Print the combined DataFrame
print(combined_df.head())

# Save the combined DataFrame to a CSV file
combined_df.to_csv('combined.csv', index=False)
