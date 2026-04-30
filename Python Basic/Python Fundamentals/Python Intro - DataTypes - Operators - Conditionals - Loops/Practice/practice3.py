"""3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
"""
import random

random_number = random.randint(1, 10)
user_number = 0

while user_number != random_number:
    user_number = int(input("Please enter the number you consider is the secret one: (1-10)\n"))
    if user_number == random_number:
        print("Congratulations! You found the secret number! You are the best!\n")
    else:
        print("Ups, that is not the secret number, please try again!\n")

