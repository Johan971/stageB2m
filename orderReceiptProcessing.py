import os,xlrd,traceback

print((os.path.join(os.getcwd(), "BCA.xlsx")))

myBook = xlrd.open_workbook(os.path.join(os.getcwd(), "BCA.xlsx"))
sheet = myBook.sheet_by_index(0)

nrows = sheet.nrows
ncols = sheet.ncols

lineCounter = 0
cellCounter = 0
header = -1
fileType=""

for i in range(sheet.nrows):
	for j in range(sheet.ncols):

		cellVal = sheet.cell_value(i, j)
		if (cellVal != "" and cellCounter == 0):
			try:
				if str(cellVal).upper() == (
					"BCA" or "DEV" or "BCV" or "BLV" or "FAV" or "BRA" or "FAA"
				):
					cellCounter = 1
					lineCounter = 1
					fileType=cellVal
					##### HAVE TO WRITE FILE ###########
					with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:

						outputFile.write(str(cellVal).upper() + "|")


				elif i == sheet.nrows and j == sheet.ncols and cellCounter == 0:
					raise Exception("Not a correct document.")

			except Exception as inst:
				print(traceback.format_exc())
				print(inst)

			#### TEXT PROCESSING ####

		try:
			if (cellCounter == 1 and lineCounter == 1):
			
				# print("not here",cellVal.upper())
				if str(cellVal.upper()) == "E":
					header = True
					cellCounter = 2
					
					with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
						outputFile.write(str(cellVal).upper() + "|")
				elif(str(cellVal).upper()!="{}".format(fileType)):
					raise Exception("Not a good document : must have a header.")

			if (header == True and str(cellVal).upper()!="E"):
				
				cellCounter += 1

				if (cellVal=="" and cellCounter>1):

					with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
						outputFile.write("|")
				
				elif type(cellVal) == type("ee"):
					
					if (cellCounter == 3 or cellCounter== 4):
						if len(cellVal) > 40:
							cellCounter -= 1
							raise ValueError("Reference1 or reference2 must have a shorter len.")
						else:
							with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
								outputFile.write(str(cellVal).upper() + "|")
				elif cellCounter==5:
					
					if len(str(cellVal))>8:
						# cellCounter -= 1
						raise ValueError("Provider code's length must be in range(0,8) ")
					else:
						with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
							outputFile.write(str(cellVal).upper() + "|")
						
				elif cellCounter==8:
					with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
						outputFile.write(str(cellVal).upper() + "|")
				elif type(cellVal) == type(12.0):
					cellVal = int(cellVal)

					if cellCounter == 6:
						if len(str(cellVal)) != 8:
							raise ValueError("Date must be DDMMYYYY format.")

					elif cellCounter == 7:
						
						if cellVal not in range(0, 50+1):
							print("not in range")
							raise ValueError("Store code must be in range(0,50).")

					elif cellCounter == 9:
						if cellVal not in range(0, 99999999+1):
							raise ValueError("Client code must be in range(0,99999999).")

					with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
						outputFile.write(str(cellVal).upper() + "|")
		
			elif (header == False):

				if type(cellVal)==type("ee"):
					
					if str(cellVal).upper()=="{}".format(fileType):
						pass

					elif str(cellVal).upper()=="C":
						
						with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
					
							outputFile.write(str(cellVal).upper() + "|")
				if (cellVal=="" and cellCounter>1):

					with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
						outputFile.write("|")

				elif cellCounter in range (3,4+1):
					if (len(str(int(cellVal)))>14):
						
						raise ValueError("Product code or provider reference must have a len in range(0,13).")
					else:
						with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
							outputFile.write(str(int(cellVal)).upper() + "|")
						
				elif cellCounter ==5:
					if (len(str(cellVal))>40+1):
						raise ValueError("Product name must have a len in range(1,40).")
					else:
						with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
							outputFile.write(str(cellVal).upper() + "|")
				elif cellCounter==6:
					with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
						outputFile.write(str(int(cellVal)).upper() + "|")
					

				elif cellCounter==7 or cellCounter==8 or cellCounter==10:
					with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
						outputFile.write(str((cellVal)) + "|")
					
				
				elif cellCounter==9:
					if cellVal not in range(0,6):
						raise ValueError("TVA code must be in range(0,5).")
					else:
						with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
							outputFile.write(str(int(cellVal)).upper() + "|")
				
				cellCounter += 1
				
			if ((cellCounter==10 and header==True) or (cellCounter==11)):
				try:
					zz=sheet.cell_value(i+1, 0)
					lineCounter+=1
					header=False
					with open(os.path.join(os.getcwd(), "IMPORTDOC.ASC"), "a") as outputFile:
						outputFile.write("\n")
						outputFile.write("{}".format(fileType) + "|")
					cellCounter=1
				except IndexError:
					pass
				except Exception as inst:
					print(traceback.format_exc())
					print(inst)
			

		except Exception as inst:
			print(traceback.format_exc())
			print(inst)

