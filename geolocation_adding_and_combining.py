import os
import pandas as pd
from geopy.geocoders import Nominatim
import time

# Define the directory containing the CSV files
data_dir = 'data'

# Create a list to store the DataFrames from each CSV file
df_list = []

# Create a geolocator object using OpenStreetMap Nominatim
geolocator = Nominatim(user_agent='my_app')

# Define a function to geocode addresses
def geocode_address(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return (location.latitude, location.longitude)
        else:
            return None
    except:
        return None
    finally:
        time.sleep(1) # add a 1-second delay between geocoding requests

# Loop through all CSV files in the directory
for file in os.listdir(data_dir):
    if file.endswith('.csv'):
        # Read the CSV file into a DataFrame
        file_path = os.path.join(data_dir, file)
        df = pd.read_csv(file_path)

        # Add a 'Geokoordinaten' column to the DataFrame
        df['Geokoordinaten'] = df['Address'].apply(geocode_address)

        # Remove rows with missing 'Geokoordinaten' values
        df = df.dropna(subset=['Geokoordinaten'])

        # Add a 'Source' column to the DataFrame with the name of the CSV file
        df['Source'] = file

        # Append the DataFrame to the list
        df_list.append(df)

# Concatenate all DataFrames in the list into one DataFrame
combined_df = pd.concat(df_list, ignore_index=True)

# Print the combined DataFrame
print(combined_df.head())

# Save the combined DataFrame to a CSV file
combined_df.to_csv('combined2.csv', index=False)

