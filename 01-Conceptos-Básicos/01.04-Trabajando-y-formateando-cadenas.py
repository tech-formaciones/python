#####################################################################
# Trabajando y formateando cadenas de texto                         #
#####################################################################


# Declaración de variables
#        01234567890123456789    <--- Posiciones
texto = "   hola mundo !!!   "
print(texto)


# Mostar determinados caractéres de la cadena
# indicando su posición o un rango
print(f"Posición 3: {texto[3]}")
print(f"Desde la posición 3 incluida: {texto[3:]}")
print(f"Hasta la posición 6 NO incluida: {texto[:6]}")
print(f"Desla la posición 2 a la 6 NO incluida: {texto[2:6]}")
print(f"Los 4 primeros caractéres empezando por derecha: {texto[-5]} \n")


# Funciones que podemos utilizar con cadenas de texto
print(f"Número de caractéres: {len(texto)}")
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.strip().capitalize())
print(texto.title())
print(texto.strip())
print(texto.count("o"))
print(f"Es un digito: {texto.isdigit()}")
print(f"Es un digito: {"57".isdigit()} \n")


# Formateando texto 
mensaje = "Mundo"

print("Hola " + mensaje + " !!!")

print("Hola {} !!!".format(mensaje))
print("Hola {s} !!!".format(s=mensaje))

print(f"Hola {mensaje} !!!")


# Formatenado números
resultado = 10 / 3

print("Resultado: " + str(resultado))
print("Resultado:", str(resultado))
print("Resultado:", resultado)

print("Resultado: {r}".format(r=resultado))
print("Resultado: {r:1.2f}".format(r=resultado))

print(f"Resultado: {resultado}")
print(f"Resultado: {resultado:1.2f}")