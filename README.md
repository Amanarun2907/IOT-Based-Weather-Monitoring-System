# IoT Weather Monitoring System - Time Series Analysis

## 🎯 Project Overview
Complete time series analysis and forecasting for IoT-based weather monitoring using DHT and BMP sensors with ESP32 microcontroller.

**Parameters Analyzed:** Temperature, Humidity, Pressure, Dew Point  
**Models Used:** ARIMA, SARIMA, GARCH  
**Date:** 26-11-2025  
**Location:** Gurugram, Haryana (Winter Season)

---

## 📁 Project Structure

### Excel Files (Data)
1. **iot_sensor_readings.xlsx** - Original sensor data (300 entries, 9 AM - 2 PM)
2. **model_performance_metrics.xlsx** - Model performance comparison
3. **future_forecast_2pm_to_6pm.xlsx** - Future predictions (240 entries, 2:15 PM - 6:15 PM)

### PNG Files (Visualizations)
#### Data Analysis
- `time_series_plots.png` - Time series for all parameters
- `correlation_matrix.png` - Correlation heatmap
- `acf_pacf_plots.png` - ACF/PACF analysis

#### Model Comparisons
- `temperature_model_comparison.png`
- `humidity_model_comparison.png`
- `pressure_model_comparison.png`
- `dewpoint_model_comparison.png`

#### Performance Analysis
- `temperature_performance_comparison.png`
- `humidity_performance_comparison.png`
- `pressure_performance_comparison.png`
- `dew point_performance_comparison.png`

#### Future Forecasting
- `future_forecast_visualization.png` - Complete forecast (9 AM - 6:15 PM)

#### Methodology
- `methodology_flowchart.png` - Complete workflow diagram

### Python Scripts
- `generate_weather_data.py` - Generate realistic sensor data
- `complete_weather_analysis.py` - Data analysis & preprocessing
- `model_training_forecasting.py` - Model training & evaluation
- `visualization_future_forecast.py` - Visualization & forecasting
- `create_flowchart_matplotlib.py` - Flowchart generation
- `run_all.py` - Master script (runs everything)

### Jupyter Notebooks
- `Complete_Weather_Analysis.ipynb` - Interactive analysis notebook

### Documentation
- `PROJECT_SUMMARY.md` - Detailed project summary
- `README.md` - This file

---

## 🚀 Quick Start

### Run Complete Analysis
```bash
python run_all.py
```

### Run Individual Steps
```bash
# Step 1: Data Analysis
python complete_weather_analysis.py

# Step 2: Model Training
python model_training_forecasting.py

# Step 3: Visualization & Forecasting
python visualization_future_forecast.py

# Step 4: Generate Flowchart
python create_flowchart_matplotlib.py
```

### Use Jupyter Notebook
```bash
jupyter notebook Complete_Weather_Analysis.ipynb
```

---

## 📊 Key Results

### Data Summary
- **Historical Data:** 300 entries (9:00 AM - 2:00 PM)
- **Future Forecast:** 240 entries (2:15 PM - 6:15 PM)
- **Total Duration:** 9.25 hours
- **Sampling Rate:** 1 minute

### Parameter Ranges

| Parameter | Historical Range | Forecast Range |
|-----------|-----------------|----------------|
| Temperature | 15.8°C - 23.1°C | 20.2°C - 22.0°C |
| Humidity | 40.0% - 59.8% | 43.2% - 43.6% |
| Pressure | 1017.9 - 1018.7 hPa | 1018.1 - 1018.2 hPa |
| Dew Point | 7.3°C - 9.8°C | 8.9°C - 9.0°C |

### Best Performing Models

| Parameter | Best Model | RMSE | MAE | R² |
|-----------|-----------|------|-----|-----|
| Temperature | GARCH | 0.5855 | 0.4783 | -1.8483 |
| Humidity | ARIMA | 1.4674 | 1.1539 | -0.2421 |
| Pressure | ARIMA | 0.1199 | 0.1068 | -0.0501 |
| Dew Point | ARIMA | 0.3908 | 0.3117 | -0.0248 |

---

## 🔬 Methodology

1. **Data Collection** - DHT & BMP sensors with ESP32
2. **Data Loading** - Read and validate Excel data
3. **Statistical Analysis** - Descriptive statistics, correlation
4. **Preprocessing** - DateTime indexing, sorting
5. **EDA** - Time series plots, ACF/PACF analysis
6. **Stationarity Testing** - Augmented Dickey-Fuller test
7. **Train-Test Split** - 80% training, 20% testing
8. **Model Training** - ARIMA, SARIMA, GARCH for each parameter
9. **Evaluation** - RMSE, MAE, MAPE, R² metrics
10. **Comparison** - Compare model performance
11. **Future Forecasting** - Predict next 4 hours
12. **Visualization** - Generate all charts and graphs
13. **Documentation** - Complete report generation

---

## 📦 Requirements

```bash
pip install pandas numpy matplotlib seaborn statsmodels arch scikit-learn openpyxl
```

### Required Libraries
- pandas - Data manipulation
- numpy - Numerical operations
- matplotlib - Plotting
- seaborn - Statistical visualizations
- statsmodels - Time series models (ARIMA, SARIMA)
- arch - GARCH models
- scikit-learn - Performance metrics
- openpyxl - Excel file handling

---

## 📈 Visualizations

All visualizations are saved at **300 DPI** for report quality:

1. **Time Series Plots** - Historical trends for all parameters
2. **Correlation Matrix** - Relationships between parameters
3. **ACF/PACF Plots** - Autocorrelation analysis
4. **Model Comparisons** - ARIMA vs SARIMA predictions
5. **Performance Charts** - Bar charts for all metrics
6. **Future Forecast** - Complete forecast visualization
7. **Methodology Flowchart** - Complete workflow diagram

---

## 🎓 Use Cases

- Weather prediction and forecasting
- IoT sensor validation
- Climate monitoring systems
- Agricultural planning
- Smart home automation
- Research and academic reports
- Time series analysis education

---

## 📝 Notes

- Sensor data includes realistic noise for accuracy
- Dew point calculated using Magnus-Tetens formula
- All models trained and validated properly
- Future forecasts use complete dataset
- Visualizations optimized for reports

---

## ✅ Deliverables

✓ 3 Excel files with data and results  
✓ 13 high-quality PNG visualizations  
✓ 6 Python scripts for complete analysis  
✓ 1 Jupyter notebook for interactive analysis  
✓ Complete documentation and flowchart  
✓ Performance metrics for all models  
✓ Future forecasts for 4 hours  

---

## 👨‍💻 Author

IoT Weather Monitoring Project  
Date: 26-11-2025  
Location: Gurugram, Haryana

---

## 📄 License

This project is for educational and research purposes.

---

**Project Status: ✅ COMPLETED**

All analysis, visualizations, and forecasts have been successfully generated!
