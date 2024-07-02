import pandas as pd

# Read the Excel file
df = pd.read_excel("/Users/kundanayare/Downloads/cluster 1.xlsx")

# Define the rain thresholds
thresholds = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200]

# Iterate over the columns and count the occurrences above each threshold
for column in df.columns[1:]:
    print(f"Column: {column}")
    if pd.to_numeric(df[column], errors='coerce').notnull().all():
        for threshold in thresholds:
            count = df[pd.to_numeric(df[column], errors='coerce') > threshold].shape[0]
            print(f"Rainfall > {threshold} mm: {count} occurrences")
    else:
        print("Column contains non-numeric values.")
    print()
