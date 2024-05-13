import pymssql

# Establecer la conexión con la base de datos
connection = pymssql.connect(
    server="hostdb-eoi.database.windows.net",
    port="1433",
    user="Administrador",
    password="azurePa$$w0rd",
    database="Northwind"
)

cursor = connection.cursor(as_dict=True)

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
    VALUES('BCR03', 'Company SL', 'Borja Cabeza')
"""

cursor.execute(command)

#connection.commit()

#connection.rollback()


connection.close()