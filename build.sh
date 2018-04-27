#!/bin/bash
pyuic5 res/GUI.ui > src/raspbioloid_gui/GUI.py
pyrcc5 res/resources.qrc > src/raspbioloid_gui/resources_rc.py
