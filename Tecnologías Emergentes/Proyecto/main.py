import sys
from datetime import time, datetime
import math
import locale
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from data import Data
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QComboBox
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('proyecto.ui', self)

        self.db = Data()

        # Menu principal
        self.usersBtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.usersView))
        self.docsBtn.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.DocsView))

        # Submenu Usuarios
        self.createBtn.clicked.connect(lambda: self.usersStackedWidget.setCurrentWidget(self.usersCreate))
        self.readBtn.clicked.connect(lambda: self.usersStackedWidget.setCurrentWidget(self.usersRead))
        self.updateBtn.clicked.connect(lambda: self.usersStackedWidget.setCurrentWidget(self.usersUpdate))
        self.deleteBtn.clicked.connect(lambda: self.usersStackedWidget.setCurrentWidget(self.usersDelete))

        # Users Create
        self.addUserBtn.clicked.connect(self.crearUsuario)
        # Users Read
        self.refreshBtn.clicked.connect(self.mostrarUsuarios)
        # Users Update
        self.userFindBtn.clicked.connect(self.encontrarUsuario)
        self.saveChangesBtn.clicked.connect(self.actualizarUsuario)
        # Users Delete
        self.userFindBtn2.clicked.connect(self.encontrarUsuario_borrar)
        self.deleteNowBtn.clicked.connect(self.eliminarUsuario)

        # Submenu Documentos
        self.correspondenciaBtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.correspondencia))
        self.docNewBtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.docNew))
        self.docUpdateBtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.docUpdate))
        self.docDeleteBtn.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.docDelete))

        # Correspondencia
        fileTitles = self.db.getTitles()
        list = [str(item[0]) for item in fileTitles]
        self.archivoComboBox.addItems(list)

        self.paraComboBox.addItems(['Un usuario', 'Todos los usuarios'])
        self.paraComboBox.currentIndexChanged.connect(self.comboBoxIndexChanged)

        rawUserList = self.db.getUserList()
        userList = [str(item[0] + " " + item[1] + " " + item[2]) for item in rawUserList]
        self.usuarioComboBox.addItems(userList)

        self.pushButton.clicked.connect(self.crearCorrespondencia)
        # New Doc
        self.saveNewDocBtn.clicked.connect(self.guardarDocumento)
        # Update Doc
        self.tituloComboBox.addItems(list)
        self.findDocBtn.clicked.connect(self.encontrarDocumento)
        self.saveDocChangesBtn.clicked.connect(self.actualizarDocumento)
        # Remove Doc
        self.tituloComboBox_2.addItems(list)
        self.findDocBtn_2.clicked.connect(self.encontrarDocumento_2)
        self.deleteDocBtn.clicked.connect(self.eliminarDocumento)
    
    def comboBoxIndexChanged(self):
        if self.paraComboBox.currentText() == 'Todos los usuarios':
            self.usuarioComboBox.setEnabled(False)
        else:
            self.usuarioComboBox.setEnabled(True)

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

    def encontrarUsuario(self):
        userId = self.findByIDLineEdit.text()
        self.user = self.db.searchByID([userId])
        if len(self.user) != 0:
            self.nombreLineEdit_3.setText(self.user[0][1])
            self.apellido1LineEdit_3.setText(self.user[0][2])
            self.apellido2LineEdit_3.setText(self.user[0][3])
            self.cargoLineEdit_3.setText(self.user[0][4])
            self.empresaLineEdit_3.setText(self.user[0][5])
            self.calleLineEdit_3.setText(self.user[0][6])
            self.numeroExtLineEdit_3.setText(self.user[0][7])
            self.numeroIntLineEdit_3.setText(self.user[0][8])
            self.coloniaLineEdit_3.setText(self.user[0][9])
            self.municipioLineEdit_3.setText(self.user[0][10])
            self.estadoLineEdit_3.setText(self.user[0][11])
            self.codigoPostalLineEdit_3.setText(self.user[0][12])
            self.telefonoLineEdit_3.setText(self.user[0][13])
            self.correoElectronicoLineEdit_3.setText(self.user[0][14])
            self.fechaNacimientoLineEdit_3.setDate(self.user[0][15])
        else:
            self.nombreLineEdit_3.clear()
            self.apellido1LineEdit_3.clear()
            self.apellido2LineEdit_3.clear()
            self.cargoLineEdit_3.clear()
            self.empresaLineEdit_3.clear()
            self.calleLineEdit_3.clear()
            self.numeroExtLineEdit_3.clear()
            self.numeroIntLineEdit_3.clear()
            self.coloniaLineEdit_3.clear()
            self.municipioLineEdit_3.clear()
            self.estadoLineEdit_3.clear()
            self.codigoPostalLineEdit_3.clear()
            self.telefonoLineEdit_3.clear()
            self.correoElectronicoLineEdit_3.clear()
            self.fechaNacimientoLineEdit_3.clear()

            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("Usuario no encontrado")
            alert.setText("No existe un usuario con ese ID todavia.")
            alert.setStandardButtons(QMessageBox.Ok)
            alert.exec_()

    def actualizarUsuario(self):
        userId = self.findByIDLineEdit.text()
        strDate = datetime.strptime(self.fechaNacimientoLineEdit_3.text(), '%d/%m/%y')
        birthDate = datetime.combine(strDate, time.min)
        print(birthDate)
        age = datetime.now() - birthDate
        age = math.floor(int(str(age).split(" ")[0]) / 365)

        userData = {
            'nombre': self.nombreLineEdit_3.text(),
            'apellido1': self.apellido1LineEdit_3.text(),
            'apellido2': self.apellido2LineEdit_3.text(),
            'cargo': self.cargoLineEdit_3.text(),
            'empresa': self.empresaLineEdit_3.text(),
            'calle': self.calleLineEdit_3.text(),
            'numeroExt': self.numeroExtLineEdit_3.text(),
            'numeroInt': self.numeroIntLineEdit_3.text(),
            'colonia': self.coloniaLineEdit_3.text(),
            'ciudad': self.municipioLineEdit_3.text(),
            'estado': self.estadoLineEdit_3.text(),
            'codigoPostal': self.codigoPostalLineEdit_3.text(),
            'telefono': self.telefonoLineEdit_3.text(),
            'correoElectronico': self.correoElectronicoLineEdit_3.text(),
            'fechaNacimiento': birthDate
        }
        print(userData)
        self.db.updateUser(userId, userData)            

    def encontrarUsuario_borrar(self):
        userId = self.findByIDLineEdit_2.text()
        self.user = self.db.searchByID([userId])
        i = len(self.user)
        self.usersTable_2.setRowCount(i)
        tablerow = 0
        id = 1
        for row in self.user:
            birthDate = datetime.combine(row[15], time.min)
            age = datetime.now() - birthDate
            age = math.floor(int(str(age).split(" ")[0]) / 365)

            self.usersTable_2.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.usersTable_2.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.usersTable_2.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(row[3]))
            self.usersTable_2.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            self.usersTable_2.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(row[5]))
            self.usersTable_2.setItem(tablerow, 6, QtWidgets.QTableWidgetItem(row[6]))
            self.usersTable_2.setItem(tablerow, 7, QtWidgets.QTableWidgetItem(row[7]))
            self.usersTable_2.setItem(tablerow, 8, QtWidgets.QTableWidgetItem(row[8]))
            self.usersTable_2.setItem(tablerow, 9, QtWidgets.QTableWidgetItem(row[9]))
            self.usersTable_2.setItem(tablerow, 10, QtWidgets.QTableWidgetItem(row[10]))
            self.usersTable_2.setItem(tablerow, 11, QtWidgets.QTableWidgetItem(row[11]))
            self.usersTable_2.setItem(tablerow, 12, QtWidgets.QTableWidgetItem(row[12]))
            self.usersTable_2.setItem(tablerow, 13, QtWidgets.QTableWidgetItem(row[13]))
            self.usersTable_2.setItem(tablerow, 14, QtWidgets.QTableWidgetItem(row[14]))
            self.usersTable_2.setItem(tablerow, 15, QtWidgets.QTableWidgetItem(str(row[15])))
            self.usersTable_2.setItem(tablerow, 16, QtWidgets.QTableWidgetItem(str(age) + " años"))
            # 17
            tablerow += 1
            id += 1

    def eliminarUsuario(self):
        userId = self.findByIDLineEdit_2.text()
        if userId != "":
            alert = QMessageBox()
            alert.setIcon(QMessageBox.Question)
            alert.setWindowTitle("Eliminar usuario")
            alert.setText("¿Estás seguro que deseas realizar esta acción?")
            alert.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            response = alert.exec()

            if response == QMessageBox.Yes:
                self.usersTable_2.clearContents()
                self.usersTable_2.setRowCount(0)
                self.findByIDLineEdit_2.clear()
                self.db.deleteUser(userId)

                alert = QMessageBox()
                alert.setIcon(QMessageBox.Information)
                alert.setWindowTitle("Usuario eliminado")
                alert.setText("El usuario ha sido eliminado exitosamente.")
                alert.setStandardButtons(QMessageBox.Ok)
                alert.exec_()

    def guardarDocumento(self):
        newDoc = {
            'title': self.tituloLineEdit.text(),
            'content': self.contenidoTextEdit.toPlainText(),
            'created': datetime.now()
        }
        print(newDoc)
        self.db.createNewDoc(newDoc)

        self.contenidoTextEdit.clear()
        self.tituloLineEdit.clear()

        fileTitles = self.db.getTitles()
        list = [str(item[0]) for item in fileTitles]
        self.archivoComboBox.clear()
        self.archivoComboBox.addItems(list)
        self.archivoComboBox.currentIndex = 0
        self.tituloComboBox.clear()
        self.tituloComboBox.addItems(list)
        self.tituloComboBox.currentIndex = 0
        self.tituloComboBox_2.clear()
        self.tituloComboBox_2.addItems(list)
        self.tituloComboBox_2.currentIndex = 0

    def encontrarDocumento(self):
        fileTitles = self.db.getTitles()
        list = [str(item[0]) for item in fileTitles]
        self.archivoComboBox.clear()
        self.archivoComboBox.addItems(list)
        self.archivoComboBox.currentIndex = 0
        self.tituloComboBox.clear()
        self.tituloComboBox.addItems(list)
        self.tituloComboBox.currentIndex = 0
        self.tituloComboBox_2.clear()
        self.tituloComboBox_2.addItems(list)
        self.tituloComboBox_2.currentIndex = 0

        cont = self.db.getFullDocument([self.tituloComboBox.currentText()])
        print(cont)
        titulo = str(cont[0][0]).replace("\\n", "\n").replace("('", "").replace("',)", "")
        contenido = str(cont[0][1]).replace("\\n", "\n").replace("('", "").replace("',)", "")
        self.tituloLineEdit_2.setText(titulo)
        self.contenidoTextEdit_2.setText(contenido)

    def actualizarDocumento(self):
        tituloComboBox = self.tituloComboBox.currentText()
        updatedDoc = {
            'titulo': self.tituloLineEdit_2.text(),
            'contenido': self.contenidoTextEdit_2.toPlainText()
        }
        self.db.updateDocument(tituloComboBox, updatedDoc)

        self.tituloLineEdit_2.clear()
        self.contenidoTextEdit_2.clear()

        fileTitles = self.db.getTitles()
        list = [str(item[0]) for item in fileTitles]
        self.archivoComboBox.clear()
        self.archivoComboBox.addItems(list)
        self.archivoComboBox.currentIndex = 0
        self.tituloComboBox.clear()
        self.tituloComboBox.addItems(list)
        self.tituloComboBox.currentIndex = 0
        self.tituloComboBox_2.clear()
        self.tituloComboBox_2.addItems(list)
        self.tituloComboBox_2.currentIndex = 0

    def encontrarDocumento_2(self):
        fileTitles = self.db.getTitles()
        list = [str(item[0]) for item in fileTitles]
        self.archivoComboBox.clear()
        self.archivoComboBox.addItems(list)
        self.archivoComboBox.currentIndex = 0
        self.tituloComboBox.clear()
        self.tituloComboBox.addItems(list)
        self.tituloComboBox.currentIndex = 0
        self.tituloComboBox_2.clear()
        self.tituloComboBox_2.addItems(list)
        self.tituloComboBox_2.currentIndex = 0

        cont = self.db.getFullDocument([self.tituloComboBox_2.currentText()])
        contenido = str(cont[0][1]).replace("\\n", "\n").replace("('", "").replace("',)", "")
        self.contenidoTextEdit_3.setText(contenido)

    def eliminarDocumento(self):
        titulo = self.tituloComboBox_2.currentText()
        alert = QMessageBox()
        alert.setIcon(QMessageBox.Question)
        alert.setWindowTitle("Eliminar usuario")
        alert.setText("¿Estás seguro que deseas realizar esta acción?")
        alert.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        response = alert.exec()

        if response == QMessageBox.Yes:
            self.contenidoTextEdit_3.clear()

            fileTitles = self.db.getTitles()
            list = [str(item[0]) for item in fileTitles]
            self.archivoComboBox.clear()
            self.archivoComboBox.addItems(list)
            self.archivoComboBox.currentIndex = 0
            self.tituloComboBox.clear()
            self.tituloComboBox.addItems(list)
            self.tituloComboBox.currentIndex = 0
            self.tituloComboBox_2.clear()
            self.tituloComboBox_2.addItems(list)
            self.tituloComboBox_2.currentIndex = 0

            self.db.deleteDocument(titulo)

            alert = QMessageBox()
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle("Documento eliminado")
            alert.setText("El documento ha sido eliminado exitosamente.")
            alert.setStandardButtons(QMessageBox.Ok)
            alert.exec_()

    def crearCorrespondencia(self):
        archivo = self.archivoComboBox.currentText()
        today = datetime.now().strftime('%d de %B de %Y')

        FileContent = self.db.getFullDocument([archivo])
        print(FileContent, "\n")

        if self.paraComboBox.currentText() == "Todos los usuarios":
            usersData = self.db.readUsers()
            print(usersData)
            x = 1
            for user in usersData:
                birthDate = datetime.combine(user[15], time.min)
                age = datetime.now() - birthDate
                age = math.floor(int(str(age).split(" ")[0]) / 365)

                doc = FileContent[0][1].replace("[fecha]", today)\
                    .replace("[nombre]", user[1])\
                    .replace("[apellido1]", user[2])\
                    .replace("[apellido2]", user[3])\
                    .replace("[cargo]", user[4])\
                    .replace('[empresa]', user[5])\
                    .replace('[calle]', user[6])\
                    .replace('[numeroExt]', user[7])\
                    .replace('[numeroInt]', f", Numero interior: {user[8]}" if user[8] != "" else "")\
                    .replace('[colonia]', user[9])\
                    .replace('[municipio]', user[10])\
                    .replace('[estado]', user[11])\
                    .replace('[codigoPostal]', user[12])\
                    .replace('[telefono]', user[13])\
                    .replace('[correoElectronico]', user[14])\
                    .replace('[fechaNacimiento]', user[15].strftime('%d de %B de %Y'))\
                    .replace('[edad]', str(age))
                with open(f"./{FileContent[0][0]}_{x}_{user[1]}_{user[2]}.txt", "w") as f:
                    f.write(doc)
                x += 1


        else:
            user = self.usuarioComboBox.currentText()
            userData = self.db.getOneUser([user])
            print([user])
            print(userData)

            birthDate = datetime.combine(userData[0][15], time.min)
            age = datetime.now() - birthDate
            age = math.floor(int(str(age).split(" ")[0]) / 365)
            doc = FileContent[0][1].replace("[fecha]", today)\
                .replace("[nombre]", userData[0][1])\
                .replace("[apellido1]", userData[0][2])\
                .replace("[apellido2]", userData[0][3])\
                .replace("[cargo]", userData[0][4])\
                .replace('[empresa]', userData[0][5])\
                .replace('[calle]', userData[0][6])\
                .replace('[numeroExt]', userData[0][7])\
                .replace('[numeroInt]', f", Numero interior: {userData[0][8]}" if userData[0][8] != "" else "")\
                .replace('[colonia]', userData[0][9])\
                .replace('[municipio]', userData[0][10])\
                .replace('[estado]', userData[0][11])\
                .replace('[codigoPostal]', userData[0][12])\
                .replace('[telefono]', userData[0][13])\
                .replace('[correoElectronico]', userData[0][14])\
                .replace('[fechaNacimiento]', userData[0][15].strftime('%d de %B de %Y'))\
                .replace('[edad]', str(age))
            with open(f"./{FileContent[0][0]}_{userData[0][1]}_{userData[0][2]}.txt", "w") as f:
                f.write(doc)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())
