def AreaRectangulo(base, altura):
   
    
    area = base * altura
    return area

print("Calcula el area del retangulo")
b = float(input("Ingrese la base: "))
h = float(input("Ingrese la altura: "))

calcularArea = AreaRectangulo(b,h)
print("El area del rectangulo es: ", calcularArea)
input("Enter para cerrar...")
