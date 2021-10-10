import getpass
def login():
    
    print("Bienvenido a al reto de programación de Andy Leiva")
    nombre = input("Ingresa tu nombre: ")
    contrasena = getpass.getpass("Ingresa tu Contraseña: ")
    
    
def menu():
    
    #___Funciones___
    def listas():
        listaNueva = []
        cantidad = int(input("¿Cuantos elementos quiere ingresar? : "))
        
        for i in range(cantidad):
            nombre = input("Ingrese el nombre del Estudiante: ")
            nombreMayus = nombre.upper()
            listaNueva.append(nombreMayus)
        print(f"\nLa lista de {len(listaNueva)} elementos es: \n{listaNueva}\n")
        
        #___Menu para la lista___
        while True:
            print("==========================================")
            print("Menu de opciones de la lista")
            print("==========================================")
            print("1-Agregar nuevos elementos")
            print("2-Modificar lista")
            print("3-Eliminar elementos")
            print("4-Salir al menu principal")
            print("==========================================")
            opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
            
            while not opcion.isdigit():
                print("==========================================")
                print("¡ERROR!\n FAVOR INGRESE UN NUMERO ENTERO\n")
                print("==========================================")
                print("Menu de opciones de la lista")
                print("==========================================")
                print("1-Agregar nuevos elementos")
                print("2-Modificar elementos")
                print("3-Eliminar elementos")
                print("4-Salir al menu principal")
                opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
                
                
            if opcion == "1":
                #Agregar nuevos elementos
                print("==========================================")
                print("AGREGAR ELEMENTOS")
                print("==========================================")
                
                
                print("\nLa lista: ", listaNueva)
                cantidad = int(input("¿Cuantos elementos quiere ingresar? : "))
        
                for i in range(cantidad):
                    nombre = input("Ingrese el nombre del Estudiante: ")
                    nombreMayus = nombre.upper()
                    listaNueva.append(nombreMayus)
                print(f"\nLa lista de {len(listaNueva)} elementos es: \n{listaNueva}\n")
                input("Enter para continuar...")
            elif opcion == "2":
                #modificar
                print("==========================================")
                print("MODIFICAR ELEMENTOS")
                print("==========================================")
                print(listaNueva)
                buscarIndex = input("Seleccione el Elemento: ")
                buscarElemento = buscarIndex.upper()
                
                
                while buscarElemento not in listaNueva:
                    print("Ese elemento no se encuentra!")
                    print(listaNueva)
                    buscarIndex = input("Seleccione el Elemento: ")
                    buscarElemento = buscarIndex.upper()
                
                indice = listaNueva.index(buscarElemento)
                    
                
                nuevoElemento= input("Remplazar elemento por: ")
            
                listaNueva[indice] = nuevoElemento.upper()
            
                print("\nLa lista: ", listaNueva)
                
                input("Enter para continuar...")
            
            elif opcion == "3":
                #eliminar elementos
                print("==========================================")
                print("ELIMINAR ELEMENTOS")
                print("==========================================")
                print(listaNueva)
                buscarElemento = input("Seleccione el Elemento: ")
                buscarElemento = buscarElemento.upper()
                
                
                while buscarElemento not in listaNueva:
                    print("Ese elemento no se encuentra!")
                    print(listaNueva)
                    buscarElemento = input("Seleccione el Elemento: ")
                    buscarElemento = buscarElemento.upper()
                    
                listaNueva.remove(buscarElemento)
                    
                print("\nLa lista: ", listaNueva)
                input("Enter para continuar...")
                
            elif opcion == "4":
                #SALIR
                break
            else:
                #OPCION INCORRECTA
                print("Esa opcion es incorrecta!")
                
        
    def tuplas():
        tupla = (8,6,10,8,6,10,11,12,12,12,7,1,9,8,0,0,10,11,12,9)
        
        
        
        while True:
            print("==========================================")
            print("COSULTAS PARA LA TUPLA:\n\n",tupla)
            print("==========================================")
            print("1-Cantidad de elementos")
            print("2-Elementos repetidos")
            print("3-Ver ultimo elemento")
            print("4-Convertir tupla a lista")
            print("5-Salir")
            print("==========================================")
            opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
        
        
            while not opcion.isdigit():
                print("==========================================")
                print("¡ERROR!\n FAVOR INGRESE UN NUMERO ENTERO\n")
                print("==========================================")
                print("COSULTAS PARA LA TUPLA:\n\n",tupla)
                print("==========================================")
                print("1-Cantidad de elementos")
                print("2-Elementos repetidos")
                print("3-Ver ultimo elemento")
                print("4-Convertir tupla a lista")
                print("5-Salir")
                print("==========================================")
                opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
        
            if opcion == "1":
                print("==========================================")
                print("Cantidad de elementos de:\n\n",tupla)
                print("==========================================")
                print("LA TUPLA TIENE: ",len(tupla)," ELEMENTOS")
                input("Enter para continuar...")
                
                
            elif opcion == "2":
                print("==========================================")
                print("Elementos repetidos:\n\n",tupla)
                print("==========================================")
                
                elementoRepetido = int(input("Selecciona el numero: "))
                
                cantidadRepetida = tupla.count(elementoRepetido)
                
                print(f"El elemento {elementoRepetido} se repite: {cantidadRepetida}")
                
                
                
                input("Enter para continuar...")
            elif opcion == "3":
                print("==========================================")
                print("Ultimo elemento de:\n\n",tupla)
                print("==========================================")
                print("Es: ", tupla[-1])
                input("Enter para continuar...")
            elif opcion == "4":
                print("==========================================")
                print("Convertir la siguiente tupla en una lista:\n\n",tupla)
                print("==========================================")
                lista = list(tupla)
                print("La tupla se convirtió a una lista correctamente\n",lista)
                input("Enter para continuar...")
            elif opcion == "5":
                break
        
    def diccionarios():
        
        diccionario = {
            123:{"RODOLFO DURÁN WILSON","CIBERSEGURIDAD"},
            456:{"MARÍA HEINZ ROMERO", "ADMININSTRACIÓN"},
            789:{"ALBERTO JUMÉNEZ ALFARO", "MECATRÓNICA"},
            159:{"ISABELLA DANTE DIVAGO", "ELECTRICIDAD"},
            753:{"STEVEN ALFRESSON STERMAN ", "CIBERSEGURIDAD"},
            177:{"FILIPAO DISOUSA FARIAS", "CONTADOR"},
            999:{"ROSA VALVERDE BELL", "PROGRAMACIÓN"},
            
        }    
        while True:
            print("==========================================")
            print("DATOS DE ESTUDIANTES")
            print("==========================================")
            print("1-CONSULTAR DATOS")
            print("2-SALIR AL MENU PRINCIPAL")
            
            print("==========================================")
            opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
        
        
        
            while not opcion.isdigit():
                print("==========================================")
                print("¡ERROR!\n FAVOR INGRESE UN NUMERO ENTERO\n")
                print("==========================================")
                print("1-CONSULTAR DATOS")
                print("2-SALIR AL MENU PRINCIPAL")
                print("==========================================")
                opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
                
            if opcion == "1":
                print("==========================================")
                print("CONSULTANDO DATOS...")
                print("==========================================")
            
                lista = diccionario.items()
                lista = list(lista)
                print(lista,end=")")
                
                
                
                print("==========================================")
                
                cedula = int(input("Ingrese la Cedula del estudiante: "))
                while cedula not in diccionario:
                    print("LA CEDULA NO EXISTE!")
                    cedula = int(input("Ingrese la Cedula del estudiante: "))
                    
                
                print(f"EL ESTUDIANTE DE CEDULA: {cedula}\nES: ",diccionario.get(cedula))
                print("==========================================")
                input("Enter para continuar...")
                
            elif opcion == "2":
                break
            else:
                print("Opcion incorrecta!")
    
    def convertir():
        
        def menu():
            listaJugadores = [(1,["KEYLOR NAVAS","ARQUERO"]),(2,["BRYAN RUIZ","DELANTERO"]),(3,["JOEL CAMPBELL","DELANTERO"]), 
                        (4,["JIMMY MARÍN","MEDIOCAMPO"]),(5,["JONATHAN MOYA","DELANTERO"]),(6,["CELSO BORGES","MEDIOCAMPO"]),
                        (7,["MANFRED UGALDE","DELANTERO"]), (8,["KENDALL WASTON","DEFENSA"]),(9,["FRANCISCO CALVO QUESADA","DEFENSA"]),
                        (10,["JOHAN VENEGAS","MEDIOCAMPO"]), (11,["ÓSCAR DUARTE","DEFENSA"])]
            diccionarioJugadores = dict(listaJugadores)

            def tablaJugadores():
                print("==========================================")
                print("DATOS DEL EQUIPO")
                print("==========================================")
                for numero, nombrePuesto in diccionarioJugadores.items():
                    print("NUMERO CAMISA: ",numero, " NOMBRE Y PUESTO: ", nombrePuesto)
            def seleccionNumero():
                numero = int(input("Seleccione el numero del jugador: "))
                
                while numero not in diccionarioJugadores.keys():
                    print("\n¡ESE NUMERO NO SE ENCUENTRA!\n")
                    numero = int(input("Seleccione el numero del jugador: "))
                
                print("Ha seleccionado el jugador: ", diccionarioJugadores[numero])
                eliminarJugador = diccionarioJugadores.pop(numero)

            def agregarJugadores():
                numero = int(input("Ingrese el numero de la camisa del nuevo jugador: "))
                while numero in diccionarioJugadores.keys():
                    print("\n¡ESE NUMERO YA SE ENCUENTRA, POR FAVOR INGRESA OTRO NUMERO!\n")
                    numero = int(input("Ingrese el numero de la camisa del nuevo jugador: "))
                    
                nombre = input("Ingrese el Nombre del jugador: ")
                nombre = nombre.upper()
                puesto = input("Ingrese el puesto del jugador: ")
                puesto = puesto.upper()

        
                diccionarioJugadores[numero] = [nombre, puesto]
                
            while True:
                print("==========================================")
                print("DATOS DEL EQUIPO")
                print("==========================================")
                print("1-CAMBIAR JUGADOR")
                print("2-SALIR AL MENU PRINCIPAL")
                
                print("==========================================")
                opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
            
            
            
                while not opcion.isdigit():
                    print("==========================================")
                    print("¡ERROR!\n FAVOR INGRESE UN NUMERO ENTERO\n")
                    print("==========================================")
                    print("1-CAMBIAR JUGADOR")
                    print("2-SALIR AL MENU PRINCIPAL")
                    print("==========================================")
                    opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
                    
                if opcion == "1":
                    print("==========================================")
                    print("CAMBIAR JUGADOR")
                    print("==========================================")

                    tablaJugadores()
                    seleccionNumero()
                    agregarJugadores()
                    tablaJugadores()
                    print("==========================================")
                    print("SE AGREGÓ EL JUGADOR CORRECTMENTE")
                    print("==========================================")
                    
                    input("Enter para continuar...")
                elif opcion == "2":
                    break
        menu()
        
        
        
    
    #_______MENU______
    while True:
        print("==========================================")
        print("MENU PRINCIPAL")
        print("==========================================")
        print("1-Listas")
        print("2-Tuplas")
        print("3-Diccionarios")
        print("4-Conversion")
        print("5-Salir")
        print("==========================================")
        opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
        
        
        
        while not opcion.isdigit():
            print("==========================================")
            print("¡ERROR!\n FAVOR INGRESE UN NUMERO ENTERO\n")
            print("==========================================")
            print("MENU PRINCIPAL")
            print("==========================================")
            print("1-Listas")
            print("2-Tuplas")
            print("3-Diccionarios")
            print("4-Conversion")
            print("5-Salir")
            print("==========================================")
            opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
        
        if opcion == "1":
            print("\nHAS ELEJIDO LISTAS\n")
            listas()
            
        elif opcion == "2":
            print("\nHAS ELEJIDO TUPLAS\n")
            tuplas()
        elif opcion == "3":
            diccionarios()
        elif opcion == "4":
            convertir()
        elif opcion == "5":
            break
        
        


    
# ___MAIN____
login()
menu()
print("Gracias por utilizar nuestro software!")
input()





