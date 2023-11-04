import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF
from sklearn.metrics import mean_squared_error

from splitdata import X_train, X_test, y_test, y_train


# Initialize a baseline GPR model using all features
baseline_model = GaussianProcessRegressor(kernel=RBF())
baseline_model.fit(X_train, y_train)
baseline_predictions, _ = baseline_model.predict(X_test, return_std=True)
baseline_mse = mean_squared_error(y_test, baseline_predictions)

# Initialize a list to store feature importance scores
feature_importance_scores = []

# Loop through each feature for feature selection
for feature_index in range(X_train.shape[1]):
    # Create a modified dataset without the current feature
    modified_X_train = np.delete(X_train, feature_index, axis=1)
    modified_X_test = np.delete(X_test, feature_index, axis=1)
    
    # Train a GPR model with the modified dataset
    gpr_model = GaussianProcessRegressor(kernel=RBF())
    gpr_model.fit(modified_X_train, y_train)
    
    # Make predictions on the test set
    gpr_predictions, _ = gpr_model.predict(modified_X_test, return_std=True)
    
    # Calculate the mean squared error for the modified model
    modified_mse = mean_squared_error(y_test, gpr_predictions)
    
    # Calculate the feature importance score based on MSE difference
    feature_importance = baseline_mse - modified_mse
    feature_importance_scores.append(feature_importance)

# Rank the features based on their impact on model performance
sorted_feature_indices = np.argsort(feature_importance_scores)[::-1]

# Set a predefined threshold or select the top N features
selected_feature_indices = sorted_feature_indices[:7]

# Select the features from the original feature matrix
selected_features = X_train[:, selected_feature_indices]

selected_features.to_csv('selected_data_gpr.csv', index=False)



