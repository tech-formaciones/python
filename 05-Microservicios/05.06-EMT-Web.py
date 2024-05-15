from flask import Flask, render_template, request
from EMTModulo import *

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

# Ruta: http://dominio.com/listado
@app.route("/listado", methods=["POST"])
def listado():
    # parada = request.args.get("parada")             # Procesar formularios GET
    parada = request.form.get("parada")             # Procesar formularios POST    
    infoData = GetArrivalBus(parada)

    return render_template("listado.html", info=infoData)


#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()
