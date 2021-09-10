def dibujarCuadrado(base, altura, caracter):
    
    for i in range(altura):
        for j in range(base):
            print(caracter," ", end="")
        print()
        
print("Dibujando rectangulos")
base = int(input("Base del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
caracter = input("Introzca el caracter que desee: ")
dibuje = dibujarCuadrado(base , altura, caracter)