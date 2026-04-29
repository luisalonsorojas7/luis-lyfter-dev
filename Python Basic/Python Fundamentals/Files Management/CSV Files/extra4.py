import csv

def find_game_developer(path, developer):
    games_found = []
    with open(path, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["name"]
            genre = row["genre"]
            clasification = row["clasification"]
            game_developer = row["developer"]
            if developer.strip().casefold() == game_developer.strip().casefold():
                game_data = {
                    "name": name,
                    "genre": genre,
                    "clasification": clasification
                }
                games_found.append(game_data)
        return games_found

def print_data_found(dic_games):
    if not dic_games:
        print("No games found for this developer.")
    else:
        for item in dic_games:
            print(f"{item['name']} (Clasification:{item['clasification']}, Genre:{item['genre']})")

def main():
    file_name = 'games.csv'
    developer = input("Please enter the game developer to find related games: \n")
    print_data_found(find_game_developer(file_name, developer))


if __name__ == "__main__":
    main()