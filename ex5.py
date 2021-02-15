#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
   QApplication,
   QFormLayout,
   QLabel,
   QLineEdit,
   QWidget
)

class Window(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle("QFormLayout Example")
      self.resize(270, 110)
      layout = QFormLayout()
      layout.addRow("Name:", QLineEdit())
      layout.addRow("Job:", QLineEdit())
      emailLabel = QLabel("Email:")
      layout.addRow(emailLabel, QLineEdit())
      self.setLayout(layout)
      
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = Window()
   window.show()
   sys.exit(app.exec())