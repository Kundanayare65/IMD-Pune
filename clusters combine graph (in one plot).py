import pandas as pd
import matplotlib.pyplot as plt

def plot_rainfall_counts(file_paths, cluster_names):
    # Create a figure with subplots
    fig, axs = plt.subplots(len(file_paths), 1, figsize=(8, 6 * len(file_paths)))

    # Iterate over the files and cluster names
    for i, (file_path, cluster_name) in enumerate(zip(file_paths, cluster_names)):
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

        # Create the line plot in the respective subplot
        for column, counts in count_dict.items():
            axs[i].plot(x, counts, marker='o', label=column)

        # Set the axis labels and title for the subplot
        axs[i].set_xlabel('Rainfall Range (mm)')
        axs[i].set_ylabel('Rainfall Count')
        axs[i].set_title(f'Count of Rainfall in Each Range - {cluster_name}')

        # Add a legend to the subplot
        axs[i].legend()

    # Adjust the spacing between subplots
    plt.tight_layout()

    # Save the plot with a custom name
    plt.savefig('combined_plots.png')

    # Show the plot
    plt.show()


# File paths and cluster names for the 6 Excel files
file_paths = [
    "/Users/kundanayare/Downloads/Cluster 1.xlsx",
    "/Users/kundanayare/Documents/Cluster 2.xlsx",
    "/Users/kundanayare/Documents/Cluster 3.xlsx",
    "/Users/kundanayare/Downloads/Cluster 4.xlsx",
    "/Users/kundanayare/Downloads/Cluster 5.xlsx",
    "/Users/kundanayare/Downloads/Cluster 6.xlsx"
]

cluster_names = [
    "Cluster 1",
    "Cluster 2",
    "Cluster 3",
    "Cluster 4",
    "Cluster 5",
    "Cluster 6"
]

# Plot the line plots for all files in a single plot
plot_rainfall_counts(file_paths, cluster_names)
