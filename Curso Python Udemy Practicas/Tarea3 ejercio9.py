juan = int(input("Ingrese el la cantidad de manzanas de Juan: "))
maria = int(input("Ingrese el la cantidad de manzanas de Maria: "))
adan = int(input("Ingrese el la cantidad de manzanas de Adan: "))

print(f"Juan tiene {juan} manzana(s), Maria tiene {maria} manzana(s), Adan tiene {adan} manzana(s)")

totalManzanasSuma = juan + maria + adan
totalManzanasResta = juan - maria - adan
totalManzanasMultiplicacion = juan * maria * adan
totalManzanasDivision = juan / maria / adan
totalDivisionEntera = juan // maria // adan
totalManzanasPotencia = juan ** maria ** adan

print("Total de la suma de manzanas: ", totalManzanasSuma)
print("Total de la resta de manzanas: ", totalManzanasResta)
print("Total de la multiplicación de manzanas:", totalManzanasMultiplicacion)
print("Total de la division con punto decimal de manzanas: ", totalManzanasDivision)
print("Total de la division entera de manzanas: ", totalDivisionEntera)
print("Total de la potencia de manzanas: ", totalManzanasPotencia)

