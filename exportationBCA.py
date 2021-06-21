import os

import PyQt5

def exporting(basePath,pbar,label):
	
	# firstPath=input("Entrez le chemin des fichiers à intégrer :\n")
	# basePath=input("Entrez le chemin du dossier magasin (ex: 'D:\\WKW3\\$ZBASE') :\n")
	try:
		cpt=22
		pbar.setValue(cpt)
		label.setText("Execution de l'automate:\nVeuillez selectionner la période ainsi que les fichiers à exporter.")
		a=basePath.split("\\")
		os.system("{}:\\WKW3\\kwisatz.exe -a30 -d{} -p99".format(basePath[0],str(a[2])[1::]))
		cpt=100
		pbar.setValue(cpt)
		PyQt5.QtWidgets.QApplication.processEvents()
	except Exception as inst:
		pbar.setValue(0)
		label.setText("Erreur: {}".format(inst.args))
	

if __name__ == "__main__":
	exporting("D:\\WKW3\\$ZBASE1\\")