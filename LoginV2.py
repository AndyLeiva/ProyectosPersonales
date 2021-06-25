#Crear registro de los usuarios con sqlite
#Crear inicio de sesión y que compruebe si el usuario y contraseña existe en sqlite

#Importar la libreria sqlite3

import sqlite3
from sqlite3.dbapi2 import Cursor

conexion = sqlite3.connect("Login.db")

cursor = conexion.cursor()

#   Creación de la Tabla
#cursor.execute("CREATE TABLE IF NOT EXISTS usuarios "\
    #"(usuario VARCHAR(100), contrasena VARCHAR(100))")


def insertarDatos(usuario,contrasena):    
    cursor.execute("INSERT INTO usuarios VALUES (?,?)",(usuario, contrasena))

    conexion.commit()
insertarDatos(input("USUARIO: "),input("CONTRASEÑA: "))

conexion.close()
