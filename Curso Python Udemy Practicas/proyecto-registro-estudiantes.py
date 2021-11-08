import time
bd = {305400271:"Andy Leiva Camacho"}
cedula = int(input("Escribe la cedula del alumno: "))

while cedula not in bd.keys():
    print("\n¡ESE NUMERO NO SE ENCUENTRA!\n")
    cedula = int(input("Seleccione el numero del jugador: "))

# busqueda = bd.get(cedula)

print("El estudiante: ", bd[cedula])

print("Fecha: ", time.strftime("%x"))
print("Hora: ", time.strftime("%X"))

