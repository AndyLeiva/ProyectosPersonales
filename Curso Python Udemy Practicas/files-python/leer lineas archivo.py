from io import open

file = open("file-Aprendizaje-Automatico.doc","r")

reading = file.readlines()
print(reading)

file.close()

print("File had read succesfully!")