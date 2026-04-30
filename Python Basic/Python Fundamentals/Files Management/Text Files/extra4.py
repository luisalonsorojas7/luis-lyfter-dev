def append_text_at_the_end(path, extra_text):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(" " + extra_text)

def main():
    file_path = 'extra4.txt'    
    user_input = input("Please enter the text that you would like to append: \n")
    append_text_at_the_end(file_path, user_input)

if __name__ == "__main__":
    main()