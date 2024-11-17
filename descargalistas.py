
# script que usa la API para descargar y guardar las listas relevantes (test_names y domains).

import requests
import json

# URLs de los endpoints
BASE_URL = "https://api.ooni.io/api/v1/"
endpoints = {
    "test_names": "test_names",
    "domains": "domains"
}

# Función para descargar listas
def download_list(endpoint, filename):
    url = BASE_URL + endpoint
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Guardar los datos en un archivo JSON
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Lista guardada en {filename}")
    else:
        print(f"Error al obtener datos de {endpoint}: {response.status_code}")

# Descargar listas
for key, endpoint in endpoints.items():
    download_list(endpoint, f"{key}.json")