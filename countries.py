import requests
import json

# Configura la URL base de la API de OONI
base_url = "https://api.ooni.io/api/_/"

# Obtener datos de domains
def get_countries(countries_filter):
    result = None
    url = f"{base_url}countries"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        result = [country for country in data["countries"] if country["name"] in countries_filter]
    else:
        print("Error:", response.status_code, response.text)
    return result

#ejecuta la funcion get_countries
countries_filter = ["Venezuela", "Uruguay", "Argentina", "Honduras", "El Salvador"]
data = get_countries(countries_filter)

#escribe el contenido de la respuesta en un archivo
with open("countries.json", "w") as f:
    if data:
        f.write(json.dumps(data, indent=4))