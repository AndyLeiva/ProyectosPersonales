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
            print("4-REDONDEO A NUMERO ENTERO")
            print("5-SALIR AL MENU PRINCIPAL")
            
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
     
                    
               
    def mod():
        numero1 = float(input("Ingrese un numero: "))
        numero2 = float(input("Ingrese otro numero: ")) 
        
        print(f"El numero mod de {numero1} y {numero2} es: ", math.fmod(numero1, numero2))
        
               
                
    def absoluto():
        numero1 = float(input("Ingrese un numero: "))
        print(f"El numero absoluto de {numero1} es: |{math.fabs(numero1)}|")
            
    
    def areaCirculo():
        radio = float(input("Ingrese la logitud de radio en cm: "))
        
        a = math.pi * radio**2
        
        print(f"El area del circulo es: {a} cm")
    
    def potencia():
        base = float(input("Ingrese la base de la potencia: "))
        exponente = float(input("Ingrese el exponente de la potencia: "))
        
        print("El resultado es: ", math.pow(base, exponente))
        
    def sumaRaiz():
        numero1 = float(input("Ingrese un numero positivo: "))
        numero2 = float(input("Ingrese un segundo numero positivo: "))
        numero3 = float(input("Ingrese un tercer numero positivo: "))
        
        print(f"La raiz cuadrada de {numero1} es: ", math.sqrt(numero1))
        print(f"La raiz cuadrada de {numero2} es: ", math.sqrt(numero2))
        print(f"La raiz cuadrada de {numero3} es: ", math.sqrt(numero3))
        
        suma  = math.sqrt(numero1) + math.sqrt(numero2) + math.sqrt(numero3)
        
        print("El total de la suma es: ", suma)
        
    def teoremaPitagoras():
        cateto1= float(input("Ingrese el valor del primer cateto: "))
        cateto2 = float(input("Ingrese el valor del segundo cateto: "))
        
        h = math.hypot(cateto1, cateto2)
        
        print("La hipotenusa es: ", h)
        
    def senoCoseno():
        numero = int(input("Ingresa el numero:"))
        
        print(f"El Seno es: {math.sin(numero)}\n El Coseno es {math.cos(numero)}")
        
    def ramainder():
        divisor = float(input("Ingrese el divisor: "))
        dividendo = float(input("Ingrese el dividendo: "))
        print("EL residuo es: ", math.fmod(divisor, dividendo))
        
    
    #___MENU____
    
    while True:
        print("==========================================")
        print("MENU PRINCIPAL")
        print("==========================================")
        print("1-Redondear numeros decimales")
        print("2-Listas")
        print("3-MOD DE DOS NUMEROS")
        print("4-NUMERO ABSOLUTO")
        print("5-AREA DEL CIRCULO")
        print("6-POTENCIA")
        print("7-RAIZ Y SU SUMA")
        print("8-TEOREMA PITAGORAS")
        print("9-SENO Y COSENO")
        print("10-REMAINDER")
        print("11-CERRAR")
       
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
            print("3-MOD DE DOS NUMEROS")
            print("4-NUMERO ABSOLUTO")
            print("5-AREA DEL CIRCULO")
            print("6-POTENCIA")
            print("7-RAIZ Y SU SUMA")
            print("8-TEOREMA PITAGORAS")
            print("9-SENO Y COSENO")
            print("10-REMAINDER")
            print("11-CERRAR")
            
           
            print("==========================================")
            opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")
            
        if opcion == "1":
            print("\nHAS ELEJIDO REDONDEAR\n")
            redondeo()
            
            
        elif opcion == "2":
            print("Has elejido Listas")
            listas()
        
        elif opcion == "3":
            print("Ha elejiido MOD")
            mod()
        elif opcion == "4":
            print("Ha elegido Numero absoluto")
            absoluto()
        elif opcion == "5":
            print("Has elegido el area del circulo")
            areaCirculo()
        elif opcion == "6":
            print("Has elegido potencia")
            potencia()
        elif opcion == "7":
            print("Has elegido Raiz y su suma")
            sumaRaiz()
        elif opcion == "8":
            print("HAS elegido Teorema Pitágoras")
            teoremaPitagoras()
        elif opcion == "9":
            print("Has elegido Seno y Coseno")
            senoCoseno()
        elif opcion == "10":
            print("Has elegido Remainder")
            ramainder()
        elif opcion == "11":
            break 
 
menu()
