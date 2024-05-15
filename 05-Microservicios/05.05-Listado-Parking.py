#####################################################################
# Consultar plazas libre en los parkings                            #
#####################################################################

import requests
import json

# Conjunto de URLs registradas en un diccionario
urls = {
    "base": "https://openapi.emtmadrid.es/v2/",
    "login": "mobilitylabs/user/login/",
    "listParkings": "citymad/places/parkings/availability/"
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
    # Obtener listado de los Parkings
    #####################################################

    # La variable endpoint contiene el resultado de concatenar los valores de dos claves del diccionario
    # https://openapi.emtmadrid.es/v2/citymad/places/parkings/availability/
    endpoint = urls["base"] + urls["listParkings"]

    # La variable headers es un diccionario que representan las cabeceras del mensaje de petición
    # Enviamos el token obtenido en la anterior petición
    headers = {"accessToken": token}

    # Realizamos una llamda GET al microservicio y almacenamos la respuesta en la variable response
    response = requests.get(endpoint, headers=headers)

    # Comprobamos que código de estado es 200 y recogemos del mensaje de respuesta
    # Procesamos la respuesta mostrando el listado de BiciMAD Station y las bicis libres
    if (response.status_code == 200):
        datos = map(lambda x: (x["name"], x["freeParking"]), response.json()["data"])

        print("======================================================================")
        print(" LISTADO DE Parkings")
        print("======================================================================")
        for item in datos:
            if (item[1] == None):
                print(f" |-> {item[0]:<35} -       sin información")
            else:                
                print(f" |-> {item[0]:<35} - {item[1]:>5} plazas libres")

        print("======================================================================")
        print(f"{"     TOTAL DE PLAZAS LIBRES":<40}   {sum(map(lambda x: x["freeParking"], filter(lambda x: x["freeParking"] != None, response.json()["data"]))):>5} ")
        print("======================================================================")
    else:
        print(f"Error ({response.status_code}): {response.reason}")

except Exception as e:
    print(f"Error: {e}")
