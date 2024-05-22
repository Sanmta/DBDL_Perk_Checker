import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCompleter, QLineEdit, QHBoxLayout, QGridLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set the window title
        self.setWindowTitle('DBDL Perk Checker')

        # set the window size
        self.setGeometry(100, 100, 1300, 800)

        # create a layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # create labels
        labels = ["Survivor 1", "Survivor 2", "Survivor 3", "Survivor 4"]
        for label in labels:
            label = create_label(self, label)
            label.setFont(QFont('Roboto', 15))
            layout.addWidget(label)
            layout.addStretch()
        
        # create QLineEdit for perks
        grid = QGridLayout()    
        layout.addLayout(grid)

        # for j in range(4):
        for i in range(4):
            perks = QLineEdit(self)
            perks.setCompleter(list_of_all_perks())
            grid.addWidget(perks, 0, i)

        

        # show the window
        self.show()

def create_label(self, text):
    return QLabel(text, self)

def create_perk_QLineEdit(self):
    return QLineEdit(self)

def list_of_all_perks():
    return QCompleter([
        'Adrenaline',
        'Ace in the Hole',
        'Aftercare',
        'Alert',
        'Autodidact',
    ])

if __name__ == '__main__':
    app = QApplication([])

    # create the main window
    window = MainWindow()

    # start the event loop
    app.exec()