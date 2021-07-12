from tkinter import *
root = Tk()
root. title("Registrar Usuarios")
root.geometry("400x300")

import sqlite3
from sqlite3.dbapi2 import Cursor

conexion = sqlite3.connect("Login.db")
#cursor = conexion.cursor()
#   Creación de la Tabla
#cursor.execute("CREATE TABLE IF NOT EXISTS usuarios "\
    #"(usuario VARCHAR(100), contrasena VARCHAR(100))")

def registrar():
    #Conexion con la Base de datos
    cursor1 = conexion.cursor()
    
    listaDatos = [valorUsuario.get(), valorContrasena.get()]
    #listaContrasena = [valorContrasena.get()]
    
    #Insertar datos ala tabla usuarios en las columnas usuario y contraseña
    cursor1.execute('INSERT INTO usuarios(usuario, contrasena) values(?,?)', listaDatos)
    conexion.commit()

    
    print("Boton presionado ", valorUsuario.get(), valorContrasena.get())



#Variable de las cajas de texto
valorUsuario = StringVar()
valorContrasena = StringVar()


#Etiquetas
etiquetaUsuario = Label(root, text="Escribe el Usuario: ")
etiquetaUsuario.place(x=10, y=50)

etiquetaContrasena = Label(root, text="Escribe la contraseña: ")
etiquetaContrasena.place(x=10, y=100)

#Cajas de texto
cajaUsuario = Entry(root, textvariable=valorUsuario)
cajaUsuario.place(x=180, y=50)

cajaContrasena = Entry(root, textvariable=valorContrasena)
cajaContrasena.place(x=180, y=100)

botonRegistrar = Button(root, text="Registrar", command=registrar)
botonRegistrar.place(x=150, y=250)


root.mainloop()
    