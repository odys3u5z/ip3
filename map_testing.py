from geopy.geocoders import Nominatim
import pandas as pd

# Define the path to the job advertisements CSV file
job_ads_csv = 'Data___(2023_04_18___[12_09_43_PM])(BIM-Manager-CH).csv'

# Read the job advertisements CSV file into a DataFrame
job_ads_df = pd.read_csv(job_ads_csv)

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

# Add a 'Geokoordinaten' column to the job advertisements DataFrame
job_ads_df['Geokoordinaten'] = job_ads_df['Address'].apply(geocode_address)

# Count the number of rows with missing 'Geokoordinaten' values
num_deleted_rows = job_ads_df['Geokoordinaten'].isnull().sum()

# Remove rows with missing 'Geokoordinaten' values
job_ads_df = job_ads_df.dropna(subset=['Geokoordinaten'])

# Print the cleaned DataFrame and the number of deleted rows
print(job_ads_df.head())
print(f"Number of deleted rows: {num_deleted_rows}")
