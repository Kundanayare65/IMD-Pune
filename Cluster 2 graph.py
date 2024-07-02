import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file
df = pd.read_excel("/Users/kundanayare/Documents/Cluster 2.xlsx")

# Define the rainfall ranges
rainfall_ranges = ['0-20', '20-40', '40-60', '60-80', '80-100', '100-120', '120-140', '140-160', '160-180', '180-200', '>200']

# Define the columns for counting
columns = ['Rainfall', 'Previous Day 1 Rainfall', 'Previous Day 2 Rainfall', 'Previous Day 3 Rainfall', 'Previous Day 4 Rainfall', 'Previous Day 5 Rainfall']

# Initialize a dictionary to store the counts
count_dict = {}

# Iterate over the columns and calculate the counts
for column in columns:
    count_list = []
    for rainfall_range in rainfall_ranges:
        if rainfall_range == '>200':
            count = df[df[column] > 200].shape[0]
        else:
            lower_bound, upper_bound = map(int, rainfall_range.split('-'))
            count = df[(df[column] > lower_bound) & (df[column] <= upper_bound)].shape[0]
        count_list.append(count)
    count_dict[column] = count_list

# Prepare the data for plotting
x = rainfall_ranges

# Create the line plot
for column, counts in count_dict.items():
    plt.plot(x, counts, marker='o', label=column)

# Set the axis labels and title
plt.xlabel('Rainfall Range (mm)')
plt.ylabel('Rainfall Count')
plt.title('Count of Rainfall in Each Range')

# Add a legend
plt.legend()

# Show the plot
plt.show()
