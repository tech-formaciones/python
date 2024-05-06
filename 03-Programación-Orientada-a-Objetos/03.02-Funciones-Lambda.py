#####################################################################
# Declaración de Funciones Lamda                                    #
#####################################################################

def Saludo(nombre):
    print(f"Hola, me llamo {nombre}.")

miNombre = "Borja"
Saludo(miNombre)
Saludo(nombre=miNombre)

Saludo("Francisco")

print("")

# Una función Lambda equivalente a la función Saludu()
demo = lambda nombre : print(f"Hola, me llamo {nombre}.")

print(f"Tipo de demo: {type(demo)}")

miNombre = "Ana María"
demo(miNombre)

demo("Ana")

# Creamos una función Calcular() que recibe como parámetro una función Lambda
# con el calculo que tiene que realizar

def Sumar(num):
    return lambda a: a + num

def Restar(num):
    return lambda a: a - num

def Multiplicar(num):
    return lambda a: a * num

def Dividir(num):
    return lambda a: a / num

def Calcular(formula):
    for n in range(1, 11, 1):
        print (f"Valor: {n} - Resultado formula: {formula(n)}")

Calcular(Multiplicar(5))
print("")
Calcular(lambda a: a * 5)
print("")
Calcular(lambda x: ((x * 5) - 10) / x)
print("")
