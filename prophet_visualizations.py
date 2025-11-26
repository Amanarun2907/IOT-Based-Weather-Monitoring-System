"""
Prophet Model Visualizations
Complete graphs and charts for all parameters
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

from prophet import Prophet

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("="*80)
print("CREATING PROPHET MODEL VISUALIZATIONS")
print("="*80)

# Load data
df = pd.read_excel('iot_sensor_readings.xlsx')
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %I:%M:%S %p')
df = df.sort_values('DateTime')

temp_col = 'Temperature (°C)'
humidity_col = 'Humidity (%)'
pressure_col = 'Pressure (hPa)'
dew_col = 'Dew Point (°C)'

# Train-test split
train_size = int(len(df) * 0.8)
train_data = df[:train_size]
test_data = df[train_size:]

print("\n[STEP 1] Creating model comparison plots...")

# ============================================================================
# TEMPERATURE - PROPHET FORECAST
# ============================================================================
print("\n  Training Temperature model...")
temp_train = train_data[['DateTime', temp_col]].copy()
temp_train.columns = ['ds', 'y']
temp_test = test_data[['DateTime', temp_col]].copy()
temp_test.columns = ['ds', 'y']

temp_model = Prophet(daily_seasonality=True, weekly_seasonality=False, 
                     yearly_seasonality=False, changepoint_prior_scale=0.5)
temp_model.fit(temp_train)
temp_forecast = temp_model.predict(temp_test[['ds']])

fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(train_data['DateTime'], train_data[temp_col], 
       label='Training Data', color='#2E86AB', linewidth=2.5, alpha=0.8)
ax.plot(test_data['DateTime'], test_data[temp_col], 
       label='Actual Test Data', color='#A23B72', linewidth=2.5, marker='o', markersize=4)
ax.plot(temp_forecast['ds'], temp_forecast['yhat'], 
       label='Prophet Prediction', color='#F18F01', linewidth=2.5, linestyle='--')
ax.fill_between(temp_forecast['ds'], temp_forecast['yhat_lower'], temp_forecast['yhat_upper'],
               alpha=0.2, color='#F18F01', label='Confidence Interval')
ax.set_title('Temperature Forecasting - Prophet Model', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=14, fontweight='bold')
ax.set_ylabel('Temperature (°C)', fontsize=14, fontweight='bold')
ax.legend(loc='best', fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('prophet_temperature_forecast.png', dpi=300, bbox_inches='tight')
print("  ✓ Temperature forecast saved")
plt.close()

# ============================================================================
# HUMIDITY - PROPHET FORECAST
# ============================================================================
print("  Training Humidity model...")
hum_train = train_data[['DateTime', humidity_col]].copy()
hum_train.columns = ['ds', 'y']
hum_test = test_data[['DateTime', humidity_col]].copy()
hum_test.columns = ['ds', 'y']

hum_model = Prophet(daily_seasonality=True, weekly_seasonality=False, 
                    yearly_seasonality=False, changepoint_prior_scale=0.5)
hum_model.fit(hum_train)
hum_forecast = hum_model.predict(hum_test[['ds']])

fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(train_data['DateTime'], train_data[humidity_col], 
       label='Training Data', color='#2E86AB', linewidth=2.5, alpha=0.8)
ax.plot(test_data['DateTime'], test_data[humidity_col], 
       label='Actual Test Data', color='#A23B72', linewidth=2.5, marker='o', markersize=4)
ax.plot(hum_forecast['ds'], hum_forecast['yhat'], 
       label='Prophet Prediction', color='#F18F01', linewidth=2.5, linestyle='--')
ax.fill_between(hum_forecast['ds'], hum_forecast['yhat_lower'], hum_forecast['yhat_upper'],
               alpha=0.2, color='#F18F01', label='Confidence Interval')
ax.set_title('Humidity Forecasting - Prophet Model', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=14, fontweight='bold')
ax.set_ylabel('Humidity (%)', fontsize=14, fontweight='bold')
ax.legend(loc='best', fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('prophet_humidity_forecast.png', dpi=300, bbox_inches='tight')
print("  ✓ Humidity forecast saved")
plt.close()

# ============================================================================
# PRESSURE - PROPHET FORECAST
# ============================================================================
print("  Training Pressure model...")
press_train = train_data[['DateTime', pressure_col]].copy()
press_train.columns = ['ds', 'y']
press_test = test_data[['DateTime', pressure_col]].copy()
press_test.columns = ['ds', 'y']

press_model = Prophet(daily_seasonality=True, weekly_seasonality=False, 
                      yearly_seasonality=False, changepoint_prior_scale=0.3)
press_model.fit(press_train)
press_forecast = press_model.predict(press_test[['ds']])

fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(train_data['DateTime'], train_data[pressure_col], 
       label='Training Data', color='#2E86AB', linewidth=2.5, alpha=0.8)
ax.plot(test_data['DateTime'], test_data[pressure_col], 
       label='Actual Test Data', color='#A23B72', linewidth=2.5, marker='o', markersize=4)
ax.plot(press_forecast['ds'], press_forecast['yhat'], 
       label='Prophet Prediction', color='#F18F01', linewidth=2.5, linestyle='--')
ax.fill_between(press_forecast['ds'], press_forecast['yhat_lower'], press_forecast['yhat_upper'],
               alpha=0.2, color='#F18F01', label='Confidence Interval')
ax.set_title('Pressure Forecasting - Prophet Model', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=14, fontweight='bold')
ax.set_ylabel('Pressure (hPa)', fontsize=14, fontweight='bold')
ax.legend(loc='best', fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('prophet_pressure_forecast.png', dpi=300, bbox_inches='tight')
print("  ✓ Pressure forecast saved")
plt.close()

# ============================================================================
# DEW POINT - PROPHET FORECAST
# ============================================================================
print("  Training Dew Point model...")
dew_train = train_data[['DateTime', dew_col]].copy()
dew_train.columns = ['ds', 'y']
dew_test = test_data[['DateTime', dew_col]].copy()
dew_test.columns = ['ds', 'y']

dew_model = Prophet(daily_seasonality=True, weekly_seasonality=False, 
                    yearly_seasonality=False, changepoint_prior_scale=0.5)
dew_model.fit(dew_train)
dew_forecast = dew_model.predict(dew_test[['ds']])

fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(train_data['DateTime'], train_data[dew_col], 
       label='Training Data', color='#2E86AB', linewidth=2.5, alpha=0.8)
ax.plot(test_data['DateTime'], test_data[dew_col], 
       label='Actual Test Data', color='#A23B72', linewidth=2.5, marker='o', markersize=4)
ax.plot(dew_forecast['ds'], dew_forecast['yhat'], 
       label='Prophet Prediction', color='#F18F01', linewidth=2.5, linestyle='--')
ax.fill_between(dew_forecast['ds'], dew_forecast['yhat_lower'], dew_forecast['yhat_upper'],
               alpha=0.2, color='#F18F01', label='Confidence Interval')
ax.set_title('Dew Point Forecasting - Prophet Model', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=14, fontweight='bold')
ax.set_ylabel('Dew Point (°C)', fontsize=14, fontweight='bold')
ax.legend(loc='best', fontsize=11, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('prophet_dewpoint_forecast.png', dpi=300, bbox_inches='tight')
print("  ✓ Dew Point forecast saved")
plt.close()

# ============================================================================
# COMBINED PLOT - ALL PARAMETERS
# ============================================================================
print("\n[STEP 2] Creating combined visualization...")

fig, axes = plt.subplots(4, 1, figsize=(16, 16))

# Temperature
axes[0].plot(train_data['DateTime'], train_data[temp_col], 
            label='Training', color='#2E86AB', linewidth=2, alpha=0.7)
axes[0].plot(test_data['DateTime'], test_data[temp_col], 
            label='Actual', color='#A23B72', linewidth=2, marker='o', markersize=3)
axes[0].plot(temp_forecast['ds'], temp_forecast['yhat'], 
            label='Prophet Forecast', color='#F18F01', linewidth=2, linestyle='--')
axes[0].fill_between(temp_forecast['ds'], temp_forecast['yhat_lower'], temp_forecast['yhat_upper'],
                    alpha=0.2, color='#F18F01')
axes[0].set_title('Temperature Forecast', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Temperature (°C)', fontsize=12, fontweight='bold')
axes[0].legend(loc='best', fontsize=10)
axes[0].grid(True, alpha=0.3)

# Humidity
axes[1].plot(train_data['DateTime'], train_data[humidity_col], 
            label='Training', color='#2E86AB', linewidth=2, alpha=0.7)
axes[1].plot(test_data['DateTime'], test_data[humidity_col], 
            label='Actual', color='#A23B72', linewidth=2, marker='o', markersize=3)
axes[1].plot(hum_forecast['ds'], hum_forecast['yhat'], 
            label='Prophet Forecast', color='#F18F01', linewidth=2, linestyle='--')
axes[1].fill_between(hum_forecast['ds'], hum_forecast['yhat_lower'], hum_forecast['yhat_upper'],
                    alpha=0.2, color='#F18F01')
axes[1].set_title('Humidity Forecast', fontsize=14, fontweight='bold')
axes[1].set_ylabel('Humidity (%)', fontsize=12, fontweight='bold')
axes[1].legend(loc='best', fontsize=10)
axes[1].grid(True, alpha=0.3)

# Pressure
axes[2].plot(train_data['DateTime'], train_data[pressure_col], 
            label='Training', color='#2E86AB', linewidth=2, alpha=0.7)
axes[2].plot(test_data['DateTime'], test_data[pressure_col], 
            label='Actual', color='#A23B72', linewidth=2, marker='o', markersize=3)
axes[2].plot(press_forecast['ds'], press_forecast['yhat'], 
            label='Prophet Forecast', color='#F18F01', linewidth=2, linestyle='--')
axes[2].fill_between(press_forecast['ds'], press_forecast['yhat_lower'], press_forecast['yhat_upper'],
                    alpha=0.2, color='#F18F01')
axes[2].set_title('Pressure Forecast', fontsize=14, fontweight='bold')
axes[2].set_ylabel('Pressure (hPa)', fontsize=12, fontweight='bold')
axes[2].legend(loc='best', fontsize=10)
axes[2].grid(True, alpha=0.3)

# Dew Point
axes[3].plot(train_data['DateTime'], train_data[dew_col], 
            label='Training', color='#2E86AB', linewidth=2, alpha=0.7)
axes[3].plot(test_data['DateTime'], test_data[dew_col], 
            label='Actual', color='#A23B72', linewidth=2, marker='o', markersize=3)
axes[3].plot(dew_forecast['ds'], dew_forecast['yhat'], 
            label='Prophet Forecast', color='#F18F01', linewidth=2, linestyle='--')
axes[3].fill_between(dew_forecast['ds'], dew_forecast['yhat_lower'], dew_forecast['yhat_upper'],
                    alpha=0.2, color='#F18F01')
axes[3].set_title('Dew Point Forecast', fontsize=14, fontweight='bold')
axes[3].set_ylabel('Dew Point (°C)', fontsize=12, fontweight='bold')
axes[3].set_xlabel('Time', fontsize=12, fontweight='bold')
axes[3].legend(loc='best', fontsize=10)
axes[3].grid(True, alpha=0.3)

plt.suptitle('Prophet Model - All Parameters Forecast', fontsize=18, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('prophet_all_parameters_combined.png', dpi=300, bbox_inches='tight')
print("  ✓ Combined forecast saved")
plt.close()

# ============================================================================
# PERFORMANCE BAR CHART
# ============================================================================
print("\n[STEP 3] Creating performance comparison chart...")

perf_df = pd.read_excel('prophet_model_performance.xlsx')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Prophet Model - Performance Metrics', fontsize=16, fontweight='bold')

metrics = ['RMSE', 'MAE', 'MAPE', 'R²']
colors = ['#FF6B6B', '#4ECDC4', '#95E1D3', '#45B7D1']

for idx, metric in enumerate(metrics):
    ax = axes[idx // 2, idx % 2]
    params = perf_df['Parameter']
    values = perf_df[metric]
    
    bars = ax.bar(params, values, color=colors[idx], edgecolor='black', linewidth=2, alpha=0.8)
    ax.set_title(f'{metric}', fontsize=13, fontweight='bold')
    ax.set_ylabel(metric, fontsize=11, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    ax.tick_params(axis='x', rotation=45)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{height:.4f}', ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('prophet_performance_metrics.png', dpi=300, bbox_inches='tight')
print("  ✓ Performance metrics chart saved")
plt.close()

print("\n✓ All Prophet visualizations completed!")
print("\nGenerated files:")
print("  1. prophet_temperature_forecast.png")
print("  2. prophet_humidity_forecast.png")
print("  3. prophet_pressure_forecast.png")
print("  4. prophet_dewpoint_forecast.png")
print("  5. prophet_all_parameters_combined.png")
print("  6. prophet_performance_metrics.png")
