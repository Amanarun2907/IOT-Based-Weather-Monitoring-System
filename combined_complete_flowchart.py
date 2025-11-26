"""
Combined Complete Project Flowchart
Hardware Setup → Software Setup → Data Collection → Time Series Analysis → Forecasting
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

print("="*80)
print("CREATING COMBINED COMPLETE PROJECT FLOWCHART")
print("="*80)

# Create figure
fig, ax = plt.subplots(figsize=(18, 24))
ax.set_xlim(0, 18)
ax.set_ylim(0, 24)
ax.axis('off')

# Define colors
color_hardware = '#FFB6C1'    # Pink - Hardware
color_software = '#87CEEB'    # Sky blue - Software
color_data = '#98FB98'        # Pale green - Data
color_analysis = '#FFD700'    # Gold - Analysis
color_model = '#DDA0DD'       # Plum - Models
color_forecast = '#FFA07A'    # Salmon - Forecast
color_result = '#F0E68C'      # Khaki - Results

# Helper functions
def create_box(ax, x, y, width, height, text, color, fontsize=10):
    box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.15",
                         edgecolor='black', facecolor=color, linewidth=2.5)
    ax.add_patch(box)
    lines = text.split('\n')
    if len(lines) > 1:
        for i, line in enumerate(lines):
            y_offset = (len(lines) - 1) * 0.12 / 2 - i * 0.12
            ax.text(x + width/2, y + height/2 + y_offset, line, 
                   ha='center', va='center', fontsize=fontsize, 
                   fontweight='bold', wrap=True)
    else:
        ax.text(x + width/2, y + height/2, text, ha='center', va='center',
               fontsize=fontsize, fontweight='bold', wrap=True)

def create_arrow(ax, x1, y1, x2, y2, label='', color='black', width=2.5):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=25, linewidth=width,
                           color=color)
    ax.add_patch(arrow)
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x + 0.5, mid_y, label, fontsize=9, style='italic', 
               fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                        edgecolor='black', linewidth=1.5))

# Title
ax.text(9, 23.3, 'IoT Weather Monitoring System\nComplete Project Flow',
       ha='center', fontsize=18, fontweight='bold', 
       bbox=dict(boxstyle='round,pad=0.6', facecolor='lightgray', 
                edgecolor='black', linewidth=3))

y_pos = 22.2

# ============================================================================
# PHASE 1: HARDWARE SETUP
# ============================================================================
ax.text(2, y_pos + 0.3, 'PHASE 1: HARDWARE SETUP', fontsize=13, fontweight='bold', 
       style='italic', color='#8B0000',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFE4E1', 
                edgecolor='#8B0000', linewidth=2))

# Hardware components
create_box(ax, 6, y_pos, 6, 0.8, 'Assemble Hardware Components\nDHT11 + BMP180 + ESP32', 
          color_hardware, 11)
y_pos -= 1

create_arrow(ax, 9, y_pos + 1, 9, y_pos + 0.8)

# Connect sensors
create_box(ax, 5.5, y_pos, 7, 0.9, 'Connect Sensors to ESP32\nDHT11 → GPIO 4 (Digital)\nBMP180 → I2C (SDA/SCL)', 
          color_hardware, 10)
y_pos -= 1.1

create_arrow(ax, 9, y_pos + 1.1, 9, y_pos + 0.9)

# Power supply
create_box(ax, 6.5, y_pos, 5, 0.7, 'Connect 5V Power Supply\n(USB/Adapter)', 
          color_hardware, 10)
y_pos -= 0.9

create_arrow(ax, 9, y_pos + 0.9, 9, y_pos + 0.7)

# ============================================================================
# PHASE 2: SOFTWARE SETUP
# ============================================================================
ax.text(2, y_pos + 0.3, 'PHASE 2: SOFTWARE SETUP', fontsize=13, fontweight='bold', 
       style='italic', color='#00008B',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#E0F0FF', 
                edgecolor='#00008B', linewidth=2))

# Arduino IDE setup
create_box(ax, 6, y_pos, 6, 0.8, 'Setup Arduino IDE\nInstall ESP32 Board Support', 
          color_software, 10)
y_pos -= 1

create_arrow(ax, 9, y_pos + 1, 9, y_pos + 0.8)

# Install libraries
create_box(ax, 5.5, y_pos, 7, 0.9, 'Install Required Libraries\nWiFi.h, WebServer.h\nDHT.h, Adafruit_BMP085.h', 
          color_software, 10)
y_pos -= 1.1

create_arrow(ax, 9, y_pos + 1.1, 9, y_pos + 0.9)

# Upload code
create_box(ax, 6, y_pos, 6, 0.8, 'Upload Arduino Code to ESP32\nConfigure WiFi (Students/0123456789)', 
          color_software, 10)
y_pos -= 1

create_arrow(ax, 9, y_pos + 1, 9, y_pos + 0.8)

# Initialize system
create_box(ax, 5.5, y_pos, 7, 0.9, 'Initialize System\nSerial: 115200 baud\nSensors: DHT11, BMP180\nWebServer: Port 80', 
          color_software, 10)
y_pos -= 1.1

create_arrow(ax, 9, y_pos + 1.1, 9, y_pos + 0.9)

# WiFi connection
create_box(ax, 6.5, y_pos, 5, 0.7, 'Connect to WiFi Network\nGet IP Address', 
          color_software, 10)
y_pos -= 0.9

create_arrow(ax, 9, y_pos + 0.9, 9, y_pos + 0.7)

# ============================================================================
# PHASE 3: DATA COLLECTION
# ============================================================================
ax.text(2, y_pos + 0.3, 'PHASE 3: DATA COLLECTION', fontsize=13, fontweight='bold', 
       style='italic', color='#006400',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#E8F5E9', 
                edgecolor='#006400', linewidth=2))

# Start monitoring
create_box(ax, 6, y_pos, 6, 0.8, 'Start Real-Time Monitoring\nAuto-refresh: 5 seconds', 
          color_data, 10)
y_pos -= 1

create_arrow(ax, 9, y_pos + 1, 9, y_pos + 0.8)

# Read sensors
create_box(ax, 5, y_pos, 8, 1, 'Read Sensor Data Every Minute\nTemperature (°C) - DHT11\nHumidity (%) - DHT11\nPressure (hPa) - BMP180\nCalculate Dew Point (Magnus Formula)', 
          color_data, 10)
y_pos -= 1.2

create_arrow(ax, 9, y_pos + 1.2, 9, y_pos + 1)

# Collect data
create_box(ax, 6, y_pos, 6, 0.8, 'Collect Data: 9 AM - 2 PM\n300 Entries (1-minute intervals)', 
          color_data, 10)
y_pos -= 1

create_arrow(ax, 9, y_pos + 1, 9, y_pos + 0.8)

# Display on web
create_box(ax, 5.5, y_pos, 7, 0.8, 'Display on Web Dashboard\nGauge Visualizations\nLocal Network Access', 
          color_data, 10)
y_pos -= 1

create_arrow(ax, 9, y_pos + 1, 9, y_pos + 0.8)

# Save to Excel
create_box(ax, 6.5, y_pos, 5, 0.7, 'Save Data to Excel\niot_sensor_readings.xlsx', 
          color_data, 10)
y_pos -= 0.9

create_arrow(ax, 9, y_pos + 0.9, 9, y_pos + 0.7)

# ============================================================================
# PHASE 4: DATA ANALYSIS
# ============================================================================
ax.text(2, y_pos + 0.3, 'PHASE 4: DATA ANALYSIS', fontsize=13, fontweight='bold', 
       style='italic', color='#8B4513',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFF8DC', 
                edgecolor='#8B4513', linewidth=2))

# Load data
create_box(ax, 6.5, y_pos, 5, 0.7, 'Load Data in Python\nPandas DataFrame', 
          color_analysis, 10)
y_pos -= 0.9

create_arrow(ax, 9, y_pos + 0.9, 9, y_pos + 0.7)

# Statistical analysis
create_box(ax, 5.5, y_pos, 7, 0.9, 'Statistical Description\nMean, Std, Min, Max\nCorrelation Matrix\nMissing Values Check', 
          color_analysis, 10)
y_pos -= 1.1

create_arrow(ax, 9, y_pos + 1.1, 9, y_pos + 0.9)

# Preprocessing
create_box(ax, 5.5, y_pos, 7, 0.9, 'Data Preprocessing\nDateTime Indexing\nSort by Time\nTrain-Test Split (80-20)', 
          color_analysis, 10)
y_pos -= 1.1

create_arrow(ax, 9, y_pos + 1.1, 9, y_pos + 0.9)

# Stationarity test
create_box(ax, 6, y_pos, 6, 0.8, 'Stationarity Testing\nAugmented Dickey-Fuller Test\nACF/PACF Analysis', 
          color_analysis, 10)
y_pos -= 1

create_arrow(ax, 9, y_pos + 1, 9, y_pos + 0.8)

# Visualizations
create_box(ax, 5.5, y_pos, 7, 0.8, 'Create Visualizations\nTime Series Plots\nCorrelation Heatmap\nACF/PACF Plots', 
          color_analysis, 10)
y_pos -= 1

create_arrow(ax, 9, y_pos + 1, 9, y_pos + 0.8)

# ============================================================================
# PHASE 5: MODEL TRAINING
# ============================================================================
ax.text(2, y_pos + 0.3, 'PHASE 5: MODEL TRAINING', fontsize=13, fontweight='bold', 
       style='italic', color='#4B0082',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#E6E6FA', 
                edgecolor='#4B0082', linewidth=2))

# Train models
create_box(ax, 4.5, y_pos, 9, 1.1, 'Train Time Series Models\nARIMA (2,1,2) - AutoRegressive Integrated Moving Average\nSARIMA (1,1,1)(1,1,1,12) - Seasonal ARIMA\nGARCH (1,1) - Volatility Modeling\nFor: Temperature, Humidity, Pressure, Dew Point', 
          color_model, 10)
y_pos -= 1.3

create_arrow(ax, 9, y_pos + 1.3, 9, y_pos + 1.1)

# Model evaluation
create_box(ax, 5.5, y_pos, 7, 0.9, 'Evaluate Model Performance\nRMSE, MAE, MAPE, R²\nCompare 12 Models (3×4)', 
          color_model, 10)
y_pos -= 1.1

create_arrow(ax, 9, y_pos + 1.1, 9, y_pos + 0.9)

# Select best models
create_box(ax, 6, y_pos, 6, 0.8, 'Select Best Models\nLowest RMSE & MAE\nHighest R² Score', 
          color_model, 10)
y_pos -= 1

create_arrow(ax, 9, y_pos + 1, 9, y_pos + 0.8)

# Save metrics
create_box(ax, 6.5, y_pos, 5, 0.7, 'Save Performance Metrics\nmodel_performance_metrics.xlsx', 
          color_model, 10)
y_pos -= 0.9

create_arrow(ax, 9, y_pos + 0.9, 9, y_pos + 0.7)

# ============================================================================
# PHASE 6: FORECASTING
# ============================================================================
ax.text(2, y_pos + 0.3, 'PHASE 6: FORECASTING', fontsize=13, fontweight='bold', 
       style='italic', color='#8B0000',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#FFE4E1', 
                edgecolor='#8B0000', linewidth=2))

# Train on full data
create_box(ax, 6, y_pos, 6, 0.8, 'Train on Complete Dataset\n300 Entries (9 AM - 2 PM)', 
          color_forecast, 10)
y_pos -= 1

create_arrow(ax, 9, y_pos + 1, 9, y_pos + 0.8)

# Generate forecast
create_box(ax, 5, y_pos, 8, 1, 'Generate Future Forecast\n2:15 PM - 6:15 PM (4 hours)\n240 Predictions (1-minute intervals)\nAll 4 Parameters', 
          color_forecast, 10)
y_pos -= 1.2

create_arrow(ax, 9, y_pos + 1.2, 9, y_pos + 1)

# Validate forecast
create_box(ax, 6, y_pos, 6, 0.8, 'Validate Forecast Ranges\nTemperature: 20-22°C\nHumidity: 43-44%\nPressure: 1018 hPa', 
          color_forecast, 10)
y_pos -= 1

create_arrow(ax, 9, y_pos + 1, 9, y_pos + 0.8)

# Save forecast
create_box(ax, 6.5, y_pos, 5, 0.7, 'Save Future Forecast\nfuture_forecast_2pm_to_6pm.xlsx', 
          color_forecast, 10)
y_pos -= 0.9

create_arrow(ax, 9, y_pos + 0.9, 9, y_pos + 0.7)

# ============================================================================
# PHASE 7: RESULTS & VISUALIZATION
# ============================================================================
ax.text(2, y_pos + 0.3, 'PHASE 7: RESULTS', fontsize=13, fontweight='bold', 
       style='italic', color='#006400',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='#E8F5E9', 
                edgecolor='#006400', linewidth=2))

# Create visualizations
create_box(ax, 5, y_pos, 8, 1, 'Create All Visualizations\nModel Comparison Charts (4)\nPerformance Bar Charts (4)\nFuture Forecast Graphs\nMethodology Flowchart', 
          color_result, 10)
y_pos -= 1.2

create_arrow(ax, 9, y_pos + 1.2, 9, y_pos + 1)

# Generate report
create_box(ax, 5.5, y_pos, 7, 0.9, 'Generate Complete Report\n3 Excel Files\n16 PNG Visualizations\n4 Documentation Files', 
          color_result, 10)
y_pos -= 1.1

create_arrow(ax, 9, y_pos + 1.1, 9, y_pos + 0.9)

# Final output
create_box(ax, 6, y_pos, 6, 0.8, 'PROJECT COMPLETE\nReady for Presentation', 
          '#90EE90', 12)

# ============================================================================
# LEGEND
# ============================================================================
legend_x = 0.3
legend_y = 8

ax.text(legend_x + 1.5, legend_y + 1.8, 'PROJECT PHASES', fontsize=12, 
       fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='lightgray', 
                edgecolor='black', linewidth=2))

legend_items = [
    ('Hardware Setup', color_hardware),
    ('Software Setup', color_software),
    ('Data Collection', color_data),
    ('Data Analysis', color_analysis),
    ('Model Training', color_model),
    ('Forecasting', color_forecast),
    ('Results', color_result)
]

for i, (label, color) in enumerate(legend_items):
    y = legend_y - i * 0.35
    box = FancyBboxPatch((legend_x, y), 1.2, 0.25, boxstyle="round,pad=0.05",
                         edgecolor='black', facecolor=color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(legend_x + 1.5, y + 0.125, label, fontsize=9, va='center', 
           fontweight='bold')

# ============================================================================
# KEY SPECIFICATIONS
# ============================================================================
spec_x = 14.5
spec_y = 18

ax.text(spec_x + 1.5, spec_y + 1.8, 'KEY SPECIFICATIONS', fontsize=11, 
       fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='lightgray', 
                edgecolor='black', linewidth=2))

specs = [
    'Hardware:',
    '• ESP32 (240 MHz)',
    '• DHT11 (Temp/Humidity)',
    '• BMP180 (Pressure)',
    '',
    'Data:',
    '• 300 historical entries',
    '• 240 forecast entries',
    '• 1-minute intervals',
    '',
    'Models:',
    '• ARIMA (2,1,2)',
    '• SARIMA (1,1,1)(1,1,1,12)',
    '• GARCH (1,1)',
    '',
    'Metrics:',
    '• RMSE, MAE',
    '• MAPE, R²',
    '',
    'Location:',
    '• Gurugram, Haryana',
    '• Date: 26-11-2025',
    '• Season: Winter'
]

for i, spec in enumerate(specs):
    fontsize = 9 if spec.startswith('•') else 10
    fontweight = 'normal' if spec.startswith('•') else 'bold'
    ax.text(spec_x + 1.5, spec_y - i * 0.28, spec, fontsize=fontsize, 
           ha='center', fontweight=fontweight)

# ============================================================================
# PROJECT TIMELINE
# ============================================================================
time_x = 14.5
time_y = 8

ax.text(time_x + 1.5, time_y + 1.8, 'PROJECT TIMELINE', fontsize=11, 
       fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='lightgray', 
                edgecolor='black', linewidth=2))

timeline = [
    'Phase 1: 30 min',
    'Phase 2: 20 min',
    'Phase 3: 5 hours',
    'Phase 4: 1 hour',
    'Phase 5: 2 hours',
    'Phase 6: 30 min',
    'Phase 7: 1 hour',
    '',
    'Total: ~10 hours',
    '',
    'Data Period:',
    '9 AM - 6:15 PM',
    '(9.25 hours)'
]

for i, item in enumerate(timeline):
    fontsize = 10 if item.startswith('Total') or item.startswith('Data') else 9
    fontweight = 'bold' if item.startswith('Total') or item.startswith('Data') else 'normal'
    ax.text(time_x + 1.5, time_y - i * 0.32, item, fontsize=fontsize, 
           ha='center', fontweight=fontweight)

# Add project info box at bottom
info_x = 4
info_y = 0.5
ax.text(info_x + 5, info_y + 0.8, 'IoT Weather Monitoring System - Complete Project Flow', 
       fontsize=12, fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.4', facecolor='lightyellow', 
                edgecolor='black', linewidth=2))

info_text = 'Hardware: DHT11 + BMP180 + ESP32  |  Software: Arduino IDE + Python  |  Analysis: ARIMA, SARIMA, GARCH  |  Output: 3 Excel + 16 PNG'
ax.text(info_x + 5, info_y + 0.2, info_text, fontsize=8, ha='center', style='italic')

plt.tight_layout()
plt.savefig('combined_complete_flowchart.png', dpi=300, bbox_inches='tight', 
           facecolor='white')
print("✓ Combined Complete Flowchart saved: combined_complete_flowchart.png")

plt.close()
print("\n" + "="*80)
print("COMBINED COMPLETE FLOWCHART COMPLETED")
print("="*80)
print("\nThis flowchart includes:")
print("  ✓ Phase 1: Hardware Setup (DHT11, BMP180, ESP32)")
print("  ✓ Phase 2: Software Setup (Arduino IDE, Libraries, WiFi)")
print("  ✓ Phase 3: Data Collection (300 entries, 9 AM - 2 PM)")
print("  ✓ Phase 4: Data Analysis (Statistics, Preprocessing, Visualization)")
print("  ✓ Phase 5: Model Training (ARIMA, SARIMA, GARCH)")
print("  ✓ Phase 6: Forecasting (240 predictions, 2:15 PM - 6:15 PM)")
print("  ✓ Phase 7: Results & Visualization (Reports, Charts)")
print("\nAll phases are color-coded and clearly labeled!")
