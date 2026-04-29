"""10. Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras
Ejemplo:
Entrada:
['sol', 'estrella', 'luz', 'planeta', 'roca']
Salida:
['estrella', 'planeta']"""

word_list = []
new_list = []
counter = 0
while counter < 5:
    word = input("Please enter the word that you would like to save in the list: \n")
    word_list.append(word)
    counter+=1

for element in word_list:
    if len(element) > 4:
        new_list.append(element)

print(new_list)