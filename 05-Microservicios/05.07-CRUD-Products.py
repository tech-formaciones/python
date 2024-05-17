from flask import Flask, render_template, request, Response, jsonify, session
from XMLModulo import *
import pymssql

#########################################################################
# Creamos una instancia de Flask
#########################################################################
app = Flask(__name__, template_folder="templates")
app.secret_key = b"5s2%_5d3'$$ds92xDS5s"


#########################################################################
# Rutas de la aplicación Flask
#########################################################################

# Retorna una lista de productos
# Ruta: http://dominio.com/api/products
@app.route("/api/products", methods=["GET"])
def products_get():
    try:
        categoria = request.args.get("categoria", None)

        connection = pymssql.connect(
            server="hostdb2-eoi.database.windows.net",
            port="1433",
            user="Administrador",
            password="azurePa$$w0rd",
            database="Northwind")

        cursor = connection.cursor(as_dict=True)
        
        if (categoria != None):
            cursor.execute(f"SELECT * FROM dbo.Products WHERE CategoryID = {categoria}")
        else:
            cursor.execute("SELECT * FROM dbo.Products")

        if (session["response_type"] == "xml"):
            xml = "<products>"
            for item in cursor.fetchall():
                xml = xml + dict_to_xml(item, "product")

            xml = xml + "</products>"
            response = Response(xml, status=200, content_type="application/xml")

            return response
        else:
            return jsonify(cursor.fetchall()), 200
    except Exception as err:
        return jsonify(err), 500

# Retorna los datos del producto 34
# Ruta: http://dominio.com/api/products/34
# @app.route("/api/products/<int:id>", methods=["GET"])
@app.route("/api/products/<id>", methods=["GET"])
def product_get(id):
    try:
        if (id.isdigit()):
            connection = pymssql.connect(
                server="hostdb2-eoi.database.windows.net",
                port="1433",
                user="Administrador",
                password="azurePa$$w0rd",
                database="Northwind")

            cursor = connection.cursor(as_dict=True)
            cursor.execute(f"SELECT * FROM dbo.Products WHERE ProductID = {id}")

            if (session["response_type"] == "xml"):
                xml = dict_to_xml(cursor.fetchone(), "product")
                response = Response(xml, status=200, content_type="application/xml")

                return response
            else:
                return jsonify(cursor.fetchone()), 200
        else:
            return jsonify({"Message": "La referencia del producto no es valida."}), 400
    except Exception as err:
        return jsonify(err), 500

# Crear un nuevo producto
# Ruta: http://dominio.com/api/products
@app.route("/api/products", methods=["POST"])
def products_post():
    try:
        new_product = request.json
        
        connection = pymssql.connect(
            server="hostdb2-eoi.database.windows.net",
            port="1433",
            user="Administrador",
            password="azurePa$$w0rd",
            database="Northwind")

        cursor = connection.cursor(as_dict=True)

        # command = f"""
        #     DECLARE @NewID INT;

        #     INSERT INTO dbo.Products(ProductName, CategoryID, Discontinued, SupplierID,
        #         ReorderLevel, QuantityPerUnit, UnitsInStock, UnitsOnOrder, UnitPrice) VALUES (
        #         '{new_product["ProductName"]}',
        #         {new_product["CategoryID"]},
        #         '{new_product["Discontinued"]}',
        #         {new_product["SupplierID"]},
        #         {new_product["ReorderLevel"]},
        #         '{new_product["QuantityPerUnit"]}',
        #         {new_product["UnitsInStock"]},
        #         {new_product["UnitsOnOrder"]},
        #         {new_product["UnitPrice"]});
            
        #     SET @NewID = SCOPE_IDENTITY();

        #     SELECT * FROM dbo.Products WHERE ProductID = @NewID
        # """

        # cursor.execute(command)
        # connection.commit()

        # return jsonify(cursor.fetchone()), 201
    
        command = f"""
            INSERT INTO dbo.Products(ProductName, CategoryID, Discontinued, SupplierID,
                ReorderLevel, QuantityPerUnit, UnitsInStock, UnitsOnOrder, UnitPrice) VALUES (
                '{new_product["ProductName"]}',
                {new_product["CategoryID"]},
                '{new_product["Discontinued"]}',
                {new_product["SupplierID"]},
                {new_product["ReorderLevel"]},
                '{new_product["QuantityPerUnit"]}',
                {new_product["UnitsInStock"]},
                {new_product["UnitsOnOrder"]},
                {new_product["UnitPrice"]});
        """

        cursor.execute(command)
        connection.commit()    

        if(cursor.rowcount == 1):
            id = cursor.lastrowid
            cursor.execute(f"SELECT * FROM dbo.Products WHERE ProductID = {id}")

            return jsonify(cursor.fetchone()), 201
        else:
            return jsonify({"Message": "Producto no insertado."}), 400
    except Exception as err:
        return jsonify(err), 500
    
# Actualizar un producto
# Ruta: http://dominio.com/api/products/77
@app.route("/api/products/<int:id>", methods=["PUT"])
def products_put(id):
    try:
        product = request.json

        if(product["ProductID"] != id):
            return jsonify({"Message": "Identificador del producto no valido."}), 400

        connection = pymssql.connect(
            server="hostdb2-eoi.database.windows.net",
            port="1433",
            user="Administrador",
            password="azurePa$$w0rd",
            database="Northwind")

        cursor = connection.cursor(as_dict=True)

        command = f"""
            UPDATE dbo.Products SET 
                ProductName = '{product["ProductName"]}',
                CategoryID = {product["CategoryID"]},
                Discontinued = '{product["Discontinued"]}',
                SupplierID = {product["SupplierID"]},
                ReorderLevel = {product["ReorderLevel"]},
                QuantityPerUnit = '{product["QuantityPerUnit"]}',
                UnitsInStock = {product["UnitsInStock"]},
                UnitsOnOrder = {product["UnitsOnOrder"]},
                UnitPrice = {product["UnitPrice"]} WHERE ProductID = {product["ProductID"]}
        """

        cursor.execute(command)
        connection.commit()

        if (cursor.rowcount == 1):
            return jsonify(""), 204
        else:
            return jsonify({"Message": "Producto no actualizado."}), 400
    except Exception as err:
        return jsonify(err), 500

# Eliminar el producto 34
# Ruta: http://dominio.com/api/products/34
# @app.route("/api/products/<int:id>", methods=["DELETE"])
@app.route("/api/products/<int:id>", methods=["DELETE"])
def products_delete(id):
    try:
        connection = pymssql.connect(
            server="hostdb2-eoi.database.windows.net",
            port="1433",
            user="Administrador",
            password="azurePa$$w0rd",
            database="Northwind")

        cursor = connection.cursor(as_dict=True)
        
        cursor.execute(f"DELETE FROM dbo.Products WHERE ProductID = {id}")
        connection.commit()

        if (cursor.rowcount == 1):
            return jsonify(""), 200
        else:
            return jsonify({"Message": "El producto no existe o no eliminado."}), 400
    except Exception as err:
        return jsonify(err), 500


#########################################################################
# Funciones que se ejecutan en todas las peticiones
#########################################################################

@app.before_request
def verificar_apikey():
    apikey = request.headers.get("Authorization", None)
    if (apikey != "8aaWPy5SzLubp9ApRQbZkWkHA6PFZ33n"):
        return jsonify({"Message" : "Acceso no autorizado"}), 401

@app.before_request
def get_type_response():
    session["response_type"] = request.args.get("rt", "json").lower()


#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()
