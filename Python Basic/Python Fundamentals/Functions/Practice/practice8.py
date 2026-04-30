'''
Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto
Ejemplo:
Entrada:
"programacion"
"Ingrese el carácter que desea buscar:"
"o"
Salida:
"Se a encontrado 2 veces el carácter"
'''

text = input("Please enter a word\n")
char = input("Please the char that you would like to find\n")   

def find_character(text, character):
    counter = 0
    for char in text:
        if character == char:
            counter+=1
    return counter
    
    
result = find_character(text, char)
print( f"Character was found {result} times.")
    