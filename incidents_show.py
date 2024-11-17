import requests
import json

# Define la URL base del endpoint
base_url = "https://api.ooni.io/api/v1/incidents/show/"

# ID del incidente (obtenido previamente)
incident_id = "45013413801"  # Reemplaza con un ID real

# Construir la URL completa
url = base_url + incident_id

# Realizar la solicitud GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta en formato JSON
    incident_details = response.json()

    # Guardar los detalles en un archivo JSON
    with open(f"incident_{incident_id}.json", "w") as file:
        json.dump(incident_details, file, indent=4)

    # Imprimir los detalles del incidente
    print(f"Detalles del incidente {incident_id}:")
    print(json.dumps(incident_details, indent=4))
else:
    # Manejar errores
    print(f"Error en la solicitud: {response.status_code}")


#Definir el incident_id:
    #Este ID se obtiene usando /api/v1/incidents/search y se pasa como parte de la URL.
#Solicitud GET:
    #La solicitud se realiza usando el ID del incidente para recuperar detalles específicos.
#Guardar Datos:
    #Los datos obtenidos se guardan en un archivo JSON (incident_{incident_id}.json) para su análisis posterior.
#Visualización:
    #Se imprime la información detallada del incidente en la consola.

