'''8. Cree un programa que muestre el valor más pequeño de una lista sin usar min().
Use una variable para comparar uno a uno
Ejemplo:
Entrada:
my_list = [9, 4, 7, 1, 5]
Salida
"El menor valor es 1"
'''
my_list = [9, 4, 7, 1, 5]
min_number = my_list[0]

for num in my_list:
    if num < min_number:
        min_number = num

print(f"Smaller value is: {min_number}")