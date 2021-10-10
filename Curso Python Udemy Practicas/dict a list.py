diccionario = {123:{"nombre" : "andy","especialidad":"ciber"},
               235:{"nombre" : "ali","especialidad":"diseño"}
               }
buscar = int(input("Cedula: "))
print(diccionario.get(buscar))

lista = diccionario.items()
lista = list(lista)
print(lista)