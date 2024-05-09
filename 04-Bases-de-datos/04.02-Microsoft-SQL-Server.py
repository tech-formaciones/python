import pymssql

# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="sqlserver-eoi.database.windows.net",
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
