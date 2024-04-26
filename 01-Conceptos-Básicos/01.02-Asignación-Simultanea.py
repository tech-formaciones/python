######################################################################
# Asignación Simultanea                                              #
######################################################################
#                                                                    #
#   Sintaxis: [var1], [var2] = [var2], [var1]                        #
#                                                                    #
#   Ejemplos:                                                        #
#       a = 10                                                       #
#       b = 5                                                        #
#       a,b = b,a                                                    #
#                                                                    #
######################################################################

# Declaración de variables
a = 5
b = 10

# Intercambiar los valores entre a y b. Intento 1.
a = b
b = a

print("Intento 1, incorrecto.")
print(f"Variable A: {a}")
print(f"Variable B: {b}")
print("")


# Intercambiar los valores entre a y b. Intento 2.
a = 5
b = 10

temp = a
a = b
b = temp

print("Intento 2, correcto con una variable temporal.")
print(f"Variable A: {a}")
print(f"Variable B: {b}")
print("")


# Intercambiar los valores entre a y b. Intento 3.
a = 5
b = 10

a,b = b,a

print("Intento 3, correcto y es la forma preferida en Python")
print(f"Variable A: {a}")
print(f"Variable B: {b}")
print("")