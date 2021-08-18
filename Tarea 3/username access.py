nombre = input("Ingrese su usuario: ")
usuario = "Andy"


for intento in range(3):
    if nombre == "Andy":
        print("Usuario correcto!")
        break
    else:
        print("INVALIDO!")
        nombre = input("Ingrese su usuario: ")