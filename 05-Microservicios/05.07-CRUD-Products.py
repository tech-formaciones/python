from flask import Flask, render_template, request, jsonify
import pymssql

#########################################################################
# Creamos una instancia de Flask
#########################################################################
app = Flask(__name__, template_folder="templates")


#########################################################################
# Rutas de la aplicación Flask
#########################################################################

# Retorna una lista de productos
# Ruta: http://dominio.com/api/products
@app.route("/api/products", methods=["GET"])
def products_get():
    try:
        connection = pymssql.connect(
            server="hostdb2-eoi.database.windows.net",
            port="1433",
            user="Administrador",
            password="azurePa$$w0rd",
            database="Northwind")

        cursor = connection.cursor(as_dict=True)
        cursor.execute("SELECT * FROM dbo.Products")

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

            return jsonify(cursor.fetchone()), 200
        else:
            return jsonify({"Message": "La referencia del producto no es valida."}), 400
    except Exception as err:
        return jsonify(err), 500


#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()
