from pymongo import MongoClient, collection
from bson.json_util import dumps, loads

"""
El resultado de una consulta que retorna ObjectId puede dar problemas al Serializar
para transfor a JSON:

    json.dumps(_Get_Collection("customers").find_one({"CustomerID": id}))                   <- Genera un error

Como alternativa podemos indicar que mongoDB no devuelva el ObjectId con la siguiente
instrucción de búsqueda:

    json.dumps(_Get_Collection("customers").find_one({"CustomerID": id}, {"_id": 0}))       <- Correcto

y también podemos serializar utilizando la utilidad de mongoDB:

    from bson.json_util import dumps, loads                                                 <- Correcto
    dumps(_Get_Collection("customers").find_one({"CustomerID": id}))                        

"""

server = "localhost"
port = 27017
db = "northwind"

# Retorna listado de todos los clientes
def Get_Customers_List() -> list:
    try:
        return list(_Get_Collection("customers").find({}, {"_id": 0}))
    except Exception as e:
        return {"Error": e}

# Retorna datos de un cliente
def Get_Customer(id) -> dict:
    try:
        return _Get_Collection("customers").find_one({"CustomerID": id}, {"_id": 0})
    except Exception as e:
        return {"Error": e}

# Retorna listado de pedido de un cliente
def Get_Orders_by_Customer(id) -> list:
    try:
        return list(_Get_Collection("orders").find({"CustomerID": id}, {"_id": 0}))
    except Exception as e:
        return {"Error": e}
    
# Retorna listado de todos los pedidos
def Get_Orders_List() -> list:
    try:
        return list(_Get_Collection("orders").find({}, {"_id": 0}))
    except Exception as e:
        return {"Error": e}

# Retorna datos de un pedido
def Get_Order(id) -> dict:
    try:
        return _Get_Collection("orders").find_one({"OrderID": id}, {"_id": 0})
    except Exception as e:
        return {"Error": e}

# Retorna un collection de mongoDB
def _Get_Collection(collection, server=server, port=port, db=db):
    return MongoClient(f"mongodb://{server}:{port}/")[db][collection]