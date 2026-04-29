import csv

def read_games_file(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"Name: {row['name']}")
            print(f"Genre: {row['genre']}")
            print(f"Developer: {row['developer']}")
            print(f"Classification: {row['clasification']}")

def main():
    read_games_file("games.csv") 

if __name__ == "__main__":
    main()