import os,xlrd,xlwt,traceback, openpyxl
import xlutils.copy as xlc

# print((os.path.join(os.getcwd(), "EXPRESS.xlsx")))

# myBook = xlrd.open_workbook(os.path.join(os.getcwd(), "EXPRESS.xlsx"))
# editingBook=xlc.copy(myBook)

# sheet = editingBook.get_sheet(0) #selectio page de travail

# nrows = sheet.nrows
# ncols = sheet.ncols

# print(nrows,ncols)

# for i in range(sheet.nrows):
# 	for j in range(sheet.ncols):
# 		sheet.write(i,j,"héhéh")


# editingBook.save('testeditingBook.xlsx')




wb = openpyxl.load_workbook('EXPRESS.xlsx')
ws = wb[0]
print("l.28")
ws['A1'] = 'héhéhéhé'
wb.save('names.xlsx')