def comprobarBisiesto(fecha):
    
    if fecha % 400 == 0 or (fecha % 100 != 0 and fecha % 4 == 0):
        print("El año", fecha, "es un año bisiesto.")
    else:
        print("El año", fecha, "no es un año bisiesto.")
        
print("Comprobando años bisiestos")
fecha = int(input("Escriba un año y le diré si es bisiesto: "))
comprobarBisiesto(fecha)
input("Enter para cerrar...")