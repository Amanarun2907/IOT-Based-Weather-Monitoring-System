"""
Generate Methodology Flowchart using Graphviz
"""

from graphviz import Digraph

print("="*80)
print("CREATING METHODOLOGY FLOWCHART")
print("="*80)

# Create a new directed graph
dot = Digraph(comment='IoT Weather Monitoring - Time Series Analysis Methodology')
dot.attr(rankdir='TB', size='12,16')
dot.attr('node', shape='box', style='filled,rounded', fontname='Arial', fontsize='11')
dot.attr('edge', fontname='Arial', fontsize='10')

# Define color scheme
color_start = '#90EE90'
color_data = '#87CEEB'
color_preprocess = '#FFD700'
color_analysis = '#FFA07A'
color_model = '#DDA0DD'
color_eval = '#F08080'
color_forecast = '#98FB98'
color_end = '#FFB6C1'

# Start
dot.node('A', 'START\nIoT Weather Monitoring System', fillcolor=color_start, fontsize='12', style='filled,rounded,bold')

# Data Collection
dot.node('B', 'Data Collection\n• DHT Sensor (Temp, Humidity)\n• BMP Sensor (Pressure)\n• ESP32 Microcontroller\n• 300 readings (9 AM - 2 PM)', fillcolor=color_data)

# Data Loading
dot.node('C', 'Load Data\n• Read Excel file\n• 300 entries\n• 6 columns', fillcolor=color_data)

# Statistical Description
dot.node('D', 'Statistical Description\n• Descriptive statistics\n• Missing value check\n• Correlation analysis', fillcolor=color_analysis)

# Data Preprocessing
dot.node('E', 'Data Preprocessing\n• Create DateTime index\n• Sort by time\n• Extract parameters', fillcolor=color_preprocess)

# Visualization
dot.node('F', 'Exploratory Data Analysis\n• Time series plots\n• Correlation heatmap\n• ACF/PACF plots', fillcolor=color_analysis)

# Stationarity Test
dot.node('G', 'Stationarity Testing\n• Augmented Dickey-Fuller Test\n• Check p-value < 0.05\n• Determine differencing', fillcolor=color_analysis)

# Train-Test Split
dot.node('H', 'Train-Test Split\n• Training: 80% (240 samples)\n• Testing: 20% (60 samples)', fillcolor=color_preprocess)

# Model Training - Temperature
dot.node('I1', 'Temperature Forecasting\n• ARIMA (2,1,2)\n• SARIMA (1,1,1)(1,1,1,12)\n• GARCH (1,1)', fillcolor=color_model)

# Model Training - Humidity
dot.node('I2', 'Humidity Forecasting\n• ARIMA (2,1,2)\n• SARIMA (1,1,1)(1,1,1,12)\n• GARCH (1,1)', fillcolor=color_model)

# Model Training - Pressure
dot.node('I3', 'Pressure Forecasting\n• ARIMA (2,1,2)\n• SARIMA (1,1,1)(1,1,1,12)\n• GARCH (1,1)', fillcolor=color_model)

# Model Training - Dew Point
dot.node('I4', 'Dew Point Forecasting\n• ARIMA (2,1,2)\n• SARIMA (1,1,1)(1,1,1,12)\n• GARCH (1,1)', fillcolor=color_model)

# Model Evaluation
dot.node('J', 'Model Evaluation\n• RMSE (Root Mean Square Error)\n• MAE (Mean Absolute Error)\n• MAPE (Mean Absolute % Error)\n• R² Score', fillcolor=color_eval)

# Model Comparison
dot.node('K', 'Model Comparison\n• Compare performance metrics\n• Select best model\n• Generate comparison charts', fillcolor=color_eval)

# Future Forecasting
dot.node('L', 'Future Forecasting\n• Predict 2:15 PM - 6:15 PM\n• 240 minutes (4 hours)\n• All 4 parameters', fillcolor=color_forecast)

# Visualization
dot.node('M', 'Results Visualization\n• Model comparison plots\n• Future forecast graphs\n• Performance bar charts\n• Save all figures', fillcolor=color_forecast)

# Report Generation
dot.node('N', 'Report Generation\n• Performance metrics table\n• Forecast data Excel\n• Methodology flowchart\n• All visualizations', fillcolor=color_end)

# End
dot.node('O', 'END\nComplete Analysis Report', fillcolor=color_end, fontsize='12', style='filled,rounded,bold')

# Define edges (connections)
dot.edge('A', 'B', label='Collect')
dot.edge('B', 'C', label='Store')
dot.edge('C', 'D', label='Analyze')
dot.edge('D', 'E', label='Process')
dot.edge('E', 'F', label='Visualize')
dot.edge('F', 'G', label='Test')
dot.edge('G', 'H', label='Split')
dot.edge('H', 'I1', label='Train')
dot.edge('H', 'I2', label='Train')
dot.edge('H', 'I3', label='Train')
dot.edge('H', 'I4', label='Train')
dot.edge('I1', 'J', label='Evaluate')
dot.edge('I2', 'J', label='Evaluate')
dot.edge('I3', 'J', label='Evaluate')
dot.edge('I4', 'J', label='Evaluate')
dot.edge('J', 'K', label='Compare')
dot.edge('K', 'L', label='Forecast')
dot.edge('L', 'M', label='Visualize')
dot.edge('M', 'N', label='Document')
dot.edge('N', 'O', label='Complete')

# Add legend
dot.attr('node', shape='plaintext', style='')
with dot.subgraph(name='cluster_legend') as legend:
    legend.attr(label='Legend', fontsize='12', style='dashed')
    legend.node('L1', 'Data Collection & Loading', fillcolor=color_data, shape='box', style='filled,rounded')
    legend.node('L2', 'Preprocessing', fillcolor=color_preprocess, shape='box', style='filled,rounded')
    legend.node('L3', 'Analysis & Testing', fillcolor=color_analysis, shape='box', style='filled,rounded')
    legend.node('L4', 'Model Training', fillcolor=color_model, shape='box', style='filled,rounded')
    legend.node('L5', 'Evaluation', fillcolor=color_eval, shape='box', style='filled,rounded')
    legend.node('L6', 'Forecasting & Results', fillcolor=color_forecast, shape='box', style='filled,rounded')

# Render the flowchart
try:
    dot.render('methodology_flowchart', format='png', cleanup=True)
    print("✓ Flowchart generated successfully: methodology_flowchart.png")
except Exception as e:
    print(f"✗ Error generating flowchart: {e}")
    print("  Note: Make sure Graphviz is installed on your system")
    print("  Install: https://graphviz.org/download/")

print("\n" + "="*80)
print("FLOWCHART GENERATION COMPLETED")
print("="*80)
