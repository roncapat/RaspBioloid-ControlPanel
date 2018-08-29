#!/usr/bin/env python

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class CustomSpinBox(QDoubleSpinBox):
    enterKeyPressed = Signal(float)
    
    def __init__(self, name):
        QDoubleSpinBox.__init__(self, name)
    
    def keyPressEvent(self, event):
        super(CustomSpinBox, self).keyPressEvent(event)
        if event.key() in [Qt.Key_Enter, Qt.Key_Return, Qt.Key_Up, Qt.Key_Down]:
            self.enterKeyPressed.emit(self.value())
            #self.clearFocus()
                
    @Slot(int, int)
    def setStatus(self, raw_position, raw_goal, raw_load):
      position = raw_position/1024.0*300
      if abs(raw_load)>160:
        self.setStyleSheet("background-color:rgb(255, 120, 120)")
      elif abs(raw_position - raw_goal) < 5:
        self.setStyleSheet("background-color:lightgreen")
      else:
        self.setStyleSheet("background-color:white")
      
      if (not self.hasFocus()):
        self.setValue(position)
