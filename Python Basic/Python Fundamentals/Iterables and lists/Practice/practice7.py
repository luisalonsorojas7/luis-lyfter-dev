'''7. Cree un programa que verifique si todos los elementos de una lista son positivos
Restricciones:
No use funciones como all()
Ejemplo:
Entrada:
my_list = [3, 6, 0, -2, 4]
Salida:
"Hay al menos un número negativo o cero"'''

my_list = [3, 6, 0, -2, 4]
neg_counter = 0

for number in my_list:
    if number == 0 or number < 0:
        message = "There is at least one negative number or a cero"
        break
    else:
        message = "All your list contains positive"
        
print(message)