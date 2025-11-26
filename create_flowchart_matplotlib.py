"""
Generate Methodology Flowchart using Matplotlib
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.lines as mlines

print("="*80)
print("CREATING METHODOLOGY FLOWCHART")
print("="*80)

# Create figure
fig, ax = plt.subplots(figsize=(14, 20))
ax.set_xlim(0, 10)
ax.set_ylim(0, 30)
ax.axis('off')

# Define colors
color_start = '#90EE90'
color_data = '#87CEEB'
color_preprocess = '#FFD700'
color_analysis = '#FFA07A'
color_model = '#DDA0DD'
color_eval = '#F08080'
color_forecast = '#98FB98'

# Helper function to create boxes
def create_box(ax, x, y, width, height, text, color, fontsize=10):
    box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.1",
                         edgecolor='black', facecolor=color, linewidth=2)
    ax.add_patch(box)
    ax.text(x + width/2, y + height/2, text, ha='center', va='center',
           fontsize=fontsize, fontweight='bold', wrap=True)

# Helper function to create arrows
def create_arrow(ax, x1, y1, x2, y2, label=''):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=20, linewidth=2,
                           color='black')
    ax.add_patch(arrow)
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x + 0.3, mid_y, label, fontsize=8, style='italic')

# Title
ax.text(5, 29, 'IoT Weather Monitoring System\nTime Series Analysis Methodology',
       ha='center', fontsize=16, fontweight='bold', bbox=dict(boxstyle='round', facecolor='lightgray'))

# Flow boxes
y_pos = 27

# 1. START
create_box(ax, 3, y_pos, 4, 0.8, 'START', color_start, 11)
y_pos -= 1.2

# Arrow
create_arrow(ax, 5, y_pos + 1.2, 5, y_pos + 0.8)

# 2. Data Collection
create_box(ax, 2, y_pos, 6, 1.2, 'Data Collection\nDHT & BMP Sensors + ESP32\n300 readings (9 AM - 2 PM)', color_data)
y_pos -= 1.6

create_arrow(ax, 5, y_pos + 1.6, 5, y_pos + 1.2)

# 3. Load Data
create_box(ax, 2.5, y_pos, 5, 1, 'Load Excel Data\n6 columns, 300 entries', color_data)
y_pos -= 1.4

create_arrow(ax, 5, y_pos + 1.4, 5, y_pos + 1)

# 4. Statistical Description
create_box(ax, 2, y_pos, 6, 1, 'Statistical Description\nDescriptive stats, Correlation', color_analysis)
y_pos -= 1.4

create_arrow(ax, 5, y_pos + 1.4, 5, y_pos + 1)

# 5. Data Preprocessing
create_box(ax, 2, y_pos, 6, 1, 'Data Preprocessing\nDateTime index, Sort, Extract', color_preprocess)
y_pos -= 1.4

create_arrow(ax, 5, y_pos + 1.4, 5, y_pos + 1)

# 6. EDA
create_box(ax, 2, y_pos, 6, 1, 'Exploratory Data Analysis\nTime series plots, ACF/PACF', color_analysis)
y_pos -= 1.4

create_arrow(ax, 5, y_pos + 1.4, 5, y_pos + 1)

# 7. Stationarity Test
create_box(ax, 2, y_pos, 6, 1, 'Stationarity Testing\nAugmented Dickey-Fuller Test', color_analysis)
y_pos -= 1.4

create_arrow(ax, 5, y_pos + 1.4, 5, y_pos + 1)

# 8. Train-Test Split
create_box(ax, 2, y_pos, 6, 1, 'Train-Test Split\n80% Train / 20% Test', color_preprocess)
y_pos -= 1.4

create_arrow(ax, 5, y_pos + 1.4, 5, y_pos + 1)

# 9. Model Training (4 branches)
create_box(ax, 2.5, y_pos, 5, 0.8, 'Model Training', color_model, 11)
y_pos -= 1.2

# Create 4 branches
branch_y = y_pos
create_arrow(ax, 5, branch_y + 1.2, 1.5, branch_y + 0.8)
create_arrow(ax, 5, branch_y + 1.2, 3.5, branch_y + 0.8)
create_arrow(ax, 5, branch_y + 1.2, 6.5, branch_y + 0.8)
create_arrow(ax, 5, branch_y + 1.2, 8.5, branch_y + 0.8)

# Temperature
create_box(ax, 0.2, branch_y, 2.5, 0.8, 'Temperature\nARIMA, SARIMA, GARCH', color_model, 8)

# Humidity
create_box(ax, 2.8, branch_y, 2.5, 0.8, 'Humidity\nARIMA, SARIMA, GARCH', color_model, 8)

# Pressure
create_box(ax, 5.4, branch_y, 2.5, 0.8, 'Pressure\nARIMA, SARIMA, GARCH', color_model, 8)

# Dew Point
create_box(ax, 8, branch_y, 2, 0.8, 'Dew Point\nARIMA, SARIMA, GARCH', color_model, 8)

y_pos -= 1.2

# Merge arrows back
create_arrow(ax, 1.5, y_pos + 1.2, 5, y_pos + 0.8)
create_arrow(ax, 4, y_pos + 1.2, 5, y_pos + 0.8)
create_arrow(ax, 6.5, y_pos + 1.2, 5, y_pos + 0.8)
create_arrow(ax, 9, y_pos + 1.2, 5, y_pos + 0.8)

# 10. Model Evaluation
create_box(ax, 2, y_pos, 6, 1, 'Model Evaluation\nRMSE, MAE, MAPE, R²', color_eval)
y_pos -= 1.4

create_arrow(ax, 5, y_pos + 1.4, 5, y_pos + 1)

# 11. Model Comparison
create_box(ax, 2, y_pos, 6, 1, 'Model Comparison\nPerformance metrics analysis', color_eval)
y_pos -= 1.4

create_arrow(ax, 5, y_pos + 1.4, 5, y_pos + 1)

# 12. Future Forecasting
create_box(ax, 2, y_pos, 6, 1, 'Future Forecasting\n2:15 PM - 6:15 PM (240 min)', color_forecast)
y_pos -= 1.4

create_arrow(ax, 5, y_pos + 1.4, 5, y_pos + 1)

# 13. Visualization
create_box(ax, 2, y_pos, 6, 1, 'Results Visualization\nCharts, Graphs, Comparisons', color_forecast)
y_pos -= 1.4

create_arrow(ax, 5, y_pos + 1.4, 5, y_pos + 1)

# 14. Report Generation
create_box(ax, 2, y_pos, 6, 1, 'Report Generation\nMetrics, Forecasts, Flowchart', color_forecast)
y_pos -= 1.4

create_arrow(ax, 5, y_pos + 1.4, 5, y_pos + 0.8)

# 15. END
create_box(ax, 3, y_pos, 4, 0.8, 'END\nComplete Analysis', color_start, 11)

# Add legend
legend_y = 1.5
ax.text(0.5, legend_y + 1.5, 'Legend:', fontsize=12, fontweight='bold')
legend_items = [
    ('Data Collection', color_data),
    ('Preprocessing', color_preprocess),
    ('Analysis', color_analysis),
    ('Model Training', color_model),
    ('Evaluation', color_eval),
    ('Results', color_forecast)
]

for i, (label, color) in enumerate(legend_items):
    y = legend_y - i * 0.3
    box = FancyBboxPatch((0.5, y), 1.5, 0.25, boxstyle="round,pad=0.05",
                         edgecolor='black', facecolor=color, linewidth=1)
    ax.add_patch(box)
    ax.text(2.1, y + 0.125, label, fontsize=9, va='center')

plt.tight_layout()
plt.savefig('methodology_flowchart.png', dpi=300, bbox_inches='tight', facecolor='white')
print("✓ Flowchart generated successfully: methodology_flowchart.png")

print("\n" + "="*80)
print("FLOWCHART GENERATION COMPLETED")
print("="*80)
