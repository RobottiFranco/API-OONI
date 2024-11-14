import requests
import json

# Configura la URL base de la API de OONI
base_url = "https://api.ooni.io/api/_/"

# Obtener datos de domains
def get_test_name():
    result = None
    url = f"{base_url}test_names"
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
    else:
        print("Error:", response.status_code, response.text)
    return result

#ejecuta la funcion get_test_name
data = get_test_name()

#escribe el contenido de la respuesta en un archivo
with open("result\\test_name.json", "w") as f:
    if data:
        f.write(json.dumps(data, indent=4))