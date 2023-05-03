import os, re, socket

def validate(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        print("Correo valido!")
    else:
        if "@" not in email or "." not in email:
            print("Tu correo debe contener un dominio valido")
        else:
            try:
                domain = email.split("@")[1]
                socket.gethostbyname(domain)
            except:
                print(f"El dominio '{domain}' no fue encontrado")

        print("Error: Ingresa un correo valido!\n")

while True:
    os.system("clear")
    print("Practica 7 \n============================================================================")
    email = input("Ingresa tu correo electronico: ")
    validate(email)
    os.system("sleep 3")