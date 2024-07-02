import netCDF4 as nc
import xarray as xr
import matplotlib.pyplot as plt

# Read the dataset using xarray
# Open the netCDF file
nc_file = nc.Dataset("/Users/kundanayare/Downloads/_Clim_Pred_LRF_New_RF25_IMD0p252019.nc")
 # Update with the actual file path
ds = xr.open_dataset(file_path)

RAINFALL = ds.RAINFALL
LATITUDE = ds.LATITUDE.values
LONGITUDE = ds.LONGITUDE.values

# Select a specific year from the dataset
specific_year_data = ds.sel(TIME='2019')  # Update with the desired year

# Get the rainfall variable
rainfall = specific_year_data['RAINFALL']

# Set the desired rainfall range
min_rainfall = 60
max_rainfall = 114

# Filter the rainfall data within the specified range
filtered_rainfall = rainfall.where((rainfall >= min_rainfall) & (rainfall <= max_rainfall))

# Plot the filtered rainfall data
plt.figure(figsize=(10, 6))
plt.scatter(LONGITUDE, LATITUDE, c=filtered_rainfall.mean(dim='TIME').values, cmap='Blues', s=10)
plt.colorbar(label='Rainfall (mm)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Moderate Rainfall (60 mm to 114 mm)')
plt.show()
