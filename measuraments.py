import requests
import json

# URL base del endpoint
base_url = "https://api.ooni.io/api/v1/measurement/"

# Definir el measurement_uid (obtenido previamente)
measurement_uid = "20230101T123456Z_12345_UY"  # Reemplaza con un ID real

# Construir la URL completa
url = base_url + measurement_uid

# Realizar la solicitud GET
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta en formato JSON
    measurement_data = response.json()

    # Guardar los detalles en un archivo JSON
    with open(f"measurement_{measurement_uid}.json", "w") as file:
        json.dump(measurement_data, file, indent=4)

    # Imprimir un resumen básico de la medición
    print(f"Detalles de la medición {measurement_uid}:")
    print(json.dumps(measurement_data, indent=4))
else:
    # Manejar errores
    print(f"Error en la solicitud: {response.status_code}")

#Definición del measurement_uid:
    #Este ID se obtiene de otros endpoints como /api/v1/measurements.
#Construcción de la URL:
    #El measurement_uid se concatena a la URL base para formar la URL completa de la solicitud.
#Solicitud GET:
    #Se realiza la consulta al endpoint con el ID especificado.
#Guardado de Resultados:
    #Los datos de la medición se guardan en un archivo JSON (measurement_{measurement_uid}.json) para su análisis.
#Visualización de Resultados:
    #Imprime la información detallada de la medición en la consola.