#!/usr/bin/env python

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CustomSpinBox(QDoubleSpinBox):
    enterKeyPressed = pyqtSignal(float)
    
    def __init__(self, name):
        QDoubleSpinBox.__init__(self, name)
        self.goalValue = None
        self.valueChanged.connect(self.onValueChanged)
    
    def keyPressEvent(self, event):
        super(CustomSpinBox, self).keyPressEvent(event)
        if event.key() in [Qt.Key_Enter, Qt.Key_Return]:
            self.goalValue = self.value()
            self.enterKeyPressed.emit(self.goalValue)
            self.clearFocus()
    
    def onValueChanged(self, value):
        p = self.palette()
        if self.goalValue is not None:
            if abs(value - self.goalValue) < 0.5:
                p.setColor(QPalette.Base, Qt.green)
            else:
                p.setColor(QPalette.Base, Qt.white)
            self.setPalette(p)

