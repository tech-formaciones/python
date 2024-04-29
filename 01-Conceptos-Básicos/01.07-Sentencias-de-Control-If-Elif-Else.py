#####################################################################
# Sentencias de Control - If / Elif / Else                          #
#####################################################################
#                                                                   #
#   Las sentencias de decisión determinar el flujo del programa     #
#   tras evaluar una expresión de comparación.                      #
#                                                                   #
#                                                                   #
#   Sintaxis:          Es igual: a == b                             #
#                   No es igual: a != b                             #
#                     Menor que: a <  b                             #
#                 Menor o igual: a <= b                             #
#                     Mayor que: a >  b                             #
#                 Mayor o igual: a >= b                             #
#                                                                   #
#####################################################################


# Declaración de variables
a = 33
b = 200

# Ejemplo 1, IF/ELIF/ELSE
print(f"Inicio del programa ==========")
print("")

if (b > a):
    print(f"B es mayor que A")
    print(f"El valor de B es igual a {b}")
elif (a > b):
    print(f"A es mayor que B")
    print(f"El valor de A es igual a {a}")  
else:
    print(f"A es igual que B")

print("")
print("Continua el programa después del IF")

print(f"Fin del programa =============")


# Ejemplo 2, IF/ELIF
print(f"Inicio del programa ==========")

if (b > a):
    print(f"B es mayor que A")
    print(f"El valor de B es igual a {b}")
elif (a > b):
    print(f"A es mayor que B")
    print(f"El valor de A es igual a {a}")
elif (a == b):
    print(f"A es igual que B")

print(f"Fin del programa =============")


# Ejemplo 3, IF/ELSE/IF/ELSE
print(f"Inicio del programa ==========")

if (b > a):
    print(f"B es mayor que A")
    print(f"El valor de B es igual a {b}")
else:
    if (a > b):
        print(f"A es mayor que B")
        print(f"El valor de A es igual a {a}")
    else:
        print(f"A es igual que B")

print(f"Fin del programa =============")