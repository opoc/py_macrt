# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/graph.ui'
#
# Created: Wed Dec 17 15:59:08 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Graph_Widget(object):
    def setupUi(self, Graph_Widget):
        Graph_Widget.setObjectName(_fromUtf8("Graph_Widget"))
        Graph_Widget.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Graph_Widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.cB_resistance = QtGui.QCheckBox(Graph_Widget)
        self.cB_resistance.setObjectName(_fromUtf8("cB_resistance"))
        self.horizontalLayout_2.addWidget(self.cB_resistance)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.cB_Time = QtGui.QComboBox(Graph_Widget)
        self.cB_Time.setObjectName(_fromUtf8("cB_Time"))
        self.cB_Time.addItem(_fromUtf8(""))
        self.cB_Time.addItem(_fromUtf8(""))
        self.cB_Time.addItem(_fromUtf8(""))
        self.cB_Time.addItem(_fromUtf8(""))
        self.cB_Time.addItem(_fromUtf8(""))
        self.cB_Time.addItem(_fromUtf8(""))
        self.cB_Time.addItem(_fromUtf8(""))
        self.cB_Time.addItem(_fromUtf8(""))
        self.cB_Time.addItem(_fromUtf8(""))
        self.cB_Time.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.cB_Time)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.PlotWidget = PlotWidget(Graph_Widget)
        self.PlotWidget.setObjectName(_fromUtf8("PlotWidget"))
        self.verticalLayout.addWidget(self.PlotWidget)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.pBtn_Close = QtGui.QPushButton(Graph_Widget)
        self.pBtn_Close.setObjectName(_fromUtf8("pBtn_Close"))
        self.horizontalLayout_3.addWidget(self.pBtn_Close)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Graph_Widget)
        QtCore.QMetaObject.connectSlotsByName(Graph_Widget)

    def retranslateUi(self, Graph_Widget):
        Graph_Widget.setWindowTitle(_translate("Graph_Widget", "Graph", None))
        self.cB_resistance.setText(_translate("Graph_Widget", "Resistance", None))
        self.cB_Time.setItemText(0, _translate("Graph_Widget", "all", None))
        self.cB_Time.setItemText(1, _translate("Graph_Widget", "5 min", None))
        self.cB_Time.setItemText(2, _translate("Graph_Widget", "15 min", None))
        self.cB_Time.setItemText(3, _translate("Graph_Widget", "30 min", None))
        self.cB_Time.setItemText(4, _translate("Graph_Widget", "1 hour", None))
        self.cB_Time.setItemText(5, _translate("Graph_Widget", "2 hours", None))
        self.cB_Time.setItemText(6, _translate("Graph_Widget", "6 hours", None))
        self.cB_Time.setItemText(7, _translate("Graph_Widget", "1 day", None))
        self.cB_Time.setItemText(8, _translate("Graph_Widget", "2 days", None))
        self.cB_Time.setItemText(9, _translate("Graph_Widget", "1 week", None))
        self.pBtn_Close.setText(_translate("Graph_Widget", "Close", None))

from pyqtgraph import PlotWidget
