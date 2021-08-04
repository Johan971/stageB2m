import traceback, itertools
# WFM181035A.dat
# MLF_31803B.dat

## ============================ VARIABLES DECLARATION ======================= ##
entree=input("Entrez le chemin du fichier à traiter :\n")
file = open(str(entree))

content=file.read()
fileHeader=content[0:3]
nLines=content.count("\n")
# input(nLines)

output=open("output.asc","w")

## =========================== FUNCTIONS ================================ ##
def MLFpreProcessing(): #cut the file in several lines and return a list
	headlines=content.count("FFE")
	fLists=[content]
	if headlines>1:
		fLists= content.split("FFE")
		for i in range(len(fLists)):
			if i>0:			
				# input(fLists[i])
				tmpstr="FFE" + str(fLists[i])  # putting back the missing elmnt
				fLists[i]=tmpstr
		# input(fLists)
	for i in range(len(fLists)):
		lList=fLists[i].split("\n")
		if len(lList[-1])<=5:
			lList.pop()
			fLists[i]=lList
	cList = list(itertools.chain.from_iterable(fLists))
	if len(cList[-1])<=5:
		cList.pop()
	# input(cList)
	return cList

def WFMpreProcessing():
	fLists= content.split("\n")
	if len(fLists[-1])<=5:
			fLists.pop()
	# input(len(fLists))
	return fLists


## ======================== PROCESSING ================================ ##
def main():

	
	WFM=False
	MLF=False
	# docCharFinder(5,6)
	try:
		if type(int(fileHeader))==type(5):
			WFM=True

	except ValueError:
		MLF=True
	except:
		print(traceback.format_exc())

	if MLF:
		print("mlf")
		cList=MLFpreProcessing()

		# headercounter=0
		docDate=str(cList[0][17:19]+cList[0][15:17]+cList[0][11:15])
		refFourni=str(cList[1][22:24])
		# input(refFourni)
		correspondance={"20":"3","19":"2","30":"4","35":"90019","65":"90053","22":"164","54":"154","40":"135"}
		
		for line in cList:
			if line[0:3]=="FFE":
				output.write("FAA|E|||")
				try:
					output.write(correspondance[refFourni]) #société emetrice =code client ou fournisseur
				except:
					print(traceback.format_exc())
				output.write("|")
				output.write(docDate)
				output.write("|")
				output.write(line[75:88]+"|") #code magasin | code affaire
				output.write("|")
				output.write(str(int(line[3:11]))) #numerodoc
				output.write("\n")
				# print(line[75:88],len(line[75:88]))

			elif line[0:3]=="FFL":
				output.write("FAA|C|")
				output.write(line[23:36]) #EAN13
				output.write("|")
				output.write("|") #no libelle produit
				output.write("|")
				try:
					pcb=int(line[86:92])
					nbrCol=int(line[49:65])
					quantity=pcb*nbrCol
					# input(quantity)
				except :
					print(traceback.format_exc())
				output.write(str(quantity)) #good quantity
				output.write("|")
				# input(line[190:203])
				output.write(line[190:203]+"|") #price
				output.write("|")
				output.write("|")
				# output.write(line[190:203])
				output.write("\n")

	elif WFM:
		print("wfm")
		print("\nImpossible de traiter les WFM : pas de reference fournisseur (autre(s) erreur(s) dans le document).")
		return -1
		cList=WFMpreProcessing()
		codeFourniAS400=cList[0][1:3] #pas bon : correspond au code region 
		input(codeFourniAS400)
		try:
			if(int(cList[0][0])==1):
				correspondance={"22":"164","54":"154","40":"135"}
			elif(int(cList[0][0])==2):
				correspondance={"20":"3","19":"2","30":"4","35":"90019","65":"90053"}
			else:
				print("mauvais code région détecté")
				raise ValueError
		except:
			print(traceback.format_exc())

		# input(codeClientFourni)
		# codeClient="00"+str(cList[0][26:32])
		dateDoc=cList[0][24:26] + cList[0][22:24] + cList[0][18:22]
		codeMagasin=cList[0][3:5]
		numeroDoc=cList[0][8:18]
		

		# print("codeClientFourni {}\n datedoc {}\n codeMagasin {}\n numeroDoc {}\n".format(codeFourniAS400,dateDoc,codeMagasin,numeroDoc))
		
		output.write("BRA|E|||")
		try:
			input(correspondance[str(codeFourniAS400)])
			output.write(correspondance[str(codeFourniAS400)])
			# print(correspondance[str(codeFourniAS400)])
		except:
			print(traceback.format_exc())
		
		output.write("|")
		output.write(dateDoc)
		output.write("|")
		output.write(codeMagasin+"|")
		output.write("|")
		output.write(numeroDoc)
		output.write("\n")

		for line in cList:
			output.write("BRA|C")
			output.write("|")
			output.write(line[88:101]) #EAN13
			output.write("|")
			# output.write("") #dont have
			output.write("|") 
			output.write(line[58:88]) #libellé article
			output.write("|")
			
			quantity=int(line[105:111])*int(line[101:105]) #quantité uc (modifiée)* nbr colis
			output.write(str(quantity)) #quantite

			output.write("|")
			 #PUHT
			
			tmpPrice=str(int(line[114:125]))
			price=tmpPrice[0:(len(tmpPrice)-2)]+"."+tmpPrice[-2]+tmpPrice[-1]
			# input(price)
			output.write(price+"|")

			output.write("|")
			output.write(line[137]) #codeTVA
			output.write("|")
			# output.write("000"+line[138:149]) #PUTTC
			output.write("\n")


if __name__=="__main__":
	main()

# aaa="C:\Users\Asus\Desktop\Projects\stageB2m\MLF_31803B.dat"