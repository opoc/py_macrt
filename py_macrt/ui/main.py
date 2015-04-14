#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Main window class."""

from configparser import ConfigParser
import sqlite3
import time
from PyQt4 import QtCore, QtGui
from .main_ui import Ui_MainWindow


SQL_CREATE_TABLE = """CREATE TABLE IF NOT EXISTS data (
datetime INTEGER,
module_name TEXT,
chan_name TEXT,
resistance REAL,
temperature REAL
);"""
SQL_STORE = "INSERT INTO data VALUES (?, ?, ?, ?, ?);"


class Main(QtGui.QMainWindow, Ui_MainWindow):
    "Main window class"
    def __init__(self, config_file):
        self.config_file = config_file
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        self.data_timer = QtCore.QTimer()
        self.store_timer = QtCore.QTimer()
        self.tw_root = self.treeWidget.invisibleRootItem()

        # Connect signals
        self.actionQuit.triggered.connect(self.quit_cb)
        self.pBtn_Scan.clicked.connect(self.scan_cb)
        self.pBtn_Refresh.clicked.connect(self.refresh_cb)
        self.pBtn_Graph.clicked.connect(self.open_graph_window)
        self.data_timer.timeout.connect(self.refresh_cb)
        self.store_timer.timeout.connect(self.store_cb)

        self.data = {'time': [], }
        self.graphs = []
        self.modules = {}

        self.config = ConfigParser()
        try:
            self.config.read(self.config_file)
        except AttributeError:
            pass

        self.scan_cb()
        if self.modules:
            self.refresh_cb()

        storage = self.config['Main'].get('save_file', 'data_storage.db')
        self.conn = sqlite3.connect(storage)
        self.cursor = self.conn.cursor()
        self.cursor.execute(SQL_CREATE_TABLE)
        self.conn.commit()
        store_period = int(self.config['Main'].get('save_period', 30))
        self.store_timer.start(store_period * 1000)

    def quit_cb(self, *args, **kwargs):
        "Quit the app. Save the config."
        self.config.write(open(self.config_file, 'w'))
        try:
            self.conn.close()
        except:
            pass
        QtGui.QApplication.quit()

    def scan_cb(self, *args, **kwargs):
        "Scan the subnet for active iMACRT modules."
        from py_macrt import scan
        self.modules = {}
        brd_addr = self.config['Main'].get('brd_addr', '255.255.255.255')
        for name, addr in scan.sort(scan.scan(brd_addr)):
            if name.startswith('MMR3'):
                from py_macrt.mmr3 import MMR3
                self.modules[name] = {'obj': MMR3(addr)}
            if name.startswith('MRHT'):
                from py_macrt.mmr3 import MRHT
                self.modules[name] = {'obj': MRHT(addr)}
        period = int(self.config['Main'].get('data_period', 5))
        self.data_timer.start(period * 1000)  # in ms
        self.add_module()

    def refresh_cb(self, *args, **kwargs):
        "Refresh values for every iMACRT modules."
        import conversion
        self.data['time'].append(time.time())
        for name, module in self.modules.items():
            for i in range(3):
                if name not in self.data:
                    self.data[name] = {}
                chan_name = self.config[name].get('Chan' + str(i),
                                                  'Chan' + str(i))
                if chan_name not in self.data[name]:
                    self.data[name][chan_name] = {'R': [], 'T': []}
                resistance = getattr(module['obj'], 'chan' + str(i + 1)).R
                module['chan_item'][i].setText(1, str(resistance))
                try:
                    law_name = self.config[name]['Law' + str(i)]
                    law = getattr(conversion, law_name)
                    converted = law(resistance)
                    formatter = self.config['Main'].get('formatter', '{:.4f}')
                    conv_str = formatter.format(converted)
                except (KeyError, AttributeError):
                    converted = float('NaN')
                    conv_str = "Wrong or missing configuration file."
                except ZeroDivisionError:
                    converted = float('NaN')
                    conv_str = 'ZeroDivision with law {}.'.format(law_name)
                module['chan_item'][i].setText(2, str(conv_str))
                self.data[name][chan_name]['R'].append(resistance)
                self.data[name][chan_name]['T'].append(converted)

    def add_module(self):
        "Actualized the TreeWidget with the active iMACRT modules."
        for name, module in self.modules.items():
            if 'treewidget' in module:  # Module already in tree
                continue
            _tw = QtGui.QTreeWidgetItem(
                self.tw_root, [name, ])
            if self.config.has_section(name):
                module_conf = self.config[name]
                chan_names = [module_conf.get(
                    'Chan' + str(i), 'Chan' + str(i + 1)) for i in range(3)]

            module['chan_item'] = [
                QtGui.QTreeWidgetItem(_tw, [chan_name, "", ""])
                for chan_name in chan_names]
            module['treewidget'] = _tw
        self.treeWidget.expandAll()

    def open_graph_window(self):
        "Open the Graph window for displaying the selected data."
        from ui.graph import Graph
        selected_items = [item for item in self.treeWidget.selectedItems()
                          if item.childCount() == 0]
        if selected_items:
            graph = Graph(self, [(item.parent().text(0), item.text(0))
                                 for item in selected_items])
            self.graphs.append(graph)
            graph.show()
        self.treeWidget.clearSelection()

    def store_cb(self):
        "Store periodically the data into a SQLite database."
        def sqlize(value):
            "Replaces NaN by NULL."
            from math import isnan
            return isnan(value) and 'NULL' or value

        to_store = []
        for module_name, mod_data in self.data.items():
            if module_name == 'time':
                continue
            for chan_name, values in mod_data.items():
            # store 'time', 'module', 'chan_name', 'R', 'T'
                to_store.append((
                    self.data['time'][-1],
                    module_name,
                    chan_name,
                    sqlize(values['R'][-1]),
                    sqlize(values['T'][-1])))
        self.cursor.executemany(SQL_STORE, to_store)
        self.conn.commit()
