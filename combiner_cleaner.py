import pandas as pd

# Read the GLOBAL.csv file into a DataFrame
global_df = pd.read_csv('GLOBAL.csv')

# Modify the 'Source' column
global_df['Source'] = global_df['Source'].apply(lambda x: x.split(')(')[1][:-5])

# Write the modified DataFrame to a new CSV file
global_df.to_csv('GLOBAL_modified.csv', index=False)
