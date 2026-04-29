my_list = ['4', 'hola', '10', '5.2']

def convert_to_int(list):
    for item in list:
        try:
            if not item.isdigit():
                raise ValueError()
            
            item_converted = int(item)
            print(f"{item} converted to: {item_converted}")
        
        except ValueError as error:
            print(f"Cannot convert element to int: {item}")
            
def main():
    convert_to_int(my_list)
        
        
if __name__ == "__main__":
    main()