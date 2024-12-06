# ECE 143 Project Fall 2024 Group 6
## EV Vehicle Charging Patterns

This dataset served as the foundation for an in-depth exploratory analysis aimed at uncovering meaningful insights and trends related to electric vehicle (EV) charging behavior. Our analysis focused on identifying interesting data points and generating visuals to better understand the underlying patterns. The study revolved around three key questions:

1. Vehicle Characteristics: Investigating how vehicle models and battery capacities impact energy consumption and cost efficiency.
2. Charger and Location Impact: Examining the effects of charging station types and locations on efficiency and overall costs.
3. Time-Based Analysis: Exploring how the time of day and day of the week influence charging trends, particularly identifying peak demand periods and their implications on costs.

Through this comprehensive approach, we aimed to gain actionable insights into EV charging trends and the factors that drive cost efficiency and energy consumption. All visuals can be found in the Juypter notebook in this repo; aswell as our functions used to generate visuals can be found in Graphs.py

## Vehicle Characteristic visualizer

The vehicle Characteristic visualizer consists of 2 files:
- ece143_vis.py
  - Main window UI created using pyqtdesigner, and then translated into python to be used for dashboard_ui. Just a supporting file
- dashboard_ui.py
  - Python script that implements functionality for the visualizer and dashboard.

To use the visualizer, simply run 'dashboard_ui.py' and have the required imports:
- PyQt6
- pyqtgraph
- pandas

The visualizer uses the csv file to parse through it's data, so make sure its in the same folder!

[![Visualization Demo](https://img.youtube.com/vi/9fW47XwXoVg/0.jpg)](https://www.youtube.com/watch?v=9fW47XwXoVg)

# Repo Format
The format of this GitHub repo is as follows. It holds all the python module we developed to not reuse code `Graphs.py`, the final juypter notebook(`visualization.ipynb`) that holds all visualizations, and a pdf copy of the slides we presented

# How to run code
To run the juypter notebook `visualization.ipynb`, make sure all third party are installed and include the aditional python file `Graph.py`

# 3rd Party Modules
* NumPy
* Pandas
* Seaborn
* Sklearn - Label Encoder
