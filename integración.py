import requests
import json

# Base URL de la API
base_url = "https://api.ooni.io/api/v1/"

# Paso 1: Buscar mediciones relevantes
def search_measurements(probe_cc, test_name, since, until):
    url = base_url + "measurements"
    params = {
        "probe_cc": probe_cc,
        "test_name": test_name,
        "since": since,
        "until": until,
        "confirmed": "true",  # Solo anomalías confirmadas
        "limit": 50
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()  # Devuelve mediciones relevantes
    else:
        print(f"Error al buscar mediciones: {response.status_code}")
        return []

# Paso 2: Validar medición con metadata
def get_measurement_meta(measurement_uid):
    url = base_url + "measurement_meta"
    params = {"measurement_uid": measurement_uid}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener metadatos: {response.status_code}")
        return {}

# Paso 3: Descargar datos crudos
def get_raw_measurement(measurement_uid):
    url = base_url + "raw_measurement"
    params = {"measurement_uid": measurement_uid}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al obtener datos crudos: {response.status_code}")
        return {}

# Paso 4: Buscar incidentes relacionados
def search_incidents():
    url = base_url + "incidents/search"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error al buscar incidentes: {response.status_code}")
        return []

# Ejecución del flujo de trabajo
if __name__ == "__main__":
    # Buscar mediciones
    measurements = search_measurements(
        probe_cc="UY", 
        test_name="dns_consistency", 
        since="2023-01-01T00:00:00", 
        until="2023-12-31T23:59:59"
    )

# Procesar las primeras mediciones
if isinstance(measurements, list):  # Asegúrate de que es una lista
    for measurement in measurements:
        if isinstance(measurement, dict):  # Verifica si es un diccionario
            uid = measurement.get("measurement_uid")
            if uid:
                print(f"Procesando medición: {uid}")

                # Obtener metadatos
                meta = get_measurement_meta(uid)
                print(f"Metadatos: {meta}")

                # Descargar datos crudos
                raw_data = get_raw_measurement(uid)
                print(f"Datos crudos descargados para {uid}")
            else:
                print("Measurement sin UID:", measurement)
        else:
            print("Formato inesperado en measurement:", measurement)
else:
    print("Measurements no es una lista:", measurements)

#Búsqueda Inicial:
    #Usa /api/v1/measurements para obtener una lista de mediciones relevantes.
    
#Validación y Análisis:
    #Usa /api/v1/measurement_meta para validar las mediciones y asegurarte de que son relevantes.
    #Luego, usa /api/v1/raw_measurement para descargar los datos completos.
    
#Ampliación de Contexto:
    #Usa /api/v1/incidents/search para buscar incidentes relacionados y comprender el contexto de las mediciones.
    
#Análisis Detallado:
    #Profundiza en los detalles específicos de una medición con /api/v1/measurement/{measurement_uid}.