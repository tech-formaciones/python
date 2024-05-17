from flask import Flask, request, Response, jsonify, session
from DemoModulo import *

#########################################################################
# Creamos una instancia de Flask
#########################################################################
app = Flask(__name__, template_folder="templates")


#########################################################################
# Rutas de la aplicación Flask
#########################################################################

# Retorna listado de clientes
# GET http://dominio.com/api/customers
@app.route("/api/customers", methods=["GET"])
def get_customers():
    return jsonify(Get_Customers_List()), 200

# Retorna datos de un cliente
# GET http://dominio.com/api/customers/ANATR
@app.route("/api/customers/<id>", methods=["GET"])
def get_customer(id):
    return jsonify(Get_Customer(id)), 200

# Retorna listado de los pedidos de un cliente
# GET http://dominio.com/api/customers/ANATR/orders
@app.route("/api/customers/<id>/orders", methods=["GET"])
def get_orders_customer(id):
    return jsonify(Get_Orders_by_Customer(id)), 200

# Retorna listado de pedidos
# GET http://dominio.com/api/orders
@app.route("/api/orders", methods=["GET"])
def get_orders():
    return jsonify(Get_Orders_List()), 200

# Retorna datos de un pedido
# GET http://dominio.com/api/orders/10250
@app.route("/api/orders/<id>", methods=["GET"])
def get_order(id):
    return jsonify(Get_Order(id)), 200


#########################################################################
# Control de errores aplicación Flask
#########################################################################

# Código para manejar la solicitud no encontrada
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({f"Error {e.code} ({e.name})": f"{e.description}"}), 404

# Código para manejar el error interno de código
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({f"Error {e.code} ({e.name})": f"{e.description}"}), 500

# Código para manejar errores genericos
@app.errorhandler(Exception)
def handle_error(e):
    return jsonify({f"Error": f"{e}"}), 500


#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()
