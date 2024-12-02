import sys
from PyQt6.QtWidgets import *
from ece143_vis import Ui_MainWindow
import pyqtgraph as pg
import pandas as pd


class Window(Ui_MainWindow, QMainWindow):
    """ Main Window """
    
    def __init__(self, parent=None):
        # Graphing settings
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        pg.setConfigOption('antialias', True)
        
        
        # Initialize main window
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)

        # Create DF
        self.data = pd.read_csv("ev_charging_patterns.csv")
        # Add grid
        self.graphWidget.showGrid(x=True, y=True)
        self.plotting_all_models = False

        """Connecting button and actions"""
        self.distance_driven.clicked.connect(self.plotdistance)
        self.energy_consumed.clicked.connect(self.plotenergy)
        self.battery_cap.clicked.connect(self.plotbat)
        self.charging_cost.clicked.connect(self.plotcost)
        # Connect combobox changes to plot updates
        self.model_1.currentTextChanged.connect(self.modelchange_flag)
        self.model_2.currentTextChanged.connect(self.modelchange_flag)
        self.plot_all_models.clicked.connect(self.plotmodels_flag)

    def plotmodels_flag(self):
        self.plotting_all_models = True
        self.update_plot()

    def modelchange_flag(self):
        self.plotting_all_models = False
        self.update_plot()

    def update_plot(self):
        if self.distance_driven.isChecked():
            self.plotdistance()
        elif self.energy_consumed.isChecked():
            self.plotenergy()
        elif self.battery_cap.isChecked():
            self.plotbat()
        elif self.charging_cost.isChecked():
            self.plotcost()

    def plotdistance(self):
        self.graphWidget.clear()

        if self.plotting_all_models:
            # Get all unique models
            models = self.data['Vehicle Model'].unique()
            distances = [self.data[self.data['Vehicle Model'] == model]['Distance Driven (since last charge) (km)'].mean() for model in models]
        else:
            # Get selected models
            model_1 = self.model_1.currentText()
            model_2 = self.model_2.currentText()
            models = [model_1, model_2]
            distances = [
                self.data[self.data['Vehicle Model'] == model_1]['Distance Driven (since last charge) (km)'].mean(),
                self.data[self.data['Vehicle Model'] == model_2]['Distance Driven (since last charge) (km)'].mean()
            ]

        x = range(len(models))
        bar_graph = pg.BarGraphItem(x=x, height=distances, width=0.6, brush='purple')
        self.graphWidget.addItem(bar_graph)
        self.graphWidget.getAxis('bottom').setTicks([[(i, model) for i, model in enumerate(models)]])

    def plotenergy(self):
        self.graphWidget.clear()

        if self.plotting_all_models:
            models = self.data['Vehicle Model'].unique()
            energy = [self.data[self.data['Vehicle Model'] == model]['Energy Consumed (kWh)'].mean() for model in models]
        else:
            model_1 = self.model_1.currentText()
            model_2 = self.model_2.currentText()
            models = [model_1, model_2]
            energy = [
                self.data[self.data['Vehicle Model'] == model_1]['Energy Consumed (kWh)'].mean(),
                self.data[self.data['Vehicle Model'] == model_2]['Energy Consumed (kWh)'].mean()
            ]

        x = range(len(models))
        bar_graph = pg.BarGraphItem(x=x, height=energy, width=0.6, brush='coral')
        self.graphWidget.addItem(bar_graph)
        self.graphWidget.getAxis('bottom').setTicks([[(i, model) for i, model in enumerate(models)]])

    def plotbat(self):
        self.graphWidget.clear()

        if self.plotting_all_models:
            models = self.data['Vehicle Model'].unique()
            capacities = [self.data[self.data['Vehicle Model'] == model]['Battery Capacity (kWh)'].mean() for model in models]
        else:
            model_1 = self.model_1.currentText()
            model_2 = self.model_2.currentText()
            models = [model_1, model_2]
            capacities = [
                self.data[self.data['Vehicle Model'] == model_1]['Battery Capacity (kWh)'].mean(),
                self.data[self.data['Vehicle Model'] == model_2]['Battery Capacity (kWh)'].mean()
            ]

        x = range(len(models))
        bar_graph = pg.BarGraphItem(x=x, height=capacities, width=0.6, brush='skyblue')
        self.graphWidget.addItem(bar_graph)
        self.graphWidget.getAxis('bottom').setTicks([[(i, model) for i, model in enumerate(models)]])

    def plotcost(self):
        self.graphWidget.clear()

        if self.plotting_all_models:
            models = self.data['Vehicle Model'].unique()
            costs = [self.data[self.data['Vehicle Model'] == model]['Charging Cost (USD)'].mean() for model in models]
        else:
            model_1 = self.model_1.currentText()
            model_2 = self.model_2.currentText()
            models = [model_1, model_2]
            costs = [
                self.data[self.data['Vehicle Model'] == model_1]['Charging Cost (USD)'].mean(),
                self.data[self.data['Vehicle Model'] == model_2]['Charging Cost (USD)'].mean()
            ]

        x = range(len(models))
        bar_graph = pg.BarGraphItem(x=x, height=costs, width=0.6, brush='lightgreen')
        self.graphWidget.addItem(bar_graph)
        self.graphWidget.getAxis('bottom').setTicks([[(i, model) for i, model in enumerate(models)]])
    



app = QApplication(sys.argv)

win = Window()
win.show()
sys.exit(app.exec())