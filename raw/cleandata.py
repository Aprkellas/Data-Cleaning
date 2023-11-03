# Values Rqeuired: PM2.5, PM10, NO2, CO, SO2, and O3. 

import pandas as pd

# Load the data into a pandas DataFrame
df = pd.read_csv("./raw/AirQualityData/city_day.csv")

# Filter rows to keep only those with at least one of PM2.5 and PM10 available
df = df.dropna(subset=['PM2.5', 'PM10'], how='all')

# Filter rows to keep only those with at least three out of the seven pollutants available
required_pollutants = ['PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3','AQI']
df = df.dropna(subset=required_pollutants, thresh=7)

# Handle duplicate data
df.drop_duplicates(inplace=True)

# remove the useless columns/data
columns_to_remove = [col for col in df.columns if col not in required_pollutants]
df.drop(columns=columns_to_remove, inplace=True)

df.to_csv('cleaned_data.csv', index=False)


