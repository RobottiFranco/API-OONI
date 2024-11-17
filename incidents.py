import requests
import json

# Definir la URL del endpoint
url = "https://api.ooni.io/api/v1/incidents/search"

# Definir los parámetros de la consulta
params = {
    "only_mine": "false"
}

# Realizar la solicitud GET
response = requests.get(url, params=params)

if response.status_code == 200:
    try:
        # Convertir la respuesta en formato JSON
        incidents = response.json()
        print("Incidents:", incidents)  # Verificar estructura de datos

        # Si incidents tiene una clave específica, accede a ella
        if isinstance(incidents, dict) and "results" in incidents:
            incidents = incidents["results"]

        # Iterar y procesar cada incidente
        for incident in incidents:
            if isinstance(incident, dict):  # Asegúrate de que sea un diccionario
                print(f"ID: {incident['id']}, Descripción: {incident['description']}, Fecha: {incident['date']}")
            else:
                print("Formato inesperado:", incident)

    except ValueError:
        print("Error: La respuesta no es un JSON válido.")
        print(response.text)  # Imprime la respuesta cruda para depuración
else:
    print(f"Error en la solicitud: {response.status_code}")

#Definir Parámetros:
#El parámetro only_mine está configurado en false para incluir todos los incidentes #disponibles públicamente.
#Solicitud GET:
#Se realiza una solicitud GET al endpoint con los parámetros especificados.
#Guardado de Resultados:
#Los datos de la respuesta se guardan en un archivo JSON (incidents.json) para su análisis posterior.
#Resumen de Resultados:
#Itera sobre los incidentes y muestra un resumen con el ID, descripción y fecha.
