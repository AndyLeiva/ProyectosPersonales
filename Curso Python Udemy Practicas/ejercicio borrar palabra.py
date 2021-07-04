string = "El camino está cerrado de seguro encontraremos una solución"
print("Este es el string original: ", end=" ")
print(string)

word = input("Introduce la palabra que deseas eliminar del texto: ")

wordEliminated = string.find(word)
subString = string[:wordEliminated] + string[wordEliminated+len(word):]

print("Texto modificado: ", subString)