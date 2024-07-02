import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

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

# Calculate the count of rainfall occurrences for each grid where rainfall is between 64mm and 114mm
occurrences = ((rainfall_2019 > 64) & (rainfall_2019 < 114)).sum(dim='TIME')

# Plot the occurrences of rainfall on a map with transparent background
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
occurrences.plot(x='LONGITUDE', y='LATITUDE', cmap='Blues', robust=True, vmin=0, vmax=10, ax=ax)
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Occurrences of Rainfall between 64mm and 114mm in 2019', fontweight='light')

# Add coastlines
ax.coastlines()

# Set longitude and latitude range
ax.set_extent([70, 100, 10, 35], crs=ccrs.PlateCarree())

# Set longitude and latitude tick range and labels
ax.set_xticks(range(70, 101, 10), crs=ccrs.PlateCarree())
ax.set_yticks(range(10, 36, 5), crs=ccrs.PlateCarree())
ax.xaxis.set_major_formatter('{.0f}°E')
ax.yaxis.set_major_formatter('{.0f}°N')

# Save the plot as a high-resolution image with transparent background
plt.savefig('rainfall_occurrences_plot_hd.png', dpi=300, transparent=True)  # Adjust the file name and dpi value as desired
plt.show()
