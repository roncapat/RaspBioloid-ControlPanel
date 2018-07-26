#!/usr/bin/env python

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class CustomSpinBox(QDoubleSpinBox):
    enterKeyPressed = Signal(float)
    
    def __init__(self, name):
        QDoubleSpinBox.__init__(self, name)
        self.goalValue = None
    
    def keyPressEvent(self, event):
        super(CustomSpinBox, self).keyPressEvent(event)
        if event.key() in [Qt.Key_Enter, Qt.Key_Return]:
            self.goalValue = self.value()
            self.enterKeyPressed.emit(self.goalValue)
            self.clearFocus()
                
    @Slot(int, int)
    def setStatus(self, raw_position, raw_load):
      position = raw_position/1024.0*360
      warning = abs(raw_load)>128
      if warning:
        self.setStyleSheet("background-color:rgb(255, 120, 120);")
      elif (self.goalValue is not None) and (abs(position - self.goalValue) < 1):
        self.setStyleSheet("background-color:lightgreen")
      else:
        self.setStyleSheet("background-color:white")
      
      if (not self.hasFocus()):
        self.setValue(position)
