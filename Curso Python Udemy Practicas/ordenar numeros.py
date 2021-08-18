listaNumeros = []
print("BIENVENIDO A LA RECTA NUMERICA")

for i in range(100):
    numero = float(input("INGRESE SU NUMERO NEGATIVO O POSITIVO: "))
    
    listaNumeros.append(numero)
    terminarBucle = input("Enter para continuar...\nN para terminar...\nOpción: ")
    terminarBucle.upper()
    if terminarBucle == "N":
        break


listaNumeros.sort()



print("******RECTA NUMERICA******")
print("**************************\n")

print(f"<-{listaNumeros}->\n")

print("***************************")

print ("NUMEROS ORDENADOS CORRECTAMENTE")