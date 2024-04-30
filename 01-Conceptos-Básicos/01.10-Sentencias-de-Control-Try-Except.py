#####################################################################
# Sentencias de Control - Try/Except/Else/Finally                   #
#####################################################################
#                                                                   #
#   try     permite controlar las excepciones producidas en un      #
#           bloque de código.                                       #
#                                                                   #
#   except  bloque de instrucciones que se ejecutan cuando se       #
#           produce una excepción.                                  #
#                                                                   #
#   else    bloque de instrucciones que se ejecutan al finalizar    #
#           el try si no se produce un excepción.                   #
#                                                                   #
#   finally bloque de instrucciones que se ejecutan siempre que     #
#           finaliza el try, except o else.                         #
#                                                                   #
#####################################################################

import sys

# Ejemplo 1
numero1 = 0
numero2 = 100

print(f"Inicio del programa.\n")
try:
    numero3 = numero2 / numero1
    print(f"Valor de número 3: {numero3}")
except ZeroDivisionError:
    print(f"Error, no se puede dividir entre cero.")
except:
    print(f"Upsss Error !!!")
else:
    print(f"El bloque ELSE se ejecuta cuando el TRY finaliza correctamente.")
finally:
    print(f"El bloque FINALLY se ejecuyta cuando el TRY o EXCEPT finalizan")

print(f"\nFin del programa.")
print("==============================================")


# Ejemplo 2
numero1 = 5
numero2 = 100

try:    
    numero3 = numero2 / numero1
    print(f"Valor de número 3: {numero3}")

    f = open("miFichero.txt")
except ZeroDivisionError as err:
    print(f"-> {err}")
    print(f"-> {type(err)}")
except FileNotFoundError as err:
    print(f"-> {err}")
    print(f"-> {type(err)}")
except Exception as err:
    print(f"{err}")
    print(f"{type(err)}")
finally:
    print(f"F I N")

print("==============================================")

# Ejemplo 3
numero = "32"

try:
    if(type(numero) is not int):
        raise Exception("La variable NUMERO no es numérica.")
except Exception as e:
    print(f"-> {e}")
    print(f"-> {type(e)}")

print("==============================================")

# Ejemplo 4
try:
    print("Nivel 1")

    print("Inicio Nivel 2")

    try:
        print("Nivel 2")
        print(100/0)
    except Exception as err:
        raise
        print(f"Nivel 2: {err}")
    finally:
        print("Fin Nivel 2")
except Exception as err:
    print(f"Nivel 1: {err}")

print("==============================================")