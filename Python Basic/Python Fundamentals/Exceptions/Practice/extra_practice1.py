def request_user_name():
    name = input("Please enter your name:\n")
    if name.isdigit():
        raise ValueError("Your name is not valid, please don't user numbers!")
    return name

def request_user_age():
    age = input("Please enter your age:\n")
    if not age.isdigit():
        raise ValueError("Please don't use words, you should use only numbers!")
    return age

def main():
    try:
        name = request_user_name()
        age = request_user_age()
        
        print(f"Hello {name}, your age is {age}")
    except ValueError as error:
        print(f"{error}")

if __name__ == "__main__":
    main()