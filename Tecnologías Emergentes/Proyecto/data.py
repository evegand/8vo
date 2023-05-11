import mysql.connector

class Data():
    def __init__(self):
        # Conexión a la base de datos
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Eve.12300217",
            database="proyecto"
        )

    def createUser(self, user_data):
        cursor = self.db.cursor()
        sql = "INSERT INTO datos_empleados (nombre, apellido_paterno, apellido_materno, puesto, empresa, calle, colonia, numero_exterior, numero_interior, ciudad, estado, codigo_postal, telefono, email, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            user_data['nombre'],
            user_data['apellido1'],
            user_data['apellido2'],
            user_data['cargo'],
            user_data['empresa'],
            user_data['calle'],
            user_data['colonia'],
            user_data['numeroExt'],
            user_data['numeroInt'],
            user_data['ciudad'],
            user_data['estado'],
            user_data['codigoPostal'],
            user_data['telefono'],
            user_data['correoElectronico'],
            user_data['fechaNacimiento']
        )
        cursor.execute(sql, values)
        self.db.commit()
        print(cursor.rowcount, "registro(s) insertado(s).")
    
    def readUsers(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM datos_empleados")
        result = cursor.fetchall()
        for row in result:
            print(row)
        return result
    
    def updateUser(self, user_id, new_data):
        cursor = self.db.cursor()
        sql = "UPDATE datos_empleados SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, puesto=%s, empresa=%s, calle=%s, colonia=%s, numero_exterior=%s, numero_interior=%s, ciudad=%s, estado=%s, codigo_postal=%s, telefono=%s, email=%s, fecha_nacimiento=%s WHERE id=%s"
        values = (
            new_data['nombre'],
            new_data['apellido1'],
            new_data['apellido2'],
            new_data['cargo'],
            new_data['empresa'],
            new_data['calle'],
            new_data['colonia'],
            new_data['numeroExt'],
            new_data['numeroInt'],
            new_data['ciudad'],
            new_data['estado'],
            new_data['codigoPostal'],
            new_data['telefono'],
            new_data['correoElectronico'],
            new_data['fechaNacimiento'],
            user_id
        )
        cursor.execute(sql, values)
        self.db.commit()
        print(cursor.rowcount, "registro(s) actualizado(s).")
    
    def deleteUser(self, user_id):
        cursor = self.db.cursor()
        sql = "DELETE FROM datos_empleados WHERE id = %s"
        value = (user_id,)
        cursor.execute(sql, value)
        self.db.commit()
        print(cursor.rowcount, "registro(s) eliminado(s).")

    def searchByID(self, id):
       cursor = self.db.cursor()
       sql = 'SELECT * FROM datos_empleados WHERE id = %s'
       value = (id)
       cursor.execute(sql, value)
       result = cursor.fetchall()
       return result

    def createNewDoc(self, docData):
        cursor = self.db.cursor()
        sql = "INSERT INTO documentos (titulo, contenido, creacion) VALUES (%s, %s, %s);"
        values = (
            docData['title'],
            docData['content'],
            docData['created']
        )
        cursor.execute(sql, values)
        self.db.commit()
        print(cursor.rowcount, "documento(s) insertado(s).")

    def getTitles(self):
        cursor = self.db.cursor()
        sql = "SELECT titulo FROM documentos"
        cursor.execute(sql)
        result = cursor.fetchall()
        for row in result:
            print(row)
        return result
    
    def getFullDocument(self, name):
        cursor = self.db.cursor()
        sql = "SELECT titulo, contenido FROM documentos WHERE titulo = %s"
        value = (name)
        cursor.execute(sql, value)
        result = cursor.fetchall()
        return result

    def updateDocument(self, title, new_data):
        cursor = self.db.cursor()
        sql = "UPDATE documentos SET titulo=%s, contenido=%s WHERE titulo=%s"
        values = (
            new_data['titulo'],
            new_data['contenido'],
            title
        )
        cursor.execute(sql, values)
        self.db.commit()
        print(cursor.rowcount, "registro(s) actualizado(s).")


    def deleteDocument(self, title):
        cursor = self.db.cursor()
        sql = "DELETE FROM documentos WHERE titulo = %s"
        value = (title,)
        cursor.execute(sql, value)
        self.db.commit()
        print(cursor.rowcount, "documento(s) eliminado(s).")

    def getUserList(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT nombre, apellido_paterno, apellido_materno FROM datos_empleados")
        result = cursor.fetchall()
        for row in result:
            print(row)
        return result

    def getOneUser(self, nombre):
        cursor = self.db.cursor()
        sql = f"SELECT * FROM datos_empleados WHERE concat(nombre, ' ', apellido_paterno, ' ', apellido_materno) = '{nombre[0]}'"
        print(sql, "\n\n\n")
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

