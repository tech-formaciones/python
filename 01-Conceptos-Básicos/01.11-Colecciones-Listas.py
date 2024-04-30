#####################################################################
# Colecciones - LISTAS                                              #
#####################################################################

# Declaración de variables
# Utilizamos [] para la declaración de variables que son listas
vacia = []
frutas = ["naranja", "limón", "pomelo", "líma", "mandarina"]

# Mostrar el contenido de una lista
print(f"Contenido de frutas: {frutas}")

# Mostrar el valor del elemento en la posición (2 = pomelo)
print(f"Posición 2: {frutas[2]}")

# Mostrar el número de elementos que contiene la lista
print(f"Número de elementos: {len(frutas)}")

# Mostrar el número de veces que tenemos un valor en la lista
# Sensible a mayúsculas y minúsculas
print(f"Naranja se repite {frutas.count("naranja")} vez/veces")

# Modificar el valor una posición (posición 2, pomelo por fresa)
frutas[2] = "fresa"
print(f"Posición 2: {frutas[2]}")

# Añadir nuevos valores a la lista utilizando APPEND
frutas.append("manzana")
frutas.append("melón")
print(f"Contenido de frutas: {frutas}")

# Añadir un nuevo valor en una posición utilizando INSERT(index, value)
# Añadir sandia en la posición 1
frutas.insert(1, "sandia")
print(f"Contenido de frutas: {frutas}")

# Añadir varios elementos utilizando EXTEND(list)
nuevasFrutas = ["maracuya", "kiwi", "frambuesa"]
frutas.extend(nuevasFrutas)
print(f"Contenido de frutas: {frutas}")
# Equivalente a frutas += nuevasFrutas

frutas.extend(["platano", "pera"])
print(f"Contenido de frutas: {frutas}")
# Equivalente a frutas += ["platano", "pera"]

# Añadir un elemento si no existe
print(f"Melocotón existe en FRUTAS: {("melocotón" in frutas)}")
print(f"Melocotón no existe en FRUTAS: {("melocotón" not in frutas)}")

if ("melocotón" not in frutas):
    frutas.append("melocotón")

print(f"Contenido de frutas: {frutas}")

# Eliminar un elemento indicando su posición (posición 5, mandarina)
frutas.pop(5)
print(f"Contenido de frutas: {frutas}")

# Eliminar un elemento indicando el valor
# En el caso de varios elementos con el mismo valor elimina únicamente la primera coincidencía
frutas.remove("naranja")
print(f"Contenido de frutas: {frutas}")

# Para evitar errores podemos preguntar por la existencia de un valor antes de eliminar
if ("uva" in frutas):
    frutas.remove("uva")

# Invertir el orden de los valores utilizando REVERSE
frutas.reverse()
print(f"Contenido de frutas: {frutas}")

# Ordernar los elementos de la lista por orden alfabético
frutas.sort()
print(f"Contenido de frutas: {frutas}")

frutas.sort(reverse=True)
print(f"Contenido de frutas: {frutas}")

# Recorremos las lista mostrando sus valores
for fruta in frutas:
    print(f"{fruta}")
print("")

for index in range(len(frutas)):
    print(f"{index}# {frutas[index]}")
print("")

for index, value in enumerate(frutas):
    print(f"{index}# {value}")
print("")

# Copiar una lista
vacia = frutas.copy()
print(f"Contenido de vacia: {vacia}")

# Eliminar todos los elementos de una lista
frutas.clear()
print(f"Contenido de frutas: {frutas}")