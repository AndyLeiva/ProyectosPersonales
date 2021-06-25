class Login():
    #   Crear login
    #   pedir el usuario y contraseña para ingresar al sistema
    #   limitar 3 intentos el acceso
    

    def Registrar(self, usuario, confirmarUsuario, contrasena, confirmarContrasena):
        self.usuario = usuario
        self.contrasena = contrasena
        self.confirmarUsuario = confirmarUsuario
        self.confirmarContrasena = confirmarContrasena
        
        
        while self.usuario != self.confirmarUsuario or self.contrasena != self.confirmarContrasena:
    
            print("Vuelve a intentarlo\n")
            self.usuario = input("Ingrese su Nombre para registrarlo: ")
            self.confirmarUsuario = input("Vuelve a confirmar tu nombre: ")
            self.contrasena = input("Ingrese su contraseña  para registrarlo para registrarla: ")
            self.confirmarContrasena = input("Vuelva a confirmar su contraseña registrada: ")
                
            if self.usuario == self.confirmarUsuario and self.contrasena == self.confirmarContrasena:
                 
                 break
            
            
        print("Has registrado tus datos correctamente")
       
      
logged = Login()
logged.Registrar(input("Ingrese su nombre para registrarlo: "),input("Vuelva a ingresar su nombre para validar su registrado: "),
                        input("Ingrese su contraseña para registrarla: "),input("Vuelva a confirmar su contraseña registrada: "))
        
