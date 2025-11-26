"""
Master Script - Run Complete Weather Analysis
"""
import subprocess
import sys

print("="*80)
print("RUNNING COMPLETE IOT WEATHER ANALYSIS")
print("="*80)

scripts = [
    ("complete_weather_analysis.py", "Data Analysis & Preprocessing"),
    ("model_training_forecasting.py", "Model Training & Evaluation"),
    ("visualization_future_forecast.py", "Visualization & Future Forecasting"),
    ("create_flowchart.py", "Flowchart Generation")
]

for script, description in scripts:
    print(f"\n{'='*80}")
    print(f"Running: {description}")
    print(f"Script: {script}")
    print(f"{'='*80}\n")
    
    try:
        result = subprocess.run([sys.executable, script], check=True)
        print(f"\n✓ {description} completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"\n✗ Error in {description}")
        print(f"  Error: {e}")
        break
    except Exception as e:
        print(f"\n✗ Unexpected error in {description}")
        print(f"  Error: {e}")
        break

print("\n" + "="*80)
print("ANALYSIS COMPLETE!")
print("="*80)
print("\nGenerated Files:")
print("  1. iot_sensor_readings.xlsx - Original sensor data")
print("  2. model_performance_metrics.xlsx - Model performance comparison")
print("  3. future_forecast_2pm_to_6pm.xlsx - Future predictions")
print("  4. time_series_plots.png - Time series visualizations")
print("  5. correlation_matrix.png - Correlation heatmap")
print("  6. acf_pacf_plots.png - ACF/PACF analysis")
print("  7. temperature_model_comparison.png - Temperature models")
print("  8. humidity_model_comparison.png - Humidity models")
print("  9. pressure_model_comparison.png - Pressure models")
print("  10. dewpoint_model_comparison.png - Dew point models")
print("  11. future_forecast_visualization.png - Future forecast")
print("  12. temperature_performance_comparison.png - Temp metrics")
print("  13. humidity_performance_comparison.png - Humidity metrics")
print("  14. pressure_performance_comparison.png - Pressure metrics")
print("  15. dew point_performance_comparison.png - Dew point metrics")
print("  16. methodology_flowchart.png - Complete flowchart")
