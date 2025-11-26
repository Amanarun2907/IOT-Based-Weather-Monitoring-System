"""
Software Flow Diagram - WebServer Approach
Code execution flow: setup → read sensors → serve webpage → loop
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

print("="*80)
print("CREATING SOFTWARE FLOW DIAGRAM - WEBSERVER APPROACH")
print("="*80)

# Create figure
fig, ax = plt.subplots(figsize=(14, 18))
ax.set_xlim(0, 14)
ax.set_ylim(0, 18)
ax.axis('off')

# Define colors
color_start = '#90EE90'       # Light green
color_init = '#87CEEB'        # Sky blue
color_wifi = '#FFD700'        # Gold
color_sensor = '#FFB6C1'      # Pink
color_process = '#DDA0DD'     # Plum
color_web = '#FFA07A'         # Light salmon
color_decision = '#F0E68C'    # Khaki
color_loop = '#98FB98'        # Pale green

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

def create_diamond(ax, x, y, width, height, text, color, fontsize=9):
    # Diamond shape for decision
    points = [(x + width/2, y + height), (x + width, y + height/2), 
              (x + width/2, y), (x, y + height/2)]
    diamond = mpatches.Polygon(points, closed=True, edgecolor='black', 
                              facecolor=color, linewidth=2.5)
    ax.add_patch(diamond)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        y_offset = (len(lines) - 1) * 0.1 / 2 - i * 0.1
        ax.text(x + width/2, y + height/2 + y_offset, line, 
               ha='center', va='center', fontsize=fontsize, 
               fontweight='bold')

def create_arrow(ax, x1, y1, x2, y2, label='', color='black'):
    arrow = FancyArrowPatch((x1, y1), (x2, y2),
                           arrowstyle='->', mutation_scale=25, linewidth=2.5,
                           color=color)
    ax.add_patch(arrow)
    if label:
        mid_x, mid_y = (x1 + x2) / 2, (y1 + y2) / 2
        ax.text(mid_x + 0.5, mid_y, label, fontsize=9, style='italic', 
               fontweight='bold',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                        edgecolor='black', linewidth=1.5))

# Title
ax.text(7, 17.3, 'IoT Weather Monitoring System\nSoftware Flow - WebServer Approach',
       ha='center', fontsize=16, fontweight='bold', 
       bbox=dict(boxstyle='round,pad=0.5', facecolor='lightgray', 
                edgecolor='black', linewidth=3))

y_pos = 16.2

# ============================================================================
# START
# ============================================================================
create_box(ax, 5.5, y_pos, 3, 0.7, 'START', color_start, 12)
y_pos -= 1

create_arrow(ax, 7, y_pos + 1, 7, y_pos + 0.7)

# ============================================================================
# SETUP PHASE
# ============================================================================
ax.text(1, y_pos + 0.5, 'SETUP PHASE', fontsize=12, fontweight='bold', 
       style='italic', color='#00008B',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='lightyellow'))

# Initialize Serial
create_box(ax, 4.5, y_pos, 5, 0.6, 'Initialize Serial Communication\nSerial.begin(115200)', 
          color_init, 9)
y_pos -= 0.9

create_arrow(ax, 7, y_pos + 0.9, 7, y_pos + 0.6)

# Initialize DHT
create_box(ax, 4.5, y_pos, 5, 0.6, 'Initialize DHT11 Sensor\ndht.begin()', 
          color_sensor, 9)
y_pos -= 0.9

create_arrow(ax, 7, y_pos + 0.9, 7, y_pos + 0.6)

# Initialize BMP
create_box(ax, 4.5, y_pos, 5, 0.6, 'Initialize BMP180 Sensor\nbmp.begin()', 
          color_sensor, 9)
y_pos -= 0.9

create_arrow(ax, 7, y_pos + 0.9, 7, y_pos + 0.6)

# WiFi Begin
create_box(ax, 4.5, y_pos, 5, 0.7, 'Start WiFi Connection\nWiFi.begin(ssid, password)', 
          color_wifi, 9)
y_pos -= 1

create_arrow(ax, 7, y_pos + 1, 7, y_pos + 0.7)

# WiFi Connection Check (Decision)
create_diamond(ax, 5, y_pos, 4, 0.7, 'WiFi\nConnected?', color_decision, 10)
y_pos -= 1

# No - Wait loop
create_arrow(ax, 9, y_pos + 1.35, 11, y_pos + 1.35, 'No')
create_box(ax, 10.5, y_pos + 1.1, 2, 0.5, 'Wait 500ms\nPrint "."', color_wifi, 8)
create_arrow(ax, 11.5, y_pos + 1.1, 11.5, y_pos + 1.8, '')
create_arrow(ax, 11.5, y_pos + 1.8, 9, y_pos + 1.8, '')

# Yes - Continue
create_arrow(ax, 7, y_pos + 0.7, 7, y_pos + 0.5, 'Yes')

# Print IP Address
create_box(ax, 4.5, y_pos, 5, 0.6, 'Print IP Address\nSerial.println(WiFi.localIP())', 
          color_wifi, 9)
y_pos -= 0.9

create_arrow(ax, 7, y_pos + 0.9, 7, y_pos + 0.6)

# Setup Web Server
create_box(ax, 4.5, y_pos, 5, 0.7, 'Setup Web Server\nserver.on("/", handleRoot)\nserver.begin()', 
          color_web, 9)
y_pos -= 1

create_arrow(ax, 7, y_pos + 1, 7, y_pos + 0.7)

# ============================================================================
# MAIN LOOP
# ============================================================================
ax.text(1, y_pos + 0.5, 'MAIN LOOP', fontsize=12, fontweight='bold', 
       style='italic', color='#8B0000',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='lightcoral'))

# Loop Start
create_box(ax, 5, y_pos, 4, 0.7, 'LOOP START\nserver.handleClient()', 
          color_loop, 10)
y_pos -= 1

create_arrow(ax, 7, y_pos + 1, 7, y_pos + 0.7)

# Check for HTTP Request
create_diamond(ax, 5, y_pos, 4, 0.7, 'HTTP Request\nReceived?', color_decision, 10)
y_pos -= 1

# No - Continue loop
create_arrow(ax, 5, y_pos + 1.35, 3, y_pos + 1.35, 'No')
create_arrow(ax, 3, y_pos + 1.35, 3, y_pos + 2.5, '')
create_arrow(ax, 3, y_pos + 2.5, 5, y_pos + 2.5, '')

# Yes - Handle Request
create_arrow(ax, 7, y_pos + 0.7, 7, y_pos + 0.5, 'Yes')

# ============================================================================
# HANDLE ROOT FUNCTION
# ============================================================================
ax.text(1, y_pos + 0.3, 'handleRoot()', fontsize=11, fontweight='bold', 
       style='italic', color='#006400',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen'))

# Read DHT
create_box(ax, 4.5, y_pos, 5, 0.7, 'Read DHT11 Sensor\nh = dht.readHumidity()\nt = dht.readTemperature()', 
          color_sensor, 9)
y_pos -= 1

create_arrow(ax, 7, y_pos + 1, 7, y_pos + 0.7)

# Read BMP
create_box(ax, 4.5, y_pos, 5, 0.7, 'Read BMP180 Sensor\np = bmp.readPressure() / 100.0', 
          color_sensor, 9)
y_pos -= 1

create_arrow(ax, 7, y_pos + 1, 7, y_pos + 0.7)

# Calculate Gauge Angles
create_box(ax, 4.5, y_pos, 5, 0.8, 'Calculate Gauge Angles\ntempAngle = map(t, 0, 50, -90, 90)\nhumAngle = map(h, 0, 100, -90, 90)\npresAngle = map(p, 900, 1100, -90, 90)', 
          color_process, 8)
y_pos -= 1.1

create_arrow(ax, 7, y_pos + 1.1, 7, y_pos + 0.8)

# Build HTML
create_box(ax, 4.5, y_pos, 5, 0.8, 'Build HTML Page\nCreate gauge visualizations\nAdd CSS styling\nEmbed sensor values', 
          color_web, 9)
y_pos -= 1.1

create_arrow(ax, 7, y_pos + 1.1, 7, y_pos + 0.8)

# Send Response
create_box(ax, 4.5, y_pos, 5, 0.7, 'Send HTTP Response\nserver.send(200, "text/html", html)', 
          color_web, 9)
y_pos -= 1

create_arrow(ax, 7, y_pos + 1, 7, y_pos + 0.7)

# Auto Refresh
create_box(ax, 4.5, y_pos, 5, 0.6, 'Browser Auto-Refresh\n(Every 5 seconds)', 
          color_web, 9)
y_pos -= 0.9

create_arrow(ax, 7, y_pos + 0.9, 7, y_pos + 0.6)

# Return to Loop
create_box(ax, 5, y_pos, 4, 0.6, 'Return to Loop', color_loop, 10)

# Loop back arrow
create_arrow(ax, 7, y_pos, 7, y_pos - 0.5, '')
create_arrow(ax, 7, y_pos - 0.5, 11, y_pos - 0.5, '')
create_arrow(ax, 11, y_pos - 0.5, 11, y_pos + 9, '')
create_arrow(ax, 11, y_pos + 9, 9, y_pos + 9, '')

# ============================================================================
# LEGEND
# ============================================================================
legend_x = 0.3
legend_y = 3

ax.text(legend_x + 1.2, legend_y + 1.5, 'LEGEND', fontsize=11, 
       fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgray', 
                edgecolor='black', linewidth=2))

legend_items = [
    ('Start/End', color_start),
    ('Initialization', color_init),
    ('WiFi Setup', color_wifi),
    ('Sensor Reading', color_sensor),
    ('Data Processing', color_process),
    ('Web Server', color_web),
    ('Decision', color_decision),
    ('Loop', color_loop)
]

for i, (label, color) in enumerate(legend_items):
    y = legend_y - i * 0.35
    box = FancyBboxPatch((legend_x, y), 0.9, 0.25, boxstyle="round,pad=0.05",
                         edgecolor='black', facecolor=color, linewidth=1.5)
    ax.add_patch(box)
    ax.text(legend_x + 1.2, y + 0.125, label, fontsize=9, va='center', 
           fontweight='bold')

# Add key features box
feature_x = 11.5
feature_y = 3
ax.text(feature_x + 1, feature_y + 1.5, 'KEY FEATURES', fontsize=11, 
       fontweight='bold', ha='center',
       bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgray', 
                edgecolor='black', linewidth=2))

features = [
    '✓ Real-time monitoring',
    '✓ Auto-refresh (5s)',
    '✓ Gauge visualization',
    '✓ Local network access',
    '✓ No internet required',
    '✓ Responsive design'
]

for i, feature in enumerate(features):
    ax.text(feature_x + 1, feature_y - i * 0.35, feature, fontsize=8, ha='center',
           bbox=dict(boxstyle='round,pad=0.2', facecolor='lightyellow', 
                    edgecolor='gray', linewidth=1))

plt.tight_layout()
plt.savefig('software_flow_webserver.png', dpi=300, bbox_inches='tight', 
           facecolor='white')
print("✓ Software Flow (WebServer) saved: software_flow_webserver.png")

plt.close()
print("\n" + "="*80)
print("SOFTWARE FLOW DIAGRAM - WEBSERVER COMPLETED")
print("="*80)
