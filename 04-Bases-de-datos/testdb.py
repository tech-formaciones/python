import pymssql

# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="sqlserver-eoi.database.windows.net",
    port="1433",
    user="Administrador",
    password="azurePa$$w0rd",
    database="Northwind"
)

cursor = connection.cursor(as_dict=True)

######################################################
# SELECT, leer registros de la base de datos
######################################################

# Ejemplos del comando SELECT, para leer registros de la base de datos
cursor.execute("SELECT * FROM dbo.Customers")

for row in cursor.fetchall():
    print(f">      ID: {row["CustomerID"]}")
    print(f"> Empresa: {row["CompanyName"]} - {row["City"]} ({row["Country"]})\n")