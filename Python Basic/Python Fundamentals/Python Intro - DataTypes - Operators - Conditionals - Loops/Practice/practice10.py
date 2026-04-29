"""10. Cree un diagrama de flujo que pida 3 números al usuario. Si uno de esos números es 30,
o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”.
Ejemplos:
23, 30, 768 → Correcto (hay un 30)
10, 15, 5 → Correcto (10 + 15 + 5 = 30)
35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)"""
sum_numbers = 0
is_thirty = False

for num in range(3):
    number = int(input(f"Please enter number {num + 1}:"))
    sum_numbers += number

    if number == 30:
        is_thirty = True

if is_thirty == True or sum_numbers == 30:
    print("Correct")
else:
    print("Incorrect")