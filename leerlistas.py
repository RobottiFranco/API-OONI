# Un ejemplo para leer las listas descargadas y decidir qué métodos llamar

import json

# Leer la lista de pruebas desde un archivo
with open("test_names.json", "r") as file:
    test_names = json.load(file)

# Mostrar las pruebas disponibles
print("Pruebas disponibles:")
for test in test_names:
    print(f"- {test['name']}: {test['description']}")
