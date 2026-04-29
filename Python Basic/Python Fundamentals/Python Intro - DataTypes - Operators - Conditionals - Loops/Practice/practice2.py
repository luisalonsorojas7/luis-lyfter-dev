"""2. Cree un programa que le pida al usuario su nombre, apellido, y edad,
y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
"""
name = input("Please enter your name:\n")
last_name = input("Please enter your last name:\n")
age = int(input("How old are you?\n"))

if age < 0:
    print("Age cannot be less than 0.")
elif age <= 2:
    print("Category: Baby.")
elif age <= 10:
    print("Category: Child.")
elif age <= 13:
    print("Category: Tween.")
elif age <= 17:
    print("Category: Teenager.")
elif age <= 39:
    print("Category: Young adult.")
elif age <= 64:
    print("Category: Adult.")
else:
    print("Category: Senior/Elderly.")
    
print(f"{name} {last_name} is {age} years old")
