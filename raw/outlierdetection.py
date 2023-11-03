import pandas as pd
from scipy import stats

# Load your cleaned data
df = pd.read_csv('cleaned_data.csv')

# Define the threshold for Z-scores
z_threshold = 3

# Select a pollutant, e.g., 'PM2.5', and calculate Z-scores
pollutant = 'PM2.5'
z_scores = stats.zscore(df[pollutant])

# Create a boolean mask to identify outliers
outliers = (abs(z_scores) > z_threshold)

# Filter the DataFrame to keep non-outliers
df_filtered = df[~outliers]

# Save the filtered data to a new CSV file
df_filtered.to_csv('outliers_filtered_data.csv', index=False)


