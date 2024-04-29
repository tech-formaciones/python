#####################################################################
# Sentencias de Control - While                                     #
#####################################################################
#                                                                   #
#   Sintaxis: while ([condición]):                                  #
#                                                                   #
#   Con while podemos ejecutar un conjunto de sentencias            #
#   siempre que la condición sea verdadera.                         #
#                                                                   #
#####################################################################


# Declaración de variables
valor = 0

# Uso de While
print(f"Inicio del WHILE")

while (valor < 5):
    valor += 1
    if (valor == 3):
        continue

    print(f"Valor actual {valor}")
else:
    print(f"No se inicia el WHILE")

print(f"Fin del WHILE \n")

#####################################################################

# Utilizamos el WHILE para recorrer colecciones
citricos = ["naranja", "limón", "pomelo", "líma", "mandarina"]
index = 0

while(index < len(citricos)):
    print(f"-> {index}# {citricos[index]}")
    index += 1      # equivalente a index = index + 1

#####################################################################

# Implementar la funcionalidad que otros lenguajes ofrecen mediante 
# el uso de DO/WHILE, consiguiendo que el bloque de sentencias se 
# ejecute al menos una vez

valor = 0

while(True):
    valor += 1
    print(f"Valor actual es  {valor}")

    if(valor > 4):
        break