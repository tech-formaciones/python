#####################################################################
# Consultar timepo de llegada del autobus                           #
#####################################################################

import requests
import json

# Conjunto de URLs registradas en un diccionario
urls = {
    "base": "https://openapi.emtmadrid.es/v2/",
    "login": "mobilitylabs/user/login/",
    "listBicimad": "transport/bicimad/stations/"
}

# Variable para alamacenar el token
token = None

#####################################################
# Obtener token de acceso al API
#####################################################
try:
    # La variable endpoint contiene el resultado de concatenar los valores de dos claves del diccionario
    # https://openapi.emtmadrid.es/v2/mobilitylabs/user/login/
    endpoint = urls["base"] + urls["login"]

    # La variable headers es un diccionario que representan las cabeceras del mensaje de petición
    headers = {
        "X-ClientId": "25d3d248-fc0c-479d-8276-78ac52c647f2",
        "passKey": "141FE2B578702B63F6EE4E03049F95AB594A28BA9B67A7CAFF0D08BDB8B045463A14B6EADF5885D589B00DA11919CB9D12FFC012A317404D1EF97656E67A86B0"
    }

    # Realizamos una llamda GET al microservicio y almacenamos la respuesta en la variable response
    response = requests.get(endpoint, headers=headers)

    # Comprobamos que código de estado es 200 y recogemos del mensaje de respuesta el token, 
    # que almacenamos en la variable token
    if (response.status_code == 200):
        token = response.json()["data"][0]["accessToken"]
    else:
        print(f"Error ({response.status_code}): {response.reason}")
        quit()

    #####################################################
    # Obtener listado de los BiciMAD
    #####################################################

    # La variable endpoint contiene el resultado de concatenar los valores de dos claves del diccionario
    # https://openapi.emtmadrid.es/v2/transport/bicimad/stations/
    endpoint = urls["base"] + urls["listBicimad"]

    # La variable headers es un diccionario que representan las cabeceras del mensaje de petición
    # Enviamos el token obtenido en la anterior petición
    headers = {"accessToken": token}

    # Realizamos una llamda GET al microservicio y almacenamos la respuesta en la variable response
    response = requests.get(endpoint, headers=headers)

    # Comprobamos que código de estado es 200 y recogemos del mensaje de respuesta
    # Procesamos la respuesta mostrando el listado de BiciMAD Station y las bicis libres
    if (response.status_code == 200):
        datos = map(lambda x: (x["address"], x["dock_bikes"]), response.json()["data"])

        print("============================================================")
        print(" LISTADO DE BiciMAD")
        print("============================================================")
        for item in datos:
            print(f" |-> {item[1]:>4} bicis libres en {item[0]}")

        print("============================================================")
        print(f"     {sum(map(lambda x: x["dock_bikes"], response.json()["data"])):>4} bicis libres")
        print("============================================================")
    else:
        print(f"Error ({response.status_code}): {response.reason}")

except Exception as e:
    print(f"Error: {e}")
