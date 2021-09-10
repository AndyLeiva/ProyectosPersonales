def creciente(anchura):
    for i in range(1, anchura + 1):
        for j in range(i):
            print("* ", end="")
        print()
        
def decreciente(anchura):
    for i in range(1, anchura):
        for j in range(anchura - i):
            print("* ", end="")
        print()
        
anchura = int(input("Anchura del triángulo: "))
for i in range(anchura, 0, -1):
    creciente(i)
    decreciente(i)
input("Enter para cerrar...")
