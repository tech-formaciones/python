from flask import Flask, render_template, request
from pymongo import MongoClient, collection

#########################################################################
# Creamos una instancia de Flask
#########################################################################
app = Flask(__name__, template_folder="templates")


#########################################################################
# Rutas de la aplicación Flask
#########################################################################

# Ruta: http://dominio.com/
@app.route("/")
def index():
    return render_template("index.html")

# Ruta: http://dominio.com/ficha
@app.route("/ficha", methods=["GET"])
def ficha():
    idCliente = request.args.get("id")

    clientDB = MongoClient("mongodb://localhost:27017/")
    db = clientDB.northwind
    collection = db.customers
    result = collection.find_one({"CustomerID": idCliente})

    return render_template("ficha.html", data=result)


#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()
