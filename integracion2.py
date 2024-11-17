import requests
import json
import os

# URL base de la API
BASE_URL = "https://api.ooni.io/api/v1/"

# Crear carpeta de salida para los archivos JSON
OUTPUT_DIR = "ooni_results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Función para guardar datos en archivos JSON
def save_to_json(filename, data):
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Archivo guardado: {filepath}")

# Paso 1: Descargar listas de mediciones relevantes
def get_measurements(probe_cc, test_name, since, until, limit=100):
    url = BASE_URL + "measurements"
    params = {
        "probe_cc": probe_cc,  # Código de país
        "test_name": test_name,  # Nombre de la prueba
        "since": since,  # Fecha inicial
        "until": until,  # Fecha final
        "confirmed": "true",  # Solo mediciones con anomalías confirmadas
        "limit": limit,  # Limitar el número de resultados
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        save_to_json("measurements.json", data)
        return data
    else:
        print(f"Error al obtener mediciones: {response.status_code}")
        return []

# Paso 2: Descargar incidentes
def get_incidents():
    url = BASE_URL + "incidents/search"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        save_to_json("incidents.json", data)
        return data
    else:
        print(f"Error al obtener incidentes: {response.status_code}")
        return []

# Paso 3: Descargar metadatos de una medición específica
def get_measurement_meta(measurement_uid):
    url = BASE_URL + "measurement_meta"
    params = {"measurement_uid": measurement_uid}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        save_to_json(f"meta_{measurement_uid}.json", data)
        return data
    else:
        print(f"Error al obtener metadatos: {response.status_code}")
        return {}

# Paso 4: Descargar datos crudos de una medición
def get_raw_measurement(measurement_uid):
    url = BASE_URL + "raw_measurement"
    params = {"measurement_uid": measurement_uid}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        save_to_json(f"raw_{measurement_uid}.json", data)
        return data
    else:
        print(f"Error al obtener datos crudos: {response.status_code}")
        return {}

# Flujo principal
if __name__ == "__main__":
    # Configuración inicial
    probe_cc = "VE"  # Código del país (Venezuela)
    #test_name = "dns_consistency"  # Nombre de la prueba
    test_name = "web_connectivity" 
    since = "2020-01-01T00:00:00"  # Fecha inicial
    until = "2023-12-31T23:59:59"  # Fecha final

    # Paso 1: Obtener mediciones relevantes
    print("Descargando mediciones relevantes...")
    measurements = get_measurements(probe_cc, test_name, since, until)

    # Paso 2: Obtener incidentes
    print("Descargando incidentes...")
    incidents = get_incidents()

# Paso 3: Procesar las mediciones descargadas
# Procesar mediciones
if isinstance(measurements, dict):  # Verifica si measurements es un diccionario
    measurements = measurements.get("results", [])  # Extrae la lista de 'results'

if not measurements:  # Si la lista está vacía
    print("No se encontraron mediciones relevantes.")
else:
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
            print(f"Elemento inesperado dentro de 'results': {measurement}")
