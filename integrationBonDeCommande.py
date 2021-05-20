import shutil, os
from subprocess import Popen, PIPE
import threading, queue
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
				
			# print(cpt*30//len(dossier),fichiers)
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
				return -1

		except Exception as inst:
			strr="ERREUR:  "+str(inst.args[1])+"."
			label.setText(strr)
			print(inst.args)
			pbar.setValue(0)
			return -1
	label.setText("Cope des fichiers terminée.\nTransfert vers Kwisatz.")
	return [importFolder,basePath]
	

	# print(str(a[2])[1::]) #trouver zbase
	# input("Point d'arrêt, appuyez sur Entrée pour continuer et commencer l'intégration.\n")
	# =========Partie envoi avec automate
def importing(importFolder,basePath,pbar,label):
	locker=threading.Lock()
	val=31
	pbar.setValue(val)
	a=basePath.split("\\")
	dossier=os.listdir(importFolder)
	val+=1
	pbar.setValue(val)
	# print("Command: ","{}:\\WKW3\\kwisatz.exe -a142 -d{} -p99".format(basePath[0],str(a[2])[1::]))
	cpt=1
	print(dossier)
	def cmd():
		locker.acquire()
		# proc = Popen(["{}:\\WKW3\\kwisatz.exe".format(basePath[0]), "-a142", "-d{}".format(str(a[2])[1::]), "-p99"], stdout=PIPE, stderr=PIPE, encoding='utf8', errors='ignore')
		proc=os.system("{}:\\WKW3\\kwisatz.exe -a142 -d{} -p99".format(basePath[0],str(a[2])[1::]))
		###Gerer la lenteur de l'exction de la commande
		print("okokokok",proc)
		locker.release()
	th2=threading.Thread(target=cmd)

	def renaming():
		locker.acquire()
		# filePath=os.path.join(importFolder,fichiers)
		print("rrr")
		# newFile=os.path.join(importFolder,"IMPORTDOC.ASC")
		# print(filePath,"->",newFile)

		# os.rename(filePath, newFile)
		# print("renamed")
		locker.release()
	th1=threading.Thread(target=renaming)

	for fichiers in dossier:
		try:
			type(int(fichiers[0]))
		except:
			print("not a right file.")
		try:
			step=val+cpt*70//len(dossier) #de 30 à 70
			print(val,step)
			pbar.setValue(step)
			# print(str(fichiers))
			if(str(fichiers)=="PDA_ANDROID"):
				raise PermissionError("PDA_ANDROID")
			# trying=type(int(fichiers[0])) #subteruge pour ne pas envoyer le dossier
			
			pbar.setValue(step)
			
			filePath=os.path.join(importFolder,fichiers)
			print("renaming")
			newFile=os.path.join(importFolder,"IMPORTDOC.ASC")
			print(filePath,"->",newFile)

			os.rename(filePath, newFile)
			print("renamed")

			# print("humm",th2.started)
			th2.start()
			th1.start()
			th2.join()
			th1.join()

			print("apres th")
			# os.system("{}:\\WKW3\\kwisatz.exe -a142 -d{} -p99".format(basePath[0],str(a[2])[1::]))
			pbar.setValue(step)
			val+=1
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
				label.setText(str(inst.args[1]))
			else:
				label.setText(str(inst.args[0]))
			return -1
			# input("break debug")
	label.setText("Fin de l'exportation des bons de commandes.")
	return 1


# input("\nFin. Appuyez sur Entrée pour finir")