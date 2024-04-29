#####################################################################
# Trabajando con fechas - Zonas horarias                            #
#####################################################################


# Importamos módulos
# Importar 
from datetime import datetime
import pytz

# Mostar las zonas horarias disponibles
print(pytz.all_timezones)
print("")

# Mostar información sobre la fecha actual, SIN zona horaria
dt = datetime.now()
print(f"Fecha: {dt}")
print(f"Zona horaria: {dt.tzinfo}")
print("")

# Mostar información sobre la fecha actual, CON zona horaria
dtTokio = datetime.now(pytz.timezone("Asia/Tokyo"))
print(f"Fecha en Tokio: {dtTokio}")
print(f"Zona horaria: {dtTokio.tzinfo}")
print("")

# Mostrar otras zonas horarias
print("Fecha Ushuaia:", datetime.now(
    pytz.timezone("America/Argentina/Ushuaia")))
print("Fecha Madrid:", datetime.now(pytz.timezone("Europe/Madrid")))
print("Fecha Alaska:", datetime.now(pytz.timezone("US/Alaska")))
print("Fecha UTC:", datetime.now(pytz.timezone("UTC")))