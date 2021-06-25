


class Login():
    
    
    
    def Registrar(self, usuario, confirmarUsuario, contrasena, confirmarContrasena):
        self.nombre = usuario
        self.contrasena = contrasena
        self.confirmarUsuario = confirmarUsuario
        self.confirmarContrasena = confirmarContrasena
        
        
        while self.nombre != self.confirmarUsuario or self.contrasena != self.confirmarContrasena:
    
            print("Vuelve a intentarlo\n")
            self.nombre = input("Ingrese su Nombre para registrarlo: ")
            self.confirmarUsuario = input("Vuelve a confirmar tu nombre: ")
            self.contrasena = input("Ingrese su contraseña  para registrarlo para registrarla: ")
            self.confirmarContrasena = input("Vuelva a confirmar su contraseña registrada: ")
                
            if self.nombre == self.confirmarUsuario and self.contrasena == self.confirmarContrasena:
                
                break
            
            
            
        #   Datos registrados en el diccionario baseDatos    
        baseDatos = {
                     "usuario": self.nombre,
                     "contraseña": self.contrasena
                     }
        
        print("Has registrado tus datos correctamente")
        

        
        ## Crear login
        #pedir el usuario y contraseña para ingresar al sistema
        validarUsuario = input("Ingrese su nombre para iniciar sesión: ")
        validarContrasena = input("Ingrese su contraseña para iniciar sesión: ")
        
        for iniciarSesion in baseDatos.values():
            print(iniciarSesion)
            
        
        
        
            
        
        
        
        
ventanaEntrar = Login()
ventanaEntrar.Registrar(input("Ingrese su nombre para registrarlo: "),input("Vuelva a ingresar su nombre para validar su registrado: "),
                        input("Ingrese su contraseña para registrarla: "),input("Vuelva a confirmar su contraseña registrada: "))