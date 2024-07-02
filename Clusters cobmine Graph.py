import pandas as pd
import matplotlib.pyplot as plt

def plot_rainfall_counts(file_path, cluster_name):
    # Read the Excel file
    df = pd.read_excel(file_path)

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
    plt.title(f'Count of Rainfall in Each Range - {cluster_name}')

    # Add a legend
    plt.legend()

    # Save the plot with a custom name
    plt.savefig(f'{cluster_name}.png')

    # Show the plot
    plt.show()


# File paths and cluster names for the 6 Excel files
file_paths = [
    ("/Users/kundanayare/Downloads/Cluster 1.xlsx", "Cluster 1"),
    ("/Users/kundanayare/Documents/Cluster 2.xlsx", "Cluster 2"),
    ("/Users/kundanayare/Documents/Cluster 3.xlsx", "Cluster 3"),
    ("/Users/kundanayare/Downloads/Cluster 4.xlsx", "Cluster 4"),
    ("/Users/kundanayare/Downloads/Cluster 5.xlsx", "Cluster 5"),
    ("/Users/kundanayare/Downloads/Cluster 6.xlsx", "Cluster 6")
]

# Plot the line plots for all files
for file_path, cluster_name in file_paths:
    plot_rainfall_counts(file_path, cluster_name)
