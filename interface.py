#!/usr/bin/python

import sys
import PyQt6.QtWidgets as wd
from PyQt6.QtWidgets import QApplication, QWidget


class Fenetre(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		# super().__init__()
		self.setWindowTitle("Interface de contrôle")

		# Creaton éléments de base
		self.layout = wd.QVBoxLayout()

		self.bouton = wd.QPushButton("bouton",self)
		self.label = wd.QLabel("hello hi",self)
		
		
		
		self.bouton.clicked.connect(self.appuiBouton1)

		
		self.bouton.resize(50, 20)
		# self.setLayout(self.layout)
		widgets = [
		            wd.QCheckBox,
		            wd.QComboBox,
		            wd.QDateEdit,
		            wd.QDateTimeEdit,
		            wd.QDial,
		            wd.QDoubleSpinBox,
		            wd.QFontComboBox,
		            wd.QLCDNumber,
		            wd.QLabel,
		            wd.QLineEdit,
		            wd.QProgressBar,
		            wd.QPushButton,
		            wd.QRadioButton,
		            wd.QSlider,
		            wd.QSpinBox,
		            wd.QTimeEdit,
		        ]
		# for w in widgets:
			# self.layout.addWidget(w())

		self.show()
	def mousePressEvent(self, event):
		print("appui",event.button())
		# print("pos:",event.x(),event.y())

	def appuiBouton1(self):
			print("bouton appuyé")






def main():

    # Première étape : création d'une application Qt avec QApplication
    #    afin d'avoir un fonctionnement correct avec IDLE ou Spyder
    #    on vérifie s'il existe déjà une instance de QApplication
	app = QApplication.instance() 
	if not app: # sinon on crée une instance de QApplication
		app = QApplication(sys.argv)

	# création d'une fenêtre avec QWidget dont on place la référence dans fen
	fen = Fenetre()
	
	# on donne un titre à la fenêtre
	
	# on fixe la position de la fenêtre
	# fen.move(300,50)
	# la fenêtre est rendue visible
	fen.show()

	# exécution de l'application, l'exécution permet de gérer les événements
	app.exec()


if __name__ == '__main__':
    main()