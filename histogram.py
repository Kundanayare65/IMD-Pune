import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colorbar import ColorbarBase
import matplotlib.colors as mcolors

# Load the data from Excel
df = pd.read_excel("/Users/kundanayare/Downloads/K-mense clustring (for 6).xlsx")

# Create a FacetGrid
g = sns.FacetGrid(df, col='Cluster', col_wrap=3, height=4)

# Assign different colors to each variable
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']

# Plot histograms for each column with respective colors
g.map(sns.histplot, 'Rainfall', color=colors[0])
g.map(sns.histplot, 'Previous Day 1 Rainfall', color=colors[1])
g.map(sns.histplot, 'Previous Day 2 Rainfall', color=colors[2])
g.map(sns.histplot, 'Previous Day 3 Rainfall', color=colors[3])
g.map(sns.histplot, 'Previous Day 4 Rainfall', color=colors[4])
g.map(sns.histplot, 'Previous Day 5 Rainfall', color=colors[5])

# Set the axis labels
g.set_axis_labels('Value', 'Count')

# Set the titles for each subplot
g.set_titles('Cluster {col_name}')

# Create a custom colormap with labels
labels = ['Rainfall', 'Previous Day 1', 'Previous Day 2', 'Previous Day 3', 'Previous Day 4', 'Previous Day 5']
cmap = mcolors.ListedColormap(colors[:len(labels)])

# Add a color scale legend
cax = g.fig.add_axes([0.9, 0.1, 0.03, 0.8])
colorbar = ColorbarBase(cax, cmap=cmap, ticks=range(len(labels)))
colorbar.set_ticklabels(labels)

# Adjust the plot appearance
g.fig.tight_layout()

# Show the plot
plt.show()
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colorbar import ColorbarBase
import matplotlib.colors as mcolors

# Load the data from Excel
df = pd.read_excel("/Users/kundanayare/Downloads/k mense clustring (for previous 10 days for 6).xlsx")

# Create a FacetGrid
g = sns.FacetGrid(df, col='Cluster', col_wrap=3, height=4)

# Assign different colors to each variable
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo']

# Plot histograms for each column with respective colors
g.map(sns.histplot, 'Rainfall', color=colors[0])
g.map(sns.histplot, 'Previous Day 1 Rainfall', color=colors[1])
g.map(sns.histplot, 'Previous Day 2 Rainfall', color=colors[2])
g.map(sns.histplot, 'Previous Day 3 Rainfall', color=colors[3])
g.map(sns.histplot, 'Previous Day 4 Rainfall', color=colors[4])
g.map(sns.histplot, 'Previous Day 5 Rainfall', color=colors[5])

# Set the axis labels
g.set_axis_labels('Value', 'Count')

# Set the titles for each subplot
g.set_titles('Cluster {col_name}')

# Create a custom colormap with labels
labels = ['Rainfall', 'Previous Day 1', 'Previous Day 2', 'Previous Day 3', 'Previous Day 4', 'Previous Day 5']
cmap = mcolors.ListedColormap(colors[:len(labels)])

# Add a color scale legend
cax = g.fig.add_axes([0.9, 0.1, 0.03, 0.8])
colorbar = ColorbarBase(cax, cmap=cmap, ticks=range(len(labels)))
colorbar.set_ticklabels(labels)

# Adjust the plot appearance
g.fig.tight_layout()

# Show the plot
plt.show()
