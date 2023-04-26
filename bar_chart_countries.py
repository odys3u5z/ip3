import pandas as pd
import matplotlib.pyplot as plt

# Read in the modified CSV file
df = pd.read_csv('GLOBAL_modified.csv')

# Extract the country code from the 'Source' column
df['Country'] = df['Source'].str[-2:]

# Create a dictionary to map country codes to colors
colors = {'CH': 'blue', 'UK': 'red', 'US': 'green', 'DE': 'orange', 'AT': 'purple'}

# Group the DataFrame by country and count the number of rows
country_counts = df.groupby('Country').size().reset_index(name='Count')

# Sort the counts in descending order
country_counts = country_counts.sort_values(by='Count', ascending=False)

# Plot the horizontal bar chart
plt.barh(country_counts['Country'], country_counts['Count'], color=[colors[c] for c in country_counts['Country']])
plt.gca().invert_yaxis()
plt.title('Number of Job Advertisements by Country')
plt.xlabel('Count')
plt.ylabel('Country')
plt.tight_layout()

# Show the plot
plt.show()
