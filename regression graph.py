import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read the Excel file
excel_file_path = "/Users/kundanayare/Downloads/K-mense clustring (for 6).xlsx"
df = pd.read_excel(excel_file_path)

# Subsample the data
sampled_df = df.sample(n=100)  # Adjust the number of samples as desired

# Scatter plot with regression line
sns.regplot(x='Rainfall', y='Previous Day 1 Rainfall', data=sampled_df, scatter_kws={'s': 10, 'alpha': 0.5})

# Set the title and labels
plt.title('Scatter Plot with Regression Line (Subsampled)')
plt.xlabel('Rainfall')
plt.ylabel('Previous Day 1 Rainfall')

# Show the plot
plt.show()
