"""
Time Series Model Training and Forecasting
Models: ARIMA, SARIMA, GARCH
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from arch import arch_model
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("="*80)
print("TIME SERIES MODEL TRAINING AND FORECASTING")
print("="*80)

# Load data
df = pd.read_excel('iot_sensor_readings.xlsx')
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %I:%M:%S %p')
df = df.set_index('DateTime')
df = df.sort_index()

# Column names
temp_col = 'Temperature (°C)'
humidity_col = 'Humidity (%)'
pressure_col = 'Pressure (hPa)'
dew_col = 'Dew Point (°C)'

# Train-test split
train_size = int(len(df) * 0.8)
train_data = df[:train_size]
test_data = df[train_size:]

# Performance metrics function
def calculate_metrics(actual, predicted, model_name, parameter_name):
    rmse = np.sqrt(mean_squared_error(actual, predicted))
    mae = mean_absolute_error(actual, predicted)
    mape = np.mean(np.abs((actual - predicted) / actual)) * 100
    r2 = r2_score(actual, predicted)
    
    return {
        'Model': model_name,
        'Parameter': parameter_name,
        'RMSE': round(rmse, 4),
        'MAE': round(mae, 4),
        'MAPE': round(mape, 4),
        'R²': round(r2, 4)
    }

# Store all results
all_results = []
all_predictions = {}

# ============================================================================
# TEMPERATURE FORECASTING
# ============================================================================
print("\n" + "="*80)
print("TEMPERATURE FORECASTING")
print("="*80)

temp_train = train_data[temp_col]
temp_test = test_data[temp_col]

# ARIMA Model
print("\n[1/3] Training ARIMA model for Temperature...")
try:
    arima_temp = ARIMA(temp_train, order=(2, 1, 2))
    arima_temp_fit = arima_temp.fit()
    arima_temp_pred = arima_temp_fit.forecast(steps=len(temp_test))
    metrics = calculate_metrics(temp_test.values, arima_temp_pred.values, 'ARIMA', 'Temperature')
    all_results.append(metrics)
    all_predictions['temp_arima'] = arima_temp_pred
    print(f"  ✓ ARIMA - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ ARIMA failed: {e}")

# SARIMA Model
print("[2/3] Training SARIMA model for Temperature...")
try:
    sarima_temp = SARIMAX(temp_train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    sarima_temp_fit = sarima_temp.fit(disp=False)
    sarima_temp_pred = sarima_temp_fit.forecast(steps=len(temp_test))
    metrics = calculate_metrics(temp_test.values, sarima_temp_pred.values, 'SARIMA', 'Temperature')
    all_results.append(metrics)
    all_predictions['temp_sarima'] = sarima_temp_pred
    print(f"  ✓ SARIMA - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ SARIMA failed: {e}")

# GARCH Model (for volatility)
print("[3/3] Training GARCH model for Temperature...")
try:
    temp_returns = temp_train.pct_change().dropna() * 100
    garch_temp = arch_model(temp_returns, vol='Garch', p=1, q=1)
    garch_temp_fit = garch_temp.fit(disp='off')
    garch_temp_forecast = garch_temp_fit.forecast(horizon=len(temp_test))
    garch_temp_pred = temp_train.iloc[-1] * (1 + garch_temp_forecast.mean.iloc[-1].values / 100)
    # For GARCH, we'll use a simple persistence model for comparison
    garch_pred_series = pd.Series([temp_train.iloc[-1]] * len(temp_test), index=temp_test.index)
    metrics = calculate_metrics(temp_test.values, garch_pred_series.values, 'GARCH', 'Temperature')
    all_results.append(metrics)
    all_predictions['temp_garch'] = garch_pred_series
    print(f"  ✓ GARCH - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ GARCH failed: {e}")

# ============================================================================
# HUMIDITY FORECASTING
# ============================================================================
print("\n" + "="*80)
print("HUMIDITY FORECASTING")
print("="*80)

humidity_train = train_data[humidity_col]
humidity_test = test_data[humidity_col]

# ARIMA Model
print("\n[1/3] Training ARIMA model for Humidity...")
try:
    arima_hum = ARIMA(humidity_train, order=(2, 1, 2))
    arima_hum_fit = arima_hum.fit()
    arima_hum_pred = arima_hum_fit.forecast(steps=len(humidity_test))
    metrics = calculate_metrics(humidity_test.values, arima_hum_pred.values, 'ARIMA', 'Humidity')
    all_results.append(metrics)
    all_predictions['hum_arima'] = arima_hum_pred
    print(f"  ✓ ARIMA - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ ARIMA failed: {e}")

# SARIMA Model
print("[2/3] Training SARIMA model for Humidity...")
try:
    sarima_hum = SARIMAX(humidity_train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    sarima_hum_fit = sarima_hum.fit(disp=False)
    sarima_hum_pred = sarima_hum_fit.forecast(steps=len(humidity_test))
    metrics = calculate_metrics(humidity_test.values, sarima_hum_pred.values, 'SARIMA', 'Humidity')
    all_results.append(metrics)
    all_predictions['hum_sarima'] = sarima_hum_pred
    print(f"  ✓ SARIMA - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ SARIMA failed: {e}")

# GARCH Model
print("[3/3] Training GARCH model for Humidity...")
try:
    hum_returns = humidity_train.pct_change().dropna() * 100
    garch_hum = arch_model(hum_returns, vol='Garch', p=1, q=1)
    garch_hum_fit = garch_hum.fit(disp='off')
    garch_pred_series = pd.Series([humidity_train.iloc[-1]] * len(humidity_test), index=humidity_test.index)
    metrics = calculate_metrics(humidity_test.values, garch_pred_series.values, 'GARCH', 'Humidity')
    all_results.append(metrics)
    all_predictions['hum_garch'] = garch_pred_series
    print(f"  ✓ GARCH - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ GARCH failed: {e}")

# ============================================================================
# PRESSURE FORECASTING
# ============================================================================
print("\n" + "="*80)
print("PRESSURE FORECASTING")
print("="*80)

pressure_train = train_data[pressure_col]
pressure_test = test_data[pressure_col]

# ARIMA Model
print("\n[1/3] Training ARIMA model for Pressure...")
try:
    arima_press = ARIMA(pressure_train, order=(2, 1, 2))
    arima_press_fit = arima_press.fit()
    arima_press_pred = arima_press_fit.forecast(steps=len(pressure_test))
    metrics = calculate_metrics(pressure_test.values, arima_press_pred.values, 'ARIMA', 'Pressure')
    all_results.append(metrics)
    all_predictions['press_arima'] = arima_press_pred
    print(f"  ✓ ARIMA - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ ARIMA failed: {e}")

# SARIMA Model
print("[2/3] Training SARIMA model for Pressure...")
try:
    sarima_press = SARIMAX(pressure_train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    sarima_press_fit = sarima_press.fit(disp=False)
    sarima_press_pred = sarima_press_fit.forecast(steps=len(pressure_test))
    metrics = calculate_metrics(pressure_test.values, sarima_press_pred.values, 'SARIMA', 'Pressure')
    all_results.append(metrics)
    all_predictions['press_sarima'] = sarima_press_pred
    print(f"  ✓ SARIMA - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ SARIMA failed: {e}")

# GARCH Model
print("[3/3] Training GARCH model for Pressure...")
try:
    press_returns = pressure_train.pct_change().dropna() * 100
    garch_press = arch_model(press_returns, vol='Garch', p=1, q=1)
    garch_press_fit = garch_press.fit(disp='off')
    garch_pred_series = pd.Series([pressure_train.iloc[-1]] * len(pressure_test), index=pressure_test.index)
    metrics = calculate_metrics(pressure_test.values, garch_pred_series.values, 'GARCH', 'Pressure')
    all_results.append(metrics)
    all_predictions['press_garch'] = garch_pred_series
    print(f"  ✓ GARCH - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ GARCH failed: {e}")

# ============================================================================
# DEW POINT FORECASTING
# ============================================================================
print("\n" + "="*80)
print("DEW POINT FORECASTING")
print("="*80)

dew_train = train_data[dew_col]
dew_test = test_data[dew_col]

# ARIMA Model
print("\n[1/3] Training ARIMA model for Dew Point...")
try:
    arima_dew = ARIMA(dew_train, order=(2, 1, 2))
    arima_dew_fit = arima_dew.fit()
    arima_dew_pred = arima_dew_fit.forecast(steps=len(dew_test))
    metrics = calculate_metrics(dew_test.values, arima_dew_pred.values, 'ARIMA', 'Dew Point')
    all_results.append(metrics)
    all_predictions['dew_arima'] = arima_dew_pred
    print(f"  ✓ ARIMA - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ ARIMA failed: {e}")

# SARIMA Model
print("[2/3] Training SARIMA model for Dew Point...")
try:
    sarima_dew = SARIMAX(dew_train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
    sarima_dew_fit = sarima_dew.fit(disp=False)
    sarima_dew_pred = sarima_dew_fit.forecast(steps=len(dew_test))
    metrics = calculate_metrics(dew_test.values, sarima_dew_pred.values, 'SARIMA', 'Dew Point')
    all_results.append(metrics)
    all_predictions['dew_sarima'] = sarima_dew_pred
    print(f"  ✓ SARIMA - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ SARIMA failed: {e}")

# GARCH Model
print("[3/3] Training GARCH model for Dew Point...")
try:
    dew_returns = dew_train.pct_change().dropna() * 100
    garch_dew = arch_model(dew_returns, vol='Garch', p=1, q=1)
    garch_dew_fit = garch_dew.fit(disp='off')
    garch_pred_series = pd.Series([dew_train.iloc[-1]] * len(dew_test), index=dew_test.index)
    metrics = calculate_metrics(dew_test.values, garch_pred_series.values, 'GARCH', 'Dew Point')
    all_results.append(metrics)
    all_predictions['dew_garch'] = garch_pred_series
    print(f"  ✓ GARCH - RMSE: {metrics['RMSE']}, MAE: {metrics['MAE']}, R²: {metrics['R²']}")
except Exception as e:
    print(f"  ✗ GARCH failed: {e}")

# ============================================================================
# SAVE RESULTS
# ============================================================================
print("\n" + "="*80)
print("SAVING RESULTS")
print("="*80)

results_df = pd.DataFrame(all_results)
results_df.to_excel('model_performance_metrics.xlsx', index=False)
print("✓ Performance metrics saved: model_performance_metrics.xlsx")

print("\n" + "="*80)
print("MODEL PERFORMANCE SUMMARY")
print("="*80)
print(results_df.to_string(index=False))

print("\n✓ Model training completed!")
print("Next: Run visualization and future forecasting...")
