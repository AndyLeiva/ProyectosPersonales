class Calculadora:
    #   Sumar, restar, multiplicar y dividir
    
    def sumar(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        
        resultado = self.numero1 + self.numero2
        
        print("El resultado de la suma es: ", resultado)
        
    def restar(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        
        resultado = self.numero1 - self.numero2
        
        print("El resultado de la resta es: ", resultado)
    
    def multiplicar(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        
        resultado = self.numero1 * self.numero2
        
        print("El resultado de la multiplicar es: ", resultado)
    
    def dividir(self,numero1,numero2):
        self.numero1 = numero1
        self.numero2 = numero2
        
        resultado = self.numero1 / self.numero2
        
        print("El resultado de la divición es: ", resultado)
        
continuar = ""        
while continuar != "1" or continuar != "2" or continuar != "3" or continuar != "4" :        
    
    print("BIENVENIDO A LA CALCULADORA, \n1-Sumar\n2-Restar\n3-Multiplicar\n4-División\n5-Salir de la calculadora\n") 


    opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")


    while not opcion.isdigit():
        print("¡ERROR!\n FAVOR INGRESE UN NUMERO ENTERO\n")
        print("BIENVENDO A LA CALCULADORA, \n1-Sumar\n2-Restar\n3-Multiplicar\n4-División\n5-Salir de la calculadora\n") 
        opcion = input("Ingrese el numero de su opcion que aparece en el menú: ")

    if opcion == "1":
        print("\nHAS ELEJIDO SUMAR\n")
        operación = Calculadora()
        operación.sumar(int(input("Ingrese el primer numero a sumar: ")), int(input("Ingrese el segundo numero a sumar: ")))
        input("Enter para continuar...\n")
    elif opcion == "2":
        print("\nHAS ELEGIDO RESTAR\n")
        operación = Calculadora()
        operación.restar(int(input("Ingrese el primer numero a restar: ")), int(input("Ingrese el segundo numero a restar: "))) 
        input("Enter para continuar...\n")
    elif opcion == "3":
        print("\nHAS ELEGIDO MULTIPLICACIÓN\n")
        operación = Calculadora()
        operación.multiplicar(int(input("Ingrese el primer numero a multiplicar: ")), int(input("Ingrese el segundo numero a multiplicar: ")))
        input("Enter para continuar...\n")
    elif opcion == "4":
        print("\nHAS ELEGIDO DIVISIÓN\n")
        operación = Calculadora()
        operación.dividir(int(input("Ingrese el primer numero a dividir: ")), int(input("Ingrese el segundo numero a dividir: ")))
        input("Enter para continuar...\n")
    elif opcion == "5":
        break
        
        
    else: 
        print("Esa opcion no existe, intentalo de nuevo\n\n")           
            

print("Has salido de la calculadora")