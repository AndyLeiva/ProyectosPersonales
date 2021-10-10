lista = [1, 50, 30, "juan"]
print(lista)
buscarIndex = input("Elemento: ")
indice = lista.index(buscarIndex)

print("El número 50 está en la posición {} de la lista".format(indice))
lista[indice] = input("Remplazar elememto por: ")
print(lista)