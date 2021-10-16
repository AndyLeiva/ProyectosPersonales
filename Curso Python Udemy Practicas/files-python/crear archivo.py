from io import open

file = open("script-hola.py","w")

text = ("print('hola')\ninput()")


file.write(text)

file.close()

print("File created succesfully!")
