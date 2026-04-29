
def addition(num, user_num):
    result = num + user_num
    return result

def substraction(num, user_num):
    result = num - user_num
    return result

def multiply(num, user_num):
    result = num * user_num
    return result

def division(num, user_num):
    if user_num <= 0:
        raise ZeroDivisionError 
    result = num / user_num
    return result

def main():
    
    menu_option = 0
    current_number = 100
    
    while True: 
        print("Welcome to Calculator App")
        print(f"Value: {current_number}")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Clear result")
        print("6. Exit")

        try:   
            menu_option = int(input("Please select which option you want to use: \n"))

            if menu_option == 6:
                print("Thanks for using App Calculator")
                break

            match menu_option:
                case 1:
                    try:
                        user_num = float(input("Please enter the number you want to add: \n"))
                        current_number = addition(current_number, user_num)
                        print(f"Operation completed. Result: {current_number} ")
                    except ValueError as error: 
                        print(f"\nThis is not a valid number, back to menu\n{error}")
                
                case 2:
                    try:
                        user_num = float(input("Please enter the number you want to substract: \n"))
                        current_number = substraction(current_number, user_num)
                        print(f"Operation completed. Result: {current_number} ")
                    except ValueError as error:
                        print(f"\nThis is not a valid number, back to menu{error}\n")
                case 3:
                    try:
                        user_num = float(input("Please enter the number you want to multiply: \n"))
                        current_number = multiply(current_number, user_num)
                        print(f"Operation completed. Result: {current_number} ")
                    except ValueError as error:
                        print(f"\nThis is not a valid number, back to menu{error}\n")
                case 4:
                    try:
                        user_num = float(input("Please enter the number you want to divide: \n"))
                        current_number = division(current_number, user_num)
                        print(f"Operation completed. Result: {current_number} ")
                    except ZeroDivisionError as error:
                        print(f"\nYou cant divide by zero, back to menu {error}\n")
                    except ValueError as error:
                        print(f'Please do not enter words, only numbers are allowed, back to menu: {error}')
                case 5:
                    current_number = 0
                    print(f"\nValue was removed: {current_number}\n")
                case _:
                    print("\nPlease enter a valid option (1-6)\n")
                    
        except ValueError:
            print("\nWords are not allowed, you must use a number!\n")

if __name__ == "__main__":
    main()