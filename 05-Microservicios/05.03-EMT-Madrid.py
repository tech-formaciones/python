#####################################################################
# Consultar timepo de llegada del autobus                           #
#####################################################################

import requests, json

urls = {
    "base": "https://openapi.emtmadrid.es/v2/",
    "login": "mobilitylabs/user/login/",
    "timeArrivalBus": "transport/busemtmad/stops/<stopId>/arrives/"
}

token = ""

parada = input("Número de la parada: ")


# Obtener token de acceso al API
try:
    endpoint = urls["base"] + urls["login"]

    headers = {
        "X-ClientId": "25d3d248-fc0c-479d-8276-78ac52c647f2",
        "passKey": "8623B97B9ACBB5BE028D1B5B5872200FE5399BDA7476CD6423DEA3A94783FB43B8E57A3F79D98E18AC41997F8434EF2F5D1EFB6240B381EA5DB1F1C798BB969E"
    }

    response = requests.get(endpoint, headers=headers)
    if(response.status_code == 200):
        token = response.json()["data"][0]["accessToken"]
    else:
        print(f"Error ({response.status_code}): {response.reason}")
        quit()

    endpoint2 = urls["base"] + urls["timeArrivalBus"].replace("<stopId>", parada)
    headers2 = {"accessToken": token}
    data2 = {
        "cultureInfo": "ES",
        "Text_StopRequired_YN": "Y",
        "Text_EstimationsRequired_YN": "Y",
        "Text_IncidencesRequired_YN": "N",
        "DateTime_Referenced_Incidencies_YYYYMMDD": "20240514"
    }

    response2 = requests.post(endpoint2, headers=headers2, json=data2)
    # response2 = requests.post(endpoint2, headers=headers2, data=json.dumps(data2))

    if (response2.status_code == 200):
        print(response2.text)
    else:
        print(f"Error ({response2.status_code}): {response2.reason}")

except Exception as e:
    print(f"Error: {e}")

