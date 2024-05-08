from pymongo import MongoClient, collection
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

clientDB = MongoClient("mongodb://localhost:27017/")
db = clientDB.northwind             
collection = db.customers

"""
===================================================
 Listado de operadores relacionales
===================================================
$eq     - equal - igual
$lt     - low than - menor que
$lte    - low than equal - menor o igual que
$gt     - greater than - mayor que
$gte    - greater than equal - mayor o igual que
$ne     - not equal - distinto
$in     - in - dentro de
$nin    - not in - no dentro de
$regex  - cumple con la expresión regular
"""

cursor = collection.find({"Country": "USA"})
cursor = collection.find({"Country": "USA"}).limit(3)
cursor = collection.find({"Country": "USA"}).skip(5)
cursor = collection.find({"Country": "USA"}).skip(5).limit(5)
cursor = collection.find({"Country": "USA"}).sort("City")               # Ordenados de A a W
cursor = collection.find({"Country": "USA"}).sort({"City": 1})          # Ordenados de A a W
cursor = collection.find({"Country": "USA"}).sort({"City": -1})         # Ordenados de W a A

# Buscar clientes de USA, ejemplos con y sin operador
cursor = collection.find({"Country": "USA"})                            # Sin operador
cursor = collection.find({"Country": {"$eq": "USA"}})                   # Con operador

# Buscar clientes fuera de USA
cursor = collection.find({"Country": {"$ne": "USA"}})

# Buscar clientes de USA y Mexico, ordenados por país y ciudad
cursor = collection.find({"Country": {"$in": ["USA", "Mexico"]}}).sort([("Country", 1), ("City", 1)])

# Buscar clientes que contenienen DE en la clave CustomerID
cursor = collection.find({"CustomerID": {"$regex": "DE"}})

# Buscar clientes que el CustomerID comienza por A y finaliza con 4 carácteres más
cursor = collection.find({"CustomerID": {"$regex": "A[A-Z]{4}"}})

while (cursor.alive == True):
    document = cursor.next()
    print(f"{document["CustomerID"]}# {document["CompanyName"]} - {document["City"]} ({document["Country"]})")
