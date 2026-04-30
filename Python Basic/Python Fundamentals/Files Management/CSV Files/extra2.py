import csv

def get_game_by_clasification(clasification, file_path):
    my_game_list = []
    with open(file_path, "r",encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            clasi = row["clasification"]
            if clasification.upper().strip() == clasi.strip().upper():
                my_game_list.append(name) 
    return my_game_list

def print_games_info(game_list):
        if not game_list:
            print("No results found... Please enter another game clasification")
        else:
            for item in game_list:
                print(f"Name: {item}")

def main():
    file_name = 'games.csv'
    try:
        clasification = input("Please enter the game clasification that you would like to search: \n")
        print_games_info(get_game_by_clasification(clasification, file_name))
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' does not exist.")
        
if __name__ == "__main__":
    main()