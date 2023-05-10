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
        sql = "INSERT INTO datos_empleados (id, nombre, apellido_paterno, apellido_materno, puesto, empresa, direccion, colonia, numero_interior, ciudad, estado, codigo_postal, telefono, correo_electronico, fecha_nacimiento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            user_data['id'],
            user_data['nombre'],
            user_data['apellido1'],
            user_data['apellido2'],
            user_data['cargo'],
            user_data['empresa'],
            user_data['calle'],
            user_data['colonia'],
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
    
    def updateUsers(self, user_id, new_data):
        cursor = self.db.cursor()
        sql = "UPDATE datos_empleados SET nombre=%s, apellido_paterno=%s, apellido_materno=%s, puesto=%s, empresa=%s, direccion=%s, colonia=%s, numero_interior=%s, ciudad=%s, estado=%s, codigo_postal=%s, telefono=%s, correo_electronico=%s, fecha_nacimiento=%s WHERE id=%s"
        values = (
            new_data['nombre'],
            new_data['apellido1'],
            new_data['apellido2'],
            new_data['cargo'],
            new_data['empresa'],
            new_data['direccion'],
            new_data['colonia'],
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

    def searchByName(self, name):
       cursor = self.db.cursor()
       sql = 'SELECT * FROM datos_empleados WHERE name LIKE "%s"'
       value = (name)
       cursor.execute(sql, value)
       result = cursor.fetchall()
       return result
