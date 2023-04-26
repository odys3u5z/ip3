import pandas as pd
import matplotlib.pyplot as plt

# Read in the modified CSV file
df = pd.read_csv('GLOBAL_modified.csv')

# Define the mapping of roles to standardized roles
role_mapping = {'Manager': 'Manager',
                'Coordinator': 'Coordinator',
                'Koordinator': 'Coordinator',
                'Modellierer': 'Modellierer/Specialist',
                'Specialist': 'Modellierer/Specialist'}

# Extract the standardized roles from the 'Name' column
df['Role'] = df['Name'].apply(lambda name: next((v for k, v in role_mapping.items() if k in name), 'Other'))

# Extract the country code from the 'Source' column
df['Country'] = df['Source'].str[-2:]

# Create a dictionary to map country codes to colors
colors = {'CH': 'blue', 'UK': 'red', 'US': 'green', 'DE': 'orange', 'AT': 'purple'}

# Group the DataFrame by role and country and count the number of rows
role_counts = df.groupby(['Role', 'Country']).size().reset_index(name='Count')

# Pivot the DataFrame to have roles as rows and countries as columns
role_counts_pivot = role_counts.pivot(index='Role', columns='Country', values='Count').fillna(0)

# Define the order of roles to plot
role_order = ['Manager', 'Coordinator', 'Modellierer/Specialist']

# Create the horizontal bar chart for each role
fig, axs = plt.subplots(len(role_order), 1, figsize=(6, 8), sharex=True)
for i, role in enumerate(role_order):
    if role in role_counts_pivot.index:
        axs[i].barh(role_counts_pivot.columns, role_counts_pivot.loc[role], color=[colors[c] for c in role_counts_pivot.columns])
        axs[i].set_title(role)
        axs[i].set_xlabel('Count')
        axs[i].set_ylabel('Country')
plt.tight_layout()

# Show the plot
plt.show()
