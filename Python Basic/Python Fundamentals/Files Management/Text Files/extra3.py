def read_file_with_lower_text(path):
    with open(path, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        result = ""
        for line in lines:
            result += line.upper().strip() + "\n"
        return result

def change_lines_to_upper_case(path, text):
    with open(path, 'w', encoding="utf-8") as file:
        file.write(text)
        
change_lines_to_upper_case('extra_upper_3.txt', read_file_with_lower_text('extra3.txt'))