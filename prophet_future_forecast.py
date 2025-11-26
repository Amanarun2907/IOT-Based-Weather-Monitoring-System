"""
Prophet Model - Future Forecasting (2:15 PM to 6:15 PM)
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
print("PROPHET MODEL - FUTURE FORECASTING")
print("="*80)

# Load data
df = pd.read_excel('iot_sensor_readings.xlsx')
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %I:%M:%S %p')
df = df.sort_values('DateTime')

temp_col = 'Temperature (°C)'
humidity_col = 'Humidity (%)'
pressure_col = 'Pressure (hPa)'
dew_col = 'Dew Point (°C)'

print("\n[STEP 1] Training models on complete dataset...")

# Forecast 240 minutes (4 hours from 2:15 PM to 6:15 PM)
forecast_steps = 240

# ============================================================================
# TEMPERATURE FORECAST
# ============================================================================
print("\n  Training Temperature model...")
temp_data = df[['DateTime', temp_col]].copy()
temp_data.columns = ['ds', 'y']

temp_model = Prophet(daily_seasonality=True, weekly_seasonality=False, 
                     yearly_seasonality=False, changepoint_prior_scale=0.5)
temp_model.fit(temp_data)

# Create future dataframe
last_time = df['DateTime'].iloc[-1]
future_dates = [last_time + timedelta(minutes=i+1) for i in range(forecast_steps)]
future_df_temp = pd.DataFrame({'ds': future_dates})

# Forecast
temp_future = temp_model.predict(future_df_temp)

# ============================================================================
# HUMIDITY FORECAST
# ============================================================================
print("  Training Humidity model...")
hum_data = df[['DateTime', humidity_col]].copy()
hum_data.columns = ['ds', 'y']

hum_model = Prophet(daily_seasonality=True, weekly_seasonality=False, 
                    yearly_seasonality=False, changepoint_prior_scale=0.5)
hum_model.fit(hum_data)

future_df_hum = pd.DataFrame({'ds': future_dates})
hum_future = hum_model.predict(future_df_hum)

# ============================================================================
# PRESSURE FORECAST
# ============================================================================
print("  Training Pressure model...")
press_data = df[['DateTime', pressure_col]].copy()
press_data.columns = ['ds', 'y']

press_model = Prophet(daily_seasonality=True, weekly_seasonality=False, 
                      yearly_seasonality=False, changepoint_prior_scale=0.3)
press_model.fit(press_data)

future_df_press = pd.DataFrame({'ds': future_dates})
press_future = press_model.predict(future_df_press)

# ============================================================================
# DEW POINT FORECAST
# ============================================================================
print("  Training Dew Point model...")
dew_data = df[['DateTime', dew_col]].copy()
dew_data.columns = ['ds', 'y']

dew_model = Prophet(daily_seasonality=True, weekly_seasonality=False, 
                    yearly_seasonality=False, changepoint_prior_scale=0.5)
dew_model.fit(dew_data)

future_df_dew = pd.DataFrame({'ds': future_dates})
dew_future = dew_model.predict(future_df_dew)

# ============================================================================
# CREATE FORECAST DATAFRAME
# ============================================================================
print("\n[STEP 2] Creating forecast dataframe...")

forecast_df = pd.DataFrame({
    'DateTime': future_dates,
    'Temperature (°C)': temp_future['yhat'].values,
    'Humidity (%)': hum_future['yhat'].values,
    'Pressure (hPa)': press_future['yhat'].values,
    'Dew Point (°C)': dew_future['yhat'].values
})

# Format time for display
forecast_df['Time'] = forecast_df['DateTime'].dt.strftime('%I:%M:%S %p')
forecast_df['Date'] = '26-11-2025'

# Reorder columns
forecast_df = forecast_df[['Date', 'Time', 'Temperature (°C)', 'Humidity (%)', 
                           'Pressure (hPa)', 'Dew Point (°C)']]

# Save forecast
forecast_df.to_excel('prophet_future_forecast_2pm_to_6pm.xlsx', index=False)
print("✓ Future forecast saved: prophet_future_forecast_2pm_to_6pm.xlsx")

print(f"\nForecast Summary:")
print(f"  Temperature: {forecast_df['Temperature (°C)'].min():.1f}°C - {forecast_df['Temperature (°C)'].max():.1f}°C")
print(f"  Humidity: {forecast_df['Humidity (%)'].min():.1f}% - {forecast_df['Humidity (%)'].max():.1f}%")
print(f"  Pressure: {forecast_df['Pressure (hPa)'].min():.1f} - {forecast_df['Pressure (hPa)'].max():.1f} hPa")
print(f"  Dew Point: {forecast_df['Dew Point (°C)'].min():.1f}°C - {forecast_df['Dew Point (°C)'].max():.1f}°C")

# ============================================================================
# FUTURE FORECAST VISUALIZATION
# ============================================================================
print("\n[STEP 3] Creating future forecast visualizations...")

fig, axes = plt.subplots(4, 1, figsize=(18, 16))

# Temperature
axes[0].plot(df['DateTime'], df[temp_col], label='Historical Data', 
            color='#2E86AB', linewidth=2.5, alpha=0.8)
axes[0].plot(forecast_df['DateTime'], forecast_df['Temperature (°C)'], 
            label='Future Forecast', color='#F18F01', linewidth=2.5, linestyle='--', marker='o', markersize=2)
axes[0].axvline(x=df['DateTime'].iloc[-1], color='red', linestyle=':', linewidth=3, label='Forecast Start')
axes[0].set_title('Temperature Forecast (9 AM - 6:15 PM)', fontsize=16, fontweight='bold')
axes[0].set_ylabel('Temperature (°C)', fontsize=13, fontweight='bold')
axes[0].legend(loc='best', fontsize=11)
axes[0].grid(True, alpha=0.3)

# Humidity
axes[1].plot(df['DateTime'], df[humidity_col], label='Historical Data', 
            color='#2E86AB', linewidth=2.5, alpha=0.8)
axes[1].plot(forecast_df['DateTime'], forecast_df['Humidity (%)'], 
            label='Future Forecast', color='#F18F01', linewidth=2.5, linestyle='--', marker='o', markersize=2)
axes[1].axvline(x=df['DateTime'].iloc[-1], color='red', linestyle=':', linewidth=3, label='Forecast Start')
axes[1].set_title('Humidity Forecast (9 AM - 6:15 PM)', fontsize=16, fontweight='bold')
axes[1].set_ylabel('Humidity (%)', fontsize=13, fontweight='bold')
axes[1].legend(loc='best', fontsize=11)
axes[1].grid(True, alpha=0.3)

# Pressure
axes[2].plot(df['DateTime'], df[pressure_col], label='Historical Data', 
            color='#2E86AB', linewidth=2.5, alpha=0.8)
axes[2].plot(forecast_df['DateTime'], forecast_df['Pressure (hPa)'], 
            label='Future Forecast', color='#F18F01', linewidth=2.5, linestyle='--', marker='o', markersize=2)
axes[2].axvline(x=df['DateTime'].iloc[-1], color='red', linestyle=':', linewidth=3, label='Forecast Start')
axes[2].set_title('Pressure Forecast (9 AM - 6:15 PM)', fontsize=16, fontweight='bold')
axes[2].set_ylabel('Pressure (hPa)', fontsize=13, fontweight='bold')
axes[2].legend(loc='best', fontsize=11)
axes[2].grid(True, alpha=0.3)

# Dew Point
axes[3].plot(df['DateTime'], df[dew_col], label='Historical Data', 
            color='#2E86AB', linewidth=2.5, alpha=0.8)
axes[3].plot(forecast_df['DateTime'], forecast_df['Dew Point (°C)'], 
            label='Future Forecast', color='#F18F01', linewidth=2.5, linestyle='--', marker='o', markersize=2)
axes[3].axvline(x=df['DateTime'].iloc[-1], color='red', linestyle=':', linewidth=3, label='Forecast Start')
axes[3].set_title('Dew Point Forecast (9 AM - 6:15 PM)', fontsize=16, fontweight='bold')
axes[3].set_ylabel('Dew Point (°C)', fontsize=13, fontweight='bold')
axes[3].set_xlabel('Time', fontsize=13, fontweight='bold')
axes[3].legend(loc='best', fontsize=11)
axes[3].grid(True, alpha=0.3)

plt.suptitle('Prophet Model - Future Forecast (2:15 PM - 6:15 PM)', 
            fontsize=18, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('prophet_future_forecast_complete.png', dpi=300, bbox_inches='tight')
print("✓ Future forecast visualization saved: prophet_future_forecast_complete.png")
plt.close()

print("\n✓ Future forecasting completed!")
print("\nGenerated files:")
print("  1. prophet_future_forecast_2pm_to_6pm.xlsx")
print("  2. prophet_future_forecast_complete.png")
