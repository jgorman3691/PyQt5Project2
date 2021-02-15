#!/usr/bin/env python3

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
   QApplication,
   QWidget,
   # QLineEdit
   QPushButton,
   QGridLayout
)

class Window(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle('QGridLayout Example')
      layout = QGridLayout()
      # self.text = QLineEdit()
      # self.text.setAlignment(Qt.AlignRight)
      # self.text.setFixedHeight(35)
      # self.text.setReadOnly(True)
      # layout.addWidget(self.text, 0, 0, 1, 3)
      layout.addWidget(QPushButton("Button ( 0, 0)"), 0, 0)
      layout.addWidget(QPushButton("Button ( 0, 1)"), 0, 1)
      layout.addWidget(QPushButton("Button ( 0, 2)"), 0, 2)
      layout.addWidget(QPushButton("Button ( 1, 0)"), 1, 0)
      layout.addWidget(QPushButton("Button ( 1, 1)"), 1, 1)
      layout.addWidget(QPushButton("Button ( 1, 2)"), 1, 2)
      layout.addWidget(QPushButton("Button ( 2, 0)"), 2, 0)
      layout.addWidget(QPushButton("Button ( 2, 1)"), 2, 1)
      layout.addWidget(QPushButton("Button ( 2, 2)"), 2, 2)
      self.setLayout(layout)
   
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = Window()
   window.show()
   sys.exit(app.exec())