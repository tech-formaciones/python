#####################################################################
# Colecciones - DICCIONARIOS                                        #
#####################################################################

# Declaración de variables
# Utilizamos {} para la declaración de variables que son diccionarios
vacio = {}
frutas = {"NA":"naranja", "LI":"limón", "PO":"pomelo", "LM":"líma", "MA":"mandarina"}

# Mostrar el contenido de un diccionario
print(f"Contenido de frutas: {frutas}")

# Mostrar el valor de un elemento con la clave (PO = pomelo)
print(f"Clave PO: {frutas["PO"]}")

# Mostrar el valor de un elemento con la función GET
print(f"Clave PO: {frutas.get("PO")}")
print(f"Clave ML: {frutas.get("ML")}")

# Mostrar el número de elementos que contiene el diccionario
print(f"Número de elementos: {len(frutas)}")

# Mostrar las claves del diccionario
print(f"Claves: {frutas.keys()}")

# Modificar valores del diccionario
frutas["NA"] = "sandia"
print(f"Contenido de frutas: {frutas}")

frutas.update({"NA":"ciruela"})
print(f"Contenido de frutas: {frutas}")

# Añadir nuevo valores al diccionario
frutas["ML"] = "melón"
print(f"Contenido de frutas: {frutas}")

frutas.update({"MZ": "manzana"})
print(f"Contenido de frutas: {frutas}")

# Eliminar valores del diccionario
frutas.pop("NA")
del frutas["MZ"]
print(f"Contenido de frutas: {frutas}")

# Recorremos el diccionario mostrando los diferentes valores
for key in frutas:
    print(f"{key}# {frutas[key]}")
print("")

# Copiar un diccionario
vacio = frutas.copy()
print(f"Contenido de vacio: {vacio}")

# Eliminar todos los elementos del diccionario
frutas.clear()
print(f"Contenido de frutas: {frutas}")