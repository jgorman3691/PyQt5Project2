#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
   QApplication,
   QGridLayout,
   QPushButton,
   QWidget
)

class Window(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle('QGridLayout v2.0')
      layout = QGridLayout()
      layout.addWidget(QPushButton("Button that Spans"), 0, 0, 1, 2)
      layout.addWidget(QPushButton("Button (1, 0)"), 1, 0)
      layout.addWidget(QPushButton("Button (1, 1)"), 1, 1)
      layout.addWidget(QPushButton("Button Spanner"), 2, 0, 2, 2)
      self.setLayout(layout)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   win = Window()
   win.show()
   sys.exit(app.exec())