import pandas as pd
import matplotlib.pyplot as plt

# Read in the modified CSV file
df = pd.read_csv('GLOBAL_modified.csv')

# Extract the country code from the 'Source' column
df['Country'] = df['Source'].str[-2:]

# Create a dictionary to map country codes to colors
colors = {'CH': 'blue', 'UK': 'red', 'US': 'green', 'DE': 'orange', 'AT': 'purple'}

# Count the number of job advertisements per source
source_counts = df['Source'].value_counts()

# Plot the horizontal bar chart
plt.barh(source_counts.index, source_counts, color=[colors[c] for c in df['Country']])
plt.gca().invert_yaxis()
plt.title('Number of Job Advertisements by Source')
plt.xlabel('Count')
plt.ylabel('Source')
plt.tight_layout()

# Show the plot
plt.show()
