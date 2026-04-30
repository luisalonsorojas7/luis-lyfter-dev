'''8. Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada numero del 1 hasta ese número ingresado. 
Luego muestre el resultado de la suma.
5 → 15 (1 + 2 + 3 + 4 + 5)
3 → 6 (1 + 2 + 3)
12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)'''
number = int(input("Please enter the number you want to calculate: \n"))
count = 1
result = 0


while count <= number:
    result += count
    count+=1
    
print("The result is:" , result)