import sys
from datetime import time, datetime
import math
import locale
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from data import Data
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('proyecto.ui', self)

        self.db = Data()

        # Menu principal
        self.usersBtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.usersView))
        self.docsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.DocsView))

        # Submenu
        self.createBtn.clicked.connect(lambda: self.usersStackedWidget.setCurrentWidget(self.usersCreate))
        self.readBtn.clicked.connect(lambda: self.usersStackedWidget.setCurrentWidget(self.usersRead))
        self.updateBtn.clicked.connect(lambda: self.usersStackedWidget.setCurrentWidget(self.usersUpdate))
        self.deleteBtn.clicked.connect(lambda: self.usersStackedWidget.setCurrentWidget(self.usersDelete))

        # Users Create
        self.addUserBtn.clicked.connect(self.crearUsuario)
        # Users Read
        self.refreshBtn.clicked.connect(self.mostrarUsuarios)
        # Users Update
        # Users Delete
        """
        self.createBtn.clicked.connect(self.usersCreate)
        self.readBtn.clicked.connect(self.usersRead)
        self.updateBtn.clicked.connect(self.usersUpdate)
        self.deleteBtn.clicked.connect(self.usersDelete)
        """
    
    def mostrarUsuarios(self):
        datos = self.db.readUsers()
        i = len(datos)
        self.usersTable.setRowCount(i)
        tablerow = 0
        id = 1
        for row in datos:
            birthDate = datetime.combine(row[15], time.min)
            age = datetime.now() - birthDate
            age = math.floor(int(str(age).split(" ")[0]) / 365)

            self.usersTable.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.usersTable.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.usersTable.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.usersTable.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.usersTable.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.usersTable.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.usersTable.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.usersTable.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.usersTable.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.usersTable.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(row[10]))
            self.usersTable.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(row[11]))
            self.usersTable.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(row[12]))
            self.usersTable.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(row[13]))
            self.usersTable.setItem(tablerow, 14, QtWidgets.QTableWidgetItem(row[14]))
            self.usersTable.setItem(tablerow, 15, QtWidgets.QTableWidgetItem(str(row[15])))
            self.usersTable.setItem(tablerow, 16, QtWidgets.QTableWidgetItem(str(age) + " años"))
            # 17
            tablerow += 1
            id += 1

    def crearUsuario(self):
        strDate = datetime.strptime(self.fechaNacimientoLineEdit_2.text(), '%d/%m/%y')
        birthDate = datetime.combine(strDate, time.min)
        print(birthDate)
        age = datetime.now() - birthDate
        age = math.floor(int(str(age).split(" ")[0]) / 365)

        userData = {
            'nombre': self.nombreLineEdit_2.text(),
            'apellido1': self.apellido1LineEdit_2.text(),
            'apellido2': self.apellido2LineEdit_2.text(),
            'cargo': self.cargoLineEdit_2.text(),
            'empresa': self.empresaLineEdit_2.text(),
            'calle': self.calleLineEdit_2.text(),
            'numeroExt': self.numeroExtLineEdit_2.text(),
            'numeroInt': self.numeroIntLineEdit_2.text(),
            'colonia': self.coloniaLineEdit_2.text(),
            'ciudad': self.municipioLineEdit_2.text(),
            'estado': self.estadoLineEdit_2.text(),
            'codigoPostal': self.codigoPostalLineEdit_2.text(),
            'telefono': self.telefonoLineEdit_2.text(),
            'correoElectronico': self.correoElectronicoLineEdit_2.text(),
            'fechaNacimiento': birthDate
        }
        print(userData)
        self.db.createUser(userData)

        self.nombreLineEdit_2.clear()
        self.apellido1LineEdit_2.clear()
        self.apellido2LineEdit_2.clear()
        self.cargoLineEdit_2.clear()
        self.empresaLineEdit_2.clear()
        self.calleLineEdit_2.clear()
        self.numeroExtLineEdit_2.clear()
        self.numeroIntLineEdit_2.clear()
        self.coloniaLineEdit_2.clear()
        self.municipioLineEdit_2.clear()
        self.estadoLineEdit_2.clear()
        self.codigoPostalLineEdit_2.clear()
        self.telefonoLineEdit_2.clear()
        self.correoElectronicoLineEdit_2.clear()
        self.fechaNacimientoLineEdit_2.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
