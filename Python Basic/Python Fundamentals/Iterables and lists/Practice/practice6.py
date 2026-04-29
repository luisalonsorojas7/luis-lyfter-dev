'''6. Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar
Ejemplo:
Entrada:
my_list = [4, 2, 7, 2, 8, 2, 1]
numero_a_buscar = 2
Salida
"El número 2 aparece 3 veces"
"'''
my_list = []
size = int(input("How many numbers do you want to add to the list?\n"))
counter = 0
number_count = 0

while counter < size:
    number = int(input("Please enter the numer you want to add\n"))
    my_list.append(number)
    counter+=1

print(my_list)

number_to_find = int(input("What is the number you would like to find in the list?\n"))

for num in my_list:
    if num == number_to_find:
        number_count += 1

print(f"Number: {number_to_find} is included in the list {number_count} times")