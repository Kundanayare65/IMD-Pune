import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the Excel sheet into a DataFrame
data_df = pd.read_excel("/Users/kundanayare/Downloads/K-mense clustring (for 6).xlsx")

# Define the columns to use for plotting
columns = ['Longitude', 'Latitude', 'Cluster']

# Create a FacetGrid using seaborn
sns.set(style='darkgrid')
g = sns.FacetGrid(data_df, col='Cluster')

# Map scatter plots to the longitude and latitude columns
g.map(plt.scatt-er, 'Longitude', 'Latitude')

# Set axis labels and title
g.set_axis_labels('Longitude', 'Latitude')

# Adjust the plot layout
g.fig.tight_layout()

# Show the plot
plt.show()