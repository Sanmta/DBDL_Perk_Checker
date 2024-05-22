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

        # create a label
        label = create_label(self, 'Hello World!')
        label.setFont(QFont('Roboto', 200))

        # create a layout
        layout = QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)

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