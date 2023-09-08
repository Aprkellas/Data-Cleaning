import os
import pandas as pd
from sklearn.model_selection import train_test_split
import csv

df = pd.read_csv('test/cleaned_data.csv', encoding='utf-8')
print(df.head())

features = ['PM2.5', 'PM10', 'NO2', 'CO', 'SO2', 'O3']

target = 'AQI'

X = df[features]
y = df[target]
try:
    X = X.astype(int)
except Exception as e:
    print(e)
try:
    y = y.astype(int)
except Exception as e:
    print(e)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the training data to a CSV file
training_data = pd.concat([X_train, y_train], axis=1)
training_data.to_csv('./train/training_data.csv', index=False)

# Save the testing data to a CSV file
testing_data = pd.concat([X_test, y_test], axis=1)
testing_data.to_csv('./test/testing_data.csv', index=False)