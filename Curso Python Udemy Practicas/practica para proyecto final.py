#   Practica de ejercicios para el proyecto final de python
#___Funciones___
def triangulo():
    print("Area del triangulo")
    base = float(input("Base del rectángulo: "))
    altura = float(input("Altura del rectángulo: "))

    areaTriangulo = base * altura

    print("El area del triangulo es: ", areaTriangulo)

def dolarColon():
    print("Dolar a colon")
    dolar = float(input("Dolar: "))

    conversion = dolar * 637.87
    print(f"{dolar} dolar estadounidense")

    print(f"{conversion} colon costarricense")

def grados():
    print("Celsius a Fahrenheit")
    centigrado = float(input("Celsius:"))

    conversion = (centigrado * 9/5) +32

    print(f"{centigrado} Grado Celsius")

    print(f"{conversion} Grado Fahrenheit") 

def segundosLustro():
    print("¿Cuantos segusndos tiene un lustro?")
    segundo = 1
    minuto = segundo * 60 
    hora = minuto * 60
    dia = hora * 24
    año = dia * 365
    lustro = año * 5

    print(f"Un lustro tiene {lustro} segundos")

def marte():
    segundos = 0
    distancia = 208000000000
    velocidadLuz = 299792458 # m/s

    duracionLuzSegundos = distancia / velocidadLuz
    duracionLuzMinutos = duracionLuzSegundos / 60


    print(f"La duracion de la luz desde el sol a marte es aproximadamente {duracionLuzSegundos} segundos\nEn minutos es aproxiamdamente {duracionLuzMinutos}")




    
#___Menu___



while True:
    print("============================")
    print("MENU")
    print("1- Area triangulo")
    print("2-Dolar a colon")
    print("3-Celsius a Fahrenheit")
    print("4-Cantidad segundos tiene el lustro")
    print("5-Duracion de luz entre Sol y Marte")
    print("6-Salir")

    opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")

    while not opcion.isdigit():
        print("============================")
        print("MENU")
        print("1- Area triangulo")
        print("2-Dolar a colon")
        print("3-Celsius a Fahrenheit")
        print("4-Cantidad segundos tiene el lustro")
        print("5-Duracion de luz entre Sol y Marte")
        print("6-Salir")
        opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")

    if opcion == "1":
        triangulo()
        input("Enter para continuar...")
    elif opcion == "2":
        dolarColon()
        input("Enter para continuar...")
    elif opcion == "3":
        grados()
        input("Enter para continuar...")
    elif opcion == "4":
        segundosLustro()
        input("Enter para continuar...")
    elif opcion == "5":
        marte()
        input("Enter para continuar...")
    elif opcion == "6":
        break

