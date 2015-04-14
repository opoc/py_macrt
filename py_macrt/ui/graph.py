#!/usr/bin/python3
# -*- coding: utf-8 -*-
"Display the data versus time."

from pyqtgraph import QtCore, QtGui
import pyqtgraph as pg
from tools.dateaxis import DateAxis
from .graph_ui import Ui_Graph_Widget
from math import isnan


DURATION = [
    0,  # All data
    5 * 60,  # 5min
    15 * 60,  # 15 min
    30 * 60,  # 60 min
    1 * 60 * 60,  # 1 hour
    2 * 60 * 60,  # 2 hours
    6 * 60 * 60,  # 6 hours
    1 * 24 * 60 * 60,  # 1 day
    2 * 24 * 60 * 60,  # 2 days
    7 * 24 * 60 * 60,  # 1 week
]


class Graph(QtGui.QWidget, Ui_Graph_Widget):
    "Graph class"
    def __init__(self, parent, channels):
        "Requires the parents and the selected channels."
        QtGui.QWidget.__init__(self, parent, QtCore.Qt.Window)
        self.setupUi(self)

        self.parent = parent
        self.config = self.parent.config
        self.data = self.parent.data
        self.channels = channels
        self.conv = 'R'

        self.timer = QtCore.QTimer()

        # Connect signals
        self.timer.timeout.connect(self.update_plot)
        self.cB_resistance.stateChanged.connect(self.resistance_temperature)
        self.pBtn_Close.clicked.connect(self.close)
        self.cB_Time.currentIndexChanged.connect(self.update_plot)

        # Prepare the plot widget
        time_axis = DateAxis(orientation='bottom')
        #vbox = QtGui.QVBoxLayout()
        #self.plot_widget = pg.PlotWidget(axisItems={'bottom': time_axis})
        self.PlotWidget.addLegend()
        self.PlotWidget.getPlotItem().axis['bottom']['item'] = time_axis
        colors = ('r', 'b', 'g', 'w')
        self.plots = {
            chan_name: self.PlotWidget.plot(pen=c, name=chan_name,
                                            symbolBrush=c, symbolPen='w')
            for (module_name, chan_name), c in zip(self.channels, colors)}
        self.PlotWidget.setLabel('bottom', 'Time', units='s')
        self.timer.start(5 * 1000)  # in ms
        self.update_plot()

    def update_plot(self):
        "Refresh the data plotted."
        last = self.data['time'][-1]
        if int(self.cB_Time.currentIndex()):
            prev = last - DURATION[int(self.cB_Time.currentIndex())]
        else:
            prev = 0  # All data
        for module_name, chan_name in self.channels:
            y_data = self.data[module_name][chan_name][self.conv]
            time_data = [[t, y] for t, y in zip(self.data['time'], y_data)
                         if t >= prev and not isnan(y)]
            time, data = [list(row) for row in zip(*time_data)]
            self.plots[chan_name].setData(x=time, y=data)

    def resistance_temperature(self):
        "Select the 'resistance' or the 'temperature' data set."
        if self.cB_resistance.checkState():
            self.conv = 'T'
            self.cB_resistance.setText("Temperature")
        else:
            self.conv = 'R'
            self.cB_resistance.setText("Resistance")
        self.update_plot()
