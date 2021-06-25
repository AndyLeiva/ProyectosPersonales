#Crear registro de los usuarios con sqlite
#Crear inicio de sesión y que compruebe si el usuario y contraseña existe en sqlite

#Importar la libreria sqlite3

import sqlite3
from sqlite3.dbapi2 import Cursor

#conexion = sqlite3.connect("Login.db")

#cursor = conexion.cursor()

#   Creación de la Tabla
#cursor.execute("CREATE TABLE IF NOT EXISTS usuarios "\
    #"(usuario VARCHAR(100), contrasena VARCHAR(100))")

#   Funcion de insertar los datos a la tabla usuarios
#def insertarDatos(usuario,contrasena):    
    #cursor.execute("INSERT INTO usuarios VALUES (?,?)",(usuario, contrasena))

    #conexion.commit()

#insertarDatos(input("USUARIO: "),input("CONTRASEÑA: "))

#conexion.close()

#Crear interfaz gráfica del login
from tkinter import *
root = Tk()
root.title("Login")
root.geometry("400x300")
root.resizable(False,False)


#Crear las etiquetas
etiquetaUsuario = Label(root, text="Ingrese su usuario: ", font="Arial 12")
etiquetaUsuario.place(x=10, y=70)

etiquetaContrasena = Label(root, text="Ingrese su usuario: ", font="Arial 12")
etiquetaContrasena.place(x=10, y=150)

#Crear los Entry(Cajas de texto)
entryUsuario = Entry(root)
entryUsuario.place(x=150, y=70)

entryContrasena = Entry(root)
entryContrasena.place(x=150, y=151)


#Crear Boton para guardar el usuario y contraseña

botonRegistrar = Button(root, text="Registrar datos", font="Arial 12")
botonRegistrar.place(x=150, y=220)

root.mainloop()





