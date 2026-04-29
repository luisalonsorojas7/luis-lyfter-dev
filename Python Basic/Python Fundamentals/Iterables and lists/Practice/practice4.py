"""4. Cree un programa que elimine todos los números impares de una lista.
Ejemplos:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9] → [2, 4, 6, 8]"""

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []

for index, num in enumerate(my_list):
    if num % 2 == 0:
        new_list.append(num)
print(new_list)
