#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
   QApplication,
   QVBoxLayout,
   QWidget,
   QPushButton
)

class Window(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle('QVBoxLayout Example')
      self.resize(270, 110)
      layout = QVBoxLayout()
      layout.addWidget(QPushButton("Top"))
      layout.addWidget(QPushButton("Center"))
      layout.addWidget(QPushButton("Bottom"))
      layout.addStretch()
      self.setLayout(layout)
      
if __name__ == '__main__':
   app = QApplication(sys.argv)
   win = Window()
   win.show()
   sys.exit(app.exec())