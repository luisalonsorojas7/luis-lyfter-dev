'''Cree una función que retorne la suma de todos los números de una lista.
La función va a tener un parámetro (la lista) y retornar un número (la suma de todos sus elementos).
[4, 6, 2, 29] → 41'''

my_list = [4, 6, 2, 29]

def sum_list_values(my_list):
    sum_numbers = 0
    for num in my_list:
        sum_numbers += num
    return sum_numbers


print(sum_list_values(my_list))