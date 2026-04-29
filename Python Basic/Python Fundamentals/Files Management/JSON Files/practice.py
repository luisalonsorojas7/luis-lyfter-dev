import json


def add_new_pokemon(path, pokemon):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            data.append(pokemon)
        
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            
        print(f"¡{pokemon['name']['english']} agregado con éxito!")

    except FileNotFoundError:
        print(f"File: {path} not found")


def main():
    try:
        file = 'pokemon.json'
        name = input("Please enter the name of your pokemon: \n")
        level = int(input("What is the level of your pokemon: \n"))
        pok_type = input("What is the pokemon type: \n")
        hp = int(input("Health Points: \n"))
        attack = int(input("Attack Points: \n"))
        defense = int(input("Defense Points: \n"))
        sp_attack = int(input("Special Attack: \n"))
        sp_defense = int(input("Special Defense: \n"))
        speed = int(input("Speed: \n"))
        
        pokemon = {
                    "name": {"english": name},
                    "level": level,
                    "type": [pok_type],
                    "base": {
                        "HP": hp,
                        "Attack": attack,
                        "Defense": defense,
                        "Sp. Attack": sp_attack,
                        "Sp. Defense": sp_defense,
                        "Speed": speed
                    }
                } 
        
        add_new_pokemon(file, pokemon)
        
    except ValueError:
        print("Please only use numbers for level and statistics")

if __name__ == "__main__":
    main()
