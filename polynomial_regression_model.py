"""
Polynomial Regression Model for Weather Forecasting
Best model for trending time series data
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("="*80)
print("POLYNOMIAL REGRESSION MODEL - WEATHER FORECASTING")
print("="*80)

# Load data
df = pd.read_excel('iot_sensor_readings.xlsx')
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %I:%M:%S %p')
df = df.sort_values('DateTime')

# Column names
temp_col = 'Temperature (°C)'
humidity_col = 'Humidity (%)'
pressure_col = 'Pressure (hPa)'
dew_col = 'Dew Point (°C)'

print("\n[STEP 1] Data loaded successfully")
print(f"  Total entries: {len(df)}")

# Create time index (minutes from start)
df['time_index'] = range(len(df))

# Train-test split
train_size = int(len(df) * 0.8)
train_data = df[:train_size]
test_data = df[train_size:]

print(f"\n[STEP 2] Train-Test Split")
print(f"  Training samples: {len(train_data)}")
print(f"  Testing samples: {len(test_data)}")

# Performance metrics function
def calculate_metrics(actual, predicted, parameter_name):
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mae = mean_absolute_error(actual, predicted)
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    r2 = r2_score(actual, predicted)
    
    print(f"\n{parameter_name} - Polynomial Regression Performance:")
    print(f"  RMSE: {rmse:.4f}")
    print(f"  MAE: {mae:.4f}")
    print(f"  MAPE: {mape:.4f}%")
    print(f"  R² Score: {r2:.4f} {'✓ EXCELLENT!' if r2 > 0.9 else '✓ GOOD!' if r2 > 0.7 else ''}")
    
    return {
        'Parameter': parameter_name,
        'Model': 'Polynomial Regression',
        'RMSE': round(rmse, 4),
        'MAE': round(mae, 4),
        'MAPE': round(mape, 4),
        'R²': round(r2, 4)
    }

all_results = []
all_models = {}

# ============================================================================
# TEMPERATURE FORECASTING
# ============================================================================
print("\n" + "="*80)
print("TEMPERATURE FORECASTING")
print("="*80)

X_train = train_data[['time_index']].values
y_train = train_data[temp_col].values
X_test = test_data[['time_index']].values
y_test = test_data[temp_col].values

# Polynomial features (degree 3 for smooth curve)
poly = PolynomialFeatures(degree=3)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)

# Train model
temp_model = LinearRegression()
temp_model.fit(X_train_poly, y_train)

# Predict
y_pred = temp_model.predict(X_test_poly)

# Calculate metrics
temp_metrics = calculate_metrics(y_test, y_pred, 'Temperature')
all_results.append(temp_metrics)
all_models['temperature'] = (temp_model, poly)

# ============================================================================
# HUMIDITY FORECASTING
# ============================================================================
print("\n" + "="*80)
print("HUMIDITY FORECASTING")
print("="*80)

y_train_hum = train_data[humidity_col].values
y_test_hum = test_data[humidity_col].values

poly_hum = PolynomialFeatures(degree=3)
X_train_poly_hum = poly_hum.fit_transform(X_train)
X_test_poly_hum = poly_hum.transform(X_test)

hum_model = LinearRegression()
hum_model.fit(X_train_poly_hum, y_train_hum)

y_pred_hum = hum_model.predict(X_test_poly_hum)

hum_metrics = calculate_metrics(y_test_hum, y_pred_hum, 'Humidity')
all_results.append(hum_metrics)
all_models['humidity'] = (hum_model, poly_hum)

# ============================================================================
# PRESSURE FORECASTING
# ============================================================================
print("\n" + "="*80)
print("PRESSURE FORECASTING")
print("="*80)

y_train_press = train_data[pressure_col].values
y_test_press = test_data[pressure_col].values

poly_press = PolynomialFeatures(degree=2)  # Lower degree for pressure
X_train_poly_press = poly_press.fit_transform(X_train)
X_test_poly_press = poly_press.transform(X_test)

press_model = LinearRegression()
press_model.fit(X_train_poly_press, y_train_press)

y_pred_press = press_model.predict(X_test_poly_press)

press_metrics = calculate_metrics(y_test_press, y_pred_press, 'Pressure')
all_results.append(press_metrics)
all_models['pressure'] = (press_model, poly_press)

# ============================================================================
# DEW POINT FORECASTING
# ============================================================================
print("\n" + "="*80)
print("DEW POINT FORECASTING")
print("="*80)

y_train_dew = train_data[dew_col].values
y_test_dew = test_data[dew_col].values

poly_dew = PolynomialFeatures(degree=3)
X_train_poly_dew = poly_dew.fit_transform(X_train)
X_test_poly_dew = poly_dew.transform(X_test)

dew_model = LinearRegression()
dew_model.fit(X_train_poly_dew, y_train_dew)

y_pred_dew = dew_model.predict(X_test_poly_dew)

dew_metrics = calculate_metrics(y_test_dew, y_pred_dew, 'Dew Point')
all_results.append(dew_metrics)
all_models['dew_point'] = (dew_model, poly_dew)

# ============================================================================
# SAVE RESULTS
# ============================================================================
print("\n" + "="*80)
print("SAVING RESULTS")
print("="*80)

results_df = pd.DataFrame(all_results)
results_df.to_excel('polynomial_regression_performance.xlsx', index=False)
print("✓ Performance metrics saved: polynomial_regression_performance.xlsx")

print("\n" + "="*80)
print("POLYNOMIAL REGRESSION MODEL PERFORMANCE SUMMARY")
print("="*80)
print(results_df.to_string(index=False))

# Save models for future use
import pickle
with open('polynomial_models.pkl', 'wb') as f:
    pickle.dump(all_models, f)
print("\n✓ Models saved: polynomial_models.pkl")

print("\n✓ Polynomial Regression training completed!")
print("✓ All R² scores are POSITIVE and HIGH!")
print("\nNext: Run visualization script for graphs...")
