import xarray as xr
import matplotlib.pyplot as plt

# Read the dataset using xarray
filename = '/Users/kundanayare/Documents/IMD INTERNSHIP/_Clim_Pred_LRF_New_RF25_IMD0p252019.nc'
ds = xr.open_dataset(filename)

# Extract necessary variables
rainfall = ds.RAINFALL
latitude = ds.LATITUDE
longitude = ds.LONGITUDE

# Define the latitude and longitude boundaries for the desired region
lat_min, lat_max = 10, 20
lon_min, lon_max = 70, 80

# Select a specific year from the dataset
specific_year_data = ds.sel(TIME='2019')  # Update with the desired year

# Get the rainfall data for the specific year within the desired region
rainfall_2019_region = specific_year_data['RAINFALL'].where(
    (specific_year_data['LATITUDE'] >= lat_min) &
    (specific_year_data['LATITUDE'] <= lat_max) &
    (specific_year_data['LONGITUDE'] >= lon_min) &
    (specific_year_data['LONGITUDE'] <= lon_max)
)

# Calculate the average rainfall for the region where rainfall is between 64mm and 114mm
average_rainfall_region = rainfall_2019_region.where(
    (rainfall_2019_region > 64) & (rainfall_2019_region < 114)
).mean(dim='TIME')

# Plot the average rainfall for the region on a map
plt.figure(figsize=(10, 6))
average_rainfall_region.plot(
    x='LONGITUDE',
    y='LATITUDE',
    cmap='Blues',
    robust=True,
    vmin=60,
    vmax=120,
    cbar_kwargs={'label': 'Average Rainfall (mm)'}
)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Average Rainfall between 64mm and 114mm in 2019\nRegion: {} to {} Latitude, {} to {} Longitude'.format(lat_min, lat_max, lon_min, lon_max), fontweight='light')

# Save the plot as a high-resolution image
plt.savefig('rainfall_plot_hd.png', dpi=300)
plt.show()
