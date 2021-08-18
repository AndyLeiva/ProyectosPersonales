numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))

if numero1 >= 0 and numero2 >= 0:
    if numero1 % numero2 == 0:
        print(f"El {numero1} es multiplo de {numero2}")
    else:
        print(f"El {numero1} no multiplo de {numero1}")
    
    if numero2 % numero1 == 0:
        print(f"El {numero2} es multiplo de {numero1}")
    else:
        print(f"El {numero2} no multiplo de {numero1}")     
        
else:
    print("El numero es negativo")