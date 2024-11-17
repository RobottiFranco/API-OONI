# Para comparar con listas históricas

import json

# Cargar dos listas históricas
with open("domains_2022.json", "r") as file1, open("domains_2023.json", "r") as file2:
    domains_2022 = json.load(file1)
    domains_2023 = json.load(file2)

# Comparar las listas
added = [d for d in domains_2023 if d not in domains_2022]
removed = [d for d in domains_2022 if d not in domains_2023]

print("Dominios agregados en 2023:")
print(added)

print("Dominios eliminados en 2023:")
print(removed)
