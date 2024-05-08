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
cursor = collection.find({"CustomerID": {"$regex": "1[A-Z]{4}"}})

# Buscar clientes de la ciudad de San Francisco en USA
# El operador AND NO se especifica, pero se aplica de forma implicita o por defecto
cursor = collection.find({"Country": "USA", "City": "San Francisco"})

# Buscar clientes de la ciudad de San Francisco en USA utilizando el operador AND
# El operador AND SI se especifica y se aplica de forma explicita
cursor = collection.find({"$and": [{"Country": "USA"}, {"City": "San Francisco"}]})

# Buscar clientes de GERMANY o USA utilizar el operador OR
# El operador OR se especifica y se aplica de forma explicita
cursor = collection.find({"$or": [{"Country": "Germany"}, {"Country": "USA"}]})

# Buscar los clientes de Mexico y sus pedidos
cursor = collection.find({"Country": "Mexico"})

while (cursor.alive == True):
    document = cursor.next()
    print(f"{document["CustomerID"]}# {document["CompanyName"]} - {document["City"]} ({document["Country"]})")

    pedidos = clientDB.northwind.orders.find({"CustomerID": document["CustomerID"]})
    while(pedidos.alive):
        pedido = pedidos.next()
        print(f">>> {pedido["OrderID"]}# - {pedido["OrderDate"]}")

    print("")

# Buscar los clientes de Mexico y sus pedidos utilizando agregación AGGREGATE
cursor = db.customers.aggregate([
    {"$match": {"Country": "Mexico"}},
    {"$sort": {"City": 1}},
    {"$lookup": {
        "from": "orders",
        "localField": "CustomerID",
        "foreignField": "CustomerID",
        "as": "Pedidos"
    }}
])

while (cursor.alive == True):
    document = cursor.next()
    print(f"{document["CustomerID"]}# {document["CompanyName"]} - {document["City"]} ({document["Country"]})")
    
    for pedido in document["Pedidos"]:
        print(f" >> {pedido["OrderID"]}# - {pedido["OrderDate"]}")
    
    print("")
