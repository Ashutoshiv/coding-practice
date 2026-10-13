# How to connect to an API using Python
import requests


base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokeman/{name}"
    response = requests.get(url)
    print(response)
    # if response.status_code == 200:
    #     pokemon_data = response.json()
    #     print(pokemon_data)
    # else:
    #     print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "pikachu"
get_pokemon_info(pokemon_name)