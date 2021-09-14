import getpass
def login():
    
    print("Bienvenido a al reto de programación de Andy Leiva")
    nombre = input("Ingresa tu nombre: ")
    contrasena = getpass.getpass("Ingresa tu Contraseña: ")
    
    
def menu():
    
    #___Funciones___
    def lista():
        listaNueva = []
        cantidad = int(input("¿Cuantos elementos quiere ingresar? : "))
        
        for i in range(cantidad):
            nombre = input("Ingrese el nombre del Estudiante: ")
            nombreMayus = nombre.upper()
            listaNueva.append(nombreMayus)
        print(f"\nLa lista de {len(listaNueva)} elementos es: \n{listaNueva}\n")
        
        #___Menu para la lista___
        while True:
            print("Menu de opciones de la lista")
            print("1-Agregar nuevos elementos")
            print("2-Modificar lista")
            print("3-Eliminar elementos")
            print("4-Salir al menu principal")
            opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
            
            while not opcion.isdigit():
                print("¡ERROR!\n FAVOR INGRESE UN NUMERO ENTERO\n")
                print("Menu de opciones de la lista")
                print("1-Agregar nuevos elementos")
                print("2-Modificar elementos")
                print("3-Eliminar elementos")
                print("4-Salir al menu principal")
                opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
                
                
            if opcion == "1":
                print("\nLa lista: ", listaNueva)
                cantidad = int(input("¿Cuantos elementos quiere ingresar? : "))
        
                for i in range(cantidad):
                    nombre = input("Ingrese el nombre del Estudiante: ")
                    nombreMayus = nombre.upper()
                    listaNueva.append(nombreMayus)
                print(f"\nLa lista de {len(listaNueva)} elementos es: \n{listaNueva}\n")
            elif opcion == "2":
                pass #modificar
            elif opcion == "3":
                pass #eliminar
                
        
    
    
    
    
    #_______MENU______
    while True:
        print("Menu de opciones")
        print("1-Listas")
        print("2-Tuplas")
        print("3-Diccionarios")
        print("4-Conversion")
        print("5-Salir")
        opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
        
        
        
        while not opcion.isdigit():
            print("¡ERROR!\n FAVOR INGRESE UN NUMERO ENTERO\n")
            print("Menu de opciones")
            print("1-Listas")
            print("2-Tuplas")
            print("3-Diccionarios")
            print("4-Conversion")
            print("5-Salir")
            opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
        
        if opcion == "1":
            print("\nHAS ELEJIDO LISTAS\n")
            lista()
            input("Enter para continuar...\n")
        elif opcion == "2":
            pass
        
        
        
                
        
        
        
        
        
    
    
    




# ___MAIN____
login()
menu()



