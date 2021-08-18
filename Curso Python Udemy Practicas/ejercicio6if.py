nombre = input("Ingrese su nombre: ")
if len(nombre) > 10:
    print("Su nombre es mayor a 10 caracteres")
else:
    print("Su nombre es menor a 10 caracteres")
    
    
nombre = input("Ingrese su nombre: ")
print("Su nombre es mayor a 10 caracteres") if len(nombre) > 10 else print("Su nombre es menor a 10 caracteres")