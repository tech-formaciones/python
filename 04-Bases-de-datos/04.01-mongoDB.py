#####################################################################
# Trabajando con mongoDB                                            #
#####################################################################

from pymongo import MongoClient, collection
from bson.objectid import ObjectId
from pprint import pprint
import sys, json

######################################################
# CONECTAR CON UN SERVIDOR mongoDB
######################################################

#clientDB = MongoClient("127.0.0.1", "27017")
#clientDB = MongoClient("localhost", "27017")
#clientDB = MongoClient("mongodb://USER:PASSWORD@<IP>:<PORT>/")
#clientDB = MongoClient("mongodb://127.0.0.1:27017/")


######################################################
# EJECUTAR COMANDO - Mostrar el estado del servidor
######################################################

# Creamos un objeto que almacenamos en la variable clientDB
# El objeto representa el cliente para trabajar con las bases de datos de mongoDB
# Se requiere una cadena de conexión
clientDB = MongoClient("mongodb://localhost:27017/")

# Nos posicionamos sobre una base de datos, en el ejemplo sobre la base de datos ADMIN
db = clientDB.admin

# Ejecutamos un comando utilizando la función COMMAND
# El comando serverStatus nos retorna el estado del servidor en formato JSON
result = db.command("serverStatus")

# Mostramos el resultado de la ejecución del comando
print(result)


######################################################
# TRABAJAR CON BASES DE DATOS Y SUS COLECCIONES
######################################################

# Mostrar el nombre de las bases de datos
print(clientDB.list_database_names())

# El listado de bases de datos es una LISTA de python que podemos recorrer con un FOR
for db in clientDB.list_database_names():
    print(f"Nombre: {db}")
    print(f" -> {clientDB[db].list_collection_names()}\n")

# Seleccionar una base de datos con la que vamos a trabajar
db = clientDB.northwind             # Sintaxis de Objeto
db2 = clientDB["northwind"]         # Sintaxis de Colección

# Motrar las colecciones que tiene una base de datos
# Las colecciones son equivalente a las tablas en las bases de datos relacionales
print(db.list_collection_names())
print(db2.list_collection_names())
print("")

# Seleccionar una colección con la que vamos a trabajar
collection = clientDB.northwind.customers
collection = clientDB["northwind"]["customers"]
collection = db.customers
collection = db["customers"]

# Mostramos el número de documentos en la colección
# Los documentos son equivalentes a los registros en bases de datos relacionales
print(f"{collection.estimated_document_count()} documentos en {collection.name}")


######################################################
# TRABAJAR CON LOS DOCUMENTOS DE LAS COLECCIONES
######################################################

