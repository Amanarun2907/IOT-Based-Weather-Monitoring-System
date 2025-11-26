"""
Improved Combined Complete Project Flowchart
Better spacing and text visibility
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

print("="*80)
print("CREATING IMPROVED COMBINED FLOWCHART")
print("="*80)

# Create larger figure
fig, ax = plt.subplots(figsize=(20, 28))
ax.set_xlim(0, 20)
ax.set_ylim(0, 28)
ax.axis('off')

# Define colors
color_hardware = '#FFB6C1'
color_software = '#87CEEB'
color_data = '#98FB98'
color_analysis = '#FFD700'
color_model = '#DDA0DD'
color_forecast = '#FFA07A'
color_result = '#F0E68C'

# Helper functions
def create_box(ax, x, y, width, height, text, color, fontsize=11):
    box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.2",
                         edgecolor='black', facecolor=color, linewidth=3)
    ax.add_patch(box)
    lines = text.split('\n')
    line_height = height / (len(lines) + 1)
    for i, line in enumerate(lines):
        y_pos = y + height - (i + 1) * line_height
        ax.text(x + width/2, y_pos, line, ha='center', va='center',
               fontsize=fontsize, fontweight='bold')

def create_arrow(ax, x1, y1, x2, y2):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=30, linewidth=3,
                           color='black')
    ax.add_patch(arrow)

# Title
ax.text(10, 27, 'IoT Weather Monitoring System', ha='center', 
       fontsize=22, fontweight='bold')
ax.text(10, 26.3, 'Complete Project Flow', ha='center', 
       fontsize=18, fontweight='bold',
       bbox=dict(boxstyle='round,pad=0.8', facecolor='lightgray', 
                edgecolor='black', linewidth=3))

y_pos = 25

# Phase labels
def create_phase_label(ax, x, y, text, color):
    ax.text(x, y, text, fontsize=14, fontweight='bold', 
           bbox=dict(boxstyle='round,pad=0.5', facecolor=color, 
                    edgecolor='black', linewidth=2.5))

# ============================================================================
# PHASE 1: HARDWARE SETUP
# ============================================================================
create_phase_label(ax, 2, y_pos, 'PHASE 1: HARDWARE', '#FFE4E1')

create_box(ax, 6, y_pos-0.5, 8, 1, 'Assemble Components\nDHT11 + BMP180 + ESP32', 
          color_hardware, 12)
y_pos -= 1.8

create_arrow(ax, 10, y_pos + 1.3, 10, y_pos + 1)

create_box(ax, 5.5, y_pos-0.5, 9, 1.2, 'Connect Sensors\nDHT11 → GPIO 4\nBMP180 → I2C (SDA/SCL)', 
          color_hardware, 12)
y_pos -= 2

create_arrow(ax, 10, y_pos + 1.5, 10, y_pos + 1.2)

create_box(ax, 6.5, y_pos-0.5, 7, 0.9, 'Connect Power Supply\n5V USB/Adapter', 
          color_hardware, 12)
y_pos -= 1.7

create_arrow(ax, 10, y_pos + 1.2, 10, y_pos + 0.9)

# ============================================================================
# PHASE 2: SOFTWARE SETUP
# ============================================================================
create_phase_label(ax, 2, y_pos, 'PHASE 2: SOFTWARE', '#E0F0FF')

create_box(ax, 6, y_pos-0.5, 8, 1, 'Setup Arduino IDE\nInstall ESP32 Support', 
          color_software, 12)
y_pos -= 1.8

create_arrow(ax, 10, y_pos + 1.3, 10, y_pos + 1)

create_box(ax, 5.5, y_pos-0.5, 9, 1.2, 'Install Libraries\nWiFi, WebServer, DHT, BMP085', 
          color_software, 12)
y_pos -= 2

create_arrow(ax, 10, y_pos + 1.5, 10, y_pos + 1.2)

create_box(ax, 6, y_pos-0.5, 8, 1, 'Upload Code to ESP32\nConfigure WiFi', 
          color_software, 12)
y_pos -= 1.8

create_arrow(ax, 10, y_pos + 1.3, 10, y_pos + 1)

create_box(ax, 6.5, y_pos-0.5, 7, 0.9, 'Connect to WiFi\nGet IP Address', 
          color_software, 12)
y_pos -= 1.7

create_arrow(ax, 10, y_pos + 1.2, 10, y_pos + 0.9)

# ============================================================================
# PHASE 3: DATA COLLECTION
# ============================================================================
create_phase_label(ax, 2, y_pos, 'PHASE 3: DATA', '#E8F5E9')

create_box(ax, 6, y_pos-0.5, 8, 1, 'Start Monitoring\nAuto-refresh: 5 seconds', 
          color_data, 12)
y_pos -= 1.8

create_arrow(ax, 10, y_pos + 1.3, 10, y_pos + 1)

create_box(ax, 5, y_pos-0.5, 10, 1.3, 'Read Sensors Every Minute\nTemp, Humidity, Pressure\nCalculate Dew Point', 
          color_data, 12)
y_pos -= 2.1

create_arrow(ax, 10, y_pos + 1.6, 10, y_pos + 1.3)

create_box(ax, 6, y_pos-0.5, 8, 1, 'Collect Data: 9 AM - 2 PM\n300 Entries', 
          color_data, 12)
y_pos -= 1.8

create_arrow(ax, 10, y_pos + 1.3, 10, y_pos + 1)

create_box(ax, 6.5, y_pos-0.5, 7, 0.9, 'Save to Excel File\niot_sensor_readings.xlsx', 
          color_data, 12)
y_pos -= 1.7

create_arrow(ax, 10, y_pos + 1.2, 10, y_pos + 0.9)

# ============================================================================
# PHASE 4: DATA ANALYSIS
# ============================================================================
create_phase_label(ax, 2, y_pos, 'PHASE 4: ANALYSIS', '#FFF8DC')

create_box(ax, 6.5, y_pos-0.5, 7, 0.9, 'Load Data in Python\nPandas DataFrame', 
          color_analysis, 12)
y_pos -= 1.7

create_arrow(ax, 10, y_pos + 1.2, 10, y_pos + 0.9)

create_box(ax, 5.5, y_pos-0.5, 9, 1.2, 'Statistical Analysis\nMean, Std, Correlation', 
          color_analysis, 12)
y_pos -= 2

create_arrow(ax, 10, y_pos + 1.5, 10, y_pos + 1.2)

create_box(ax, 5.5, y_pos-0.5, 9, 1.2, 'Data Preprocessing\nDateTime Index, Sort\nTrain-Test Split', 
          color_analysis, 12)
y_pos -= 2

create_arrow(ax, 10, y_pos + 1.5, 10, y_pos + 1.2)

create_box(ax, 6, y_pos-0.5, 8, 1, 'Create Visualizations\nTime Series, Correlation', 
          color_analysis, 12)
y_pos -= 1.8

create_arrow(ax, 10, y_pos + 1.3, 10, y_pos + 1)

# ============================================================================
# PHASE 5: MODEL TRAINING
# ============================================================================
create_phase_label(ax, 2, y_pos, 'PHASE 5: MODELING', '#E6E6FA')

create_box(ax, 4.5, y_pos-0.5, 11, 1.4, 'Train Polynomial Regression\nDegree 3 for Temp, Humidity, Dew Point\nDegree 2 for Pressure', 
          color_model, 12)
y_pos -= 2.2

create_arrow(ax, 10, y_pos + 1.7, 10, y_pos + 1.4)

create_box(ax, 5.5, y_pos-0.5, 9, 1.2, 'Evaluate Performance\nRMSE, MAE, R² Score', 
          color_model, 12)
y_pos -= 2

create_arrow(ax, 10, y_pos + 1.5, 10, y_pos + 1.2)

create_box(ax, 6, y_pos-0.5, 8, 1, 'Results: R² = 0.98 (Temp)\nR² = 0.95 (Humidity)', 
          color_model, 12)
y_pos -= 1.8

create_arrow(ax, 10, y_pos + 1.3, 10, y_pos + 1)

# ============================================================================
# PHASE 6: FORECASTING
# ============================================================================
create_phase_label(ax, 2, y_pos, 'PHASE 6: FORECAST', '#FFE4E1')

create_box(ax, 6, y_pos-0.5, 8, 1, 'Train on Full Dataset\n300 Entries', 
          color_forecast, 12)
y_pos -= 1.8

create_arrow(ax, 10, y_pos + 1.3, 10, y_pos + 1)

create_box(ax, 5, y_pos-0.5, 10, 1.3, 'Generate Future Forecast\n2:15 PM - 6:15 PM\n240 Predictions', 
          color_forecast, 12)
y_pos -= 2.1

create_arrow(ax, 10, y_pos + 1.6, 10, y_pos + 1.3)

create_box(ax, 6.5, y_pos-0.5, 7, 0.9, 'Save Forecast to Excel', 
          color_forecast, 12)
y_pos -= 1.7

create_arrow(ax, 10, y_pos + 1.2, 10, y_pos + 0.9)

# ============================================================================
# PHASE 7: RESULTS
# ============================================================================
create_phase_label(ax, 2, y_pos, 'PHASE 7: RESULTS', '#E8F5E9')

create_box(ax, 5, y_pos-0.5, 10, 1.3, 'Create All Visualizations\n8 PNG Files + Charts', 
          color_result, 12)
y_pos -= 2.1

create_arrow(ax, 10, y_pos + 1.6, 10, y_pos + 1.3)

create_box(ax, 5.5, y_pos-0.5, 9, 1.2, 'Generate Report\n3 Excel + 8 PNG Files', 
          color_result, 12)
y_pos -= 2

create_arrow(ax, 10, y_pos + 1.5, 10, y_pos + 1.2)

create_box(ax, 6, y_pos-0.5, 8, 1, 'PROJECT COMPLETE\nReady for Presentation', 
          '#90EE90', 13)

# ============================================================================
# LEGEND
# ============================================================================
legend_x = 0.5
legend_y = 10

ax.text(legend_x + 1.8, legend_y + 2, 'LEGEND', fontsize=13, 
       fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', 
                edgecolor='black', linewidth=2.5))

legend_items = [
    ('Hardware', color_hardware),
    ('Software', color_software),
    ('Data', color_data),
    ('Analysis', color_analysis),
    ('Modeling', color_model),
    ('Forecast', color_forecast),
    ('Results', color_result)
]

for i, (label, color) in enumerate(legend_items):
    y = legend_y - i * 0.5
    box = FancyBboxPatch((legend_x, y), 1.5, 0.35, boxstyle="round,pad=0.08",
                         edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(legend_x + 1.8, y + 0.175, label, fontsize=11, va='center', 
           fontweight='bold')

# ============================================================================
# SPECIFICATIONS
# ============================================================================
spec_x = 16
spec_y = 20

ax.text(spec_x + 1.5, spec_y + 2, 'SPECIFICATIONS', fontsize=13, 
       fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', 
                edgecolor='black', linewidth=2.5))

specs = [
    'Hardware:',
    'ESP32 (240 MHz)',
    'DHT11 Sensor',
    'BMP180 Sensor',
    '',
    'Data:',
    '300 historical',
    '240 forecast',
    '1-min intervals',
    '',
    'Model:',
    'Polynomial Reg.',
    'R² = 0.98 (Temp)',
    'R² = 0.95 (Hum)',
    '',
    'Location:',
    'Gurugram',
    '26-11-2025',
    'Winter Season'
]

for i, spec in enumerate(specs):
    fontsize = 11 if spec and not spec.endswith(':') else 12
    fontweight = 'bold' if spec.endswith(':') or not spec else 'normal'
    ax.text(spec_x + 1.5, spec_y - i * 0.35, spec, fontsize=fontsize, 
           ha='center', fontweight=fontweight)

# Project info at bottom
ax.text(10, 0.8, 'IoT Weather Monitoring System - Complete Project Flow', 
       fontsize=14, fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.5', facecolor='lightyellow', 
                edgecolor='black', linewidth=2.5))

ax.text(10, 0.2, 'Hardware + Software + Data Collection + Analysis + Modeling + Forecasting', 
       fontsize=11, ha='center', style='italic')

plt.tight_layout()
plt.savefig('combined_flowchart_improved.png', dpi=300, bbox_inches='tight', 
           facecolor='white')
print("✓ Improved flowchart saved: combined_flowchart_improved.png")

plt.close()
print("\n" + "="*80)
print("IMPROVED FLOWCHART COMPLETED")
print("="*80)
print("\nImprovements:")
print("  ✓ Larger boxes with more spacing")
print("  ✓ Bigger font sizes (11-13pt)")
print("  ✓ Better text positioning")
print("  ✓ No overlapping text")
print("  ✓ Clearer phase labels")
print("  ✓ Thicker lines and borders")
