#Combinar Búsqueda de IDs y Detalles
import requests

# Endpoint para listar mediciones
url_measurements = "https://api.ooni.io/api/v1/measurements"
params = {
    "probe_cc": "UY",  # Código de país (Uruguay)
    "test_name": "dns_consistency",  # Tipo de prueba
    "since": "2023-01-01",  # Fecha de inicio
    "until": "2023-12-31"   # Fecha de fin
}

# Realizar la solicitud para obtener mediciones
response = requests.get(url_measurements, params=params)

if response.status_code == 200:
    measurements = response.json()
    print("Contenido de measurements:", measurements)  # Verificar contenido

    # Accede a 'results' si está disponible
    measurements = measurements.get("results", [])
    if measurements:
        measurement_uid = measurements[0]["measurement_uid"]
        print(f"Measurement UID encontrado: {measurement_uid}")

        # Consultar detalles de la medición con el UID
        url_detail = f"https://api.ooni.io/api/v1/measurement/{measurement_uid}"
        response_detail = requests.get(url_detail)

        if response_detail.status_code == 200:
            measurement_detail = response_detail.json()
            print(f"Detalles de la medición: {measurement_detail}")
        else:
            print(f"Error al obtener detalles: {response_detail.status_code}")
    else:
        print("No se encontraron mediciones.")
else:
    print(f"Error en la solicitud de mediciones: {response.status_code}")
