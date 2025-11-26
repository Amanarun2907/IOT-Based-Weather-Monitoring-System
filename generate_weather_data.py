import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import openpyxl

# Set random seed for reproducibility
np.random.seed(42)

# Function to calculate dew point using Magnus formula
def calculate_dew_point(temp_celsius, humidity_percent):
    """
    Calculate dew point using Magnus-Tetens formula
    temp_celsius: Temperature in Celsius
    humidity_percent: Relative humidity in percentage
    Returns: Dew point in Celsius
    """
    a = 17.27
    b = 237.7
    
    alpha = ((a * temp_celsius) / (b + temp_celsius)) + np.log(humidity_percent / 100.0)
    dew_point = (b * alpha) / (a - alpha)
    
    return dew_point

# Configuration
date = "26-11-2025"
start_time = datetime.strptime("26-11-2025 09:00:00", "%d-%m-%Y %H:%M:%S")
total_minutes = 5 * 60  # 5 hours = 300 entries

# Initialize lists to store data
timestamps = []
dates = []
temperatures = []
humidities = []
pressures = []
dew_points = []

# Generate data for each minute
for minute in range(total_minutes):
    current_time = start_time + timedelta(minutes=minute)
    
    # Time in hours from start (0 to 5)
    hour_offset = minute / 60.0
    
    # Temperature pattern (Winter morning in Gurgaon)
    # Cooler at 9 AM (~16°C), peaks at 1 PM (~22-23°C), slight decrease by 2 PM
    if hour_offset <= 4:  # 9 AM to 1 PM (4 hours)
        # Gradual increase from 16°C to 23°C
        base_temp = 16 + (7 * (hour_offset / 4.0))
    else:  # 1 PM to 2 PM (1 hour)
        # Slight decrease from 23°C to 22°C
        base_temp = 23 - (1 * ((hour_offset - 4) / 1.0))
    
    # Add realistic sensor noise (±0.1-0.3°C)
    temp = base_temp + np.random.uniform(-0.3, 0.3)
    temp = round(temp, 1)
    
    # Humidity pattern (Inverse relationship with temperature)
    # Higher in morning (~55-60%), lower at peak temperature (~40-45%)
    if hour_offset <= 4:  # 9 AM to 1 PM
        # Gradual decrease from 58% to 41%
        base_humidity = 58 - (17 * (hour_offset / 4.0))
    else:  # 1 PM to 2 PM
        # Slight increase from 41% to 43%
        base_humidity = 41 + (2 * ((hour_offset - 4) / 1.0))
    
    # Add realistic sensor noise (±1-2%)
    humidity = base_humidity + np.random.uniform(-2, 2)
    humidity = round(humidity, 1)
    # Ensure within range
    humidity = max(40, min(60, humidity))
    
    # Pressure pattern (Small natural fluctuations)
    # Range: 1016.5 - 1019.0 hPa
    # Slight decrease during day (typical pattern)
    base_pressure = 1018.5 - (0.4 * (hour_offset / 5.0))
    
    # Add realistic sensor noise (±0.1-0.2 hPa)
    pressure = base_pressure + np.random.uniform(-0.2, 0.2)
    pressure = round(pressure, 1)
    # Ensure within range
    pressure = max(1016.5, min(1019.0, pressure))
    
    # Calculate dew point using Magnus formula
    dew_point = calculate_dew_point(temp, humidity)
    # Add small sensor noise (±0.1°C)
    dew_point = dew_point + np.random.uniform(-0.1, 0.1)
    dew_point = round(dew_point, 1)
    # Ensure within realistic range
    dew_point = max(0.2, min(13.3, dew_point))
    
    # Store data
    timestamps.append(current_time.strftime("%I:%M:%S %p"))
    dates.append(date)
    temperatures.append(temp)
    humidities.append(humidity)
    pressures.append(pressure)
    dew_points.append(dew_point)

# Create DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Time': timestamps,
    'Temperature (°C)': temperatures,
    'Humidity (%)': humidities,
    'Pressure (hPa)': pressures,
    'Dew Point (°C)': dew_points
})

# Save to Excel
output_file = 'iot_sensor_readings.xlsx'
df.to_excel(output_file, index=False, sheet_name='Weather Data')

print(f"✓ Excel file generated: {output_file}")
print(f"✓ Total entries: {len(df)}")
print(f"\nData Summary:")
print(f"Temperature: {df['Temperature (°C)'].min():.1f}°C - {df['Temperature (°C)'].max():.1f}°C")
print(f"Humidity: {df['Humidity (%)'].min():.1f}% - {df['Humidity (%)'].max():.1f}%")
print(f"Pressure: {df['Pressure (hPa)'].min():.1f} hPa - {df['Pressure (hPa)'].max():.1f} hPa")
print(f"Dew Point: {df['Dew Point (°C)'].min():.1f}°C - {df['Dew Point (°C)'].max():.1f}°C")
print(f"\nFirst 5 entries:")
print(df.head())
print(f"\nLast 5 entries:")
print(df.tail())
