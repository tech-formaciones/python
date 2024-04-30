#####################################################################
# Declaración de Funciones                                          #
#####################################################################
#                                                                   #
#   Sintaxis: def [nombre de la funcion](arg, args-1):              #
#                                                                   #
#   Ejemplos:                                                       #
#       def Saludar() -> None:                                      #
#       def Suma(a, b) -> int:                                      #
#                                                                   #
#####################################################################

from datetime import datetime

# Ejemplo de una función que NO recibe datos (NO tiene parámetros) y NO retorna datos
def Func1():
    """Func1, no tiene parámtros y no retorna datos"""

    print(f"Hola Mundo !!!")

# Ejemplo de una función que SI recibe datos (SI tiene parámetros) y NO retorna datos
def Func2(nombre, numero):
    """Func2, tiene dos parámtros y no retorna datos"""

    print(f"Me llamo {nombre} y mi número de la suerte es {numero}")

# Ejemplo de una función que SI recibe datos (SI tiene parámetros) y SI retorna datos
def Func3(frase):
    cantidad = len(frase)
    return cantidad

# Ejemplo de una función que SI recibe datos (NO tiene parámetros) y SI retorna datos
def Func4():
    return datetime.now().date().strftime("%A")

# Ejecutar las funciones
Func2("Borja", 8)
Func1()
Func3("En un lugar de la mancha de cuyo nombre ....")
print(f"{Func4()}")


#####################################################################
# Asignación de valores a los parámetros                            #
#####################################################################

def Resta(a, b):                                   # todos los parámtros son obligatorios
    return a - b

print(f"1) 85 - 10 = {Resta(85, 10)}")             # por posición
print(f"1) 85 - 10 = {Resta(a=85, b=10)}")         # por nombre
print(f"1) 85 - 10 = {Resta(b=10, a=85)}\n")       # por nombre


def Resta1(a, b=10):                               # solo el parámtro A es obligatorio
    return a - b

print(f"2) 85 - 10 = {Resta1(85, 10)}")            # por posición
print(f"2) 85 - 10 = {Resta1(a=85, b=10)}")        # por nombre
print(f"2) 85 - 10 = {Resta1(b=10, a=85)}")        # por nombre
print(f"2) 85 - 10 = {Resta1(85)}")                # por posición, valor para A
print(f"2) 85 - 10 = {Resta1(a=85)}\n")            # por nombre, valor para A


def Resta2(a=85, b=10):                            # todos los parámtros son opcionales
    return a - b


print(f"3) 85 - 10 = {Resta2()}")                  # sin valores para los parámetros
print(f"3) 85 - 10 = {Resta2(85, 10)}")            # por posición
print(f"3) 85 - 10 = {Resta2(a=85, b=10)}")        # por nombre
print(f"3) 85 - 10 = {Resta2(b=10, a=85)}")        # por nombre
print(f"3) 85 - 10 = {Resta2(85)}")                # por posición, valor para A
print(f"3) 85 - 10 = {Resta2(a=85)}")              # por nombre, valor para A
print(f"3) 85 - 10 = {Resta2(b=10)}\n")            # por nombre, valor para B
