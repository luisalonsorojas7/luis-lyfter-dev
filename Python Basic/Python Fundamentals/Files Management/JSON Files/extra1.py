import json

def get_pokemon_information(json_file):
    result = ""
    with open(json_file, 'r', encoding="utf-8") as file:
        data = json.load(file)
        
        for item in data:
            result = f"Name: {item['name']['english']} Type: {", ".join(item['type'])} Level: {item['level']} Attack: {item['base']['Attack']}"
            print(result)

def main():
    try:
        file_name = 'pokemon.json'
        get_pokemon_information(file_name)
    except FileNotFoundError:
        print(f"File {file_name} not found.")

if __name__ == "__main__":
    main()