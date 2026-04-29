def count_words_in_file(path):
    with open(path, "r", encoding="utf-8") as file:
        content = file.read()
        my_list = content.split()
        return f"This file has: {len(my_list)} words."

print(count_words_in_file("extra2.txt"))