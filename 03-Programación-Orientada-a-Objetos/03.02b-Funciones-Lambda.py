#####################################################################
# Declaración de Funciones Lamda                                    #
#####################################################################

from functools import reduce


numeros = [1, 85, 200, 15, 152, 450, 5, 3061, 63, 77, 8]

# Escribe una función que retorne una lista con los número mayores de 100
def MayorDeCien(lista):
    resultado = []

    for numero in lista:
        if (numero > 100):
            resultado.append(numero)

    return resultado


print(f"Número mayores de 100 - Función Estándar: {MayorDeCien(numeros)}")


# Escribe una función que return TRUE cuando un número es mayor de 100, si no retorna FALSE
def NumMayorCien(numero):
    if (numero > 100):
        return True
    else:
        return False
    
print(f"Número mayores de 100 - FILTER + Función Estándar: {list(filter(NumMayorCien, numeros))}")

# Extraer número mayores de 100 utilizando FILTER y LAMBDA
print(f"Número mayores de 100 - FILTER + Función Lambda: {list(filter(lambda x: x > 100, numeros))}")


print(f"Número menores de 50: {list(filter(lambda x: x < 50, numeros))}")
print(f"Número pares: {list(filter(lambda x: x % 2 == 0, numeros))}")

print(f"Datos: {numeros}")
resultado = list(map(lambda x: (x + 10) / 2, numeros))
print(f"Resultado de sumar 10 y dividir entre 2: {resultado}")

# Ejemplo de REDUCE con una suma
print(f"Resultado SUM: {sum(numeros)}")
print(f"Resultado: {reduce(lambda x, y: x + y, numeros,)}\n")

print(f"Datos: {numeros}")
print(f"Pares: {list((map(lambda x: x % 2 == 0, numeros)))}")

print(f"Algún número es par: {any((map(lambda x: x % 2 == 0, numeros)))}")
print(f"Algún número es par: {any(x % 2 == 0 for x in numeros)}")

print(f"Todos los números pares: {all((map(lambda x: x % 2 == 0, numeros)))}")
print(f"Algún número es par: {all(x % 2 == 0 for x in numeros)}")
