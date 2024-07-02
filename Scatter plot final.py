import pandas as pd
import matplotlib.pyplot as plt

# Read the data from Excel file
df = pd.read_excel("/Users/kundanayare/Downloads/K-mense clustring (for 6).xlsx")

# Create the scatter plot
plt.scatter(df['Rainfall'], df['Previous Day 1 Rainfall'])
plt.xlabel('Rainfall (Present Day Rainfall)')
plt.ylabel('Previous Day 1 Rainfall')
plt.title('Scatter Plot of Present Day Rainfall vs Previous Day 1 Rainfall')

# Show the plot
plt.show()
