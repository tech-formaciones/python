import pymssql

# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="hostdb2-eoi.database.windows.net",
    port="1433",
    user="Administrador",
    password="azurePa$$w0rd",
    database="Northwind"
)

cursor = connection.cursor(as_dict=True)

######################################################
# UPDATE, actulizar registros
######################################################


# Cierre de la conexión
connection.close()