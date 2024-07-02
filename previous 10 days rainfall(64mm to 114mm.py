import xarray as xr
import matplotlib.pyplot as plt

# Read the dataset using xarray
filename = '/Users/kundanayare/Documents/IMD INTERNSHIP/_Clim_Pred_LRF_New_RF25_IMD0p252019.nc'
ds = xr.open_dataset(filename)

# Extract necessary variables
rainfall = ds.RAINFALL
latitude = ds.LATITUDE
longitude = ds.LONGITUDE

# Select a specific year from the dataset
specific_year_data = ds.sel(TIME='2019')  # Update with the desired year

# Get the rainfall data for the specific year
rainfall_2019 = specific_year_data['RAINFALL']

# Calculate the average rainfall for each grid where rainfall is between 64mm and 114mm
average_rainfall = rainfall_2019.where((rainfall_2019 > 64) & (rainfall_2019 < 114)).mean(dim='TIME')

# Plot the average rainfall on a map
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
average_rainfall.plot(x='LONGITUDE', y='LATITUDE', cmap='Blues', robust=True, vmax=120)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Average Rainfall between 64mm and 114mm in 2019')

# Save the plot as a high-resolution image
plt.savefig('rainfall_plot_hd.png', dpi=300)  # Adjust the file name and dpi value as desired
plt.show()
