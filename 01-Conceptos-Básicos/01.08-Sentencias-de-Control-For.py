#####################################################################
# Sentencias de Control - For                                       #
#####################################################################


# Declaración de variables
citricos = ["naranja", "limón", "pomelo", "líma", "mandarina"]

# Utilizamos FOR para recorrer colecciones con IN
# No tenemos la posición de los elementos
print("===========================")

for fruta in citricos:
    print(f"-> {fruta}")

print("===========================")

# Utilizamos FOR para crear contadores con RANGE

# Contador de 0 a 10
for numero in range(11):
    print(f"-> {numero}")

print("===========================")

# Contador de 10 a 20 de 2 en 2
for numero in range(10, 21, 2):
    print(f"-> {numero}")

print("===========================")

# Contador de 20 a 5 de -3 en -3
for numero in range(20, 4, -3):
    print(f"-> {numero}")

print("===========================")

# La combinación de RANGE con LEN nos permite también recorrer colecciones
# Tenemos la posición de cada elemento en la colección

for index in range(len(citricos)):
    print(f"-> {index}# {citricos[index]}")

print("===========================")
