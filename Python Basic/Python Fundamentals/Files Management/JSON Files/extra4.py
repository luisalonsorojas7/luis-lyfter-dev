import json

def group_pokemon_by_type(json_file):
    types_dictionary = {}
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
        
        for pokemon in data:
            level = pokemon['level']
            for pokemon_type in pokemon['type']:
                if pokemon_type not in types_dictionary:
                    types_dictionary[pokemon_type] = [level, 1]
                else:
                    types_dictionary[pokemon_type][0] += level
                    types_dictionary[pokemon_type][1] += 1
                
        return types_dictionary

def main():
    try:
        file = 'pokemon.json'
        results = group_pokemon_by_type(file)
        
        for poke_type, value in results.items():
            average = value[0] / value[1]
            print(f"Type: {poke_type}  Average: {average}")
        
        
    except FileNotFoundError:
        print("File not found, please validate file name.")

if __name__ == "__main__":
    main()