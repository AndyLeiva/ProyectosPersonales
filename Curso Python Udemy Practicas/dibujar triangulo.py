def dibujarTriangulo(anchura):

    for i in range(1, anchura + 1):
        for j in range(i):
            print("* ", end="")
        print()
    for i in range(1, anchura):
        for j in range(anchura - i):
            print("* ", end="")
        print()
    
anchura = int(input("Anchura del triángulo: "))
dibujarTriangulo(anchura)

