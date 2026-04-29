'''Cree una función que reciba un string y retorne cuántas vocales contiene
Ejemplo:
Entrada:

"Hola mundo"
Salida:
4'''

def find_vocals(text):
    vocal = "aeiou"
    vocalupper = "AEIOU"
    counter = 0
    for char in text:
        if char in vocal or char in vocalupper:
            counter+=1
    return counter

print(find_vocals("Hola Mundo"))