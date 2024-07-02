import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set the bin intervals
bins = [0, 50, 100, 150, 200, 250, 300]

# Create a function to calculate the counts within each bin for a specific cluster
def calculate_counts(df, cluster):
    df_sub = df[df['Cluster'] == cluster]
    counts, _ = np.histogram(df_sub['Rainfall'], bins=bins)
    return counts

# Load the data from the Excel file
df = pd.read_excel("/Users/kundanayare/Downloads/k mense clustring (for previous 10 days for 6).xlsx")

# Calculate the counts for each cluster
cluster_counts = {}
for cluster in range(1, 6):
    cluster_counts[cluster] = calculate_counts(df, cluster)

# Define the x-axis midpoint values based on the bin intervals
x_midpoints = [(bins[i] + bins[i+1]) / 2 for i in range(len(bins)-1)]

# Plot the line plot using the counts for each cluster
for cluster in range(1, 6):
    plt.plot(x_midpoints, cluster_counts[cluster], label=f'Cluster {cluster}')

# Set the axis labels and title
plt.xlabel('Rainfall Range Midpoint (mm)')
plt.ylabel('Count')
plt.title('Count of Rainfall within Each Range Midpoint for Different Clusters')

# Display the legend
plt.legend()

# Show the plot
plt.show()
