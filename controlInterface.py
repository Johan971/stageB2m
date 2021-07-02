#!/usr/bin/python3

import os, subprocess,time,asyncio,concurrent.futures,sys
import scapy.all as sm
from PyQt5 import QtCore, QtGui, QtWidgets

class windowState():
	def __init__(self):
		self.state="Unknown"
	def correctState(self):
		self.state="OK"
	def processFrozen(self):
		self.state="processFrozen"
	def processDead(self):
		self.state="processDead"

class Chrono():
	def __init__(self):
		self.initialisation=time.time()
		self.chrono=1.1

	def checkingTime(self):
		QtWidgets.QApplication.processEvents()
		self.chrono= time.time() - self.initialisation

	def reinit(self):
		QtWidgets.QApplication.processEvents()
		self.initialisation=time.time()


#======================================================================== GLOBAL VARIABLES ==========================================================================#

timeMax=5
serviceName = "BCOMM_BASETES"
nssmFolder = "C:\\Users\\SUPPORT_COMMERCIAL\\Downloads\\nssm-2.24-101-g897c7ad\\win64"
state=windowState()
chrono=Chrono()
#===============================================================================================================================================================#

#====================================================================== DECLARATION ===========================================================================#

#checking if BCOMM service is running
async def checkingProcess():
	# print("\ncheckingProcess=================")
	ret = subprocess.run(
		os.path.join(nssmFolder, "nssm.exe") + " status " + serviceName, capture_output=True
	)
	QtWidgets.QApplication.processEvents()
	return str(ret.stdout.decode("utf-8")).replace("\r", "").replace("\n", "")


#checking if we receive packets in the rights ports
def wiresharking(chrono):
	def callback(pkt):
		# print("\n\n\ncb=============")
		QtWidgets.QApplication.processEvents()
		tmp=pkt.sprintf("\nSource :: Ether:%Ether.src% IP:%IP.src% =======> Destination :: Ether:%Ether.dst% IP:%IP.dst%")
		# print("l.42")
		# print("pkt",tmp)

		if (tmp!=""):
			chrono.reinit()
			chrono.checkingTime()
			print("reinit",chrono.chrono)
		

	sm.sniff(prn= callback,filter = 'dst port 12005')
	QtWidgets.QApplication.processEvents()
	sm.sniff(prn= callback,filter = 'dst port 12006')
	return 1


#windows declaration
class Ui_MainWindow(object):
	#main program
	def main(self):
		#needed an asyn function : so we work in it
		async def  functionn():
			
			returnValue=await checkingProcess()
			self.startButton.setMaximumSize(QtCore.QSize(0, 0))
			with concurrent.futures.ThreadPoolExecutor() as executor: #Threads

				while (returnValue=="SERVICE_RUNNING" and chrono.chrono<=timeMax):
					QtWidgets.QApplication.processEvents() #This line is useful to prevent windows freezing
					self.ExchangesOkay()
					executor.submit(wiresharking,chrono) #threadMethod
					await asyncio.sleep(0.5) #threadMethod too
					QtWidgets.QApplication.processEvents()
					chrono.checkingTime()
					returnValue=await checkingProcess()


					# print("chrono",chrono.chrono)
					# print("l.62")

					while returnValue!="SERVICE_RUNNING":
						QtWidgets.QApplication.processEvents()
						self.processDead()
						print("ERREUR : service stoppé !")
						chrono.reinit()
						returnValue = await checkingProcess()

					if(chrono.chrono>=timeMax):
				
						while(chrono.chrono>=timeMax):
							# print("\n\n=====FROZEN=====")
							self.processFrozen()
							# print("chrono",chrono.chrono)
							QtWidgets.QApplication.processEvents()
							await asyncio.sleep(0.5)
							QtWidgets.QApplication.processEvents()
							chrono.checkingTime()
							executor.submit(wiresharking,chrono)

				# print("\n\n============jesors================\n\n")

			with concurrent.futures.ThreadPoolExecutor() as executor: #Thread s

				while returnValue!="SERVICE_RUNNING":

					QtWidgets.QApplication.processEvents()
					self.processDead()
					# print("ERREUR :  service stoppé !")
					chrono.reinit()
					returnValue = await checkingProcess()

					while (returnValue=="SERVICE_RUNNING" and chrono.chrono<=timeMax):
						QtWidgets.QApplication.processEvents()
						self.ExchangesOkay()
						executor.submit(wiresharking,chrono) #Chrono is an argument of wireshaking()
						await asyncio.sleep(0.5)
						QtWidgets.QApplication.processEvents()
						chrono.checkingTime()
						returnValue=await checkingProcess()
						# print("chrono",chrono.chrono)
						# print("l.96")

						while returnValue!="SERVICE_RUNNING":
							QtWidgets.QApplication.processEvents()
							self.processDead()
							# print("ERREUR : service arrété !")
							chrono.checkingTime()
							returnValue = await checkingProcess()

						if(chrono.chrono>=timeMax):
							while(chrono.chrono>=timeMax):
								QtWidgets.QApplication.processEvents()
								# print("\n\n=====FROZEN=====")
								self.processFrozen()
								chrono.checkingTime()
								await asyncio.sleep(0.5)
								QtWidgets.QApplication.processEvents()
								executor.submit(wiresharking,chrono)
		asyncio.run(functionn())

	def processFrozen(self):
		self.MainWindow.setStyleSheet("background-color: red;")
		chrono.checkingTime()
		# print("eee")
		# print(chrono.chrono)
		self.label.setText("BCOMM/FCOMM ne répond pas \nDernier packet reçu il y a {} secondes".format(int(chrono.chrono)))

	def ExchangesOkay(self):
		self.MainWindow.setStyleSheet("background-color: green;")
		self.label.setText("BCOMM/FCOMM en état de fonctionnement\nDernier packet reçu il y a {} secondes".format(int(chrono.chrono)))


	def processDead(self):
		self.MainWindow.setStyleSheet("background-color: red;")
		self.label.setText("BCOMM/FCOMM en non exécution \nDernier packet reçu il y a {} secondes".format(int(chrono.chrono)))
		
	def retranslateUi(self):
		_translate = QtCore.QCoreApplication.translate
		self.MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "Interface de contrôle des modules BCOMM/FCOMM"))
		self.startButton.setText(_translate("MainWindow", "Démarrer"))

	def setupUi(self, MainWindow):
		self.MainWindow=MainWindow
		self.MainWindow.setObjectName("MainWindow")
		self.MainWindow.resize(678, 285)
		self.centralwidget = QtWidgets.QWidget(self.MainWindow)
		self.centralwidget.setObjectName("centralwidget")

		self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
		self.gridLayout.setObjectName("gridLayout")

		self.label = QtWidgets.QLabel(self.centralwidget)
		font = QtGui.QFont()
		font.setFamily("Yu Gothic UI Semibold")
		font.setPointSize(20)
		self.label.setFont(font)

		self.label.setTextFormat(QtCore.Qt.AutoText)
		self.label.setScaledContents(False)
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

		self.startButton = QtWidgets.QPushButton(self.centralwidget)
		self.startButton.setMaximumSize(QtCore.QSize(200, 30))
		self.startButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.startButton.setObjectName("startButton")

		self.startButton.clicked.connect(self.main)

		self.gridLayout.addWidget(self.startButton, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)

		self.MainWindow.setCentralWidget(self.centralwidget)
		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

#===============================================================================================================================================================#


#================================================================================ MAIN ========================================================================#
if __name__ == "__main__":
	
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.setWindowIcon(QtGui.QIcon("b2m.ico"))
	sys.exit(app.exec())
	MainWindow.show()

#===============================================================================================================================================================#
