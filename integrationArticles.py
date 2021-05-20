import shutil, os
def integration(articlesPath,basePath,pbar,label):
	try:

		a=articlesPath.split("\\")
		b=basePath.split("\\")
		wkw3=os.path.dirname(basePath)
		baseFolder=str(b[2])[1::]
		
		if (str(a[-1]).upper()!="ARTICLE.DAT"): #gestion si user fait rentrer article.dat ou pas
			articlesPath=os.path.join(articlesPath,"article.dat")

		print("\nCONVERSION ET INTEGRATION DES ARTICLES VENANT DU SIEGE...\n")
		pbar.setValue(2)

		os.system("{} -PImpArtDdr2 -S{} -C{}".format(os.path.join(wkw3,"wkw_convert_ascii.exe"),articlesPath,os.path.join(basePath,"import")))
		pbar.setValue(30)
		os.system("{} -A129 -D{} -P99".format(os.path.join(wkw3,"kwisatz.exe"),baseFolder))
		pbar.setValue(50)
		print("\nMISE À JOUR DES ARTICLES VERS LES CAISSES...\n")
		# label.setText("\nMISE À JOUR DES ARTICLES VERS LES CAISSES...\n")

		os.system("{} -A1 -D{} -P99".format(os.path.join(wkw3,"kwisatz.exe"),baseFolder))
		pbar.setValue(80)
		tmp=os.path.join(os.path.dirname(articlesPath),"article.old")
		pbar.setValue(90)
		if(os.path.exists(tmp)):
			os.remove(tmp)
		os.rename(articlesPath,tmp)
		pbar.setValue(95)

	except Exception as inst:
		strr="ERREUR:  "+str(inst.args[1])+"."
		label.setText(strr)
		print(inst.args)
		pbar.setValue(0)
		return -1
	print("\nFIN.\n")
	pbar.setValue(100)
	label.setText("Fin de l'exportation des articles.")
	return 1

if __name__ == "__main__":

	"""===========SUPPRIMER LE 3e ARGUMENT ET TOUT CE QUI CONCERNE LE LABEL============="""
	
	articlesPath=input("Entrez le chemin des articles à récupérer :\n") #obligé parce qu'on sait pas la lettre
	basePath=input("Entrez le chemin du dossier magasin (ex: 'D:\\WKW3\\$ZBASE') :\n")
	integration(articlesPath, basePath)