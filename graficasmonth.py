import requests
import matplotlib.pyplot as plt

# Definir la URL del endpoint
url = "https://api.ooni.io/api/_/global_overview_by_month"

# Realizar la solicitud GET al endpoint
response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()
        print(data)  # Verifica la estructura de los datos

        # Si data es un diccionario, accede a la clave correcta
        if isinstance(data, dict):
            data = data.get("results", [])  # Ajusta según la estructura

        # Extraer meses y conteos
        months = [item["month"] for item in data]
        counts = [item["count"] for item in data]

        # Crear un gráfico
        plt.figure(figsize=(10, 6))
        plt.plot(months, counts, marker="o", label="Pruebas realizadas")
        plt.xlabel("Mes")
        plt.ylabel("Cantidad de Pruebas")
        plt.title("Resumen Global de Pruebas por Mes")
        plt.xticks(rotation=45)
        plt.legend()
        plt.grid()
        plt.show()

    except ValueError:
        print("Error: La respuesta no es un JSON válido")
        print(response.text)
else:
    print(f"Error en la solicitud: {response.status_code}")
