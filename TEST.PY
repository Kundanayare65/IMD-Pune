import netCDF4 as nc
import pandas as pd
from datetime import datetime, timedelta

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

# Set the starting date
start_date = datetime(2019, 10, 1)

# Iterate over each grid point
for i, lon in enumerate(longitudes):
    for j, lat in enumerate(latitudes):
        # Get the rainfall values for the current grid point
        rainfall_values = rainfall_reshaped[:, j, i]

        # Get the indices of dates starting from the specified date
        start_index = (times >= start_date).tolist().index(True)
        indices = list(range(start_index, len(times)))

        # Filter the rainfall values for values between 64.5 mm and 114 mm
        filtered_rainfall_values = rainfall_values[indices][(rainfall_values[indices] > 64.5) & (rainfall_values[indices] < 114)]

        # If any filtered values exist, add them to the data list
        if len(filtered_rainfall_values) > 0:
            for k, rainfall_value in enumerate(filtered_rainfall_values):
                # Get the index of the current rainfall value
                rainfall_index = ((rainfall_values[indices] > 64) & (rainfall_values[indices] < 114)).tolist().index(True) + k

                # Get the previous day's rainfall values from the original array
                previous_day_rainfalls = []
                for n in range(1, 7):  # Consider the past 6 days
                    if rainfall_index >= n:
                        previous_day_rainfall = rainfall_values[indices][rainfall_index - n]
                        previous_day_rainfalls.append(previous_day_rainfall)
                    else:
                        previous_day_rainfalls.append(None)

                # Calculate the previous day's dates
                previous_days = [times[indices][rainfall_index] - timedelta(days=n) for n in range(1, 7)]

                data.append({
                    'Longitude': lon,
                    'Latitude': lat,
                    'Date': times[rainfall_index],
                    'Rainfall': rainfall_value,
                    'Previous Day 1': previous_days[0],
                    'Previous Day 1 Rainfall': previous_day_rainfalls[0],
                    'Previous Day 2': previous_days[1],
                    'Previous Day 2 Rainfall': previous_day_rainfalls[1],
                    'Previous Day 3': previous_days[2],
                    'Previous Day 3 Rainfall': previous_day_rainfalls[2],
                    'Previous Day 4': previous_days[3],
                    'Previous Day 4 Rainfall': previous_day_rainfalls[3],
                    'Previous Day 5': previous_days[4],
                    'Previous Day 5 Rainfall': previous_day_rainfalls[4],
                    'Previous Day 6': previous_days[5],
                    'Previous Day 6 Rainfall': previous_day_rainfalls[5],
                    'Previous Day 7': previous_days[6],
                    'Previous Day 7 Rainfall': previous_day_rainfalls[6],
                    'Previous Day 8': previous_days[7],
                    'Previous Day 8 Rainfall': previous_day_rainfalls[7],
                    'Previous Day 9': previous_days[8],
                    'Previous Day 9 Rainfall': previous_day_rainfalls[8],
                    'Previous Day 10': previous_days[9],
                    'Previous Day 10 Rainfall': previous_day_rainfalls[9]
                })

# Create DataFrame from the data list
data_df = pd.DataFrame(data)

# Drop rows with missing values
data_df = data_df.dropna().reset_index(drop=True)

# Specify the desired output path and file name
output_path = r"/Users/kundanayare/Downloads/"  # Update with your desired output folder path
output_filename = output_path + "previous dates (60 mm to 114mm).xlsx"  # Choose the desired output file name

# Save the DataFrame to an Excel file
data_df.to_excel(output_filename, index=False)

print("Excel file saved successfully!")
