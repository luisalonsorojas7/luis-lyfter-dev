"""Cree una función que le dé la vuelta a un string y lo retorne.
Esto ya lo hicimos en iterables.
“Hola mundo” → “odnum aloH”"""

def modify_string(phrase):
    word = ""
    for index in range(len(phrase) - 1, -1, -1):
        word += phrase[index]
    return word


print(modify_string("Hola mundo"))
