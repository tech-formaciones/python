import sqlite3, json

# Establecer una conexión con la base de datos, especificando la ruta del fichero
# Si el fichero no exite (la base de datos no existe) se crea

# Ruta absoluta
#connection = sqlite3.connect("C:\\Formación_EOI\\Repos\\python\\04-Bases-de-datos\\databases\\demo.db")

# Ruta relativa
connection = sqlite3.connect(".\\databases\\demo.db")

# Ruta, la misma ubicación del fichero de python
#connection = sqlite3.connect("demo.db")

# Crea una base de datos en memory ram, es rapido pero lo datos se eliminan al
# finalizar la ejecuación de programa Pyhton
#connection = sqlite3.connect(":memory:")

# Creamos un cursor para ejecutar comandos en la base de datos
cursor = connection.cursor()

# Consultar la existencia de tablas en la base de datos
# Si la tabla no existe la creamos
command = """
    SELECT COUNT() FROM sqlite_master WHERE type = 'table' AND name = 'Alumnos'
"""
cursor.execute(command)
numTablas = cursor.fetchone()[0]
print(f"Número de tablas con nombre Alumnos: {numTablas}")

if(numTablas == 0):
    command = """
        CREATE TABLE Alumnos (id, nombre, apellidos, curso, notas)
    """
    cursor.execute(command)

    command = """
        CREATE TABLE Profesores (
            id integer, nombre text, apellidos text, 
            curso text, salario real, foto blob)
    """
    cursor.execute(command)



# Insertamos registros mediante INSERT
command = " INSERT INTO Alumnos (id, nombre) VALUES ('000', 'Borja')"
cursor.execute(command)
connection.commit()
print(f"{cursor.rowcount} registros insertados")
