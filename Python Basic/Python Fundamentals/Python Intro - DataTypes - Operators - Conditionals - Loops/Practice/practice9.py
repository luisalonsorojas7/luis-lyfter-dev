'''Cree un diagrama de flujo que tenga un numero secreto del 1 al 10, 
y le pida al usuario adivinar ese número. El algoritmo no debe terminar hasta que el usuario adivine el numero.'''
import random
user_number = 0
secret_number = random.randint(1, 10)

while user_number != secret_number:
    user_number = int(input("Please enter enter a number: (1-10)\n"))
    if user_number == secret_number:
        print("Congratulations! You found the secret number!\n")
    else:
        print("That is not the secret number, please try again!\n")