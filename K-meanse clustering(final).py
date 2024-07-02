import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import geopandas as gpd
import cartopy.crs as ccrs
import netCDF4 as nc

def perform_kmeans_clustering(data):
    # Convert Date column to datetime type
    data['Date'] = pd.to_datetime(data['Date'])

    # Convert datetime column to numeric representation
    data['Date'] = data['Date'].map(pd.Timestamp.toordinal)

    # Drop rows with non-numeric values
    data = data.dropna().reset_index(drop=True)

    # Convert columns to numeric data type
    numeric_cols = data.select_dtypes(include='number').columns
    data[numeric_cols] = data[numeric_cols].astype(float)

    # Perform k-means clustering
    kmeans = KMeans(n_clusters=3)  # Set the desired number of clusters
    kmeans.fit(data[['Date', 'Rainfall']])

    # Add the cluster labels to the DataFrame
    data['Cluster'] = kmeans.labels_

    # Plot the clusters on India map
    # Read the shapefile of India
    shapefile_path = "/path/to/shapefile/India.shp"  # Replace with the actual path to the shapefile
    india_map = gpd.read_file(shapefile_path)

    # Plot the India map
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    india_map.plot(ax=ax, color='lightgray', edgecolor='black')

    # Plot the clusters on the map
    for cluster_label in data['Cluster'].unique():
        cluster_points = data[data['Cluster'] == cluster_label]
        ax.scatter(cluster_points['Longitude'], cluster_points['Latitude'], label=f'Cluster {cluster_label}')

    # Set the map projection to India-centric
    ax.set_extent([67, 98, 5, 38], crs=ccrs.PlateCarree())

    # Add title and labels
    plt.title('K-means Clustering on Rainfall Data')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    # Add legend
    plt.legend()

    # Show the map
    plt.show()


# File path for the NetCDF file
netcdf_file_path = "/Users/kundanayare/Documents/IMD INTERNSHIP/_Clim_Pred_LRF_New_RF25_IMD0p252019.nc"  # Replace with the actual path to the NetCDF file

# Read and process NetCDF file
dataset = nc.Dataset(netcdf_file_path)
longitude = dataset.variables['LONGITUDE'][:]
latitude = dataset.variables['LATITUDE'][:]
rainfall_data = dataset.variables['RAINFALL'][:]

# Create a grid of latitude-longitude points
lon, lat = np.meshgrid(longitude, latitude)

# Flatten the grid and rainfall data
data = pd.DataFrame({
    'Longitude': lon.flatten(),
    'Latitude': lat.flatten(),
    'Rainfall': rainfall_data.flatten()
})

# Perform k-means clustering and plot clusters on India map
perform_kmeans_clustering(data)
