# Nota: El metodo actualmente no funciona por parte de la documentacion de OONI

import requests
import json

# Configura la URL base de la API de OONI
base_url = "https://api.ooni.io/api/_/"

# Obtener datos de im_stats
def get_im_stats():
    url = f"{base_url}im_stats"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

data = get_im_stats()

#escribe el contenido de la respuesta en un archivo
with open("im_stats.json", "w") as f:
    f.write(json.dumps(data, indent=4))