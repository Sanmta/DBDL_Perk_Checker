import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QFont

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
        

        # show the window
        self.show()

def create_label(self, text):
    return QLabel(text, self)

if __name__ == '__main__':
    app = QApplication([])

    # create the main window
    window = MainWindow()

    # start the event loop
    app.exec()