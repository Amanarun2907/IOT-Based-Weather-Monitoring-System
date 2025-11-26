"""
Prophet Model for Weather Forecasting
Best model for time series with trends and seasonality
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from prophet import Prophet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("="*80)
print("PROPHET MODEL - WEATHER FORECASTING")
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
print(f"  Time range: {df['DateTime'].min()} to {df['DateTime'].max()}")

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
    
    print(f"\n{parameter_name} - Prophet Model Performance:")
    print(f"  RMSE: {rmse:.4f}")
    print(f"  MAE: {mae:.4f}")
    print(f"  MAPE: {mape:.4f}%")
    print(f"  R² Score: {r2:.4f}")
    
    return {
        'Parameter': parameter_name,
        'Model': 'Prophet',
        'RMSE': round(rmse, 4),
        'MAE': round(mae, 4),
        'MAPE': round(mape, 4),
        'R²': round(r2, 4)
    }

all_results = []

# ============================================================================
# TEMPERATURE FORECASTING
# ============================================================================
print("\n" + "="*80)
print("TEMPERATURE FORECASTING WITH PROPHET")
print("="*80)

# Prepare data for Prophet (requires 'ds' and 'y' columns)
temp_train = train_data[['DateTime', temp_col]].copy()
temp_train.columns = ['ds', 'y']

temp_test = test_data[['DateTime', temp_col]].copy()
temp_test.columns = ['ds', 'y']

# Train Prophet model
print("\nTraining Prophet model for Temperature...")
temp_model = Prophet(
    daily_seasonality=True,
    weekly_seasonality=False,
    yearly_seasonality=False,
    changepoint_prior_scale=0.5,
    seasonality_prior_scale=10
)
temp_model.fit(temp_train)

# Make predictions
temp_forecast = temp_model.predict(temp_test[['ds']])
temp_pred = temp_forecast['yhat'].values

# Calculate metrics
temp_metrics = calculate_metrics(temp_test['y'].values, temp_pred, 'Temperature')
all_results.append(temp_metrics)

# ============================================================================
# HUMIDITY FORECASTING
# ============================================================================
print("\n" + "="*80)
print("HUMIDITY FORECASTING WITH PROPHET")
print("="*80)

hum_train = train_data[['DateTime', humidity_col]].copy()
hum_train.columns = ['ds', 'y']

hum_test = test_data[['DateTime', humidity_col]].copy()
hum_test.columns = ['ds', 'y']

print("\nTraining Prophet model for Humidity...")
hum_model = Prophet(
    daily_seasonality=True,
    weekly_seasonality=False,
    yearly_seasonality=False,
    changepoint_prior_scale=0.5,
    seasonality_prior_scale=10
)
hum_model.fit(hum_train)

hum_forecast = hum_model.predict(hum_test[['ds']])
hum_pred = hum_forecast['yhat'].values

hum_metrics = calculate_metrics(hum_test['y'].values, hum_pred, 'Humidity')
all_results.append(hum_metrics)

# ============================================================================
# PRESSURE FORECASTING
# ============================================================================
print("\n" + "="*80)
print("PRESSURE FORECASTING WITH PROPHET")
print("="*80)

press_train = train_data[['DateTime', pressure_col]].copy()
press_train.columns = ['ds', 'y']

press_test = test_data[['DateTime', pressure_col]].copy()
press_test.columns = ['ds', 'y']

print("\nTraining Prophet model for Pressure...")
press_model = Prophet(
    daily_seasonality=True,
    weekly_seasonality=False,
    yearly_seasonality=False,
    changepoint_prior_scale=0.3,
    seasonality_prior_scale=5
)
press_model.fit(press_train)

press_forecast = press_model.predict(press_test[['ds']])
press_pred = press_forecast['yhat'].values

press_metrics = calculate_metrics(press_test['y'].values, press_pred, 'Pressure')
all_results.append(press_metrics)

# ============================================================================
# DEW POINT FORECASTING
# ============================================================================
print("\n" + "="*80)
print("DEW POINT FORECASTING WITH PROPHET")
print("="*80)

dew_train = train_data[['DateTime', dew_col]].copy()
dew_train.columns = ['ds', 'y']

dew_test = test_data[['DateTime', dew_col]].copy()
dew_test.columns = ['ds', 'y']

print("\nTraining Prophet model for Dew Point...")
dew_model = Prophet(
    daily_seasonality=True,
    weekly_seasonality=False,
    yearly_seasonality=False,
    changepoint_prior_scale=0.5,
    seasonality_prior_scale=10
)
dew_model.fit(dew_train)

dew_forecast = dew_model.predict(dew_test[['ds']])
dew_pred = dew_forecast['yhat'].values

dew_metrics = calculate_metrics(dew_test['y'].values, dew_pred, 'Dew Point')
all_results.append(dew_metrics)

# ============================================================================
# SAVE RESULTS
# ============================================================================
print("\n" + "="*80)
print("SAVING RESULTS")
print("="*80)

results_df = pd.DataFrame(all_results)
results_df.to_excel('prophet_model_performance.xlsx', index=False)
print("✓ Performance metrics saved: prophet_model_performance.xlsx")

print("\n" + "="*80)
print("PROPHET MODEL PERFORMANCE SUMMARY")
print("="*80)
print(results_df.to_string(index=False))

print("\n✓ Prophet model training completed!")
print("✓ All R² scores should be positive and close to 1.0")
print("\nNext: Run visualization script for graphs...")
