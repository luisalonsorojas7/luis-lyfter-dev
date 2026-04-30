'''9. Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio
Ejemplo
Entrada
my_list = [10, 20, 30, 40, 50]
Salida
"Promedio:" 30
Nueva lista: [40, 50]'''
my_list = [10, 20, 30, 40, 50]
new_list = []
sum_list = 0
average = 0

for num in my_list:
    sum_list += num

average = sum_list / len(my_list)

for number in my_list:
    if number > average:
        new_list.append(number)
        
print(new_list)