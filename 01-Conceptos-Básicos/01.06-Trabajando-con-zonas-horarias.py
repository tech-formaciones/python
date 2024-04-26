#####################################################################
# Trabajando con fechas - Zonas horarias                            #
#####################################################################

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
