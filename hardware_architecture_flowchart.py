"""
Hardware Architecture Flowchart
Physical connections: Sensors → ESP32 → WiFi → Display
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import matplotlib.lines as mlines

print("="*80)
print("CREATING HARDWARE ARCHITECTURE FLOWCHART")
print("="*80)

# Create figure
fig, ax = plt.subplots(figsize=(16, 12))
ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
ax.axis('off')

# Define colors
color_sensor = '#FFB6C1'      # Light pink for sensors
color_esp32 = '#87CEEB'       # Sky blue for ESP32
color_wifi = '#98FB98'        # Pale green for WiFi
color_display = '#FFD700'     # Gold for display
color_power = '#FFA07A'       # Light salmon for power
color_connection = '#333333'  # Dark gray for connections

# Helper function to create boxes
def create_box(ax, x, y, width, height, text, color, fontsize=11, shape='round'):
    if shape == 'round':
        box = FancyBboxPatch((x, y), width, height, boxstyle="round,pad=0.15",
                             edgecolor='black', facecolor=color, linewidth=2.5)
    else:
        box = Rectangle((x, y), width, height,
                       edgecolor='black', facecolor=color, linewidth=2.5)
    ax.add_patch(box)
    
    # Handle multi-line text
    lines = text.split('\n')
    if len(lines) > 1:
        for i, line in enumerate(lines):
            y_offset = (len(lines) - 1) * 0.15 / 2 - i * 0.15
            ax.text(x + width/2, y + height/2 + y_offset, line, 
                   ha='center', va='center', fontsize=fontsize, 
                   fontweight='bold', wrap=True)
    else:
        ax.text(x + width/2, y + height/2, text, ha='center', va='center',
               fontsize=fontsize, fontweight='bold', wrap=True)

# Helper function to create arrows with labels
def create_arrow(ax, x1, y1, x2, y2, label='', color='black', style='->', width=2.5):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle=style, mutation_scale=25, linewidth=width,
                           color=color)
    ax.add_patch(arrow)
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        # Add white background for label
        ax.text(mid_x, mid_y, label, fontsize=9, style='italic', 
               fontweight='bold', ha='center',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                        edgecolor='black', linewidth=1.5))

# Title
ax.text(8, 11.3, 'IoT Weather Monitoring System\nHardware Architecture',
       ha='center', fontsize=18, fontweight='bold', 
       bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', 
                edgecolor='black', linewidth=3))

# ============================================================================
# LAYER 1: SENSORS (Top)
# ============================================================================
ax.text(8, 9.8, 'SENSOR LAYER', ha='center', fontsize=14, 
       fontweight='bold', style='italic', color='#8B0000')

# DHT11 Sensor
create_box(ax, 1, 8.5, 2.5, 1.2, 'DHT11 Sensor\n(Temperature\n& Humidity)', 
          color_sensor, 10)
ax.text(2.25, 7.9, 'Digital Output', ha='center', fontsize=8, style='italic')

# BMP180/085 Sensor
create_box(ax, 5.5, 8.5, 2.5, 1.2, 'BMP180/085\nSensor\n(Pressure)', 
          color_sensor, 10)
ax.text(6.75, 7.9, 'I2C Protocol', ha='center', fontsize=8, style='italic')

# Power Supply (right side)
create_box(ax, 12.5, 8.5, 2.5, 1.2, '5V Power\nSupply\n(USB/Adapter)', 
          color_power, 10)

# ============================================================================
# LAYER 2: MICROCONTROLLER (Middle)
# ============================================================================
ax.text(8, 6.8, 'PROCESSING LAYER', ha='center', fontsize=14, 
       fontweight='bold', style='italic', color='#00008B')

# ESP32 (Main component)
create_box(ax, 4.5, 5, 7, 1.5, 'ESP32 Microcontroller\n(WiFi + Bluetooth Enabled)\nDual-Core Processor', 
          color_esp32, 12)

# Pin labels
ax.text(4.2, 5.75, 'GPIO 4', ha='right', fontsize=9, fontweight='bold',
       bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow'))
ax.text(4.2, 5.3, 'I2C (SDA/SCL)', ha='right', fontsize=9, fontweight='bold',
       bbox=dict(boxstyle='round,pad=0.2', facecolor='yellow'))
ax.text(11.8, 5.75, '5V/3.3V', ha='left', fontsize=9, fontweight='bold',
       bbox=dict(boxstyle='round,pad=0.2', facecolor='orange'))

# ============================================================================
# CONNECTIONS: Sensors to ESP32
# ============================================================================
# DHT11 to ESP32
create_arrow(ax, 2.25, 8.5, 5.5, 6.5, 'GPIO 4\n(Digital)', '#FF1493', '<->', 3)

# BMP to ESP32
create_arrow(ax, 6.75, 8.5, 7, 6.5, 'I2C Bus\n(SDA/SCL)', '#4169E1', '<->', 3)

# Power to ESP32
create_arrow(ax, 13.75, 8.5, 11.5, 6.3, '5V Power', '#FF4500', '->', 3)

# ============================================================================
# LAYER 3: CONNECTIVITY (Lower Middle)
# ============================================================================
ax.text(8, 3.8, 'CONNECTIVITY LAYER', ha='center', fontsize=14, 
       fontweight='bold', style='italic', color='#006400')

# WiFi Router
create_box(ax, 6, 2.5, 4, 1.2, 'WiFi Router\n(Students Network)', 
          color_wifi, 11)
ax.text(8, 1.9, 'SSID: Students\nPassword: 0123456789', 
       ha='center', fontsize=8, style='italic')

# Connection ESP32 to WiFi
create_arrow(ax, 8, 5, 8, 3.7, 'WiFi\nConnection\n(2.4 GHz)', '#228B22', '<->', 3)

# ============================================================================
# LAYER 4: DISPLAY/OUTPUT (Bottom)
# ============================================================================
ax.text(8, 1.3, 'DISPLAY LAYER', ha='center', fontsize=14, 
       fontweight='bold', style='italic', color='#8B4513')

# WebServer Display
create_box(ax, 0.5, 0.1, 4.5, 0.9, 'Web Browser\n(Local Network)', 
          color_display, 10)
ax.text(2.75, -0.4, 'http://192.168.x.x', ha='center', fontsize=8, 
       style='italic', fontweight='bold')

# Blynk Display
create_box(ax, 11, 0.1, 4.5, 0.9, 'Blynk App\n(Cloud/Mobile)', 
          color_display, 10)
ax.text(13.25, -0.4, 'Blynk Cloud Server', ha='center', fontsize=8, 
       style='italic', fontweight='bold')

# Connections to displays
create_arrow(ax, 4, 2.5, 2.75, 1, 'HTTP\nRequest', '#DAA520', '<->', 2.5)
create_arrow(ax, 12, 2.5, 13.25, 1, 'MQTT/HTTP\nAPI', '#DAA520', '<->', 2.5)

# ============================================================================
# LEGEND
# ============================================================================
legend_x = 0.3
legend_y = 5.5

ax.text(legend_x + 1, legend_y + 1.2, 'LEGEND', fontsize=12, 
       fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgray', 
                edgecolor='black', linewidth=2))

legend_items = [
    ('Sensors', color_sensor),
    ('Microcontroller', color_esp32),
    ('Network', color_wifi),
    ('Display', color_display),
    ('Power', color_power)
]

for i, (label, color) in enumerate(legend_items):
    y = legend_y - i * 0.35
    box = FancyBboxPatch((legend_x, y), 0.8, 0.25, boxstyle="round,pad=0.05",
                         edgecolor='black', facecolor=color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(legend_x + 1, y + 0.125, label, fontsize=9, va='center', 
           fontweight='bold')

# Add data flow indicators
ax.text(legend_x + 1, legend_y - 2, 'DATA FLOW', fontsize=10, 
       fontweight='bold', ha='center')
arrow1 = FancyArrowPatch((legend_x, legend_y - 2.3), (legend_x + 0.6, legend_y - 2.3),
                        arrowstyle='<->', mutation_scale=15, linewidth=2, color='red')
ax.add_patch(arrow1)
ax.text(legend_x + 1, legend_y - 2.5, 'Bidirectional', fontsize=8, ha='center')

arrow2 = FancyArrowPatch((legend_x, legend_y - 2.8), (legend_x + 0.6, legend_y - 2.8),
                        arrowstyle='->', mutation_scale=15, linewidth=2, color='blue')
ax.add_patch(arrow2)
ax.text(legend_x + 1, legend_y - 3, 'Unidirectional', fontsize=8, ha='center')

# Add specifications box
spec_x = 14
spec_y = 5.5
ax.text(spec_x + 0.9, spec_y + 1.2, 'SPECIFICATIONS', fontsize=11, 
       fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgray', 
                edgecolor='black', linewidth=2))

specs = [
    'DHT11: ±2°C, ±5% RH',
    'BMP: ±0.5 hPa',
    'ESP32: 240 MHz',
    'WiFi: 802.11 b/g/n',
    'Update: 5 seconds'
]

for i, spec in enumerate(specs):
    ax.text(spec_x + 0.9, spec_y - i * 0.3, spec, fontsize=8, ha='center',
           bbox=dict(boxstyle='round,pad=0.2', facecolor='lightyellow', 
                    edgecolor='gray', linewidth=1))

plt.tight_layout()
plt.savefig('hardware_architecture_flowchart.png', dpi=300, bbox_inches='tight', 
           facecolor='white')
print("✓ Hardware Architecture Flowchart saved: hardware_architecture_flowchart.png")

plt.close()
print("\n" + "="*80)
print("HARDWARE ARCHITECTURE FLOWCHART COMPLETED")
print("="*80)
