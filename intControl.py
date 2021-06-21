#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(790, 253)

		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")

		self.label = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI Semibold")
		font.setPointSize(20)
		self.label.setFont(font)

		self.label.setTextFormat(QtCore.Qt.AutoText)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "BCOMM/FCOMM en état de fonctionnement\n"
"Dernier packet reçu il y a "))

	def processFrozen():
		pass

	def exchangesOkay():
		pass

	def processNotResponding():
		pass


if __name__ == "__main__":
	import sys
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec())
