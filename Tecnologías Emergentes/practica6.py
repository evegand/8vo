print("Practica 6 \n============================================================================")
# 1) Verdadero o Falso si la primera letra de la cadena es mayuscula 
def checkString(string):
    res = "Verdadero" if string[0:1].isupper() else "Falso"
    return res

# 2) Funcion que cuente las palabras de la cadena de texto
def countStringCharacters(string):
    return len(split(string))

# 3) Funcion que regrese una lista de las palabras
def split(string):
    return string.split(" ")

# 4) Funcion para regresar la cadena de texto invertida
def reverse(string):
    return string[::-1]

# 5) Funcion para regresar la ultima letra de cada palabra invertida
def lastCharFormat(string):
    list = split(string)
    for each in list:
        key = list.index(each)
        each = each.strip(each[-1]) + each[-1].upper()
        list[key] = each
    return list

string = input("Ingresa una cadena de texto: ")
print(f"\n1) ¿La primera letra es mayuscula? {checkString(string)}\n")
print(f"2) ¿Cuantas palabras tiene la cadena de texto? {countStringCharacters(string)}\n")
print(f"3) ¿Cuales palabras forman la cadena de texto?\n{split(string)}\n")
print(f"4) Cadena de texto invertida:\n{reverse(string)}\n")
print(f"5) Convertir ultimo caracter en mayusculas:\n{lastCharFormat(string)}\n")