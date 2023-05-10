import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from data import Data;

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('proyecto.ui', self)

        self.db = Data()

        # Menu principal
        self.usersBtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.usersView))
        self.docsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.usersView))

        """
        self.createBtn.clicked.connect(self.usersCreate)
        self.readBtn.clicked.connect(self.usersRead)
        self.updateBtn.clicked.connect(self.usersUpdate)
        self.deleteBtn.clicked.connect(self.usersDelete)
        """

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
