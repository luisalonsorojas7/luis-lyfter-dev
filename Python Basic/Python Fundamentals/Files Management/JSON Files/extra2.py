import json

def find_pokemon_by_type(json_file, type_pokemon):
    pokemon_list = []
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
        
        for item in data:
            name = item['name']['english']
            for poke_type in item['type']:
                if type_pokemon.strip().lower() == poke_type.strip().lower():
                    pokemon_list.append(name)
                    break
        return pokemon_list

def print_pokemon_data(pokemon_list):
    if not pokemon_list:
        print("No Pokemon was found with that type!")
    else:
        for pokemon in pokemon_list:
            print(pokemon)

def main():
    try:
        file_name = 'pokemon.json'
        find_type = input("Enter the Pokémon type to search for: \n")
        print_pokemon_data(find_pokemon_by_type(file_name, find_type))
    except FileNotFoundError:
        print("File not found, please validate file name.")

if __name__ == "__main__":
    main()