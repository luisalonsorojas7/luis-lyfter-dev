"""4. Cree un programa que le pida tres números al usuario y muestre el mayor."""

number1 = int(input("Please enter the first number: \n"))
number2 = int(input("Please enter the second number: \n"))
number3 = int(input("Please enter the third number: \n"))
max_value = 0

if number1 > number2 and number1 > number3:
    max_value = number1
elif number2 > number1 and number2 > number3:
    max_value = number2
else:
    max_value = number3

print(f"Max value is {max_value}")