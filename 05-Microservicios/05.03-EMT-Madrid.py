#####################################################################
# Consultar timepo de llegada del autobus                           #
#####################################################################

import requests, json

# Función para procesar las información
def InfoBus(item):
    data = {}
    data["linea"] = item["line"]
    data["distancia"] = item["DistanceBus"]

    if (item["estimateArrive"] < 60):
        data["tiempo"] = "está en la parada."
    else:
        time = item["estimateArrive"] / 60
        if(time >= 20):
            data["tiempo"] = "llegará en 20 min o más."
        else:
            data["tiempo"] = f"llegará aproximadamente en {time:1.0f} min."

    data["mensaje"] = f"el {data["linea"]} {data["tiempo"]} ({data["distancia"]} m.)"
    
    return data

# Colección de URLs utilizadas
urls = {
    "base": "https://openapi.emtmadrid.es/v2/",
    "login": "mobilitylabs/user/login/",
    "timeArrivalBus": "transport/busemtmad/stops/<stopId>/arrives/"
}

# Variable para alamacenar el token
token = None

# Preguntamos al usuario que parada quiere consultar y lo almacenamos en la variable parada
parada = input("Número de la parada: ")

#####################################################
# Obtener token de acceso al API
#####################################################
try:
    # La variable endpoint contiene el resultado de concatenar los valores de dos claves del diccionario
    # https://openapi.emtmadrid.es/v2/mobilitylabs/user/login/
    endpoint = urls["base"] + urls["login"]

    # Cabecera para el login en la API
    headers = {
        "X-ClientId": "25d3d248-fc0c-479d-8276-78ac52c647f2",
        "passKey": "141FE2B578702B63F6EE4E03049F95AB594A28BA9B67A7CAFF0D08BDB8B045463A14B6EADF5885D589B00DA11919CB9D12FFC012A317404D1EF97656E67A86B0"
    }

    # Llamda al API, login para obtener el token de acceso
    response = requests.get(endpoint, headers=headers)

    # Comprobamos que código de estado es 200 y recogemos del mensaje de respuesta el token,
    # que almacenamos en la variable token
    if(response.status_code == 200):
        token = response.json()["data"][0]["accessToken"]
    else:
        print(f"Error ({response.status_code}): {response.reason}")
        quit()


    # Si tenemos token realizamos una segunda llamda al API para obtener la información
    # de los autobuses proximos a la parada de autobus

    #####################################################
    # Obtener listado autobuses
    #####################################################

    # La variable endpoint contiene el resultado de concatenar los valores de dos claves del diccionario
    # https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/<stopId>/arrives/
    # Remplazamos el texto <stopId> por el número de la parada almacenado en la variable parada
    endpoint = urls["base"] + urls["timeArrivalBus"].replace("<stopId>", parada)

    # Datos del HEADER, incluye el token de acceso obtenido anteriormente
    headers = {"accessToken": token}

    # Datos del BODY
    data = {
        "cultureInfo": "ES",
        "Text_StopRequired_YN": "Y",
        "Text_EstimationsRequired_YN": "Y",
        "Text_IncidencesRequired_YN": "N",
        "DateTime_Referenced_Incidencies_YYYYMMDD": "20240514"
    }

    # Llamada al API, para obtener información sobre los autobuses
    # Dos opciones posible para pasar los datos del BODY del mensaje

    response = requests.post(endpoint, headers=headers, json=data)
    # response = requests.post(endpoint, headers=headers, data=json.dumps(data))

    # Comprobamos que código de estado es 200 y recogemos del mensaje de respuesta
    # Procesamos la respuesta mostrando el listado de autobuses por llegar a la parada indicada
    if (response.status_code == 200):
        # Opción A
        datos = map(InfoBus, response.json()["data"][0]["Arrive"])
        for item in datos: 
            print(item["mensaje"])

        # Opción B
        # for item in response.json()["data"][0]["Arrive"]:
        #     print(InfoBus(item)["mensaje"])
    else:
        print(f"Error ({response.status_code}): {response.reason}")

except Exception as e:
    print(f"Error: {e}")