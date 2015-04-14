#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
from ui.main import Main
from PyQt4 import QtGui
#import pyqtgraph as pg
#from py_macrt.graph import DateAxis


if __name__ == '__main__':
    QT_APP = QtGui.QApplication(sys.argv)
    MAIN_APP = Main('config.ini')
    MAIN_APP.show()
    sys.exit(QT_APP.exec_())
