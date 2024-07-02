import netCDF4 as nc
import pandas as pd
from datetime import timedelta

# Open the netCDF file
nc_file = nc.Dataset('/Users/kundanayare/Documents/IMD INTERNSHIP/_Clim_Pred_LRF_New_RF25_IMD0p252019.nc')

# Get the variable objects
longitude_var = nc_file.variables['LONGITUDE']
latitude_var = nc_file.variables['LATITUDE']
time_var = nc_file.variables['TIME']
rainfall_var = nc_file.variables['RAINFALL']

# Get the data arrays
longitudes = longitude_var[:]
latitudes = latitude_var[:]
times = nc.num2date(time_var[:], time_var.units)
rainfall = rainfall_var[:]

# Reshape rainfall array to match grid dimensions
rainfall_reshaped = rainfall.reshape(len(times), len(latitudes), len(longitudes))

# Create a DataFrame to store the data
data = []

# Iterate over each grid point
for i, lon in enumerate(longitudes):
    for j, lat in enumerate(latitudes):
        # Get the rainfall values for the current grid point
        rainfall_values = rainfall_reshaped[:, j, i]
        
        # Filter the rainfall values for values between 1 mm and the maximum value
        filtered_rainfall_values = rainfall_values[(rainfall_values >= 1) & (rainfall_values <= rainfall_values.max())]
        
        # If any filtered values exist, add the previous day's value to the data list
        if len(filtered_rainfall_values) > 0:
            for k, rainfall_value in enumerate(filtered_rainfall_values):
                previous_day = times[k] - timedelta(days=1)
                data.append({
                    'Longitude': lon,
                    'Latitude': lat,
                    'Date': previous_day,
                    'Rainfall': rainfall_value
                })

# Create a DataFrame from the data list
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_file = '/Users/kundanayare/Downloads/previous dates (60 mm to 114mm).xlsx'
df.to_excel(output_file, index=False)

# Close the netCDF file
nc_file.close()
previous dates


