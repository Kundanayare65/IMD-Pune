import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel("/Users/kundanayare/Downloads/k mense clustring (for previous 10 days for 6).xlsx")

# Define the rainfall ranges
ranges = ['0', '0-20', '20-40', '40-60', '60-80', '80-100', '100-120', '120-140', '140-160', '160-180', '180-200', '>200']

# Create an empty DataFrame to store the line plot data
line_data = pd.DataFrame(columns=['Range', 'Count'])

# Iterate over each range
for i in range(len(ranges)):
    # Get the lower and upper limits of the current range
    if i == 0:
        lower_limit = 0
        upper_limit = 0
    elif i == len(ranges) - 1:
        lower_limit = int(ranges[i][1:])
        upper_limit = float('inf')
    else:
        lower_limit = int(ranges[i].split('-')[0])
        upper_limit = int(ranges[i].split('-')[1])

    # Filter the data within the current range
    filtered_data = df[(df['Rainfall'] >= lower_limit) & (df['Rainfall'] < upper_limit)]

    # Get the count of data within the current range
    count = len(filtered_data)

    # Add the range and count to the line_data DataFrame
    line_data.loc[i] = [ranges[i], count]

# Plot the line plot
plt.plot(line_data['Range'], line_data['Count'])
plt.xlabel('Range (mm)')
plt.ylabel('Count')
plt.title('Count of Rainfall within Each Range')

# Rotate the x-axis labels for better visibility
plt.xticks(rotation=45)

# Show the plot
plt.show()
