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
    command = "INSERT INTO Alumnos (id, nombre) VALUES ('000', 'Borja')"
    cursor.execute(command)
    connection.commit()
    print(f"{cursor.rowcount} registros insertados")

    command = "INSERT INTO Alumnos VALUES ('001', 'Julian', 'Sánchez', '2A', Null)"
    cursor.execute(command)
    connection.commit()
    print(f"{cursor.rowcount} registros insertados")

    data = [
        ('002', 'Ana', 'Trujillo', '2C', None),
        ('003', 'Antonio', 'Sánchez', '2A', json.dumps([7.5, 6, 9, 5, 6.9])),
        ('004', 'María', 'Sanz', '2B', None)
    ]

    command = " INSERT INTO Alumnos VALUES (?, ?, ?, ?, ?)"
    cursor.executemany(command, data)
    connection.commit()
    print(f"{cursor.rowcount} registros insertados")


# Eliminar registros mediante DELETE
command = "DELETE FROM Alumnos WHERE id = '004'"
cursor.execute(command)
connection.commit()
print(f"{cursor.rowcount} registros eliminados")


# Actualizamos registros mediante UPDATE
command = "UPDATE Alumnos SET apellidos = 'Cabeza', curso = '2C' WHERE id = '000'"
cursor.execute(command)
connection.commit()
print(f"{cursor.rowcount} registros actualizados")


# Consultamos registros mediante SELECT
command = "SELECT * FROM Alumnos WHERE curso = '2A' ORDER BY apellidos, nombre"
command = "SELECT * FROM Alumnos"

cursor.execute(command)

for row in cursor.fetchall():    
    print(f"{row[0]}# {row[1]} {row[2]}")
    print(row)
    print("")