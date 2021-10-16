from io import open

file = open("file-Aprendizaje-Automatico.doc","a")

text = ("\nPuedes aplicar la misma idea a sistemas de recomendación (piensa en YouTube, Amazon y Netflix), Reconocimiento facial o reconocimiento de voz entre otras aplicaciones.”")


file.write(text)

file.close()

print("File updated succesfully!")
input()