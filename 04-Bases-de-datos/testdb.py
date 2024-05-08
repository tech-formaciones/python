from pymongo import MongoClient, collection
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

clientDB = MongoClient("mongodb://localhost:27017/")
db = clientDB.northwind             
collection = db.customers

# Mostrar el documento por identificador del objeto
# Filtro: _id = identificador
result = collection.find_one({"_id": ObjectId("663a105807258656ed9eae3a")})
pprint(result)
print("")

# Mostrar el primer el documento que coincide con el filtro
# Filtro: Country = USA
result = collection.find_one({"Country": "USA"})
print(type(result))
pprint(result)
print("")

# Mostrar el todos los documentos que coincide con el filtro
# Filtro: Country = USA
# Retornar un cursor
cursor = collection.find({"Country": "USA"})
print(type(cursor))

# Mostrar el número de documentos de una búsqueda
# print(f"Resultado de la búsqueda {cursor.count()} documentos.")    # No disponible desde la versión 
print(f"Resultado de la búsqueda {collection.count_documents({"Country": "USA"})} documentos.")

# Cuando ALIVE retorna TRUE significa que tenemos documentos pendientes de leer en el cursor
print(f"Documentos pendientes de leer: {cursor.alive}")
print("")

# Utilizamos WHILE para mostrar los documentos del cursor
# El bloque del WHILE se ejecuta mientras ALIVE retorne TRUE (documentos pendientes de leer)
# Con la función .NEXT() para posicionarnos en el siguiente documentos del cursor
while(cursor.alive == True):
    document = cursor.next()
    pprint(document)
    print("")

# Cuando ALIVE retorna FALSE significa que no tenemos documentos pedientes de leer en el cursor
print(f"Documentos pendientes de leer: {cursor.alive}")
print("")