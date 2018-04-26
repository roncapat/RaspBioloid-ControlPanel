#!/usr/bin/env python

import rospy
from std_msgs.msg import String, Float32
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import GUI

from mopi.srv import *

class Application(QMainWindow):
	def __init__(self):
		super(Application, self).__init__()
		self.ui = GUI.Ui_MainWindow()
		self.ui.setupUi(self)
		rospy.init_node('raspbioloid_control_panel', anonymous=True)
		rospy.Subscriber("battery_lvl", Float32, self.callback)

	def something(self):
		self.setValueMotor(5,5);
		print(self.getValueMotor(1))

	def callback(self, res):
		self.ui.voltage.setText(str(res.data))

def main():
	app = QApplication(sys.argv)
	form = Application()
	form.show()
	app.exec_()

if __name__ == '__main__':
	try:	
		main()
	except rospy.ROSInterruptException:
		pass
