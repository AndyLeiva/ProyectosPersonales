def dibujarCuadrado(base, altura):
    
    for i in range(altura):
        for j in range(base):
            print("* ", end="")
        print()
        

base = int(input("Base del rectángulo: "))
altura = int(input("Altura del rectángulo: "))
dibuje = dibujarCuadrado(base , altura)