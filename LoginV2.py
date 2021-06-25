#Crear registro de los usuarios con sqlite
#Crear inicio de sesión y que compruebe si el usuario y contraseña existe en sqlite

#Importar la libreria sqlite3
from tkinter import *
from tkinter import Entry
import sqlite3
from sqlite3.dbapi2 import Cursor

conexion = sqlite3.connect("Login.db")

cursor = conexion.cursor()

#   Creación de la Tabla
#cursor.execute("CREATE TABLE IF NOT EXISTS usuarios "\
    #"(usuario VARCHAR(100), contrasena VARCHAR(100))")


conexion.close()



#Crear interfaz gráfica del login

root = Tk()
root.title("Login")
root.geometry("400x300")
root.resizable(False,False)

#   Funcion de insertar los datos a la tabla usuarios
def registrar():
    #cursor.execute('INSERT INTO usuarios()nombre values()')
    #conexion.commit()
    print("Boton presionado ", valorUsuario.get())

valorUsuario = StringVar()
valorContrasena = StringVar()

#Crear las etiquetas
etiquetaUsuario = Label(root, text="Ingrese su usuario: ", font="Arial 12")
etiquetaUsuario.place(x=10, y=70)

etiquetaContrasena = Label(root, text="Ingrese su Contraseña: ", font="Arial 12")
etiquetaContrasena.place(x=10, y=150)

#Crear los Entry(Cajas de texto)
entryUsuario = Entry(root, textvariable=valorUsuario)
entryUsuario.place(x=180, y=70)

entryContrasena = Entry(root, textvariable=valorContrasena)
entryContrasena.place(x=180, y=151)


#Crear Boton para guardar el usuario y contraseña

botonRegistrar = Button(root, text="Registrar datos", font="Arial 12", command="registrar")
botonRegistrar.place(x=150, y=220)

root.mainloop()





