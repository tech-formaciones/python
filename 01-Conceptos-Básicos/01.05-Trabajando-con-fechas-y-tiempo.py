#####################################################################
# Trabajando con fechas                                             #
#####################################################################
#                                                                   #
#   Sintaxis: datetime.now()                                        #
#             datetime.now().date()                                 #
#             datetime.now().today()                                #
#                                                                   #
#             datetime.strptime("11-03-1998", "%d-%m-%Y").date()    #
#             print(datetime.now().strftime("%A, %d %m, %Y")        #
#                                                                   #
#####################################################################


# Importamos módulos
from datetime import datetime
import time
import locale

# Configuración reginal
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')


# Declaración de variables
# Almacenamos en la variable dt1 la fecha y hora actual del sistema
dt1 = datetime.now().date()     # creamos una variable de tipo date
dt1 = datetime.now()            # creamos una variable de tipo datetime

# Mostramos la fecha almacenada en la varibale dt1
print(f"Fecha 1: {dt1}")

# Mostramos parte de la fecha almacenada en la variable dt1
print(f"Día: {dt1.day}")
print(f"Día: {str(dt1.day).zfill(2)}")
print(f"Mes: {dt1.month}")
print(f"Mes: {str(dt1.month).zfill(2)}")
print(f"Año: {dt1.year}")
print(f"Hora: {dt1.hour}")
print(f"Minutos: {dt1.minute}")
print(f"Segundos: {dt1.second}")
print(f"Milisegundos: {dt1.microsecond}")


# Convertir un texto en una fecha utilizando la función STRPTIME
fecha = input("Escribe tu fecha de nacimiento (dd-mm-yyyy): ")

dt2 = datetime.strptime(fecha, "%d-%m-%Y").date()   # retorna un date
dt2 = datetime.strptime(fecha, "%d-%m-%Y")          # retorna un datetime

# Mostramos la fecha sin formatear
print(f"Fecha 2: {dt2}")

# Mostramos la fecha formateada utilizando la función SRTFTIME
print(f"Hoy es {dt2.strftime("%A, %d de %B de %Y")}")
print("")


# Calculo entre fechas
# Buscamos calcular la edad de una persona

#Opción 1, restamos los años (el resultado puede ser erroneo)
print(f"Tienes {dt1.year - dt2.year} años\n")

# Restamos dos fechas y la diferencia crea una variable de tipo TIMEDELTA
dtr = dt1 - dt2

# Mostar información del una variable TIMEDELTA
print("")
print(dtr)
print(dtr.days)
print(dtr.seconds)
print(dtr.microseconds)
print(dtr.total_seconds())

# Opción 2, mediante la división de los días entre 365
print(f"Tienes {dtr.days / 365 } años")         # División CON parte decimal
print(f"Tienes {dtr.days // 365 } años")        # División SIN parte decimal

# Opción 3, mediante la división con la función DIVMOD
edad = divmod(dtr.days, 365)                    # Retorna el resulto y el resto
print(edad)                   
print(f"Tienes {edad[0]} años y {edad[1]} días")

# Opción 4, obtenemos la misma información que utilizando la función DIVMOD
print(f"Tienes {dtr.days // 365} años y {dtr.days % 365} días")


# TIME retorna la cantidad de segundos transcurridos desde el comienzo
# que se fija en el 01-Enero-1970 00:00:00
t1 = time.time()
print(f"Segundo desde 01-Ene-1970: {t1} \n")

# Tranformación de segundos en una fecha
t2 = time.localtime(t1)
print(f"Tupla: {t2}")
print(f"Año: {t2.tm_year} \n")

# Conversión de T2 en una representación de fecha y hora local
print(f"Fecha: {time.asctime(t2)} \n")