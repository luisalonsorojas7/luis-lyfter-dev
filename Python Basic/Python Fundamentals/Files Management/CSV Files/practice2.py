import csv

game_headers = (
    "name",
    "genre",
    "developer",
    "clasification",
)


def get_games_information(number_of_games):
    counter = 0
    my_list_of_games = []

    while counter < number_of_games:
        name = input("Please enter the name of the game: \n")
        game_genre = input("Please enter the type of game: \n")
        developer = input("Please enter the game developer: \n")
        clasification = input("Please enter the game ESRB clasification: \n")

        game = {
            "name": name,
            "genre": game_genre,
            "developer": developer,
            "clasification": clasification,
        }

        counter += 1
        my_list_of_games.append(game)
        print("Videogame was successfully added!\n")

    return my_list_of_games


def create_csv_file(file_path, data, headers):
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(
            file, headers, delimiter="\t"
        )  # Using \t to save data using tabs
        writer.writeheader()
        writer.writerows(data)


def main():
    try:
        number_games = int(input("How many games would you like to add: \n"))
        create_csv_file("games2.csv", get_games_information(number_games), game_headers)
    except ValueError:
        print("Please enter a numeric value.")

if __name__ == "__main__":
    main()
