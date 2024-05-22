# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QCompleter


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 900)
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        # MainWindow.setSizePolicy(sizePolicy)
        # MainWindow.setAutoFillBackground(False)

        # central widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # create perk search bars
        for i in range(1, 5): # 4 survivors
            create_survivor_label(self, str(i), 30, 120 + 200*(i-1)) # create a label for each survivor
            create_valid_label(self, str(i), 1050, 120 + 200*(i-1)) # create a valid label for each survivor
            for j in range(1, 5): # 4 perks per survivor
                create_perk_icon(self, str(j), str(i), 225*(j-1) + 200, 200*(i-1) + 40) # create a perk icon for each perk
                create_perk_search_bar(self, str(j), str(i), 225 * j - 25, 200*(i-1) + 20) # create a search bar for each perk

        # create buttons
        btnPaste = create_button(self, 380, 840, 261, 31, "Paste and Search")
        btnReset = create_button(self, 660, 840, 171, 31, "Reset")
       
        # set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        #QtCore.QMetaObject.connectSlotsByName(MainWindow) unsure if this is needed

        # set window title and show
        MainWindow.setWindowTitle("DBDL Perk Checker")
        MainWindow.show()

def create_survivor_label(self, survivor_no, x, y):
    _translate = QtCore.QCoreApplication.translate
    labelSurvivor = QtWidgets.QLabel(parent=self.centralwidget)
    labelSurvivor.setGeometry(QtCore.QRect(x, y, 101, 21))
    font = QtGui.QFont()
    font.setFamily("Roboto")
    font.setPointSize(16)
    labelSurvivor.setFont(font)
    labelSurvivor.setObjectName("lblSurvivor" + survivor_no)
    labelSurvivor.setText(_translate("MainWindow", "Survivor "  + survivor_no + ":"))

def create_valid_label(self, survivor_no, x, y):
    _translate = QtCore.QCoreApplication.translate
    labelValid = QtWidgets.QLabel(parent=self.centralwidget)
    labelValid.setGeometry(QtCore.QRect(x, y, 101, 21))
    font = QtGui.QFont()
    font.setFamily("Roboto")
    font.setPointSize(16)
    labelValid.setFont(font)
    labelValid.setObjectName("lblSurv" + survivor_no + "Valid")
    labelValid.setText(_translate("MainWindow", "Valid!"))
    labelValid.hide()

def create_perk_icon(self, perk_no, survivor_no, x, y):
    perkIcon = QtWidgets.QLabel(parent=self.centralwidget)
    perkIcon.setGeometry(QtCore.QRect(x, y, 150, 150))
    perkIcon.setPixmap(QtGui.QPixmap("assets/DBDL.png"))
    perkIcon.setScaledContents(True)
    perkIcon.setObjectName("lblPerk" + perk_no + "Surv" + survivor_no)                   

def create_perk_search_bar(self, perk_no, survivor_no, x, y):
    perkSearchBar = QtWidgets.QLineEdit(parent=self.centralwidget)
    perkSearchBar.setGeometry(QtCore.QRect(x, y, 151, 22))
    perkSearchBar.setObjectName("linePerk" + perk_no + "Surv" + survivor_no)
    perkSearchBar.setCompleter(list_of_all_perks())
    return perkSearchBar

def create_button(self, x, y, width, height, text):
    button = QtWidgets.QPushButton(parent=self.centralwidget)
    button.setGeometry(QtCore.QRect(x, y, width, height))
    font = QtGui.QFont()
    font.setFamily("Roboto")
    font.setPointSize(16)
    button.setFont(font)
    button.setObjectName("btn" + text)
    button.setText(text)
    return button

def list_of_all_perks():
    return QCompleter([
        'Adrenaline',
        'Ace in the Hole',
        'Aftercare',
        'Alert',
        'Autodidact',
    ])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
