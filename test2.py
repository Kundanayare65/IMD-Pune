import pandas as pd

# Assuming your dataset is stored in a dataframe named 'df'
df['Date'] = pd.to_datetime(df['Date'])
df.sort_values('Date', inplace=True)
df['Previous Day Rainfall'] = df['Rainfall'].shift(1)
df.sort_values('Date', inplace=True)

# Print the updated dataframe
print(df)
