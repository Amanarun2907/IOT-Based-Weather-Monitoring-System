"""
IoT Weather Monitoring System - Complete Time Series Analysis
Temperature, Humidity, Pressure & Dew Point Forecasting
Date: 26-11-2025 | Location: Gurugram, Haryana
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Time series models
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from arch import arch_model

# Statistical tests
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

# Performance metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Flowchart
from graphviz import Digraph

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("="*80)
print("IoT WEATHER MONITORING SYSTEM - TIME SERIES ANALYSIS")
print("="*80)

# ============================================================================
# STEP 1: LOAD AND EXPLORE DATA
# ============================================================================
print("\n[STEP 1] Loading Data...")
df = pd.read_excel('iot_sensor_readings.xlsx')

print(f"✓ Dataset loaded successfully")
print(f"  Shape: {df.shape}")
print(f"  Columns: {list(df.columns)}")

# ============================================================================
# STEP 2: STATISTICAL DESCRIPTION
# ============================================================================
print("\n[STEP 2] Statistical Description")
print("-"*80)
print(df.describe().round(2))

print("\n✓ Missing Values Check:")
print(df.isnull().sum())

# ============================================================================
# STEP 3: DATA PREPROCESSING
# ============================================================================
print("\n[STEP 3] Data Preprocessing...")

# Create datetime index
df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d-%m-%Y %I:%M:%S %p')
df = df.set_index('DateTime')
df = df.sort_index()

# Extract numeric columns
temp_col = 'Temperature (°C)'
humidity_col = 'Humidity (%)'
pressure_col = 'Pressure (hPa)'
dew_col = 'Dew Point (°C)'

print("✓ DateTime index created")
print("✓ Data sorted by time")

# ============================================================================
# STEP 4: VISUALIZATION - TIME SERIES PLOTS
# ============================================================================
print("\n[STEP 4] Creating visualizations...")

fig, axes = plt.subplots(4, 1, figsize=(15, 12))

# Temperature
axes[0].plot(df.index, df[temp_col], color='#FF6B6B', linewidth=2, label='Temperature')
axes[0].set_title('Temperature Over Time', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Temperature (°C)', fontsize=12)
axes[0].legend(loc='best')
axes[0].grid(True, alpha=0.3)

# Humidity
axes[1].plot(df.index, df[humidity_col], color='#4ECDC4', linewidth=2, label='Humidity')
axes[1].set_title('Humidity Over Time', fontsize=14, fontweight='bold')
axes[1].set_ylabel('Humidity (%)', fontsize=12)
axes[1].legend(loc='best')
axes[1].grid(True, alpha=0.3)

# Pressure
axes[2].plot(df.index, df[pressure_col], color='#95E1D3', linewidth=2, label='Pressure')
axes[2].set_title('Pressure Over Time', fontsize=14, fontweight='bold')
axes[2].set_ylabel('Pressure (hPa)', fontsize=12)
axes[2].legend(loc='best')
axes[2].grid(True, alpha=0.3)

# Dew Point
axes[3].plot(df.index, df[dew_col], color='#F38181', linewidth=2, label='Dew Point')
axes[3].set_title('Dew Point Over Time', fontsize=14, fontweight='bold')
axes[3].set_ylabel('Dew Point (°C)', fontsize=12)
axes[3].set_xlabel('Time', fontsize=12)
axes[3].legend(loc='best')
axes[3].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('time_series_plots.png', dpi=300, bbox_inches='tight')
print("✓ Time series plots saved: time_series_plots.png")
plt.close()

# Correlation heatmap
correlation_matrix = df[[temp_col, humidity_col, pressure_col, dew_col]].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, fmt='.3f', 
            linewidths=2, square=True, cbar_kws={"shrink": 0.8})
plt.title('Correlation Matrix of Weather Parameters', fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
print("✓ Correlation matrix saved: correlation_matrix.png")
plt.close()

# ============================================================================
# STEP 5: STATIONARITY TEST
# ============================================================================
print("\n[STEP 5] Stationarity Tests (ADF Test)...")
print("-"*80)

def adf_test(series, name):
    result = adfuller(series.dropna())
    print(f"\n{name}:")
    print(f"  ADF Statistic: {result[0]:.4f}")
    print(f"  p-value: {result[1]:.4f}")
    print(f"  Critical Values: {result[4]}")
    if result[1] <= 0.05:
        print(f"  ✓ Stationary (p-value <= 0.05)")
    else:
        print(f"  ✗ Non-stationary (p-value > 0.05)")
    return result[1] <= 0.05

temp_stationary = adf_test(df[temp_col], "Temperature")
humidity_stationary = adf_test(df[humidity_col], "Humidity")
pressure_stationary = adf_test(df[pressure_col], "Pressure")
dew_stationary = adf_test(df[dew_col], "Dew Point")

# ============================================================================
# STEP 6: ACF AND PACF PLOTS
# ============================================================================
print("\n[STEP 6] Creating ACF and PACF plots...")

fig, axes = plt.subplots(4, 2, figsize=(15, 16))

# Temperature
plot_acf(df[temp_col].dropna(), lags=40, ax=axes[0, 0])
axes[0, 0].set_title('Temperature - ACF', fontsize=12, fontweight='bold')
plot_pacf(df[temp_col].dropna(), lags=40, ax=axes[0, 1])
axes[0, 1].set_title('Temperature - PACF', fontsize=12, fontweight='bold')

# Humidity
plot_acf(df[humidity_col].dropna(), lags=40, ax=axes[1, 0])
axes[1, 0].set_title('Humidity - ACF', fontsize=12, fontweight='bold')
plot_pacf(df[humidity_col].dropna(), lags=40, ax=axes[1, 1])
axes[1, 1].set_title('Humidity - PACF', fontsize=12, fontweight='bold')

# Pressure
plot_acf(df[pressure_col].dropna(), lags=40, ax=axes[2, 0])
axes[2, 0].set_title('Pressure - ACF', fontsize=12, fontweight='bold')
plot_pacf(df[pressure_col].dropna(), lags=40, ax=axes[2, 1])
axes[2, 1].set_title('Pressure - PACF', fontsize=12, fontweight='bold')

# Dew Point
plot_acf(df[dew_col].dropna(), lags=40, ax=axes[3, 0])
axes[3, 0].set_title('Dew Point - ACF', fontsize=12, fontweight='bold')
plot_pacf(df[dew_col].dropna(), lags=40, ax=axes[3, 1])
axes[3, 1].set_title('Dew Point - PACF', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('acf_pacf_plots.png', dpi=300, bbox_inches='tight')
print("✓ ACF and PACF plots saved: acf_pacf_plots.png")
plt.close()

print("\n[STEP 7] Preparing for model training...")
print("  Train-Test Split: 80-20")

# Split data
train_size = int(len(df) * 0.8)
train_data = df[:train_size]
test_data = df[train_size:]

print(f"  Training samples: {len(train_data)}")
print(f"  Testing samples: {len(test_data)}")

print("\n✓ Data preprocessing completed!")
print("\nNext: Run model training and forecasting...")
