'''Cree una función que acepte un string con palabras separadas por un guion y 
retorne un string igual pero ordenado alfabéticamente.
Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
“python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”'''

def create_new_string(string):
    my_list = string.split("-")
    my_list.sort()
    result = "-".join(my_list)
    return result

print(create_new_string("python-variable-funcion-computadora-monitor"))