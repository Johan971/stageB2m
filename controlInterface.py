#!/usr/bin/python3

import os, subprocess,time,asyncio,concurrent.futures
import scapy.all as sm
from PyQt5 import QtCore, QtGui, QtWidgets


timeMax=5
serviceName = "BCOMM_BASETES"

nssmFolder = "C:\\Users\\SUPPORT_COMMERCIAL\\Downloads\\nssm-2.24-101-g897c7ad\\win64"

async def checkingProcess():
	# print("\ncheckingProcess=================")
	ret = subprocess.run(
		os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
	)
	
	return str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")


def wiresharking(chrono):
	def callback(pkt):
		# print("\n\n\ncb=============")
		tmp=pkt.sprintf("\nSource :: Ether:%Ether.src% IP:%IP.src% =======> Destination :: Ether:%Ether.dst% IP:%IP.dst%")
		# print("l.42")
		# print("pkt",tmp)

		if (tmp!=""):
			chrono.reinit()
			chrono.checkingTime()
			print("reinit",chrono.chrono)
		

	sm.sniff(prn= callback,filter = 'dst port 12005')
	sm.sniff(prn= callback,filter = 'dst port 12006')
	return 1

class Chrono():
	def __init__(self):
		self.initialisation=time.time()
		self.chrono=1.1

	def checkingTime(self):
		self.chrono= time.time() - self.initialisation

	def reinit(self):
		self.initialisation=time.time()



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

	def processFrozen(self):
		pass

	def ExchangesOkay(self):
		pass

	def processNotResponding(self):
		pass



def main():
	#DANS LE MAINS ON utilise Les fonctions aux bon moment
	async def  functionn():
		chrono=Chrono()
		returnValue=await checkingProcess()

		with concurrent.futures.ThreadPoolExecutor() as executor:

			while (returnValue=="SERVICE_RUNNING" and chrono.chrono<=timeMax):

				executor.submit(wiresharking,chrono)
				await asyncio.sleep(0.5)
				chrono.checkingTime()
				print("chrono",chrono.chrono)
				returnValue=await checkingProcess()
				print("l.62")

				while returnValue!="SERVICE_RUNNING":
					print("ERREUR : service stoppé !")
					chrono.reinit()
					returnValue = await checkingProcess()

				if(chrono.chrono>=timeMax):
					chronoDrama=Chrono()
					chrono.reinit()
					while(chrono.chrono>=timeMax):
						print("\n\n=====FROZEN=====")

						chronoDrama.checkingTime()
						await asyncio.sleep(0.5)
						executor.submit(wiresharking,chrono)

			# print("\n\n============jesors================\n\n")

		with concurrent.futures.ThreadPoolExecutor() as executor:

			while returnValue!="SERVICE_RUNNING":

				print("ERREUR :  service stoppé !")
				chrono.reinit()
				returnValue = await checkingProcess()

				while (returnValue=="SERVICE_RUNNING" and chrono.chrono<=timeMax):

					executor.submit(wiresharking,chrono)
					await asyncio.sleep(0.5)
					chrono.checkingTime()
					print("chrono",chrono.chrono)
					returnValue=await checkingProcess()
					print("l.96")

					while returnValue!="SERVICE_RUNNING":
						print("ERREUR : service stoppé !")
						chrono.reinit()
						returnValue = await checkingProcess()

					if(chrono.chrono>=timeMax):
						chronoDrama=Chrono()
						chrono.reinit()
						while(chrono.chrono>=timeMax):
							print("\n\n=====FROZEN=====")

							chronoDrama.checkingTime()
							await asyncio.sleep(0.5)
							executor.submit(wiresharking,chrono)
	asyncio.run(functionn())


if __name__ == "__main__":
	##Main et window en boucle infinie faut gerer avec events !!!! 
	import sys
	main()
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec())

	
