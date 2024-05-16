import pymssql

# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="hostdb2-eoi.database.windows.net",
    port="1433",
    user="Administrador",
    password="azurePa$$w0rd",
    database="Northwind"
)

# Creamos un cursor para ejecutar comando en la base de datos
# Creamos un cursor que retorna Tuplas
cursor = connection.cursor()

# Creamos un cursor que retorna Diccionarios
cursor = connection.cursor(as_dict=True)

######################################################
# SELECT, leer registros de la base de datos
######################################################

# Ejemplos del comando SELECT, para leer registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")

# Mostar el contenido del cursor utilizando un WHILE
row = cursor.fetchone()
while (row):
    print(f"      ID: {row["CustomerID"]}")
    print(f" Empresa: {row["CompanyName"]
                       } - {row["City"]} ({row["Country"]})\n")
    row = cursor.fetchone()

# El siguiente ejemplo comentado muestra como tratar los registros cuando se
# entregan como Tuplas en lugar de Diccionarios
"""
row = cursor.fetchone()
while (row):
    print(f"      ID: {row[0]}")
    print(f" Empresa: {row[1]} - {row[5]} ({row[8]})\n")
    row = cursor.fetchone()
"""

cursor.execute("SELECT * FROM dbo.Customers")
for row in cursor.fetchall():
    print(f">      ID: {row["CustomerID"]}")
    print(f"> Empresa: {row["CompanyName"]
                        } - {row["City"]} ({row["Country"]})\n")

# El siguiente ejemplo comentado muestra como tratar los registros cuando se
# entregan como Tuplas en lugar de Diccionarios
"""
for row in cursor.fetchall():
    print(f">      ID: {row[0]}")
    print(f"> Empresa: {row[1]} - {row[5]} ({row[8]})\n") 
"""

# Ejemplos del comando SELECT, para leer registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", "USA")

pais = input("Nombre del pais: ")
cursor.execute(f"SELECT * FROM dbo.Customers WHERE Country = '{pais}'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", pais)

cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' AND City = 'San Francisco'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany'")

cursor.execute("SELECT CustomerID, CompanyName, City, Country FROM dbo.Customers WHERE Country = 'USA'")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country ASC")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country DESC")
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA' OR Country = 'Germany' ORDER BY Country, City")

for row in cursor.fetchall():
    print(f"     ID: {row["CustomerID"]}")
    print(f"Empresa: {row["CompanyName"]} - {row["City"]} ({row["Country"]})")


######################################################
# SELECT, ejemplos de JOIN
######################################################

# Ejemplo que comienza con una consulta y realiza 830 subconsultas dentro del for
# NO ES UN JOIN, son subconsultas que deben evitarse por rendimiento
cursor.execute("SELECT * FROM dbo.Orders")

for row in cursor.fetchall():
    print(f" -> {row["OrderID"]}# - {row["CustomerID"]} {row["OrderDate"]}")

    cursor2 = connection.cursor(as_dict=True)
    cursor2.execute("SELECT * FROM dbo.Employees WHERE EmployeeID = %d", row["EmployeeID"])
    cursor2.execute(f"SELECT * FROM dbo.Employees WHERE EmployeeID = '{row["EmployeeID"]}'")
    employee = cursor2.fetchone()

    print(f"    Pedido gestionado por el empleado {row["EmployeeID"]}: {employee["FirstName"]} {employee["LastName"]}")


# Ejemplo que ser realiza con una consulta
# query y query2 contienen el mismo JOIN con distinta sintaxis
query = """
    "SELECT o.OrderID, o.CustomerID, o.OrderDate, o.EmployeeID, e.FirstName, e.LastName 
    FROM dbo.Orders AS o, dbo.Employees AS e 
    WHERE o.EmployeeID = e.EmployeeID"
"""
query2 = """
    SELECT o.OrderID, o.CustomerID, o.OrderDate, o.EmployeeID, e.FirstName, e.LastName
    FROM dbo.Orders AS o
    JOIN dbo.Employees AS e
    ON o.EmployeeID = e.EmployeeID
"""
cursor.execute(query)

for row in cursor.fetchall():
    print(f" -> {row["OrderID"]}# - {row["CustomerID"]} {row["OrderDate"]}")
    print(f"    Pedido gestionado por el empleado {
          row["EmployeeID"]}: {row["FirstName"]} {row["LastName"]}")


######################################################
# SELECT, las agrupaciones
######################################################

# Listado de clientes de USA y el número de pedidos de cada cliente
# NO ES UNA AGRUPACIÓN, es una subconsulta dentro del for que debemos evitar por rendimiento
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")
for row in cursor.fetchall():
    cursor2 = connection.cursor()
    cursor2.execute(f"SELECT COUNT(*) FROM dbo.Orders WHERE CustomerID = '{row["CustomerID"]}'")
    print(f"{row["CustomerID"]}# {row["CompanyName"]} -> {cursor2.fetchone()[0]} pedidos")

"""
    Opcionalmente podemos trabajar con cursores que retornan diccionarios, pero estamos 
    obligados a definir alias para el dato calculado usando AS

    cursor2 = connection.cursor(as_dict=True)
    cursor2.execute(f"SELECT COUNT(*) AS NumPedidos FROM dbo.Orders WHERE CustomerID = '{row["CustomerID"]}'")
    print(f"{row["CustomerID"]}# {row["CompanyName"]} -> {cursor2.fetchone()["NumPedidos"]} pedidos")
"""

# Listado de clientes de USA y el número de pedidos de cada cliente
# Solo los cliente con más de 10 pedidos
query = """
    SELECT c.CustomerID, c.CompanyName, COUNT(o.OrderID) AS NumPedidos
    FROM dbo.Customers c
    JOIN dbo.Orders o
    ON c.CustomerID = o.CustomerID
    WHERE c.Country = 'USA'
    GROUP BY c.CustomerID, c.CompanyName
    HAVING COUNT(o.OrderID) > 10
"""
cursor.execute(query)
for row in cursor.fetchall():
    print(f"{row["CustomerID"]}# {row["CompanyName"]} -> {row["NumPedidos"]} pedidos")


######################################################
# INSERT, insertar nuevo registros
######################################################

# Definición de un objeto que representa el registro CUSTOMER 
class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Region = None
    PostalCode = None
    Country = None
    Phone = None
    Fax = None

# Instaciamos el objeto CUSTOMER
cliente = Customer()
cliente.CustomerID = "DEMO1"
cliente.CompanyName = "Empresa Uno, SL"
cliente.ContactName = "Borja"
cliente.ContactTitle = "Gerente"
cliente.Address = "Calle Uno, S/N"
cliente.City = "Madrid"
cliente.Region = "Madrid"
cliente.PostalCode = "28016"
cliente.Country = "España"
cliente.Phone = "900100100"
cliente.Fax = "900100200"

# cliente2 es un diccionario que también representa el registro CUSTOMER
cliente2 = {"CustomerID": "DEMO2",
            "CompanyName": "Empresa Dos, SL",
            "ContactName": "Borja Cabeza",
            "ContactTitle": "Gerente",
            "Address": "Calle Dos S/N",
            "City": "Madrid",
            "Region": "Madrid",
            "PostalCode": "28019",
            "Country": "España",
            "Phone": "910 101 102",
            "Fax": "910 101 103"}

# INSERT comando de inserción
command = """
    INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactTitle, City, Country)
    VALUES('BCR01', 'Company SL', 'Borja Cabeza', 'Madrid', 'España')
"""

# Insertamos nuevos registros ejecutado el comando INSERT
#cursor.execute(command)

# Utilizamos la función commit() de la conexión para CONFIRMAR la transación
# tanto para operaciones de inserción, actualización y borrado
connection.commit()

# Utilizamos la función rollback() de la conexión para ANULAR la transación
# tanto para operaciones de inserción, actualización y borrado
connection.rollback()

# Ejemplo de un comando INSERT que indica las columnas o campos y sus valores
command = """
    INSERT INTO dbo.Customers(
        CustomerID, 
        CompanyName, 
        ContactTitle, 
        City, 
        Country) VALUES('BCR01', 'Company SL', 'Borja Cabeza', 'Madrid', 'España')
"""
# Ejemplo de un comando INSERT que indica las columnas o campos y comodines para los valores
command2 = """
    INSERT INTO dbo.Customers(
        CustomerID, 
        CompanyName, 
        ContactName,
        ContactTitle, 
        City, 
        Country) VALUES(%s, %s, %s, %s, %s, %s)
"""

# Al ejecutar el comando con comides, pasamos como segundo parámetros los valores en una lista
cursor.execute(command2, ["BCR02", "Company Demo, SL", "Borja", "CEO", "Valencia", "España"])

# El mismo ejemplo donde pasamos los valores en una tupla
cursor.execute(command2, ("BCR03", "Company Demo, SL", "Borja", "CEO", "Valencia", "España"))
connection.commit()

# Para insertar varios registros al mismo tiempo creamos una lista que contiene en cada posición
# una tupla con los valores de cada registro que vamos a insertar
data = []
data.append(("BCR10", "Company Demo 10, SL", "Borja", "CEO", "Sevilla", "España"))
data.append(("BCR11", "Company Demo 11, SL", "Carlos", "CEO", "Bilbao", "España"))
data.append(("BCR12", "Company Demo 12, SL", "Julian", "CEO", "Málaga", "España"))    

# Utilizamos las función .executemany() para insertar varios registro y pasamos como segundo
# parámetro la lista de tuplas con los valores de los diferentes registros
cursor.executemany(command2, data)
connection.commit()

# La propieda o variable .rowcount nos devuelve el número de registros insertados, actualizados o borrados
print(f"{cursor.rowcount} registros insertados.")

# Ejemplo de un INSERT donde se especifican valores para todos los campos o columnas del registro
command = """
    INSERT INTO dbo.Customers VALUES(
        'DEMO2',
        'Empresa Dos, SL',
        'Borja Cabeza',
        'Gerente',
        'Calle Dos S/N',
        'Madrid',
        'Madrid',
        '28019',
        'España',
        '910 101 102',
        '910 101 103')
"""

# Ejemplo de un INSERT donde se especifican comodines para los valores para todos los 
# campos o columnas del registro
command = """
    INSERT INTO dbo.Customers VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""


######################################################
# UPDATE, actulizar registros
######################################################

# Utilizamos UPDATE para actualizar registros en la base de datos
command = """
    UPDATE dbo.Customers
    SET Address = 'Calle Uno, S/N', ContactName = 'Carlos Sánchez'
    WHERE CustomerID = 'BCR11'
"""

# Ejecutamos el comando de actulización
cursor.execute(command)

# Confirmamos la transación y por tanto la operación de actulización
connection.commit()

# Mostramos los registros actualizados
print(f"{cursor.rowcount} registros actualizados.")

# Utilizamos UPDATE para actualizar registros en la base de datos
# El comando contiene comodine o parámetros para sustituir por valores en el momento de la ejecución
command = """
    UPDATE dbo.Customers
    SET Address = %s, ContactName = %s
    WHERE CustomerID = 'BCR12'
"""

# Ejecutamos el comando de actulización y pasamos los valores para los comodines o parámetros
cursor.execute(command, ("Calle Principal, 10", "María José Sanz"))

# Confirmamos la transación y por tanto la operación de actulización
connection.commit()

# Mostramos los registros actualizados
print(f"{cursor.rowcount} registros actualizados.")

# Utilizamos UPDATE para actualizar registros en la base de datos
# El comando contiene comodine o parámetros para sustituir por valores en el momento de la ejecución
command = """
    UPDATE dbo.Customers
    SET Address = %s, ContactName = %s
    WHERE CustomerID = %s
"""

# Ejecutamos el comando de actulización y pasamos los valores para los comodines o parámetros
cursor.execute(command, ("Calle Principal, 10", "María Sanz", "BCR12"))

# Confirmamos la transación y por tanto la operación de actulización
connection.commit()

# Mostramos los registros actualizados
print(f"{cursor.rowcount} registros actualizados.")


######################################################
# DELETE, eliminar registros
######################################################

# Utilizamos DELETE para eliminar registros en la base de datos
command = """
    DELETE FROM dbo.Customers
    WHERE CustomerID = 'BCR10'
"""

# Ejecutamos el comando y confirmamos la transación mediante connection.commit()
# Si se produce un error retrocedemos la transación mediante connection.rollback() y la operación de borrado se anual
# Siempre mostramos el número de registros eliminados
try:
    cursor.execute(command)
    connection.commit()
except Exception as e:
    connection.rollback()
    print(f"Error: {e}")
finally:
    print(f"{cursor.rowcount} registros eliminados.")
    connection.close()

# Utilizamos DELETE para eliminar registros en la base de datos, el comando contiene parámetros
command = """
    DELETE FROM dbo.Customers
    WHERE CustomerID = %s
"""

# Ejecutamos el comando y suminstramos valores para los parámetros
try:
    cursor.execute(command, ("BCR11"))
    connection.commit()
except Exception as e:
    connection.rollback()
    print(f"Error: {e}")
finally:
    print(f"{cursor.rowcount} registros eliminados.")
    connection.close()
