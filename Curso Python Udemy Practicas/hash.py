rotacion = int(input("Introduce tu numero de rotación: "))

letraAscci = 65

while letraAscci <= 90:
    if letraAscci + rotacion <= 90:
        print(chr(letraAscci), ": ", chr(letraAscci + rotacion))
    else:
        print(chr(letraAscci), ": ", chr((letraAscci-26)+rotacion))
    letraAscci += 1