import shutil, os
import threading, queue
import PyQt5

def renaming(firstPath,basePath,pbar,label):
	
	# firstPath=input("Entrez le chemin des fichiers à intégrer :\n")
	# basePath=input("Entrez le chemin du dossier magasin (ex: 'D:\\WKW3\\$ZBASE') :\n")
	dossier=os.listdir(firstPath)
	importFolder=os.path.join(basePath,"IMPORT")
	cpt=1
	pbar.setValue(cpt)
	for fichiers in dossier:

		try:
			if(str(fichiers)=="PDA_ANDROID"):
				# print("raising")
				raise PermissionError("PDA_ANDROID")
			a=str(firstPath) +"\\"+ fichiers
			dest= importFolder+"\\"+str(cpt)+"_"+"IMPORT.ASC"
			shutil.copy2(a,dest)
			cpt+=1
			pbar.setValue(cpt*30//len(dossier))
		except PermissionError as inst:
			
			if(str(inst.args[0])=="PDA_ANDROID"):
				print("pass : not a file.")
			else:
				strr="ERREUR:  "+str(inst.args[1])+"."
				label.setText(strr)
				print(inst.args)
				pbar.setValue(0)
				return strr

		except Exception as inst:
			strr="ERREUR:  "+str(inst.args[1])+"."
			label.setText(strr)
			print(inst.args)
			pbar.setValue(0)
			return strr
	label.setText("Copie des fichiers terminée.\nTransfert vers Kwisatz.")
	return [importFolder,basePath]
	
	# print(str(a[2])[1::]) #trouver zbase
	
	# =========Partie envoi avec automate
def importing(importFolder,basePath,pbar,label):
	
	val=30
	pbar.setValue(val)
	a=basePath.split("\\")
	dossier=os.listdir(importFolder)
	cpt=0
	def cmd():
		print("importing")
		# proc = Popen(["{}:\\WKW3\\kwisatz.exe".format(basePath[0]), "-a142", "-d{}".format(str(a[2])[1::]), "-p99"], stdout=PIPE, stderr=PIPE, encoding='utf8', errors='ignore')
		proc=os.system("{}:\\WKW3\\kwisatz.exe -a142 -d{} -p99".format(basePath[0],str(a[2])[1::]))
		
		PyQt5.QtWidgets.QApplication.processEvents()
		label.setText("Transfert éléments {}/{}.".format(cpt,len(dossier)))
		return 1

	for fichiers in dossier:
		try:
			type(int(fichiers[0]))
		except:
			print("not a right file.")
		try:
			step=30+cpt*70//len(dossier) #de 30 à 70
			print(val,step)
			pbar.setValue(step)
			# print(str(fichiers))
			if(str(fichiers)=="PDA_ANDROID"):
				print("raising")
				raise PermissionError("PDA_ANDROID")
			# trying=type(int(fichiers[0])) #subteruge pour ne pas envoyer le dossier
			
			pbar.setValue(step)
			
			filePath=os.path.join(importFolder,fichiers)
			newFile=os.path.join(importFolder,"IMPORTDOC.ASC")
			print(filePath,"->",newFile)

			os.rename(filePath, newFile)
			PyQt5.QtWidgets.QApplication.processEvents()
			th2=threading.Thread(target=cmd)
			th2.start()
			PyQt5.QtWidgets.QApplication.processEvents()
			th2.join()
			PyQt5.QtWidgets.QApplication.processEvents()
			# os.system("{}:\\WKW3\\kwisatz.exe -a142 -d{} -p99".format(basePath[0],str(a[2])[1::]))
			pbar.setValue(step)
			cpt+=1
			# os.rename(newFile, filePath) #we can't name to thing import.asc
			# input("debug")

		except PermissionError as inst:
			
			if(str(inst.args[0])=="PDA_ANDROID"):
				print("pass : not a file.")
			else:
				strr="ERREUR:  "+str(inst.args[1])+"."
				label.setText(strr)
				print(inst.args)
				pbar.setValue(0)
				return -1

		except Exception as inst:
			print(inst.args)

			if (type(inst.args[0])==type(5)):
				print("not",inst.args)
				print(type(inst.args[0]))
				label.setText(str(inst.args))
			else:
				label.setText(str(inst.args))
			return -1
	pbar.setValue(100)
	label.setText("Fin de l'exportation des bons de commandes.")
	return 1