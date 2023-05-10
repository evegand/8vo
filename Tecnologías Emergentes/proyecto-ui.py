from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime, timedelta
import math
import locale
import os

# Configuración regional para mostrar fechas en formato español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# Ruta del archivo de datos
data_file_path = './datafile'

# Función para obtener la lista de usuarios a partir del archivo de datos
def getUsers():
    users = []
    today = datetime.now()

    # Abrir archivo de datos
    try:
        with open(data_file_path, 'r', encoding='utf-8') as df:
            fileText = df.read()
            if fileText != "":
                dataFile = fileText.split("\n")

                # Crear diccionario de usuarios
                id = 1
                for data in dataFile:
                    data = data.split(",")
                    if len(data) < 15:
                        continue

                    # Obtener la fecha de nacimiento del usuario
                    birthDate = datetime(int(data[14][6:]), int(data[14][3:5]), int(data[14][0:2]))
                    age = today - birthDate
                    age = math.floor(int(str(age).split(" ")[0]) / 365)

                    user = {
                        'id': id,
                        'nombre': data[0],
                        'apellido1': data[1],
                        'apellido2': data[2],
                        'fechaNacimiento': data[14],
                        'edad': str(age),
                    }

                    id += 1
                    users.append(user)
    except FileNotFoundError:
        print("Error: no se encontró el archivo 'datafile'.")
    return users

# Función para guardar la lista de usuarios en el archivo de datos
def saveUsers(users):
    with open(data_file_path, 'w', encoding='utf-8') as df:
        for user in users:
            df.write(f"{user['nombre']},{user['apellido1']},{user['apellido2']},{user['fechaNacimiento']}\n")

# Función para crear un archivo de oficio a partir de un usuario
def createDoc(user):
    today = datetime.now().strftime('%d de %B de %Y')

    try:
        with open('./oficio.txt', 'r') as df:
            docFile = df.read()
    except FileNotFoundError:
        print("Error: no se encontró el archivo 'oficio.txt'.")
        return

    doc = docFile.replace("[fecha]", today)\
        .replace("[nombre]", user['nombre'])\
        .replace("[apellido1]", user['apellido1'])\
        .replace("[apellido2]", user['apellido2'])\
        .replace('[fechaNacimiento]', user['fechaNacimiento'])\
        .replace('[edad]', user['edad'])
    with open(f"./{user['nombre']}_{user['apellido1']}_{user['apellido2']}.txt", "w") as f:
        f.write(doc)

# Función para mostrar una ventana con el formulario para agregar un usuario
def showAddUserForm():
    addUserWindow = Toplevel(root)
    addUserWindow.title("Agregar usuario")

    nameLabel = Label(addUserWindow, text="Nombre:")
    nameLabel.grid(row=0, column=0)
    nameEntry = Entry(addUserWindow)
    nameEntry.grid(row=0, column=1)

    apellido1Label = Label(addUserWindow, text="Primer apellido:")
    apellido1Label.grid(row=1, column=0)
    apellido1Entry = Entry(addUserWindow)
    apellido1Entry.grid(row=1, column=1)

    apellido2Label = Label(addUserWindow, text="Segundo apellido:")
    apellido2Label.grid(row=2, column=0)
    apellido2Entry = Entry(addUserWindow)
    apellido2Entry.grid(row=2, column=1)

    fechaLabel = Label(addUserWindow, text="Fecha de nacimiento (DD/MM/AAAA):")
    fechaLabel.grid(row=3, column=0)
    fechaEntry = Entry(addUserWindow)
    fechaEntry.grid(row=3, column=1)

    def addUser():
        # Obtener los datos del formulario
        nombre = nameEntry.get()
        apellido1 = apellido1Entry.get()
        apellido2 = apellido2Entry.get()
        fechaNacimiento = fechaEntry.get()

        # Validar los datos
        if nombre == "" or apellido1 == "" or apellido2 == "" or fechaNacimiento == "":
            messagebox.showerror("Error", "Por favor, rellene todos los campos.")
            return

        # Agregar el usuario al archivo
        try:
            with open('./datafile', 'a', encoding='utf-8') as file:
                file.write(f"{nombre},{apellido1},{apellido2},{fechaNacimiento}\n")
            messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
            addUserWindow.destroy()
        except:
            messagebox.showerror("Error", "Ha ocurrido un error al agregar el usuario.")

        addButton = Button(addUserWindow, text="Agregar", command=addUser)
        addButton.grid(row=4, column=1)

    # Función para mostrar una ventana con el formulario para modificar un usuario
    def showModifyUserForm(user):
        modifyUserWindow = Toplevel(root)
        modifyUserWindow.title("Modificar usuario")
        nameLabel = Label(modifyUserWindow, text="Nombre:")
        nameLabel.grid(row=0, column=0)
        nameEntry = Entry(modifyUserWindow)
        nameEntry.insert(END, user['nombre'])
        nameEntry.grid(row=0, column=1)

        apellido1Label = Label(modifyUserWindow, text="Primer apellido:")
        apellido1Label.grid(row=1, column=0)
        apellido1Entry = Entry(modifyUserWindow)
        apellido1Entry.insert(END, user['apellido1'])
        apellido1Entry.grid(row=1, column=1)

        apellido2Label = Label(modifyUserWindow, text="Segundo apellido:")
        apellido2Label.grid(row=2, column=0)
        apellido2Entry = Entry(modifyUserWindow)
        apellido2Entry.insert(END, user['apellido2'])
        apellido2Entry.grid(row=2, column=1)

        fechaLabel = Label(modifyUserWindow, text="Fecha de nacimiento (DD/MM/AAAA):")
        fechaLabel.grid(row=3, column=0)
        fechaEntry = Entry(modifyUserWindow)
        fechaEntry.insert(END, user['fechaNacimiento'])
        fechaEntry.grid(row=3, column=1)

    def modifyUser():
        # Obtener los datos del formulario
        nombre = modifyNameEntry.get()
        apellido1 = modifyApellido1Entry.get()
        apellido2 = modifyApellido2Entry.get()
        fechaNacimiento = modifyFechaNacimientoEntry.get()
        id = modifyIdEntry.get()

        # Validar que los campos no estén vacíos
        if nombre == "" or apellido1 == "" or apellido2 == "" or fechaNacimiento == "":
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return

        # Crear el diccionario de datos del usuario
        birthDate = datetime.strptime(fechaNacimiento, '%d/%m/%Y')
        age = datetime.now().year - birthDate.year - ((datetime.now().month, datetime.now().day) < (birthDate.month, birthDate.day))
        user = {
            'id': id,
            'nombre': nombre,
            'apellido1': apellido1,
            'apellido2': apellido2,
            'fechaNacimiento': fechaNacimiento,
            'edad': str(age)
        }

        # Actualizar el usuario en la lista de usuarios
        global users
        index = None
        for i, u in enumerate(users):
            if u['id'] == id:
                index = i
                break
        if index is None:
            messagebox.showerror("Error", "El usuario no existe.")
            return
        users[index] = user

        # Actualizar la tabla de usuarios
        updateTable()

        # Cerrar la ventana de modificación
        modifyUserWindow.destroy()

        #Función para mostrar una ventana con la tabla de usuarios
        def showUserTable():
            userTableWindow = Toplevel(root)
            userTableWindow.title("Tabla de usuarios")
            # Crear la tabla
            tree = ttk.Treeview(userTableWindow, columns=('ID', 'Nombre', 'Apellido 1', 'Apellido 2', 'Fecha de Nacimiento', 'Edad'))
            tree.heading('#0', text='')
            tree.heading('#1', text='ID')
            tree.heading('#2', text='Nombre')
            tree.heading('#3', text='Apellido 1')
            tree.heading('#4', text='Apellido 2')
            tree.heading('#5', text='Fecha de Nacimiento')
            tree.heading('#6', text='Edad')
            tree.column('#0', width=0, stretch=NO)
            tree.column('#1', width=50, anchor=CENTER)
            tree.column('#2', width=100, anchor=CENTER)
            tree.column('#3', width=100, anchor=CENTER)
            tree.column('#4', width=100, anchor=CENTER)
            tree.column('#5', width=150, anchor=CENTER)
            tree.column('#6', width=50, anchor=CENTER)

            # Insertar los usuarios en la tabla
            global users
            for user in users:
                tree.insert('', 'end', text='', values=(user['id'], user['nombre'], user['apellido1'], user['apellido2'], user['fechaNacimiento'], user['edad']))

            # Agregar la tabla a la ventana
            tree.pack()

            #Función para actualizar la tabla de usuarios
            def updateTable():
                # Limpiar la tabla
                for i in tree.get_children():
                tree.delete(i)
                # Insertar los usuarios en la tabla
                global users
                for user in users:
                    tree.insert('', 'end', text='', values=(user['id'], user['nombre'], user['apellido1'], user['apellido2'], user['fechaNacimiento'], user['edad']))

def deleteUser():
    # Obtener el ID del usuario a eliminar
    id = idToDelete.get()
    # Buscar el usuario en la lista
    foundUser = False
    for user in users:
        if user['id'] == id:
            foundUser = True
            # Eliminar el usuario de la lista
            users.remove(user)
            # Actualizar la tabla
            updateTable()
            # Mostrar mensaje de éxito
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
            break

    # Si no se encontró el usuario, mostrar mensaje de error
    if not foundUser:
        messagebox.showerror("Error", f"No se encontró un usuario con ID {id}.")



