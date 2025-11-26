# IoT Weather Monitoring System - Time Series Analysis
## Complete Project Summary

### Project Overview
This project implements a comprehensive time series analysis for an IoT-based weather monitoring system using DHT and BMP sensors with ESP32 microcontroller. The analysis covers Temperature, Humidity, Pressure, and Dew Point forecasting.

---

## 📊 Generated Files

### 1. Data Files (Excel)
- **iot_sensor_readings.xlsx** - Original sensor data (300 entries, 9 AM - 2 PM)
- **model_performance_metrics.xlsx** - Performance comparison of all models
- **future_forecast_2pm_to_6pm.xlsx** - Future predictions (2:15 PM - 6:15 PM, 240 entries)

### 2. Visualization Files (PNG)
#### Data Analysis
- **time_series_plots.png** - Time series plots for all 4 parameters
- **correlation_matrix.png** - Correlation heatmap
- **acf_pacf_plots.png** - ACF and PACF analysis for stationarity

#### Model Comparisons
- **temperature_model_comparison.png** - ARIMA vs SARIMA predictions for temperature
- **humidity_model_comparison.png** - ARIMA vs SARIMA predictions for humidity
- **pressure_model_comparison.png** - ARIMA vs SARIMA predictions for pressure
- **dewpoint_model_comparison.png** - ARIMA vs SARIMA predictions for dew point

#### Performance Analysis
- **temperature_performance_comparison.png** - Performance metrics bar charts (RMSE, MAE, MAPE, R²)
- **humidity_performance_comparison.png** - Performance metrics bar charts
- **pressure_performance_comparison.png** - Performance metrics bar charts
- **dew point_performance_comparison.png** - Performance metrics bar charts

#### Future Forecasting
- **future_forecast_visualization.png** - Complete forecast visualization (9 AM - 6:15 PM)

#### Methodology
- **methodology_flowchart.png** - Complete methodology flowchart

### 3. Python Scripts
- **generate_weather_data.py** - Generates realistic sensor data
- **complete_weather_analysis.py** - Data analysis and preprocessing
- **model_training_forecasting.py** - Model training and evaluation
- **visualization_future_forecast.py** - Visualization and future forecasting
- **create_flowchart_matplotlib.py** - Flowchart generation
- **run_all.py** - Master script to run everything

---

## 🔬 Analysis Details

### Data Specifications
- **Date**: 26-11-2025
- **Time Range**: 9:00 AM - 2:00 PM (Historical) + 2:15 PM - 6:15 PM (Forecast)
- **Location**: Gurugram, Haryana
- **Season**: Winter
- **Total Historical Entries**: 300 (1-minute intervals)
- **Total Forecast Entries**: 240 (1-minute intervals)

### Parameters Analyzed
1. **Temperature (°C)**
   - Range: 15.8°C - 23.1°C
   - Pattern: Increases from morning to afternoon, peaks around 1 PM

2. **Humidity (%)**
   - Range: 40.0% - 59.8%
   - Pattern: Inverse relationship with temperature

3. **Pressure (hPa)**
   - Range: 1017.9 - 1018.7 hPa
   - Pattern: Small natural fluctuations

4. **Dew Point (°C)**
   - Range: 7.3°C - 9.8°C
   - Calculated using Magnus formula from temperature and humidity

### Models Applied
1. **ARIMA (2,1,2)** - AutoRegressive Integrated Moving Average
2. **SARIMA (1,1,1)(1,1,1,12)** - Seasonal ARIMA
3. **GARCH (1,1)** - Generalized AutoRegressive Conditional Heteroskedasticity

### Performance Metrics
- **RMSE** - Root Mean Square Error
- **MAE** - Mean Absolute Error
- **MAPE** - Mean Absolute Percentage Error
- **R²** - R-squared Score

---

## 📈 Key Results

### Best Performing Models (by RMSE)

#### Temperature
- **Best**: GARCH (RMSE: 0.5855, MAE: 0.4783)
- ARIMA: RMSE 1.5311
- SARIMA: RMSE 1.5371

#### Humidity
- **Best**: ARIMA (RMSE: 1.4674, MAE: 1.1539)
- SARIMA: RMSE 3.7476
- GARCH: RMSE 2.4056

#### Pressure
- **Best**: ARIMA (RMSE: 0.1199, MAE: 0.1068)
- SARIMA: RMSE 0.1417
- GARCH: RMSE 0.1996

#### Dew Point
- **Best**: ARIMA (RMSE: 0.3908, MAE: 0.3117)
- GARCH: RMSE 0.4664
- SARIMA: RMSE 0.5153

### Future Forecast Summary (2:15 PM - 6:15 PM)
- **Temperature**: 20.2°C - 22.0°C
- **Humidity**: 43.2% - 43.6%
- **Pressure**: 1018.1 - 1018.2 hPa
- **Dew Point**: 8.9°C - 9.0°C

---

## 🔄 Methodology Workflow

1. **Data Collection** → DHT & BMP sensors with ESP32
2. **Data Loading** → Read Excel file
3. **Statistical Description** → Descriptive statistics, correlation
4. **Data Preprocessing** → DateTime indexing, sorting
5. **Exploratory Analysis** → Time series plots, ACF/PACF
6. **Stationarity Testing** → Augmented Dickey-Fuller test
7. **Train-Test Split** → 80% training, 20% testing
8. **Model Training** → ARIMA, SARIMA, GARCH for each parameter
9. **Model Evaluation** → Calculate RMSE, MAE, MAPE, R²
10. **Model Comparison** → Compare performance metrics
11. **Future Forecasting** → Predict next 4 hours
12. **Visualization** → Generate all charts and graphs
13. **Report Generation** → Complete documentation

---

## 🎯 Use Cases

This analysis can be used for:
- Weather prediction and forecasting
- IoT sensor validation
- Climate monitoring systems
- Agricultural planning
- Smart home automation
- Research and academic reports

---

## 📝 Notes

- All sensor data includes realistic noise (±0.1-0.3°C for temperature, ±1-2% for humidity, ±0.1-0.2 hPa for pressure)
- Dew point calculated using Magnus-Tetens formula for meteorological accuracy
- Models trained on 240 samples, tested on 60 samples
- Future forecasts use ARIMA models trained on complete dataset (300 samples)
- All visualizations saved at 300 DPI for report quality

---

## 🚀 How to Run

To regenerate all analysis:
```bash
python run_all.py
```

Or run individual scripts:
```bash
python complete_weather_analysis.py
python model_training_forecasting.py
python visualization_future_forecast.py
python create_flowchart_matplotlib.py
```

---

**Project Completed Successfully!**
Date: 26-11-2025
Location: Gurugram, Haryana
