# Form implementation generated from reading ui file 'importation.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def importing(self):
        import intégrationBonDeCommande

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(384, 130)
        font = QtGui.QFont()
        font.setFamily("Gill Sans MT")
        MainWindow.setFont(font)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)

        self.articlesButton = QtWidgets.QPushButton(self.centralwidget)
        
        font.setPointSize(10)

        self.articlesButton.setFont(font)
        self.articlesButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.articlesButton.setMouseTracking(False)
        self.articlesButton.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.articlesButton.setObjectName("articlesButton")

        self.gridLayout.addWidget(self.articlesButton, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(52, 24, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 2, 1, 1)

        self.BCAButton = QtWidgets.QPushButton(self.centralwidget)
        self.BCAButton.setFont(font)
        self.BCAButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.BCAButton.setObjectName("BCAButton")

        self.gridLayout.addWidget(self.BCAButton, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(44, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 4, 1, 1)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        
        self.BCAButton.clicked.connect(self.importing())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Imports kwisatz"))
        self.articlesButton.setText(_translate("MainWindow", "Importation\n Articles"))
        self.BCAButton.setText(_translate("MainWindow", "Importation\nBCA fournisseurs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # b2.setIcon(QIcon(QPixmap("python.gif")))
    

    MainWindow.show()

    sys.exit(app.exec())
