# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created: Wed Dec 17 15:58:40 2014
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(779, 249)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.treeWidget = QtGui.QTreeWidget(self.centralwidget)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pBtn_Scan = QtGui.QPushButton(self.centralwidget)
        self.pBtn_Scan.setObjectName(_fromUtf8("pBtn_Scan"))
        self.verticalLayout.addWidget(self.pBtn_Scan)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.pBtn_Refresh = QtGui.QPushButton(self.centralwidget)
        self.pBtn_Refresh.setObjectName(_fromUtf8("pBtn_Refresh"))
        self.verticalLayout.addWidget(self.pBtn_Refresh)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.pBtn_Graph = QtGui.QPushButton(self.centralwidget)
        self.pBtn_Graph.setObjectName(_fromUtf8("pBtn_Graph"))
        self.verticalLayout.addWidget(self.pBtn_Graph)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 779, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuQuitter = QtGui.QMenu(self.menubar)
        self.menuQuitter.setObjectName(_fromUtf8("menuQuitter"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuQuitter.addAction(self.actionQuit)
        self.menubar.addAction(self.menuQuitter.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "pyMACRT", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Name", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "R", None))
        self.treeWidget.headerItem().setText(2, _translate("MainWindow", "Conv.", None))
        self.pBtn_Scan.setText(_translate("MainWindow", "Scan iMACRT", None))
        self.pBtn_Refresh.setText(_translate("MainWindow", "Refresh", None))
        self.pBtn_Graph.setText(_translate("MainWindow", "Graph", None))
        self.menuQuitter.setTitle(_translate("MainWindow", "Application", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

