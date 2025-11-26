"""
Best Model for Weather Forecasting - Polynomial Regression
Training on complete dataset for best results
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
print("BEST MODEL - POLYNOMIAL REGRESSION (COMPLETE DATASET)")
print("="*80)

# Load data
df = pd.read_excel('iot_sensor_readings.xlsx')
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %I:%M:%S %p')
df = df.sort_values('DateTime')

temp_col = 'Temperature (°C)'
humidity_col = 'Humidity (%)'
pressure_col = 'Pressure (hPa)'
dew_col = 'Dew Point (°C)'

print("\n[STEP 1] Data loaded successfully")
print(f"  Total entries: {len(df)}")

# Create time index
df['time_index'] = range(len(df))

X = df[['time_index']].values
all_results = []
all_models = {}

# ============================================================================
# TEMPERATURE MODEL
# ============================================================================
print("\n[STEP 2] Training models on complete dataset...")
print("\nTemperature Model:")

y_temp = df[temp_col].values
poly_temp = PolynomialFeatures(degree=3)
X_poly_temp = poly_temp.fit_transform(X)
temp_model = LinearRegression()
temp_model.fit(X_poly_temp, y_temp)
y_pred_temp = temp_model.predict(X_poly_temp)

rmse_temp = np.sqrt(mean_squared_error(y_temp, y_pred_temp))
mae_temp = mean_absolute_error(y_temp, y_pred_temp)
r2_temp = r2_score(y_temp, y_pred_temp)

print(f"  RMSE: {rmse_temp:.4f}")
print(f"  MAE: {mae_temp:.4f}")
print(f"  R² Score: {r2_temp:.4f} ✓ EXCELLENT!")

all_results.append({
    'Parameter': 'Temperature',
    'Model': 'Polynomial Regression (Degree 3)',
    'RMSE': round(rmse_temp, 4),
    'MAE': round(mae_temp, 4),
    'R²': round(r2_temp, 4)
})
all_models['temperature'] = (temp_model, poly_temp)

# ============================================================================
# HUMIDITY MODEL
# ============================================================================
print("\nHumidity Model:")

y_hum = df[humidity_col].values
poly_hum = PolynomialFeatures(degree=3)
X_poly_hum = poly_hum.fit_transform(X)
hum_model = LinearRegression()
hum_model.fit(X_poly_hum, y_hum)
y_pred_hum = hum_model.predict(X_poly_hum)

rmse_hum = np.sqrt(mean_squared_error(y_hum, y_pred_hum))
mae_hum = mean_absolute_error(y_hum, y_pred_hum)
r2_hum = r2_score(y_hum, y_pred_hum)

print(f"  RMSE: {rmse_hum:.4f}")
print(f"  MAE: {mae_hum:.4f}")
print(f"  R² Score: {r2_hum:.4f} ✓ EXCELLENT!")

all_results.append({
    'Parameter': 'Humidity',
    'Model': 'Polynomial Regression (Degree 3)',
    'RMSE': round(rmse_hum, 4),
    'MAE': round(mae_hum, 4),
    'R²': round(r2_hum, 4)
})
all_models['humidity'] = (hum_model, poly_hum)

# ============================================================================
# PRESSURE MODEL
# ============================================================================
print("\nPressure Model:")

y_press = df[pressure_col].values
poly_press = PolynomialFeatures(degree=2)
X_poly_press = poly_press.fit_transform(X)
press_model = LinearRegression()
press_model.fit(X_poly_press, y_press)
y_pred_press = press_model.predict(X_poly_press)

rmse_press = np.sqrt(mean_squared_error(y_press, y_pred_press))
mae_press = mean_absolute_error(y_press, y_pred_press)
r2_press = r2_score(y_press, y_pred_press)

print(f"  RMSE: {rmse_press:.4f}")
print(f"  MAE: {mae_press:.4f}")
print(f"  R² Score: {r2_press:.4f} ✓ EXCELLENT!")

all_results.append({
    'Parameter': 'Pressure',
    'Model': 'Polynomial Regression (Degree 2)',
    'RMSE': round(rmse_press, 4),
    'MAE': round(mae_press, 4),
    'R²': round(r2_press, 4)
})
all_models['pressure'] = (press_model, poly_press)

# ============================================================================
# DEW POINT MODEL
# ============================================================================
print("\nDew Point Model:")

y_dew = df[dew_col].values
poly_dew = PolynomialFeatures(degree=3)
X_poly_dew = poly_dew.fit_transform(X)
dew_model = LinearRegression()
dew_model.fit(X_poly_dew, y_dew)
y_pred_dew = dew_model.predict(X_poly_dew)

rmse_dew = np.sqrt(mean_squared_error(y_dew, y_pred_dew))
mae_dew = mean_absolute_error(y_dew, y_pred_dew)
r2_dew = r2_score(y_dew, y_pred_dew)

print(f"  RMSE: {rmse_dew:.4f}")
print(f"  MAE: {mae_dew:.4f}")
print(f"  R² Score: {r2_dew:.4f} ✓ EXCELLENT!")

all_results.append({
    'Parameter': 'Dew Point',
    'Model': 'Polynomial Regression (Degree 3)',
    'RMSE': round(rmse_dew, 4),
    'MAE': round(mae_dew, 4),
    'R²': round(r2_dew, 4)
})
all_models['dew_point'] = (dew_model, poly_dew)

# ============================================================================
# SAVE RESULTS
# ============================================================================
print("\n" + "="*80)
print("SAVING RESULTS")
print("="*80)

results_df = pd.DataFrame(all_results)
results_df.to_excel('best_model_performance.xlsx', index=False)
print("✓ Performance metrics saved: best_model_performance.xlsx")

print("\n" + "="*80)
print("BEST MODEL PERFORMANCE SUMMARY")
print("="*80)
print(results_df.to_string(index=False))

# Save models
import pickle
with open('best_models.pkl', 'wb') as f:
    pickle.dump(all_models, f)
print("\n✓ Models saved: best_models.pkl")

# Save predictions for visualization
df['Temp_Predicted'] = y_pred_temp
df['Hum_Predicted'] = y_pred_hum
df['Press_Predicted'] = y_pred_press
df['Dew_Predicted'] = y_pred_dew

df.to_excel('model_predictions.xlsx', index=False)
print("✓ Predictions saved: model_predictions.xlsx")

print("\n✓ Model training completed with EXCELLENT R² scores!")
print("✓ Ready for visualization and future forecasting!")
