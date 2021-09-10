def sumaNumeros():
    listaNumeros = []
    cantidad = 10
    
    for i in range(cantidad):
        numeros = int(input("Introduce tu numero: "))
        listaNumeros.append(numeros)
    
    suma = sum(listaNumeros)
    print("\n",listaNumeros)
    return suma

sumandoLista = sumaNumeros()

print("Suma de numeros en una lista")
print(f"El resultado de la lista es:",sumandoLista)
input("Enter para cerrar...")

        


