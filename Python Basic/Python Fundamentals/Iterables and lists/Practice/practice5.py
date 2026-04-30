"""5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
Ejemplos:
86, 54, 23, 54, 67, 21, 2, 65, 10, 32 →
[86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86."""
my_list = []
counter = 0

while counter < 10:
    number = int(input("Please enter the number you want to add to the list: \n"))
    my_list.append(number)
    counter += 1

max_number = my_list[0]

for index, num in enumerate(my_list):
    if num > max_number:
        max_number = num


print(f"Numbers inside the list {my_list}. Max number is: {max_number}")