values = input("Ingresa valores numericos: ")
list = [int(value) for value in values]

# a) Sublista a la mitad
sublist = list[int(len(list)/2)-1:int(len(list)/2)+1]
print(f"a) Sublista con 2 valores centrales\n{sublist}")

# b) Primer y ultimo elemento
print(f"b) Primer y ultimo elemento\n{list[0]}, {list[-1]}",)