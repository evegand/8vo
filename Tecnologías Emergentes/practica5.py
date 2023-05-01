values = input("Ingresa valores numericos: ")
list = [int(value) for value in values]

# a) Sublista a la mitad
sublist = list[int(len(list)/2)-1:int(len(list)/2)+1]
print(f"a) {sublist}")

# b) Primer y ultimo elemento
print(f"b) {list[0]}, {list[-1]}",)