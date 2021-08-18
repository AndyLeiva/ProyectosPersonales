print("Porgrama para saber si en un intervalo hay numeros divisible entre 2, 3 y 5")
numeroIncial = int(input("Introduce el incio del intervalo: "))
numeroFinal = int(input("Introduce el final del intervalo: "))
index = numeroIncial
while index <= numeroFinal:
    if index % 2 == 0 and index % 3 == 0 and index % 5 == 0:
        print(f"El numero {index} son divisible entre 2, 3 y 5")
        #break
    
    
    elif index == numeroFinal + 1:
        print(f"En el rango entre {numeroIncial} y {numeroFinal} no hay numeros divisibles entre 2, 3 y 5")
    index += 1
        