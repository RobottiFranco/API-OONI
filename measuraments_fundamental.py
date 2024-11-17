import requests
import json

# URL base del endpoint
url = "https://api.ooni.io/api/v1/measurements"

# Parámetros de consulta
params = {
    "probe_cc": "UY",  # Código de país: Uruguay
    "test_name": "dns_consistency",  # Tipo de prueba: DNS Consistency
    "since": "2023-01-01T00:00:00",  # Fecha de inicio
    "until": "2023-12-31T23:59:59",  # Fecha de fin
    "confirmed": "true",  # Solo mediciones con anomalías confirmadas
    "limit": 50  # Número de resultados por página
}

# Realizar la solicitud GET
response = requests.get(url, params=params)

if response.status_code == 200:
    measurements = response.json()
    print("Contenido de measurements:", measurements)  # Ver estructura

    # Acceder a los resultados si existe una clave específica
    measurements = measurements.get("results", measurements)

    if isinstance(measurements, list):  # Verifica si es una lista
        print(f"Se encontraron {len(measurements)} mediciones:")
        for measurement in measurements:
            if isinstance(measurement, dict):  # Verifica si es un diccionario
                print(f"- Measurement UID: {measurement['measurement_uid']}")
            else:
                print(f"- Measurement inesperado: {measurement}")
    else:
        print("Formato inesperado en measurements:", measurements)
else:
    print(f"Error en la solicitud: {response.status_code}")
