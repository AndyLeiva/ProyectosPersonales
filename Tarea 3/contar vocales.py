string = input("Introduce tu texto para contar sus vocales: ")
string.lower()

incrementador = 0
contarVocales = 0




while incrementador < len(string):
    if string[incrementador] == "a" or string[incrementador] == "e" or string[incrementador] == "i" or string[incrementador] == "o" or string[incrementador] == "u":
        contarVocales += 1
    incrementador += 1
    
print(f"\n\nEl texto '{string}' \nContiene {contarVocales} vocales")