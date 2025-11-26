# IoT Weather Monitoring System - Hardware Flowcharts

## 📊 Generated Flowcharts

### 1. Hardware Architecture Flowchart
**File:** `hardware_architecture_flowchart.png`

**Description:** Complete physical architecture showing:
- **Sensor Layer:** DHT11 (Temperature & Humidity) + BMP180/085 (Pressure)
- **Processing Layer:** ESP32 Microcontroller with WiFi
- **Connectivity Layer:** WiFi Router (Students Network)
- **Display Layer:** Web Browser (Local) + Blynk App (Cloud)
- **Power Supply:** 5V USB/Adapter

**Key Components:**
- DHT11 → GPIO 4 (Digital)
- BMP180 → I2C Bus (SDA/SCL)
- ESP32 → WiFi 2.4 GHz
- WebServer → HTTP (Local Network)
- Blynk → MQTT/HTTP API (Cloud)

**Color Coding:**
- 🌸 Pink: Sensors
- 🔵 Blue: Microcontroller
- 🟢 Green: Network/WiFi
- 🟡 Gold: Display/Output
- 🟠 Orange: Power Supply

---

### 2. Software Flow - WebServer Approach
**File:** `software_flow_webserver.png`

**Description:** Complete code execution flow for your current Arduino implementation

**Flow Stages:**

#### SETUP PHASE
1. Initialize Serial Communication (115200 baud)
2. Initialize DHT11 Sensor
3. Initialize BMP180 Sensor
4. Connect to WiFi (Students network)
5. Wait for connection (print dots)
6. Print IP Address
7. Setup Web Server routes
8. Start server

#### MAIN LOOP
1. Handle client requests (`server.handleClient()`)
2. Check for HTTP requests
3. If request received → Execute `handleRoot()`

#### handleRoot() FUNCTION
1. Read DHT11 (temperature & humidity)
2. Read BMP180 (pressure)
3. Calculate gauge angles using `map()` function
4. Build HTML page with CSS styling
5. Create gauge visualizations
6. Send HTTP response (200 OK)
7. Browser auto-refreshes every 5 seconds

**Key Features:**
- ✓ Real-time monitoring
- ✓ Auto-refresh (5 seconds)
- ✓ Gauge visualization
- ✓ Local network access
- ✓ No internet required
- ✓ Responsive design

---

### 3. Software Flow - Blynk Approach
**File:** `software_flow_blynk.png`

**Description:** Alternative implementation using Blynk IoT platform

**Flow Stages:**

#### SETUP PHASE
1. Initialize Serial Communication
2. Initialize DHT11 Sensor
3. Initialize BMP180 Sensor
4. Initialize Blynk with auth token
5. Connect to Blynk Cloud
6. Setup timer (1 second interval)

#### MAIN LOOP
1. Run Blynk connection (`Blynk.run()`)
2. Run timer (`timer.run()`)
3. Check if timer triggered (every 1 second)

#### sendSensorData() FUNCTION
1. Read DHT11 (temperature & humidity)
2. Read BMP180 (pressure)
3. Validate sensor data
4. Send to Blynk Virtual Pins:
   - V0 → Temperature
   - V1 → Humidity
   - V2 → Pressure
5. Blynk Cloud processes data
6. Update app widgets (gauges, graphs, values)
7. Send notifications (if thresholds exceeded)

**Key Features:**
- ✓ Cloud-based monitoring
- ✓ Mobile app access
- ✓ Remote access (anywhere)
- ✓ Data logging
- ✓ Notifications/Alerts
- ✓ Multiple widgets
- ✓ Historical graphs
- ✓ Multi-device support

**Virtual Pin Mapping:**
- V0 → Temperature (°C)
- V1 → Humidity (%)
- V2 → Pressure (hPa)

---

## 🔧 Hardware Specifications

### DHT11 Sensor
- **Measures:** Temperature & Humidity
- **Accuracy:** ±2°C, ±5% RH
- **Interface:** Digital (GPIO 4)
- **Voltage:** 3.3V - 5V

### BMP180/085 Sensor
- **Measures:** Atmospheric Pressure
- **Accuracy:** ±0.5 hPa
- **Interface:** I2C (SDA/SCL)
- **Voltage:** 3.3V

### ESP32 Microcontroller
- **Processor:** Dual-core 240 MHz
- **WiFi:** 802.11 b/g/n (2.4 GHz)
- **Bluetooth:** BLE 4.2
- **GPIO Pins:** 34 programmable
- **Voltage:** 3.3V logic, 5V power

### WiFi Network
- **SSID:** Students
- **Password:** 0123456789
- **Frequency:** 2.4 GHz
- **Protocol:** 802.11 b/g/n

---

## 📱 Display Options Comparison

| Feature | WebServer Approach | Blynk Approach |
|---------|-------------------|----------------|
| **Access** | Local network only | Anywhere (internet) |
| **Setup** | Simple (no account) | Requires Blynk account |
| **Cost** | Free | Free tier available |
| **Customization** | Full HTML/CSS control | Widget-based |
| **Data Logging** | Manual implementation | Built-in |
| **Notifications** | Manual implementation | Built-in |
| **Mobile App** | Browser only | Native app |
| **Offline** | Works offline | Requires internet |
| **Update Rate** | 5 seconds (auto-refresh) | 1 second (configurable) |

---

## 🎨 Flowchart Color Legend

### Hardware Architecture
- 🌸 **Pink** - Sensors (DHT11, BMP180)
- 🔵 **Blue** - Microcontroller (ESP32)
- 🟢 **Green** - Network/WiFi
- 🟡 **Gold** - Display/Output
- 🟠 **Orange** - Power Supply

### Software Flow
- 🟢 **Light Green** - Start/End
- 🔵 **Sky Blue** - Initialization
- 🟡 **Gold** - WiFi Setup
- 🌸 **Pink** - Sensor Reading
- 🟣 **Plum** - Data Processing
- 🟠 **Salmon** - Web Server / Blynk
- 🟡 **Khaki** - Decision Points
- 🟢 **Pale Green** - Loop

---

## 📝 Code Reference

### WebServer Approach (Current Implementation)
```cpp
// Key Libraries
#include <WiFi.h>
#include <WebServer.h>
#include "DHT.h"
#include <Adafruit_BMP085.h>

// Pin Configuration
#define DHTPIN 4
#define DHTTYPE DHT11

// Network Credentials
const char* ssid = "Students";
const char* password = "0123456789";

// Main Functions
void setup() - Initialize all components
void loop() - Handle client requests
void handleRoot() - Serve HTML page with gauges
```

### Blynk Approach (Alternative)
```cpp
// Additional Library Required
#include <BlynkSimpleEsp32.h>

// Blynk Auth Token
char auth[] = "YourAuthToken";

// Virtual Pins
V0 - Temperature
V1 - Humidity
V2 - Pressure

// Main Functions
void setup() - Initialize Blynk connection
void loop() - Run Blynk and timer
void sendSensorData() - Send data to cloud
```

---

## 🚀 Usage

### View Flowcharts
All flowcharts are saved as high-resolution PNG files (300 DPI):
1. `hardware_architecture_flowchart.png`
2. `software_flow_webserver.png`
3. `software_flow_blynk.png`

### Regenerate Flowcharts
```bash
python hardware_architecture_flowchart.py
python software_flow_webserver.py
python software_flow_blynk.py
```

---

## 📊 Project Files

### Flowchart Generation Scripts
- `hardware_architecture_flowchart.py` - Hardware diagram
- `software_flow_webserver.py` - WebServer flow
- `software_flow_blynk.py` - Blynk flow

### Documentation
- `HARDWARE_FLOWCHARTS_README.md` - This file
- `README.md` - Main project documentation

---

## ✅ Deliverables

✓ **3 Professional Flowcharts** with clear text and proper styling  
✓ **Hardware Architecture** showing physical connections  
✓ **Software Flow (WebServer)** showing your current code execution  
✓ **Software Flow (Blynk)** showing alternative cloud approach  
✓ **Color-coded** for easy understanding  
✓ **High-resolution** (300 DPI) for reports and presentations  
✓ **Detailed documentation** with specifications  

---

## 📖 How to Use in Report

1. **Hardware Section:** Use `hardware_architecture_flowchart.png` to explain physical setup
2. **Software Section:** Use `software_flow_webserver.png` to explain code logic
3. **Alternative Approach:** Use `software_flow_blynk.png` to show cloud option
4. **Comparison:** Use the comparison table to discuss pros/cons

---

**Project Status: ✅ COMPLETED**

All hardware flowcharts have been successfully generated with proper styling, clear text, and professional colors!
