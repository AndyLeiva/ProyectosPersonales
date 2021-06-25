class Login():
    
    def __init__(self, usuario, contrasena) -> None:
        self.usuario = usuario
        self.contrasena = contrasena
    
    def Registrar(self, usuario, confirmarUsuario, contrasena, confirmarContrasena):
        self.nombre = usuario
        self.contrasena = contrasena
        self.confirmarUsuario = confirmarUsuario
        self.confirmarContrasena = confirmarContrasena
        
        intentos = 3
        while self.nombre != self.confirmarUsuario or self.contrasena != self.confirmarContrasena:
            
            for intentoslimitados in range(1,3,1):
                
                print(f"Te quedan {intentos - 1} intentos\n")
                intentos = intentos - 1
           
                print("Vuelve a intentarlo\n")
                self.nombre = input("Ingrese su Nombre: ")
                self.confirmarUsuario = input("Vuelve a confirmar tu nombre: ")
                self.contrasena = input("Ingrese su contraseña: ")
                self.confirmarContrasena = input("Vuelva a confirmar su contraseña: ")
                
            if intentos <= 1:
                print("Acceso denegando")
                break
            elif self.nombre == self.confirmarUsuario and self.contrasena == self.confirmarContrasena:
                
                break
        print("Has registrado tus datos correctamente")
        
        ## Crear login
        #pedir el usuario y contraseña para ingresar al sistema
        
        #def login(self, usuario, contrasena):
            
            
            
            
            
            
            

   
        
        
        
ventanaEntrar = Login()
ventanaEntrar.Registrar(input("Ingrese su nombre: "),input("Vuelva a ingresar su nombre: "),
                        input("Ingrese su contraseña: "),input("Vuelva a confirmar su contraseña: "))