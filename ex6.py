#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import (
   QApplication,
   QVBoxLayout,
   QFormLayout,
   QWidget,
   QLabel,
   QLineEdit,
   QCheckBox
)

class Window(QWidget):
   def __init__(self):
      super().__init__()
      self.setWindowTitle("Nested Layouts Example")

      # Create an outer layout
      outerLayout = QVBoxLayout()

      # Create a form layout for the label and line edit
      topLayout = QFormLayout()

      # Add a label and a line to the form layout
      topLayout.addRow("Chaos:", QLineEdit())

      # Create a layout for the checkboxes
      optionsLayout = QVBoxLayout()

      # Add some checkboxes to the options
      optionsLayout.addWidget(QCheckBox("Khorne"))
      optionsLayout.addWidget(QCheckBox("Tzeentch"))
      optionsLayout.addWidget(QCheckBox("Nurgle"))
      optionsLayout.addWidget(QCheckBox("Slaanesh"))
      
      # Nest the inner layouts into the outer layout
      outerLayout.addLayout(topLayout)
      outerLayout.addLayout(optionsLayout)
      
      # Set the window's main layout
      self.setLayout(outerLayout)
      
if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = Window()
   window.show()
   sys.exit(app.exec())