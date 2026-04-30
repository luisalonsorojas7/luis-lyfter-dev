"""Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
[1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]
Tip 1: Investigue la lógica matemática para averiguar si un número es primo, y conviértala a código. No busque el código, eso no ayudaría.
Tip 2: Aquí hay que hacer varias cosas (recorrer la lista, revisar si cada numero es primo, y agregarlo a otra lista).
Así que lo mejor es agregar otra función para revisar si el numero es primo o no."""
import math

my_list = [1, 4, 6, 7, 13, 9, 67]


def is_prime(number):
    if number <= 1:
        return False
    for num in range(2, int(math.sqrt(number)) + 1):
        if number % num == 0:
            return False
    return True


def create_prime_list(num_list):
    new_list = []
    for number in num_list:
        if is_prime(number):
            new_list.append(number)
    return new_list

print(create_prime_list(my_list))
