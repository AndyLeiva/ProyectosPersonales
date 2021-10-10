import math
def menu():
    
    #___Funciones___
    
    def redondeo():
        while True:
            print("==========================================")
            print("MENU DE REDONDEO")
            print("==========================================")
            print("1-REDONDEO NORMAL")
            print("2-REDONDEO PARA ARRIBA")
            print("3-REDONDEO PARA ABAJO")
            print("4-SALIR AL MENU PRINCIPAL")
            
            print("==========================================")
            opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
        
        
        
            while not opcion.isdigit():
                print("==========================================")
                print("¡ERROR!\n FAVOR INGRESE UN NUMERO ENTERO\n")
                print("==========================================")
                print("MENU DE REDONDEO")
                print("==========================================")
                print("1-REDONDEO NORMAL")
                print("2-REDONDEO PARA ARRIBA")
                print("3-REDONDEO PARA ABAJO")
                print("4-REDONDEO A NUMERO ENTERO")
                print("5-SALIR AL MENU PRINCIPAL")
                print("==========================================")
                opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
                
            if opcion == "1":
                print("==========================================")
                print("REDONDEO NORMAL")
                print("==========================================")
                numero = float(input("Ingrese un numero decimal: ")) 
                
                print("El numero redondeado es: ",round(numero))
            elif opcion == "2":
                print("==========================================")
                print("REDONDEO PARA ARRIBA")
                print("==========================================")
                numero = float(input("Ingrese un numero decimal: "))
                
                print("El numero redondeado para arriba es: ",math.ceil(numero))
            elif opcion == "3":
                print("==========================================")
                print("REDONDEO PARA ABAJO")
                print("==========================================")
                numero = float(input("Ingrese un numero decimal: "))
                
                print("El numero redondeado para abajo es: ",math.floor(numero))
            elif opcion == "4":
                print("==========================================")
                print("REDONDEO A NUMERO ENTERO")
                print("==========================================")
                numero = float(input("Ingrese un numero decimal: "))
                
                print("El numero redondeado a numero entero es: ",math.trunc(numero))
            elif opcion == "5":
                break
    
    
    def listas():
        listaNueva = []
        cantidad = int(input("¿Cuantos elementos quiere ingresar? : "))
        
        for i in range(cantidad):
            numeros = float(input("Ingrese el nombre del Estudiante: "))
            listaNueva.append(numeros)
        print(f"\nLa lista de {len(listaNueva)} elementos es: \n{listaNueva}\n")
        
        
        print("==========================================")
        print("Sumar numeros de la lista")
        print("==========================================")
        
        print("El total es: ", math.fsum(listaNueva))
        input("Enter para continuar...")
     
                    
               
            
                
        
    
    
    
    
    #___MENU____
    
    while True:
        print("==========================================")
        print("MENU PRINCIPAL")
        print("==========================================")
        print("1-Redondear numeros decimales")
        print("2-Listas")
       
        print("==========================================")
        opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
        
        
        
        while not opcion.isdigit():
            print("==========================================")
            print("¡ERROR!\n FAVOR INGRESE UN NUMERO ENTERO\n")
            print("==========================================")
            print("MENU PRINCIPAL")
            print("==========================================")
            print("1-Redondear numeros decimales")
            print("2-Listas")
           
            print("==========================================")
            opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
            
        if opcion == "1":
            print("\nHAS ELEJIDO REDONDEAR\n")
            redondeo()
            
            
        elif opcion == "2":
            print("Has elejido Listas")
            listas()
 
 
menu()