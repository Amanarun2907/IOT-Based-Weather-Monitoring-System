"""
Visualization and Future Forecasting (2:15 PM to 6:15 PM)
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

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("="*80)
print("VISUALIZATION AND FUTURE FORECASTING")
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

print("\n[STEP 1] Creating model comparison visualizations...")

# ============================================================================
# TEMPERATURE COMPARISON PLOT
# ============================================================================
temp_train = train_data[temp_col]
temp_test = test_data[temp_col]

# Train models
arima_temp = ARIMA(temp_train, order=(2, 1, 2)).fit()
sarima_temp = SARIMAX(temp_train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)).fit(disp=False)

arima_temp_pred = arima_temp.forecast(steps=len(temp_test))
sarima_temp_pred = sarima_temp.forecast(steps=len(temp_test))

fig, ax = plt.subplots(figsize=(15, 6))
ax.plot(train_data.index, temp_train, label='Training Data', color='#2E86AB', linewidth=2)
ax.plot(test_data.index, temp_test, label='Actual Test Data', color='#A23B72', linewidth=2, marker='o', markersize=3)
ax.plot(test_data.index, arima_temp_pred, label='ARIMA Prediction', color='#F18F01', linewidth=2, linestyle='--')
ax.plot(test_data.index, sarima_temp_pred, label='SARIMA Prediction', color='#C73E1D', linewidth=2, linestyle=':')
ax.set_title('Temperature Forecasting - Model Comparison', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=12, fontweight='bold')
ax.set_ylabel('Temperature (°C)', fontsize=12, fontweight='bold')
ax.legend(loc='best', fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('temperature_model_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Temperature comparison saved")
plt.close()

# ============================================================================
# HUMIDITY COMPARISON PLOT
# ============================================================================
humidity_train = train_data[humidity_col]
humidity_test = test_data[humidity_col]

arima_hum = ARIMA(humidity_train, order=(2, 1, 2)).fit()
sarima_hum = SARIMAX(humidity_train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)).fit(disp=False)

arima_hum_pred = arima_hum.forecast(steps=len(humidity_test))
sarima_hum_pred = sarima_hum.forecast(steps=len(humidity_test))

fig, ax = plt.subplots(figsize=(15, 6))
ax.plot(train_data.index, humidity_train, label='Training Data', color='#2E86AB', linewidth=2)
ax.plot(test_data.index, humidity_test, label='Actual Test Data', color='#A23B72', linewidth=2, marker='o', markersize=3)
ax.plot(test_data.index, arima_hum_pred, label='ARIMA Prediction', color='#F18F01', linewidth=2, linestyle='--')
ax.plot(test_data.index, sarima_hum_pred, label='SARIMA Prediction', color='#C73E1D', linewidth=2, linestyle=':')
ax.set_title('Humidity Forecasting - Model Comparison', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=12, fontweight='bold')
ax.set_ylabel('Humidity (%)', fontsize=12, fontweight='bold')
ax.legend(loc='best', fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('humidity_model_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Humidity comparison saved")
plt.close()

# ============================================================================
# PRESSURE COMPARISON PLOT
# ============================================================================
pressure_train = train_data[pressure_col]
pressure_test = test_data[pressure_col]

arima_press = ARIMA(pressure_train, order=(2, 1, 2)).fit()
sarima_press = SARIMAX(pressure_train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)).fit(disp=False)

arima_press_pred = arima_press.forecast(steps=len(pressure_test))
sarima_press_pred = sarima_press.forecast(steps=len(pressure_test))

fig, ax = plt.subplots(figsize=(15, 6))
ax.plot(train_data.index, pressure_train, label='Training Data', color='#2E86AB', linewidth=2)
ax.plot(test_data.index, pressure_test, label='Actual Test Data', color='#A23B72', linewidth=2, marker='o', markersize=3)
ax.plot(test_data.index, arima_press_pred, label='ARIMA Prediction', color='#F18F01', linewidth=2, linestyle='--')
ax.plot(test_data.index, sarima_press_pred, label='SARIMA Prediction', color='#C73E1D', linewidth=2, linestyle=':')
ax.set_title('Pressure Forecasting - Model Comparison', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=12, fontweight='bold')
ax.set_ylabel('Pressure (hPa)', fontsize=12, fontweight='bold')
ax.legend(loc='best', fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('pressure_model_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Pressure comparison saved")
plt.close()

# ============================================================================
# DEW POINT COMPARISON PLOT
# ============================================================================
dew_train = train_data[dew_col]
dew_test = test_data[dew_col]

arima_dew = ARIMA(dew_train, order=(2, 1, 2)).fit()
sarima_dew = SARIMAX(dew_train, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12)).fit(disp=False)

arima_dew_pred = arima_dew.forecast(steps=len(dew_test))
sarima_dew_pred = sarima_dew.forecast(steps=len(dew_test))

fig, ax = plt.subplots(figsize=(15, 6))
ax.plot(train_data.index, dew_train, label='Training Data', color='#2E86AB', linewidth=2)
ax.plot(test_data.index, dew_test, label='Actual Test Data', color='#A23B72', linewidth=2, marker='o', markersize=3)
ax.plot(test_data.index, arima_dew_pred, label='ARIMA Prediction', color='#F18F01', linewidth=2, linestyle='--')
ax.plot(test_data.index, sarima_dew_pred, label='SARIMA Prediction', color='#C73E1D', linewidth=2, linestyle=':')
ax.set_title('Dew Point Forecasting - Model Comparison', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=12, fontweight='bold')
ax.set_ylabel('Dew Point (°C)', fontsize=12, fontweight='bold')
ax.legend(loc='best', fontsize=10, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('dewpoint_model_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Dew Point comparison saved")
plt.close()

# ============================================================================
# FUTURE FORECASTING (2:15 PM to 6:15 PM)
# ============================================================================
print("\n[STEP 2] Forecasting future values (2:15 PM to 6:15 PM)...")

# Train on full dataset
full_temp = df[temp_col]
full_humidity = df[humidity_col]
full_pressure = df[pressure_col]
full_dew = df[dew_col]

# Forecast 240 minutes (4 hours)
forecast_steps = 240

# Train final models
print("  Training final models on complete dataset...")
final_arima_temp = ARIMA(full_temp, order=(2, 1, 2)).fit()
final_arima_hum = ARIMA(full_humidity, order=(2, 1, 2)).fit()
final_arima_press = ARIMA(full_pressure, order=(2, 1, 2)).fit()
final_arima_dew = ARIMA(full_dew, order=(2, 1, 2)).fit()

# Generate forecasts
print("  Generating forecasts...")
future_temp = final_arima_temp.forecast(steps=forecast_steps)
future_humidity = final_arima_hum.forecast(steps=forecast_steps)
future_pressure = final_arima_press.forecast(steps=forecast_steps)
future_dew = final_arima_dew.forecast(steps=forecast_steps)

# Create future datetime index
last_time = df.index[-1]
future_times = [last_time + timedelta(minutes=i+1) for i in range(forecast_steps)]

# Create forecast dataframe
forecast_df = pd.DataFrame({
    'DateTime': future_times,
    'Temperature (°C)': future_temp.values,
    'Humidity (%)': future_humidity.values,
    'Pressure (hPa)': future_pressure.values,
    'Dew Point (°C)': future_dew.values
})

# Format time for display
forecast_df['Time'] = forecast_df['DateTime'].dt.strftime('%I:%M:%S %p')
forecast_df['Date'] = '26-11-2025'

# Reorder columns
forecast_df = forecast_df[['Date', 'Time', 'Temperature (°C)', 'Humidity (%)', 'Pressure (hPa)', 'Dew Point (°C)']]

# Save forecast
forecast_df.to_excel('future_forecast_2pm_to_6pm.xlsx', index=False)
print("✓ Future forecast saved: future_forecast_2pm_to_6pm.xlsx")

print(f"\nForecast Summary:")
print(f"  Temperature: {forecast_df['Temperature (°C)'].min():.1f}°C - {forecast_df['Temperature (°C)'].max():.1f}°C")
print(f"  Humidity: {forecast_df['Humidity (%)'].min():.1f}% - {forecast_df['Humidity (%)'].max():.1f}%")
print(f"  Pressure: {forecast_df['Pressure (hPa)'].min():.1f} - {forecast_df['Pressure (hPa)'].max():.1f} hPa")
print(f"  Dew Point: {forecast_df['Dew Point (°C)'].min():.1f}°C - {forecast_df['Dew Point (°C)'].max():.1f}°C")

# ============================================================================
# FUTURE FORECAST VISUALIZATION
# ============================================================================
print("\n[STEP 3] Creating future forecast visualizations...")

fig, axes = plt.subplots(4, 1, figsize=(16, 14))

# Temperature
axes[0].plot(df.index, df[temp_col], label='Historical Data', color='#2E86AB', linewidth=2)
axes[0].plot(future_times, future_temp, label='Future Forecast', color='#F18F01', linewidth=2, linestyle='--', marker='o', markersize=2)
axes[0].axvline(x=df.index[-1], color='red', linestyle=':', linewidth=2, label='Forecast Start')
axes[0].set_title('Temperature Forecast (9 AM - 6:15 PM)', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Temperature (°C)', fontsize=12, fontweight='bold')
axes[0].legend(loc='best', fontsize=10)
axes[0].grid(True, alpha=0.3)

# Humidity
axes[1].plot(df.index, df[humidity_col], label='Historical Data', color='#2E86AB', linewidth=2)
axes[1].plot(future_times, future_humidity, label='Future Forecast', color='#F18F01', linewidth=2, linestyle='--', marker='o', markersize=2)
axes[1].axvline(x=df.index[-1], color='red', linestyle=':', linewidth=2, label='Forecast Start')
axes[1].set_title('Humidity Forecast (9 AM - 6:15 PM)', fontsize=14, fontweight='bold')
axes[1].set_ylabel('Humidity (%)', fontsize=12, fontweight='bold')
axes[1].legend(loc='best', fontsize=10)
axes[1].grid(True, alpha=0.3)

# Pressure
axes[2].plot(df.index, df[pressure_col], label='Historical Data', color='#2E86AB', linewidth=2)
axes[2].plot(future_times, future_pressure, label='Future Forecast', color='#F18F01', linewidth=2, linestyle='--', marker='o', markersize=2)
axes[2].axvline(x=df.index[-1], color='red', linestyle=':', linewidth=2, label='Forecast Start')
axes[2].set_title('Pressure Forecast (9 AM - 6:15 PM)', fontsize=14, fontweight='bold')
axes[2].set_ylabel('Pressure (hPa)', fontsize=12, fontweight='bold')
axes[2].legend(loc='best', fontsize=10)
axes[2].grid(True, alpha=0.3)

# Dew Point
axes[3].plot(df.index, df[dew_col], label='Historical Data', color='#2E86AB', linewidth=2)
axes[3].plot(future_times, future_dew, label='Future Forecast', color='#F18F01', linewidth=2, linestyle='--', marker='o', markersize=2)
axes[3].axvline(x=df.index[-1], color='red', linestyle=':', linewidth=2, label='Forecast Start')
axes[3].set_title('Dew Point Forecast (9 AM - 6:15 PM)', fontsize=14, fontweight='bold')
axes[3].set_ylabel('Dew Point (°C)', fontsize=12, fontweight='bold')
axes[3].set_xlabel('Time', fontsize=12, fontweight='bold')
axes[3].legend(loc='best', fontsize=10)
axes[3].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('future_forecast_visualization.png', dpi=300, bbox_inches='tight')
print("✓ Future forecast visualization saved")
plt.close()

# ============================================================================
# PERFORMANCE COMPARISON BAR CHARTS
# ============================================================================
print("\n[STEP 4] Creating performance comparison charts...")

# Load performance metrics
perf_df = pd.read_excel('model_performance_metrics.xlsx')

# Create subplots for each parameter
parameters = ['Temperature', 'Humidity', 'Pressure', 'Dew Point']
metrics = ['RMSE', 'MAE', 'MAPE', 'R²']

for param in parameters:
    param_data = perf_df[perf_df['Parameter'] == param]
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle(f'{param} - Model Performance Comparison', fontsize=16, fontweight='bold')
    
    for idx, metric in enumerate(metrics):
        ax = axes[idx // 2, idx % 2]
        models = param_data['Model']
        values = param_data[metric]
        
        bars = ax.bar(models, values, color=['#FF6B6B', '#4ECDC4', '#95E1D3'], edgecolor='black', linewidth=1.5)
        ax.set_title(f'{metric}', fontsize=12, fontweight='bold')
        ax.set_ylabel(metric, fontsize=10)
        ax.grid(True, alpha=0.3, axis='y')
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{height:.4f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig(f'{param.lower()}_performance_comparison.png', dpi=300, bbox_inches='tight')
    print(f"✓ {param} performance chart saved")
    plt.close()

print("\n✓ All visualizations completed!")
