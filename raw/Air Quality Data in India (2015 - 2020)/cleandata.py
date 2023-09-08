# Values I need: PM2.5, PM10, NO2, CO, SO2, and O3. 

import pandas as pd

# Load the data into a pandas DataFrame
df = pd.read_csv("./city_day.csv")

# Filter rows to keep only those with at least one of PM2.5 and PM10 available
df = df.dropna(subset=['PM2.5', 'PM10'], how='all')

# Filter rows to keep only those with at least three out of the seven pollutants available
required_pollutants = ['City', 'PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3']
df = df.dropna(subset=required_pollutants, thresh=3)

# Handle duplicate data
df.drop_duplicates(inplace=True)

df.to_csv('cleaned_data.csv', index=False)


