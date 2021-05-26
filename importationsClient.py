# THREAD CAN ONLY BE STARTED ONCE : aaaahhhhhh il faut le renommer à chaque fois !!!!???????


from PyQt5 import QtCore, QtGui, QtWidgets
from integrationBonDeCommande import renaming,importing
from integrationArticles import integration
from exportationBCA import exporting
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(597, 205)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        MainWindow.setFont(font)

        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 5, 1, 1)
        
        self.BCAButton = QtWidgets.QPushButton(self.centralwidget)
        font.setPointSize(10)
        self.BCAButton.setFont(font)
        self.BCAButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BCAButton.setObjectName("BCAButton")
        self.gridLayout.addWidget(self.BCAButton, 6, 4, 1, 1)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 4)
        
        spacerItem1 = QtWidgets.QSpacerItem(52, 24, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 6, 0, 1, 1)
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFont(font)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 2)

        self.articlesButton = QtWidgets.QPushButton(self.centralwidget)
        self.articlesButton.setFont(font)
        self.articlesButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.articlesButton.setMouseTracking(False)
        self.articlesButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.articlesButton.setObjectName("articlesButton")
        self.gridLayout.addWidget(self.articlesButton, 6, 1, 1, 1)

        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setFont(font)
        self.exportButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.exportButton.setObjectName("exportButton")
        self.gridLayout.addWidget(self.exportButton, 6, 2, 1, 2)
        
        # self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.pbar = QtWidgets.QProgressBar(self.centralwidget)
        self.pbar.setObjectName("pbar")
        # self.label_2.setFont(font)
        # self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.pbar, 2, 1, 1, 5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.BCAButton.clicked.connect(self.importingBCA)
        self.articlesButton.clicked.connect(self.importingArticles)
        self.exportButton.clicked.connect(self.exportingBCA)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
       
        # self.basePath="C:\\WKW3\\$ZBASE1"
        # self.articlesPath="C:\\Users\\SUPPORT_COMMERCIAL\\Downloads"
        self.basePath="D:\\WKW3\\$BASE"
        self.articlesPath="C:\\GESTION\\IMPORT\\article.dat"
        self.intFilePath="C:\\wkw3\\$BASE\\Import"
    
    def importingArticles(self):
        # from integrationArticles import integration
        if self.pbar.value()==100:
            self.pbar.setValue(0)
        """input non toléré"""
        # articlesPath=input("Entrez le chemin des articles à récupérer :\n") #obligé parce qu'on sait pas la lettre
        # basePath=input("Entrez le chemin du dossier magasin (ex: 'D:\\WKW3\\$ZBASE') :\n")
        integration(self.articlesPath,self.basePath,self.pbar,self.label_2)
        
        
        
    
    def importingBCA(self):

        if self.pbar.value()==100:
            self.pbar.setValue(0)

        paths=renaming(self.intFilePath,self.basePath,self.pbar,self.label_2)
        if(len(paths)==2):
            importing(paths[0],paths[1],self.pbar,self.label_2)

    def exportingBCA(self):

    	exporting(self.basePath,self.pbar,self.label)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Imports kwisatz"))
        self.BCAButton.setText(_translate("MainWindow", "Importation\n"
"Bons de commandes fournisseurs"))
        self.label.setText(_translate("MainWindow", "Cette interface vous permet d\'importer vers Kwisatz : les articles envoyés par la centrale ainsi que\n"
"vos bons de commandes fournisseurs."))
        self.articlesButton.setText(_translate("MainWindow", "Importation\n"
"Articles"))
        self.exportButton.setText(_translate("MainWindow", "Exportation des bons\n"
"de commandes fournisseurs"))
        # self.label_2.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication.instance() 
    if not app: # sinon on crée une instance de QApplication
        app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowIcon(QtGui.QIcon("b2m.ico"))
    MainWindow.show()
    sys.exit(app.exec())
