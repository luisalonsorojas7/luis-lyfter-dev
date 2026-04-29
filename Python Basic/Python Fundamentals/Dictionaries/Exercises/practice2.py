"""''Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
Ejemplos:
list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]
→ {"first_name": "Alek", "last_name": "Castillo", "role": "Software Engineer"}
"""

list_a = ["first_name", "last_name", "role"]
list_b = ["Alek", "Castillo", "Software Engineer"]

dictionary = {}

for index, item in enumerate(list_a):
    dictionary[item] = list_b[index]

print(dictionary)
