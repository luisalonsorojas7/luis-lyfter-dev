'''Cree un programa que abra un archivo .json con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
Lea el archivo JSON de Pokémon
Para cada Pokémon, muestre sus estadísticas principales (por ejemplo: ataque, defensa, velocidad, etc.)
Ejemplo:
Salida:

Copiar
Nombre: Pikachu
Ataque: 55
Defensa: 40
Velocidad: 90
Nombre: Bulbasaur
Ataque: 49
Defensa: 49
Velocidad: 45
'''

import json

def get_pokemon_data(json_file):
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
        for pokemon in data:
            name = pokemon['name']['english']
            attack = pokemon['base']['Attack']
            defense = pokemon['base']['Defense']
            speed = pokemon['base']['Speed']
            print("-----------------")
            print(f"Name: {name}\nAttack: {attack}\nDefense: {defense}\nSpeed: {speed}")


def main():
    try:
        file = 'pokemon.json'
        get_pokemon_data(file)
    except FileNotFoundError:
        print("File not found, please validate file name.")
    

if __name__ == "__main__":
    main()