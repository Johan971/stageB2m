import shutil, os

firstPath=input("Entrez le chemin des fichiers à intégrer :\n")
basePath=input("Entrez le chemin du dossier magasin (ex: 'D:\\WKW3\\$ZBASE') :\n")
dossier=os.listdir(firstPath)
importFolder=os.path.join(basePath,"IMPORT")

cpt=1
for fichiers in dossier:
	
	a=str(firstPath) +"\\"+ fichiers
	dest= importFolder+"\\"+str(cpt)+"_"+"IMPORT.ASC"
	shutil.copy2(a,dest)
	cpt+=1
	
input("Point d'arrêt, appuyez sur Entrée pour continuer et commencer l'intégration.\n")
# =========Partie envoi avec automate

dossier=os.listdir(importFolder)
for fichiers in dossier:
	try:
		trying=type(int(fichiers[0])) #subterufge pour ne pas envoyer le dossier
		filePath=os.path.join(importFolder,fichiers)
		newFile=os.path.join(importFolder,"IMPORTDOC.ASC")
		print(filePath,newFile)
		os.rename(filePath, newFile)
		os.system("D:\\WKW3\\kwisatz.exe -a142 -dZBASE -p99")
		# os.rename(newFile, filePath) #we can't name to thing import.asc
		# input("debug")
	except:
		print("pass : not a file.")

input("\nFin. Appuyez sur Entrée pour finir")