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

# Select a specific time step from the dataset
specific_time_step = 0  # Replace 0 with the desired time step index
rainfall_data = rainfall.isel(TIME=specific_time_step)

# Plot the rainfall data on a contour map
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.coastlines()
plot = rainfall_data.plot.contourf(ax=ax, transform=ccrs.PlateCarree(), cmap='Blues')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title(f'Rainfall at Time Step {specific_time_step}', fontweight='light')

# Add a colorbar to the plot
cbar = plt.colorbar(plot, ax=ax, orientation='horizontal', pad=0.05, shrink=0.8)
cbar.set_label('Rainfall (mm)')

# Set longitude and latitude range
ax.set_extent([70, 100, 10, 35], crs=ccrs.PlateCarree())

# Set longitude and latitude tick range and labels
ax.set_xticks(range(70, 101, 10), crs=ccrs.PlateCarree())
ax.set_yticks(range(10, 36, 5), crs=ccrs.PlateCarree())
ax.xaxis.set_major_formatter('{.0f}°E')
ax.yaxis.set_major_formatter('{.0f}°N')

plt.show()
