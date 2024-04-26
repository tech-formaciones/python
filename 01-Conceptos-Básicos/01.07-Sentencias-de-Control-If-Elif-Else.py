#####################################################################
# Sentencias de Control - If / Elif / Else                          #
#####################################################################


# Declaración de variables
a = 33
b = 200

# Ejemplo 1, IF/ELIF/ELSE
print(f"Inicio del programa ==========")

if (b > a):
    print(f"B es mayor que A")
    print(f"El valor de B es igual a {b}")
elif (a > b):
    print(f"A es mayor que B")
    print(f"El valor de A es igual a {a}")  
else:
    print(f"A es igual que B")

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
