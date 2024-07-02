import pandas as pd
from sklearn.cluster import KMeans

# Read the Excel file
df = pd.read_excel("/Users/kundanayare/Downloads/previous 10 days data.xlsx")

# Select relevant columns for clustering
columns = ["Rainfall", "Previous Day 1 Rainfall", "Previous Day 2 Rainfall",
           "Previous Day 3 Rainfall", "Previous Day 4 Rainfall", "Previous Day 5 Rainfall","Previous Day 6 Rainfall","Previous Day 7 Rainfall","Previous Day 8 Rainfall","Previous Day 9 Rainfall","Previous Day 10 Rainfall"]
data = df[columns]

# Perform clustering using k-means
num_clusters = 6
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
cluster_labels = kmeans.fit_predict(data)

# Add 1 to cluster labels to start from 1 instead of 0
cluster_labels += 1

# Assign the cluster labels to the DataFrame
df['Cluster'] = cluster_labels

# Define the file path and save the clustered data to the specified location
output_path = "/Users/kundanayare/Downloads/k mense clustring (for previous 10 days for 6).xlsx"
df.to_excel(output_path, index=False)