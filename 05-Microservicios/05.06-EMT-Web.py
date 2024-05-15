from flask import Flask, render_template, render_template_string

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


#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()
