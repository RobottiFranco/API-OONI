
# script en Python que descarga datos históricos y los guarda en archivos separados por años

import requests
import json

# URL base del endpoint
base_url = "https://api.ooni.io/api/v1/measurements"

# Función para descargar datos históricos
def download_measurements(probe_cc, test_name, since, until, filename):
    # Definir los parámetros de la consulta
    params = {
        "probe_cc": probe_cc,  # País
        "test_name": test_name,  # Tipo de prueba
        "since": since,  # Fecha de inicio
        "until": until,  # Fecha de fin
        "limit": 1000  # Número máximo de resultados por página
    }
    
    # Realizar la solicitud GET
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()  # Convertir respuesta a JSON
        
        # Guardar los datos en un archivo
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
        
        print(f"Datos guardados en {filename}")
    else:
        print(f"Error al descargar datos: {response.status_code}")

# Descargar datos para 2022
download_measurements(
    probe_cc="UY",
    test_name="dns_consistency",
    since="2022-01-01T00:00:00",
    until="2022-12-31T23:59:59",
    filename="domains_2022.json"
)

# Descargar datos para 2023
download_measurements(
    probe_cc="UY",
    test_name="dns_consistency",
    since="2023-01-01T00:00:00",
    until="2023-12-31T23:59:59",
    filename="domains_2023.json"
)
