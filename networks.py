import requests
import json

#Nota: El metodo trae las networks de los paises seleccionados

# Configura la URL base de la API de OONI
base_url = "https://api.ooni.io/api/_/"

# Obtener datos de networks
def get_networks(network_filter):
    result = None
    url = f"{base_url}networks"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        result = [
            org_name for org_name in data["results"]
            if any(country in org_name["org_name"] for country in network_filter)
        ]
    else:
        print("Error:", response.status_code, response.text)
    return result

#ejecuta la funcion get_networks
network_filter = ["Venezuela", "Uruguay", "Argentina", "Honduras", "El Salvador"]
data = get_networks(network_filter)

#escribe el contenido de la respuesta en un archivo
with open("result\\networks.json", "w", encoding='utf-8') as f:
    if data:
        f.write(json.dumps(data, indent=4, ensure_ascii=False))