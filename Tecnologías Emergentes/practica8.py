from datetime import time, datetime
import math
import locale
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

print("Practica 8 \n============================================================================")

def getUsers():
    users = []
    today = datetime.now()
    
    # Open File
    df = open('./datafile', 'r')
    
    fileText = df.read()
    if fileText != "":
        dataFile = fileText.split("\n")

        # Creating user dictionary
        id = 1
        for data in dataFile:
            data = data.split(",")

            # Getting the user's age
            birthDate = datetime(int(data[14][6:]), int(data[14][3:5]), int(data[14][0:2]))
            age = today - birthDate
            age = math.floor(int(str(age).split(" ")[0]) / 365)

            user = {
                'id': id,
                'nombre': data[0],
                'apellido1': data[1],
                'apellido2': data[2],
                'cargo': data[3],
                'empresa': data[4],
                'calle': data[5],
                'numeroExt': data[6],
                'numeroInt': data[7],
                'colonia': data[8],
                'municipio': data[9],
                'estado': data[10],
                'codigoPostal': data[11],
                'telefono': data[12],
                'correoElectronico': data[13],
                'fechaNacimiento': data[14],
                'edad': str(age),
            }

            id += 1
            users.append(user)

    df.close()
    return users

def createDocs():
    today = datetime.now().strftime('%d de %B de %Y')
    x = 1

    try:
        with open('./oficio.txt', 'r') as df:
            docFile = df.read()
    except FileNotFoundError:
        print("Error: no se encontró el archivo 'oficio.txt'.")
        return

    for user in users:
        doc = docFile.replace("[fecha]", today)\
            .replace("[nombre]", user['nombre'])\
            .replace("[apellido1]", user['apellido1'])\
            .replace("[apellido2]", user['apellido2'])\
            .replace("[cargo]", user['cargo'])\
            .replace('[empresa]', user['empresa'])\
            .replace('[calle]', user['calle'])\
            .replace('[numeroExt]', user['numeroExt'])\
            .replace('[numeroInt]', f", Numero interior: {user['numeroInt']}" if user['numeroInt'] != "" else "")\
            .replace('[colonia]', user['colonia'])\
            .replace('[municipio]', user['municipio'])\
            .replace('[estado]', user['estado'])\
            .replace('[codigoPostal]', user['codigoPostal'])\
            .replace('[telefono]', user['telefono'])\
            .replace('[correoElectronico]', user['correoElectronico'])\
            .replace('[fechaNacimiento]', user['fechaNacimiento'])\
            .replace('[edad]', user['edad'])
        with open(f"./{x}_{user['nombre']}_{user['apellido1']}_{user['apellido2']}.txt", "w") as f:
            f.write(doc)
        x += 1

users = getUsers()
createDocs()