nombre = input("Introduce tu nombre: ")
contrasena = input("Introduce tu contrseña: ")

while len(contrasena) < 7:
    print("Su contrseña es muy corta, debe ser de al menos 8 caracteres")
    nombre = input("Introduce tu nombre: ")
    contrasena = input("Introduce tu contrseña: ")
    
print("USUARIO CORRECTO \nCONTRASEÑA SEGURA")
    
