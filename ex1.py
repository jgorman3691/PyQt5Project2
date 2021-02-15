#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
   QApplication,
   QWidget,
   QHBoxLayout,
   QPushButton
)

class Window(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle('QHBoxLayout Example')
      layout = QHBoxLayout()
      layout.addWidget(QPushButton("Left-Most"))
      layout.addWidget(QPushButton("Center"), 1)
      layout.addWidget(QPushButton("Right-Most"), 2)
      self.setLayout(layout)
      print(self.children())


if __name__ == '__main__':
   app = QApplication(sys.argv)
   win = Window()
   win.show()
   sys.exit(app.exec())
