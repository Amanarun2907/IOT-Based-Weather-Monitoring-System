"""
Best Model Visualizations - All Graphs and Charts
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

print("="*80)
print("CREATING BEST MODEL VISUALIZATIONS")
print("="*80)

# Load data with predictions
df = pd.read_excel('model_predictions.xlsx')

temp_col = 'Temperature (°C)'
humidity_col = 'Humidity (%)'
pressure_col = 'Pressure (hPa)'
dew_col = 'Dew Point (°C)'

print("\n[STEP 1] Creating individual parameter plots...")

# ============================================================================
# TEMPERATURE PLOT
# ============================================================================
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(df['DateTime'], df[temp_col], label='Actual Data', 
       color='#2E86AB', linewidth=2.5, marker='o', markersize=3, alpha=0.7)
ax.plot(df['DateTime'], df['Temp_Predicted'], label='Polynomial Regression Fit', 
       color='#F18F01', linewidth=3, linestyle='--')
ax.set_title('Temperature - Polynomial Regression Model (R² = 0.9871)', 
            fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=14, fontweight='bold')
ax.set_ylabel('Temperature (°C)', fontsize=14, fontweight='bold')
ax.legend(loc='best', fontsize=12, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('best_model_temperature.png', dpi=300, bbox_inches='tight')
print("  ✓ Temperature plot saved")
plt.close()

# ============================================================================
# HUMIDITY PLOT
# ============================================================================
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(df['DateTime'], df[humidity_col], label='Actual Data', 
       color='#2E86AB', linewidth=2.5, marker='o', markersize=3, alpha=0.7)
ax.plot(df['DateTime'], df['Hum_Predicted'], label='Polynomial Regression Fit', 
       color='#F18F01', linewidth=3, linestyle='--')
ax.set_title('Humidity - Polynomial Regression Model (R² = 0.9518)', 
            fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=14, fontweight='bold')
ax.set_ylabel('Humidity (%)', fontsize=14, fontweight='bold')
ax.legend(loc='best', fontsize=12, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('best_model_humidity.png', dpi=300, bbox_inches='tight')
print("  ✓ Humidity plot saved")
plt.close()

# ============================================================================
# PRESSURE PLOT
# ============================================================================
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(df['DateTime'], df[pressure_col], label='Actual Data', 
       color='#2E86AB', linewidth=2.5, marker='o', markersize=3, alpha=0.7)
ax.plot(df['DateTime'], df['Press_Predicted'], label='Polynomial Regression Fit', 
       color='#F18F01', linewidth=3, linestyle='--')
ax.set_title('Pressure - Polynomial Regression Model (R² = 0.4840)', 
            fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=14, fontweight='bold')
ax.set_ylabel('Pressure (hPa)', fontsize=14, fontweight='bold')
ax.legend(loc='best', fontsize=12, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('best_model_pressure.png', dpi=300, bbox_inches='tight')
print("  ✓ Pressure plot saved")
plt.close()

# ============================================================================
# DEW POINT PLOT
# ============================================================================
fig, ax = plt.subplots(figsize=(16, 6))
ax.plot(df['DateTime'], df[dew_col], label='Actual Data', 
       color='#2E86AB', linewidth=2.5, marker='o', markersize=3, alpha=0.7)
ax.plot(df['DateTime'], df['Dew_Predicted'], label='Polynomial Regression Fit', 
       color='#F18F01', linewidth=3, linestyle='--')
ax.set_title('Dew Point - Polynomial Regression Model (R² = 0.5185)', 
            fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Time', fontsize=14, fontweight='bold')
ax.set_ylabel('Dew Point (°C)', fontsize=14, fontweight='bold')
ax.legend(loc='best', fontsize=12, framealpha=0.9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('best_model_dewpoint.png', dpi=300, bbox_inches='tight')
print("  ✓ Dew Point plot saved")
plt.close()

# ============================================================================
# COMBINED PLOT
# ============================================================================
print("\n[STEP 2] Creating combined visualization...")

fig, axes = plt.subplots(4, 1, figsize=(18, 16))

# Temperature
axes[0].plot(df['DateTime'], df[temp_col], label='Actual', 
            color='#2E86AB', linewidth=2.5, marker='o', markersize=2, alpha=0.7)
axes[0].plot(df['DateTime'], df['Temp_Predicted'], label='Model Fit (R²=0.9871)', 
            color='#F18F01', linewidth=3, linestyle='--')
axes[0].set_title('Temperature Forecast', fontsize=15, fontweight='bold')
axes[0].set_ylabel('Temperature (°C)', fontsize=13, fontweight='bold')
axes[0].legend(loc='best', fontsize=11)
axes[0].grid(True, alpha=0.3)

# Humidity
axes[1].plot(df['DateTime'], df[humidity_col], label='Actual', 
            color='#2E86AB', linewidth=2.5, marker='o', markersize=2, alpha=0.7)
axes[1].plot(df['DateTime'], df['Hum_Predicted'], label='Model Fit (R²=0.9518)', 
            color='#F18F01', linewidth=3, linestyle='--')
axes[1].set_title('Humidity Forecast', fontsize=15, fontweight='bold')
axes[1].set_ylabel('Humidity (%)', fontsize=13, fontweight='bold')
axes[1].legend(loc='best', fontsize=11)
axes[1].grid(True, alpha=0.3)

# Pressure
axes[2].plot(df['DateTime'], df[pressure_col], label='Actual', 
            color='#2E86AB', linewidth=2.5, marker='o', markersize=2, alpha=0.7)
axes[2].plot(df['DateTime'], df['Press_Predicted'], label='Model Fit (R²=0.4840)', 
            color='#F18F01', linewidth=3, linestyle='--')
axes[2].set_title('Pressure Forecast', fontsize=15, fontweight='bold')
axes[2].set_ylabel('Pressure (hPa)', fontsize=13, fontweight='bold')
axes[2].legend(loc='best', fontsize=11)
axes[2].grid(True, alpha=0.3)

# Dew Point
axes[3].plot(df['DateTime'], df[dew_col], label='Actual', 
            color='#2E86AB', linewidth=2.5, marker='o', markersize=2, alpha=0.7)
axes[3].plot(df['DateTime'], df['Dew_Predicted'], label='Model Fit (R²=0.5185)', 
            color='#F18F01', linewidth=3, linestyle='--')
axes[3].set_title('Dew Point Forecast', fontsize=15, fontweight='bold')
axes[3].set_ylabel('Dew Point (°C)', fontsize=13, fontweight='bold')
axes[3].set_xlabel('Time', fontsize=13, fontweight='bold')
axes[3].legend(loc='best', fontsize=11)
axes[3].grid(True, alpha=0.3)

plt.suptitle('Polynomial Regression Model - All Parameters', 
            fontsize=18, fontweight='bold', y=0.995)
plt.tight_layout()
plt.savefig('best_model_all_parameters.png', dpi=300, bbox_inches='tight')
print("  ✓ Combined plot saved")
plt.close()

# ============================================================================
# PERFORMANCE BAR CHART
# ============================================================================
print("\n[STEP 3] Creating performance metrics chart...")

perf_df = pd.read_excel('best_model_performance.xlsx')

fig, axes = plt.subplots(1, 3, figsize=(16, 6))
fig.suptitle('Polynomial Regression Model - Performance Metrics', 
            fontsize=16, fontweight='bold')

metrics = ['RMSE', 'MAE', 'R²']
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']

for idx, metric in enumerate(metrics):
    ax = axes[idx]
    params = perf_df['Parameter']
    values = perf_df[metric]
    
    bars = ax.bar(params, values, color=colors[idx], edgecolor='black', 
                 linewidth=2, alpha=0.8)
    ax.set_title(f'{metric}', fontsize=14, fontweight='bold')
    ax.set_ylabel(metric, fontsize=12, fontweight='bold')
    ax.grid(True, alpha=0.3, axis='y')
    ax.tick_params(axis='x', rotation=45)
    
    # Add value labels
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
               f'{height:.4f}', ha='center', va='bottom', 
               fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('best_model_performance_metrics.png', dpi=300, bbox_inches='tight')
print("  ✓ Performance metrics chart saved")
plt.close()

# ============================================================================
# RESIDUAL PLOTS
# ============================================================================
print("\n[STEP 4] Creating residual analysis plots...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Residual Analysis - Model Quality Check', fontsize=16, fontweight='bold')

# Temperature residuals
temp_residuals = df[temp_col] - df['Temp_Predicted']
axes[0, 0].scatter(df['Temp_Predicted'], temp_residuals, alpha=0.6, color='#FF6B6B')
axes[0, 0].axhline(y=0, color='black', linestyle='--', linewidth=2)
axes[0, 0].set_title('Temperature Residuals', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Predicted Values', fontsize=10)
axes[0, 0].set_ylabel('Residuals', fontsize=10)
axes[0, 0].grid(True, alpha=0.3)

# Humidity residuals
hum_residuals = df[humidity_col] - df['Hum_Predicted']
axes[0, 1].scatter(df['Hum_Predicted'], hum_residuals, alpha=0.6, color='#4ECDC4')
axes[0, 1].axhline(y=0, color='black', linestyle='--', linewidth=2)
axes[0, 1].set_title('Humidity Residuals', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('Predicted Values', fontsize=10)
axes[0, 1].set_ylabel('Residuals', fontsize=10)
axes[0, 1].grid(True, alpha=0.3)

# Pressure residuals
press_residuals = df[pressure_col] - df['Press_Predicted']
axes[1, 0].scatter(df['Press_Predicted'], press_residuals, alpha=0.6, color='#95E1D3')
axes[1, 0].axhline(y=0, color='black', linestyle='--', linewidth=2)
axes[1, 0].set_title('Pressure Residuals', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Predicted Values', fontsize=10)
axes[1, 0].set_ylabel('Residuals', fontsize=10)
axes[1, 0].grid(True, alpha=0.3)

# Dew Point residuals
dew_residuals = df[dew_col] - df['Dew_Predicted']
axes[1, 1].scatter(df['Dew_Predicted'], dew_residuals, alpha=0.6, color='#F38181')
axes[1, 1].axhline(y=0, color='black', linestyle='--', linewidth=2)
axes[1, 1].set_title('Dew Point Residuals', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Predicted Values', fontsize=10)
axes[1, 1].set_ylabel('Residuals', fontsize=10)
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('best_model_residual_analysis.png', dpi=300, bbox_inches='tight')
print("  ✓ Residual analysis saved")
plt.close()

print("\n✓ All visualizations completed!")
print("\nGenerated files:")
print("  1. best_model_temperature.png")
print("  2. best_model_humidity.png")
print("  3. best_model_pressure.png")
print("  4. best_model_dewpoint.png")
print("  5. best_model_all_parameters.png")
print("  6. best_model_performance_metrics.png")
print("  7. best_model_residual_analysis.png")
