#!/bin/bash
pyside2_uic res/GUI.ui > src/raspbioloid_gui/GUI.py
sed -i '10ifrom motor_loop_qt_demo.custom_spin_box import *' src/raspbioloid_gui/GUI.py
sed -i 's/QtWidgets.QDoubleSpinBox/CustomSpinBox/g' src/raspbioloid_gui/GUI.py
pyrcc5 res/resources.qrc > src/raspbioloid_gui/resources_rc.py
