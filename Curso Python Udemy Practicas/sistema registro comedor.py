#modulos importados time y sqlite3
import sqlite3 as sql 
import time



#conexion con la base de datos

def crearBD():
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()
    conexion.close()

#tabla Estudiantes
#Columnas: Cedula, Nombre, Sección, Fecha y Hora

def crearTabla():
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()
    
#Datos del estudiante
    cursor.execute(
    """CREATE TABLE Estudiantes (
        cedula integer,
        nombre text,
        seccion text

    )"""
    )
#Se guarda la entrada del estudiante
    cursor.execute(
        """CREATE TABLE Registros (
            cedula integer,
            nombre text,
            seccion text,
            fecha text,
            hora text

        )"""
    )
    conexion.commit()
    conexion.close()


# Insertar registos 
def insertardatos(cedula, nombre, seccion): #tabla estudiantes
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO Estudiantes VALUES({cedula}, '{nombre}', '{seccion}')"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()

def insertarRegistros(cedula, nombre, seccion, fecha, hora): #tabla registros
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()
    instruccion = f"INSERT INTO Registros VALUES({cedula}, '{nombre}', '{seccion}', '{fecha}', '{hora}')"
    cursor.execute(instruccion)
    conexion.commit()
    conexion.close()


#leer datos de las tablas

def leerFilas():
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM Estudiantes"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print("TABLA ESTUDIANTES\n",datos)

def buscarDatos(cedula):
    conexion = sql.connect("Estudiantes.db")
    cursor = conexion.cursor()
    instruccion = f"SELECT * FROM Estudiantes WHERE cedula = {cedula}"
    cursor.execute(instruccion)
    datos = cursor.fetchall()
    conexion.commit()
    conexion.close()
    print("ESTUDIANTE:\n",datos)


#funcion de registrar el estudiante
# crear una tabla para los datos del estudiante y otra tabla donde guarda el registra la entrada del estudiante al comedor.
# 
# el programa pide la cedula, luego busca si existe en la tabla estudiantes, si existe pues se guarda el la cedula, nombre, seccion,  fecha y hora automaticamente
# si la cedula no existe hay dos opciones, se puede agregar los datos del estudiante, o denegar la entrada al comedor. 


#el menu podria tener las opciones: 
# 1-consultar base de datos,  "read"
# 2-agregar datos del estudiante, "write-update"
# 3-registar el estudiante para la hora de almuerzo "register" por medio de la cedula
# 4-Salir "exit"

# crear una funcion que extraiga los datos de la tabla estudiantes y los inserte en la tabla registro segun la cedula


if __name__ == "__main__":
    print("Sistema Registro Comedor")
    #crearBD()
    #crearTabla()


    cedula = int(input("Cedula:"))
    #nombre = input("Nombre: ")
    #seccion = input("Seccion: ")
    #fecha = time.strftime("%x")
    #hora = time.strftime("%X")
    #fecha = str(fecha)
    #hora = str(hora)

    #insertarRegistros(cedula, nombre, seccion, fecha, hora) # tabla registros
    #insertardatos(cedula, nombre, seccion) # tabla estudiantes

    #leerFilas()
    buscarDatos(cedula)