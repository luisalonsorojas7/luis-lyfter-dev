import csv

def count_games(path):
    genre_dic = {}
    try:
        with open(path, 'r', encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                genre = row["genre"]
                if genre not in genre_dic:
                    genre_dic[genre] = 1
                else: 
                    genre_dic[genre] += 1
            return genre_dic
    except FileNotFoundError:
        print(f"Error: File {path} does not exists.")


def print_data(dictionary):
    sorted_genres = sorted(dictionary.keys())
    for item in sorted_genres:
        print(f"{item}: {dictionary[item]}")


def main():
    file_name = 'games.csv'
    results = count_games(file_name)
    
    if results:
        print_data(results)

if __name__ == "__main__":
    main()