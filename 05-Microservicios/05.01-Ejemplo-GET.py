#####################################################################
# Trabajando Request                                                #
#####################################################################

# Importar los módulos necesarios
import requests, pprint

# En el ejemplo consultamos una base de datos de direcciones IP
# La dirección IP es suministrada por el usuario
ip = input("Dirección IP pública: ")

# El usuario determina el formato de la respuesta
responseType = input("Formato de respuesta JSON o XML: ")

# Endpoint del microservicio APIRest
endpoint = f"http://ip-api.com/{responseType.lower()}/{ip}"

try:
    # Utilizamos la función get() para llamar al microservicio
    # La función get() retorna el mensaje de respuesta
    response = requests.get(endpoint)

    # La variable response contiene el mensaje de respuesta
    # Mostramos el código de estado
    # Mostramos el código de estado en modo texto utilizando REASON
    print(f"Estado: {response.status_code} / {response.reason}")

    if(response.status_code == 200):
        # Mostramos las cabeceras del mensaje de respuesta
        print(f"Cabeceras: {response.headers}\n")
        print(f"Content-Type: {response.headers["Content-Type"]}")
        print("Content-Type, indica el formato de la información enviada en el BODY.\n")
        print(f"Content-Length: {response.headers["Content-Length"]} bytes")
        print("Content-Length, indica el tamaño en bytes de la información enviada en el BODY.\n")

        # Mostramos el contenido del cuerpo del mensaje de respuesta
        print(f"  Contenido en bytes: {response.content}\n")
        print(f"Contenido como texto: {response.text}\n")

        if ("application/json" in response.headers["Content-Type"].lower()):
            data = response.json()  # La función JSON retorna un objeto de tipo diccionario

            print(f"   Ubicación: {data["regionName"]} ({data["country"]})")
            print(f"     Latitud: {data["lat"]}")
            print(f"    Longitud: {data["lon"]}")
            print(f"Organización: {data["isp"]} - {data["org"]}")
        else:
            print("La respuesta no es JSON.\n")
    else:
        print(f"{response.reason}")


except requests.ConnectionError as err:     # Indica errores de DNS
    print(f"{err}")
except requests.Timeout as err:             # Timeout superado
    print(f"{err}")
except requests.TooManyRedirects as err:    # Demasiados redirecionamientos
    print(f"{err}")
except requests.HTTPError as err:           # Errores que retornan códigos HTTP 4xx o 5xx
    print(f"{err}")
except requests.RequestException as err:    # Genérico de requests
    print(f"{err}")
except Exception as err:                    # Genérico de python
    print(f"{err}")
