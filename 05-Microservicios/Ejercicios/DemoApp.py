from flask import Flask, request, Response, jsonify, session
from DemoModulo import *

#########################################################################
# Creamos una instancia de Flask
#########################################################################
app = Flask(__name__, template_folder="templates")


#########################################################################
# Rutas de la aplicación Flask
#########################################################################

@app.route("/api/customers", methods=["GET"])
def get_customers():
    return "Hola Mundo !!!"


@app.route("/api/customers/<id>", methods=["GET"])
def get_customer(id):
    return "Hola Mundo !!!"


#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()
