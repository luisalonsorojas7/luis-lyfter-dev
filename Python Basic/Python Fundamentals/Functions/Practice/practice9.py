'''Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras
Ejemplo:
Entrada:
["cielo","sol","maravilloso","día"]

"Ingrese el numero de letras minimas en la palabra: "
4

Salida:
["cielo","maravilloso"]'''

my_list = ["cielo","sol","maravilloso","día"]

def generate_list(lista, num):
    new_list = []
    for item in lista:
        if len(item) > num:
            new_list.append(item)
    return new_list    

print(generate_list(my_list, 4))