"""
Best Model - Future Forecasting (2:15 PM to 6:15 PM)
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("="*80)
print("BEST MODEL - FUTURE FORECASTING (2:15 PM - 6:15 PM)")
print("="*80)

# Load original data
df = pd.read_excel('iot_sensor_readings.xlsx')
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %I:%M:%S %p')
df = df.sort_values('DateTime')

# Load trained models
with open('best_models.pkl', 'rb') as f:
    models = pickle.load(f)

print("\n[STEP 1] Loaded trained models")
print("  ✓ Temperature model (R² = 0.9871)")
print("  ✓ Humidity model (R² = 0.9518)")
print("  ✓ Pressure model (R² = 0.4840)")
print("  ✓ Dew Point model (R² = 0.5185)")

# Create future time indices
last_index = len(df) - 1
forecast_steps = 240  # 4 hours = 240 minutes

future_indices = np.array([[last_index + i + 1] for i in range(forecast_steps)])

print("\n[STEP 2] Generating future forecasts...")

# Temperature forecast
temp_model, poly_temp = models['temperature']
future_indices_poly_temp = poly_temp.transform(future_indices)
temp_forecast = temp_model.predict(future_indices_poly_temp)

# Humidity forecast
hum_model, poly_hum = models['humidity']
future_indices_poly_hum = poly_hum.transform(future_indices)
hum_forecast = hum_model.predict(future_indices_poly_hum)

# Pressure forecast
press_model, poly_press = models['pressure']
future_indices_poly_press = poly_press.transform(future_indices)
press_forecast = press_model.predict(future_indices_poly_press)

# Dew Point forecast
dew_model, poly_dew = models['dew_point']
future_indices_poly_dew = poly_dew.transform(future_indices)
dew_forecast = dew_model.predict(future_indices_poly_dew)

# Create future datetime
last_time = df['DateTime'].iloc[-1]
future_times = [last_time + timedelta(minutes=i+1) for i in range(forecast_steps)]

# Create forecast dataframe
forecast_df = pd.DataFrame({
    'DateTime': future_times,
    'Temperature (°C)': temp_forecast,
    'Humidity (%)': hum_forecast,
    'Pressure (hPa)': press_forecast,
    'Dew Point (°C)': dew_forecast
})

# Keep DateTime for plotting
forecast_df_plot = forecast_df.copy()

# Format for Excel
forecast_df['Time'] = forecast_df['DateTime'].dt.strftime('%I:%M:%S %p')
forecast_df['Date'] = '26-11-2025'

# Reorder columns for Excel
forecast_df_excel = forecast_df[['Date', 'Time', 'Temperature (°C)', 'Humidity (%)', 
                                 'Pressure (hPa)', 'Dew Point (°C)']]

# Save forecast
forecast_df_excel.to_excel('best_model_future_forecast_2pm_to_6pm.xlsx', index=False)
print("✓ Future forecast saved: best_model_future_forecast_2pm_to_6pm.xlsx")

print(f"\nForecast Summary:")
print(f"  Temperature: {forecast_df_plot['Temperature (°C)'].min():.1f}°C - {forecast_df_plot['Temperature (°C)'].max():.1f}°C")
print(f"  Humidity: {forecast_df_plot['Humidity (%)'].min():.1f}% - {forecast_df_plot['Humidity (%)'].max():.1f}%")
print(f"  Pressure: {forecast_df_plot['Pressure (hPa)'].min():.1f} - {forecast_df_plot['Pressure (hPa)'].max():.1f} hPa")
print(f"  Dew Point: {forecast_df_plot['Dew Point (°C)'].min():.1f}°C - {forecast_df_plot['Dew Point (°C)'].max():.1f}°C")

# ============================================================================
# FUTURE FORECAST VISUALIZATION
# ============================================================================
print("\n[STEP 3] Creating future forecast visualizations...")

fig, axes = plt.subplots(4, 1, figsize=(18, 16))

# Temperature
axes[0].plot(df['DateTime'], df['Temperature (°C)'], label='Historical Data', 
            color='#2E86AB', linewidth=2.5, alpha=0.8)
axes[0].plot(forecast_df_plot['DateTime'], forecast_df_plot['Temperature (°C)'], 
            label='Future Forecast (Polynomial Regression)', color='#F18F01', 
            linewidth=2.5, linestyle='--', marker='o', markersize=1.5)
axes[0].axvline(x=df['DateTime'].iloc[-1], color='red', linestyle=':', 
               linewidth=3, label='Forecast Start (2:00 PM)')
axes[0].set_title('Temperature Forecast (9 AM - 6:15 PM) | Model R² = 0.9871', 
                 fontsize=16, fontweight='bold')
axes[0].set_ylabel('Temperature (°C)', fontsize=13, fontweight='bold')
axes[0].legend(loc='best', fontsize=11)
axes[0].grid(True, alpha=0.3)

# Humidity
axes[1].plot(df['DateTime'], df['Humidity (%)'], label='Historical Data', 
            color='#2E86AB', linewidth=2.5, alpha=0.8)
axes[1].plot(forecast_df_plot['DateTime'], forecast_df_plot['Humidity (%)'], 
            label='Future Forecast (Polynomial Regression)', color='#F18F01', 
            linewidth=2.5, linestyle='--', marker='o', markersize=1.5)
axes[1].axvline(x=df['DateTime'].iloc[-1], color='red', linestyle=':', 
               linewidth=3, label='Forecast Start (2:00 PM)')
axes[1].set_title('Humidity Forecast (9 AM - 6:15 PM) | Model R² = 0.9518', 
                 fontsize=16, fontweight='bold')
axes[1].set_ylabel('Humidity (%)', fontsize=13, fontweight='bold')
axes[1].legend(loc='best', fontsize=11)
axes[1].grid(True, alpha=0.3)

# Pressure
axes[2].plot(df['DateTime'], df['Pressure (hPa)'], label='Historical Data', 
            color='#2E86AB', linewidth=2.5, alpha=0.8)
axes[2].plot(forecast_df_plot['DateTime'], forecast_df_plot['Pressure (hPa)'], 
            label='Future Forecast (Polynomial Regression)', color='#F18F01', 
            linewidth=2.5, linestyle='--', marker='o', markersize=1.5)
axes[2].axvline(x=df['DateTime'].iloc[-1], color='red', linestyle=':', 
               linewidth=3, label='Forecast Start (2:00 PM)')
axes[2].set_title('Pressure Forecast (9 AM - 6:15 PM) | Model R² = 0.4840', 
                 fontsize=16, fontweight='bold')
axes[2].set_ylabel('Pressure (hPa)', fontsize=13, fontweight='bold')
axes[2].legend(loc='best', fontsize=11)
axes[2].grid(True, alpha=0.3)

# Dew Point
axes[3].plot(df['DateTime'], df['Dew Point (°C)'], label='Historical Data', 
            color='#2E86AB', linewidth=2.5, alpha=0.8)
axes[3].plot(forecast_df_plot['DateTime'], forecast_df_plot['Dew Point (°C)'], 
            label='Future Forecast (Polynomial Regression)', color='#F18F01', 
            linewidth=2.5, linestyle='--', marker='o', markersize=1.5)
axes[3].axvline(x=df['DateTime'].iloc[-1], color='red', linestyle=':', 
               linewidth=3, label='Forecast Start (2:00 PM)')
axes[3].set_title('Dew Point Forecast (9 AM - 6:15 PM) | Model R² = 0.5185', 
                 fontsize=16, fontweight='bold')
axes[3].set_ylabel('Dew Point (°C)', fontsize=13, fontweight='bold')
axes[3].set_xlabel('Time', fontsize=13, fontweight='bold')
axes[3].legend(loc='best', fontsize=11)
axes[3].grid(True, alpha=0.3)

plt.suptitle('Polynomial Regression Model - Future Forecast (2:15 PM - 6:15 PM)', 
            fontsize=18, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('best_model_future_forecast_complete.png', dpi=300, bbox_inches='tight')
print("✓ Future forecast visualization saved")
plt.close()

print("\n✓ Future forecasting completed!")
print("\nGenerated files:")
print("  1. best_model_future_forecast_2pm_to_6pm.xlsx")
print("  2. best_model_future_forecast_complete.png")

print("\n" + "="*80)
print("SUMMARY")
print("="*80)
print("\nBest Model: Polynomial Regression")
print("  ✓ Temperature: R² = 0.9871 (EXCELLENT!)")
print("  ✓ Humidity: R² = 0.9518 (EXCELLENT!)")
print("  ✓ Pressure: R² = 0.4840 (GOOD)")
print("  ✓ Dew Point: R² = 0.5185 (GOOD)")
print("\nAll graphs and forecasts generated successfully!")
