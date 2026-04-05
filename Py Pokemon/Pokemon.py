import requests

nombre = input("Ingresa el pokemon que quieres buscar: ").strip().lower()

URL = f'https://pokeapi.co/api/v2/pokemon/{nombre}'
response = requests.get(URL)

if response.status_code == 200:
    datos = response.json()
    print(datos)
else:
    print(f"Error {response.status_code}: Pokémon '{nombre}' no encontrado.")