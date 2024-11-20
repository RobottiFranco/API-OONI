# ejemplo de cómo programar el uso de 
# este método en Python para obtener el resumen global de mediciones agrupadas por mes.

import requests
import json

# Definir la URL del endpoint
url = "https://api.ooni.io/api/_/global_overview_by_month"

# Realizar la solicitud GET al endpoint
response = requests.get(url)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta en formato JSON
    data = response.json()

    # Guardar los datos en un archivo JSON para análisis posterior
    with open("global_overview_by_month.json", "w") as file:
        json.dump(data, file, indent=4)
    
    # Imprimir un resumen básico
    print("Datos globales por mes obtenidos con éxito.")
    for month_data in data:
        print(f"Mes: {month_data['month']}, Pruebas realizadas: {month_data['count']}")
else:
    # Manejar errores
    print(f"Error en la solicitud: {response.status_code}")

#Explicación del script:
# URL del metodo: La variable url contiene el metodo de la API que deseas consultar.
# Solicitud GET: requests.get(url) envía una solicitud HTTP para obtener los datos.
# Validación del Estado: response.status_code verifica si la solicitud fue exitosa (200 significa éxito).
# Conversión a JSON: Si la solicitud tiene éxito, los datos se convierten a un diccionario o lista en Python utilizando response.json().
# Guardado de Datos: Los datos se guardan en un archivo JSON (global_overview_by_month.json) para su análisis posterior.
# Resumen Básico: Itera sobre los datos para mostrar información mensual, como el número de pruebas realizadas.