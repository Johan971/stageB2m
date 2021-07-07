import csv,traceback

def main():
	with open('ARTICLE.CSV', newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=';', skipinitialspace=True)
		with open('output.csv','w', newline='') as output:
			
			writer=csv.writer(output, delimiter=';')
			for row in spamreader:
				print("ligne num : ", spamreader.line_num)
				# input("e")
				
				try:
					if spamreader.line_num==1:
							writer.writerow(row)
							print("ok")
							# input("ok")

					if type(int(row[0]))==type(55):
						row[0]=str(int(row[0]))

					print("osk")
					

						# print(len(str(int(row[0]))),str(row[0]),'e')

					if (type(int(row[0]))!=type(55) and spamreader.line_num!=1 ):
						print("\n\npasssssinnnng")
						print(row)
						input("r")
					elif (10<len(str(row[0]))<13):

						numberOf0=13-len(str(row[0]))

						zeros=""
						for i in range(numberOf0):
							zeros+="0"

						print("zz",row[0])
						row[0]=str(zeros)+ str(row[0])
						print("eeeee",row)
						writer.writerow(row)
					else:
						writer.writerow(row)
						# input("here we r")
						
					# input("ee")
				except ValueError:
					pass
				# except:
				# 	print(traceback.format_exc())
					# input("e")



if __name__ == '__main__':
	main()