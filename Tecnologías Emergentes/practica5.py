print("Practica 5 \n============================================================================")
values = input("Ingresa valores numericos: ")
list = [int(value) for value in values]

# 1) Sublista a la mitad
sublist = list[int(len(list)/2)-1:int(len(list)/2)+1]
print(f"\n1) Sublista con 2 valores centrales\n{sublist}\n")

# 2) Primer y ultimo elemento
print(f"2) Primer y ultimo elemento\n{list[0:1]}, [{list[-1]}]\n")

# 3) Agregar elementos de la lista al final de la lista
list.extend(list)
print(f"3) Agregar elementos de la lista al final de la lista\n{list}\n")

# 4) Ordenar de menor a mayor
list.sort(reverse=False)
print(f"4) Ordenar elementos de la lista de menor a mayor\n{list}\n")

# 5) Ordenar de mayor a menor
list.sort(reverse=True)
print(f"5) Ordenar elementos de la lista de mayor a menor\n{list}\n")

# 6) Funcion cubo
def cubo(v):
    return v*v*v

for each in list:
    list[list.index(each)] = cubo(each)

print(f"6) Funcion cubica de la lista\n{list}\n")