import pandas as pd
from sklearn.linear_model import LinearRegression

# Load your cleaned data
df = pd.read_csv('./cleaned_data.csv')

# Identify the required features
features = ['PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3']

# Identify the target
target = 'AQI'

# Calculate correlation with the target
correlation_matrix = df.corr()
correlation_with_target = correlation_matrix[target]

# Set a correlation threshold for feature selection
correlation_threshold = 0.2  # Adjust as needed

# Identify features with strong correlations
correlated_features = correlation_with_target[abs(correlation_with_target) > correlation_threshold].index.tolist()

# Combine selected features
selected_features = correlated_features.copy()  # Start with correlated features

# Create a DataFrame with the selected features and the target
selected_data = df[selected_features + [target]]

# Save the selected data to a CSV file
selected_data.to_csv('selected_data.csv', index=False)

