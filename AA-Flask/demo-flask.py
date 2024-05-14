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
    return f'<h1 style="color: blue;">Hola Mundo !!!</h1>'

# Ruta: http://dominio.com/saludo/<nombre>
@app.route("/saludo/<nombre>")
def saludo(nombre):
    return f'<h1 style="color: blue;">Hola {nombre} !!!</h1>'

# Ruta: http://dominio.com/template/<nombre>
@app.route("/template/<nombre>")
def template(nombre):
    return render_template("demotemplate.html", nombreenlaplantilla=nombre)


#########################################################################
# Ejecutar la aplicación de Flask en el servidor web integrado
#########################################################################
app.run()