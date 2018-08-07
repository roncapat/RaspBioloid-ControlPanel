cmake_minimum_required(VERSION 2.8.3)
project(raspbioloid_gui)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  pico_msgs
  motors_msgs
  motors_srvs
)
catkin_python_setup()

set (qt_ui_src   "res/GUI.ui")
set (qt_qrc_src  "res/resources.qrc")
set (py_ui_dest  "src/raspbioloid_gui/GUI.py")
set (py_qrc_dest "src/raspbioloid_gui/resources_rc.py")

execute_process(COMMAND pyside2-uic ${qt_ui_src} 
                WORKING_DIRECTORY ${raspbioloid_gui_SOURCE_DIR}
                OUTPUT_FILE ${py_ui_dest})

execute_process(COMMAND sed -i "10ifrom raspbioloid_gui.custom_spin_box import *" ${py_ui_dest}
                WORKING_DIRECTORY ${raspbioloid_gui_SOURCE_DIR})

execute_process(COMMAND sed -i "s/QtWidgets.QDoubleSpinBox/CustomSpinBox/g" ${py_ui_dest}
                WORKING_DIRECTORY ${raspbioloid_gui_SOURCE_DIR})

execute_process(COMMAND pyside2-rcc -py2 ${qt_qrc_src}
                WORKING_DIRECTORY ${raspbioloid_gui_SOURCE_DIR}
                OUTPUT_FILE ${py_qrc_dest})

message(STATUS "Generated Python modules from Qt resources")

catkin_package(
  CATKIN_DEPENDS   rospy std_msgs pico_msgs motors_msgs motors_srvs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

install(PROGRAMS
  nodes/raspbioloid_gui
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
