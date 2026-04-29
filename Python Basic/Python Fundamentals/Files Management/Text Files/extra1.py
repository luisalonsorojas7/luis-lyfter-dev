def remove_line_breaks(path):
    my_list = []
    full_phrase = ""
    with open(path, 'r', encoding="utf8") as file:
        lines = file.readlines()
        
        for line in lines:
            my_list.append(line.replace("\n",""))
        
        for item in my_list:
            full_phrase += item + " "
        
    return full_phrase

def create_new_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)
        
create_new_file("new_file_combined.txt",remove_line_breaks('breaklines.txt'))

print(remove_line_breaks('breaklines.txt'))