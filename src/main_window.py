# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from image_processing import search
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QCompleter
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # main window setup
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 900)

        # central widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # dictionary to hold line edit widgets
        self.line_edits = {'searchPerk_1_Surv_1': 'lblPerk_1_Surv_1', 'searchPerk_2_Surv_1': 'lblPerk_2_Surv_1', 'searchPerk_3_Surv_1': 'lblPerk_3_Surv_1', 'searchPerk_4_Surv_1': 'lblPerk_4_Surv_1',
                      'searchPerk_1_Surv_2': 'lblPerk_1_Surv_2', 'searchPerk_2_Surv_2': 'lblPerk_2_Surv_2', 'searchPerk_3_Surv_2': 'lblPerk_3_Surv_2', 'searchPerk_4_Surv_2': 'lblPerk_4_Surv_2',
                      'searchPerk_1_Surv_3': 'lblPerk_1_Surv_3', 'searchPerk_2_Surv_3': 'lblPerk_2_Surv_3', 'searchPerk_3_Surv_3': 'lblPerk_3_Surv_3', 'searchPerk_4_Surv_3': 'lblPerk_4_Surv_3',
                      'searchPerk_1_Surv_4': 'lblPerk_1_Surv_4', 'searchPerk_2_Surv_4': 'lblPerk_2_Surv_4', 'searchPerk_3_Surv_4': 'lblPerk_3_Surv_4', 'searchPerk_4_Surv_4': 'lblPerk_4_Surv_4'}

        # create perk search bars
        for i in range(1, 5): # 4 survivors
            create_survivor_label(self, str(i), 30, 120 + 200*(i-1)) # create a label for each survivor
            create_valid_label(self, str(i), 1050, 120 + 200*(i-1)) # create a valid label for each survivor
            for j in range(1, 5): # 4 perks per survivor
                create_perk_icon(self, str(j), str(i), 225*(j-1) + 200, 200*(i-1) + 40) # create a perk icon for each perk
                create_perk_search_bar(self, str(j), str(i), 225 * j - 25, 200*(i-1) + 20) # create a search bar for each perk
                # line_edit = self.centralwidget.findChild(QtWidgets.QLineEdit, "linePerk" + str(j) + "Surv" + str(i))

        # create buttons
        btnPaste = create_button(self, 380, 840, 261, 31, "Paste and Search") # TODO: add paste function
        btnReset = create_button(self, 660, 840, 171, 31, "Reset")
        btnPaste.clicked.connect(lambda: search()) # TODO: add paste function
        btnReset.clicked.connect(lambda: reset_perks(self))
        
        # set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # set window title and show
        MainWindow.setWindowTitle("DBDL Perk Checker")
        MainWindow.setWindowIcon(QtGui.QIcon("assets/DBDL.png"))
        MainWindow.show()

# function to create a label for each survivor
def create_survivor_label(self, survivor_no, x, y):
    _translate = QtCore.QCoreApplication.translate
    labelSurvivor = QtWidgets.QLabel(parent=self.centralwidget)

    # set position
    labelSurvivor.setGeometry(QtCore.QRect(x, y, 101, 21))

    # set font & size
    font = QtGui.QFont()
    font.setFamily("Roboto")
    font.setPointSize(16)
    labelSurvivor.setFont(font)

    # set object information
    labelSurvivor.setObjectName("lblSurvivor_" + survivor_no)
    labelSurvivor.setText(_translate("MainWindow", "Survivor "  + survivor_no + ":"))

# function to create a "valid" label for each build
def create_valid_label(self, survivor_no, x, y):
    _translate = QtCore.QCoreApplication.translate
    labelValid = QtWidgets.QLabel(parent=self.centralwidget)

    # set position
    labelValid.setGeometry(QtCore.QRect(x, y, 101, 21))

    # set font & size
    font = QtGui.QFont()
    font.setFamily("Roboto")
    font.setPointSize(16)
    labelValid.setFont(font)

    # set object information
    labelValid.setObjectName("lblSurv_" + survivor_no + "_Valid")
    labelValid.setText(_translate("MainWindow", "Valid!"))

    # set label to hidden by default
    labelValid.hide()

# function to create a perk icon for each perk
def create_perk_icon(self, perk_no, survivor_no, x, y):
    # create perk icon background
    perkIconBG = QtWidgets.QLabel(parent=self.centralwidget)
    perkIconBG.setGeometry(QtCore.QRect(x, y, 150, 150))
    perkIconBG.setPixmap(QtGui.QPixmap("assets/perks/perkBG.png"))
    perkIconBG.setScaledContents(True)

    # create perk icon over background
    perkIcon = QtWidgets.QLabel(parent=self.centralwidget)
    perkIcon.setGeometry(QtCore.QRect(x, y, 150, 150))
    perkIcon.setPixmap(QtGui.QPixmap("assets/perks/perkBG.png"))
    perkIcon.setProperty("Valid", False)
    perkIcon.setScaledContents(True)
    perkIcon.setObjectName("lblPerk_" + perk_no + "_Surv_" + survivor_no)     

# function to try and update the perk icon when the search bar is changed
def on_selection_changed(self, perkSearchBar):
    # get the object name of the search bar
    object_name = perkSearchBar.objectName()

    # get the perk number and survivor number from the object name
    perk_no = object_name.split('_')[1]
    survivor_no = object_name.split('_')[3]

    # get the perkIcon object
    perkIcon = self.centralwidget.findChild(QtWidgets.QLabel, "lblPerk_" + perk_no + "_Surv_" + survivor_no)
    
    # call function
    try_icon_update(perkSearchBar, perkIcon)
    
# function to update perk icon
def try_icon_update(perkSearchBar, perkIcon):
    # check if perk exists
    perk = format_perk_name(perkSearchBar.text())
    if perk_exists(perk) == True:
        perkIcon.setPixmap(QtGui.QPixmap("assets/perks/iconPerks_" + perk + ".png")) # update icon if exists
        perkIcon.setProperty("Valid", True) # set property to true (this will be used to check if the build is valid)
        perkIcon.show() # show icon
        return True
    else:
        perkIcon.setProperty("Valid", False) # set property to false
        perkIcon.hide() # hide icon
        return False

# function to check if perk exists in the assets folder
def perk_exists(perk_name):
    if os.path.exists("assets/perks/iconPerks_" + perk_name + ".png"):
        return True
    else:
        return False

# function to create a search bar for each perk
def create_perk_search_bar(self, perk_no, survivor_no, x, y):
    perkSearchBar = QtWidgets.QLineEdit(parent=self.centralwidget)

    # set position
    perkSearchBar.setGeometry(QtCore.QRect(x, y, 151, 22))
    perkSearchBar.setObjectName("searchPerk_" + perk_no + "_Surv_" + survivor_no) 

    # create completer
    completer = list_of_all_perks()
    completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
    perkSearchBar.setCompleter(completer)

    # connect function to search bar when text changes
    perkSearchBar.textChanged.connect(lambda: on_selection_changed(self, perkSearchBar))
    return perkSearchBar

# function to create a button
def create_button(self, x, y, width, height, text):
    button = QtWidgets.QPushButton(parent=self.centralwidget)

    # set position
    button.setGeometry(QtCore.QRect(x, y, width, height))

    # set font & size
    font = QtGui.QFont()
    font.setFamily("Roboto")
    font.setPointSize(16)
    button.setFont(font)

    # set object information
    button.setObjectName("btn_" + text)
    button.setText(text)
    return button

# function to reset all perk search bars, this will in turn reset all the perk icons
def reset_perks(self):
    for i in range(1, 5): # 4 survivors
        for j in range(1, 5): # 4 perks per survivor
            line_edit = self.centralwidget.findChild(QtWidgets.QLineEdit, "searchPerk_" + str(j) + "_Surv_" + str(i))
            line_edit.clear()

# function to format perk name into valid path to locate the perk icon
def format_perk_name(input_string):
    # Remove : ' - and spaces from the string
    formatted_string = input_string.replace(":", "").replace("'", "").replace(" ", "").replace("-", "")
    formatted_string = " ".join(word.capitalize() for word in formatted_string.split())
    return formatted_string

# function to return a QCompleter object with a list of all survivor perks
def list_of_all_perks():
    return QCompleter([
        'Ace in the Hole',
        'Adrenaline',
        'Aftercare',
        'Alert',
        'Any Means Necessary',
        'Appraisal',
        'Autodidact',
        'Babysitter',
        'Background Player',
        'Balanced Landing',
        'Bardic Inspiration',
        'Better Together',
        'Better Than New',
        'Bite the Bullet',
        'Blast Mine',
        'Blood Pact',
        'Blood Rush',
        'Boil Over',
        'Bond',
        'Boon: Circle of Healing',
        'Boon: Dark Theory',
        'Boon: Exponential',
        'Boon: Illumination',
        'Boon: Shadow Step',
        'Borrowed Time',
        'Botany Knowledge',
        'Breakdown',
        'Breakout',
        'Buckle Up',
        'Built to Last',
        'Calm Spirit',
        'Camaraderie',
        'Champion of Light',
        'Chemical Trap',
        'Clairvoyance',
        'Corrective Action',
        'Counterforce',
        'Cut Loose',
        'Dance With Me',
        'Dark Sense',
        'Dead Hard',
        'Deadline',
        'Deception',
        'Decisive Strike',
        'Deja Vu',
        'Deliverance',
        'Desperate Measures',
        'Detective\'s Hunch',
        'Distortion',
        'Diversion',
        'Dramaturgy',
        'Empathic Connection',
        'Empathy',
        'Fast Track',
        'Fixated',
        'Flashbang',
        'Flip-Flop',
        'Fogwise',
        'For the People',
        'Friendly Competition',
        'Head On',
        'Hope',
        'Hyperfocus',
        'Inner Focus',
        'Inner Strength',
        'Invocation: Weaving Spiders',
        'Iron Will',
        'Kindred',
        'Leader',
        'Left Behind',
        'Light-Footed',
        'Lightweight',
        'Lithe',
        'Low Profile',
        'Lucky Break',
        'Lucky Star',
        'Made For This',
        'Mettle of Man',
        'Mirrored Illusion',
        'No Mither',
        'No One Left Behind',
        'Object of Obsession',
        'Off the Record',
        'Open-Handed',
        'Overcome',
        'Overzealous',
        'Parental Guidance',
        'Pharmacy',
        'Plot Twist',
        'Plunderer\'s Instinct',
        'Poised',
        'Potential Energy',
        'Power Struggle',
        'Premonition',
        'Prove Thyself',
        'Quick & Quiet',
        'Quick Gambit',
        'Reactive Healing',
        'Reassurance',
        'Red Herring',
        'Repressed Alliance',
        'Residual Manifest',
        'Resilience',
        'Resurgence',
        'Rookie Spirit',
        'Saboteur',
        'Scavenger',
        'Scene Partner',
        'Second Wind',
        'Self-Care',
        'Self-Preservation',
        'Slippery Meat',
        'Small Game',
        'Smash Hit',
        'Sole Survivor',
        'Solidarity',
        'Soul Guard',
        'Spine Chill',
        'Sprint Burst',
        'Stake Out',
        'Still Sight',
        'Streetwise',
        'Strength in Shadows',
        'Teamwork: Collective Stealth',
        'Teamwork: Power of Two',
        'Technician',
        'Tenacity',
        'This is Not Happening',
        'Troubleshooter',
        'Unbreakable',
        'Up the Ante',
        'Urban Evasion',
        'Vigil',
        'Visionary',
        'Wake Up!',
        'We\'ll Make It',
        'We\'re Gonna Live Forever',
        'Wicked',
        'Windows of Opportunity',
        'Wiretap'
    ])

# main function
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())