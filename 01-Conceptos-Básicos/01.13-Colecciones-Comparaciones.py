#####################################################################
# Comparaciones entre las diferentes colecciones                    #
#####################################################################


# Declaración o creación de las colecciones
#####################################################################

lista = ["naranja", "limón", "pomelo", "líma", "mandarina"]
dicc = {0:"naranja", 1:"limón", 2:"pomelo", 3:"líma", 4:"mandarina"}
tupla = ("naranja", "limón", "pomelo", "líma", "mandarina")
conjunto = {"naranja", "limón", "pomelo", "líma", "mandarina"}


#####################################################################
# Las sentencias comentadas no estan permitidas                     #
#####################################################################

# Modificar a un elemento de la colección
#####################################################################

lista[2] = "fresa"
dicc[2] = "fresa"
#tupla[2] = "fresa"
#conjunto[2] = "fresa"


# Acceder a un elemento de la colección
#####################################################################

print(lista[2])
print(dicc[2])
print(tupla[2])
#print(conjunto[2])


# Añadir un elemento de la colección
#####################################################################

lista.append("manzana")
dicc[5] = "manzana"
#tupla.append("manzana")
conjunto.add("manzana")


# Eliminar un elemento de la colección
#####################################################################

lista.remove("líma")
dicc.pop(3)
# tupla.remove("líma")
conjunto.discard("líma")


# Recorrer la colección
#####################################################################

for item in lista:
    print(item)
print("")

for key in dicc:
    print(dicc[key])
print("")

for item in tupla:
    print(item)
print("")

for item in conjunto:
    print(item)
print("")

print(list(enumerate(lista)))
print(dicc)