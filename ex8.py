#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
   QApplication,
   QCheckBox,
   QTabWidget,
   QVBoxLayout,
   QWidget
)

class Window(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle("QTabWidget Example")
      self.resize(270, 110)
      
      # Create a top level layout
      layout = QVBoxLayout()
      self.setLayout(layout)
      
      # Create the tab widget with two tabs
      tabs = QTabWidget()
      tabs.addTab(self.generalTabUI(), "General")
      tabs.addTab(self.networkTabUI(), "Network")
      layout.addWidget(tabs)
      
   def generalTabUI(self):
      # Create the UI for the General Page
      generalTab = QWidget()
      layout = QVBoxLayout()
      layout.addWidget(QCheckBox("Chaos"))
      layout.addWidget(QCheckBox("Imperium"))
      generalTab.setLayout(layout)
      return generalTab

   def networkTabUI(self):
      # Create the UI for the Network Page
      networkTab = QWidget()
      layout = QVBoxLayout()
      layout.addWidget(QCheckBox("Materium"))
      layout.addWidget(QCheckBox("Immaterium"))
      networkTab.setLayout(layout)
      return networkTab
   
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = Window()
   window.show()
   sys.exit(app.exec())