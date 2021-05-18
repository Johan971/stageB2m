import shutil, os

firstPath=input("Entrez le chemin des fichiers à intégrer :\n")
basePath=input("Entrez le chemin du dossier magasin (ex: 'D:\\WKW3\\$ZBASE') :\n")
dossier=os.listdir(firstPath)
importFolder=os.path.join(basePath,"IMPORT")
print(basePath[0])
cpt=1
for fichiers in dossier:
	try:
		if(str(fichiers)=="PDA_ANDROID"):
			raise Exception
			
		print("2",fichiers)
		a=str(firstPath) +"\\"+ fichiers
		dest= importFolder+"\\"+str(cpt)+"_"+"IMPORT.ASC"
		shutil.copy2(a,dest)
		cpt+=1
	except:
		print("pass : not a file.")

a=basePath.split("\\")
# print(str(a[2])[1::]) #trouver zbase 
input("Point d'arrêt, appuyez sur Entrée pour continuer et commencer l'intégration.\n")
# =========Partie envoi avec automate

dossier=os.listdir(importFolder)
print("Command: ","{}:\\WKW3\\kwisatz.exe -a142 -d{} -p99".format(basePath[0],str(a[2])[1::]))
for fichiers in dossier:
	try:
		# print(str(fichiers))
		if(str(fichiers)=="PDA_ANDROID"):
			raise Exception("PDA_ANDROID")
		# trying=type(int(fichiers[0])) #subterufge pour ne pas envoyer le dossier
		filePath=os.path.join(importFolder,fichiers)
		newFile=os.path.join(importFolder,"IMPORTDOC.ASC")
		print(filePath,newFile)
		os.rename(filePath, newFile)

		os.system("{}:\\WKW3\\kwisatz.exe -a142 -d{} -p99".format(basePath[0],str(a[2])[1::]))
		# os.rename(newFile, filePath) #we can't name to thing import.asc
		# input("debug")
	except Exception as inst:
		print(inst.args)
		input("break debug")


input("\nFin. Appuyez sur Entrée pour finir")