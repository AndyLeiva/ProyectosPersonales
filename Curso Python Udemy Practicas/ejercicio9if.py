numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 >= 0 and numero2 >= 0:
    if numero1 % numero2 == 0:
        print(f"La división entre {numero1} y {numero2} es entera y el cociente es {numero1 // numero2}")
        
    else:
        print(f"La división entre {numero1} y {numero2} no es entera, el cociente es {numero1 / numero2} y el resto es {numero1 % numero2}")

    if numero1 > numero2:
        print(f"El {numero1} es mayor que el {numero2}")
    elif numero1 < numero2:
        print(f"El {numero1} es menor que el {numero2}")
    elif numero1 == numero2:
        print("Los numeros son iguales")    