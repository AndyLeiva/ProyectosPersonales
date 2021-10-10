
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
            print("¡ESE NUMERO NO SE ENCUENTRA!")
            numero = int(input("Seleccione el numero del jugador: "))
        
        print("Ha seleccionado el jugador: ", diccionarioJugadores[numero])
        eliminarJugador = diccionarioJugadores.pop(numero)

    def agregarJugadores():
        numero = int(input("Ingrese el numero de la camisa del nuevo jugador: "))
        while numero in diccionarioJugadores.keys():
            print("¡ESE NUMERO YA SE ENCUENTRA, POR FAVOR INGRESA OTRO NUMERO!")
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