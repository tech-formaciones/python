# Importar los módulos necesarios
import requests, pprint

postalcode = input("Indica un código postal: ")
endpoint = f"https://api.zippopotam.us/es/{postalcode}"

try:
    response = requests.get(endpoint)
    
    if (response.status_code == 200):
        data = response.json()

        print(f"{data["post code"]} {data["country"]}")
        for resultado in data["places"]:
            print(f" |-> {resultado["place name"]} ({resultado["state"]})")
    else:
        print(f"Error ({response.status_code}): {response.reason}")
    
except Exception as err:
    print(f"{err}")
