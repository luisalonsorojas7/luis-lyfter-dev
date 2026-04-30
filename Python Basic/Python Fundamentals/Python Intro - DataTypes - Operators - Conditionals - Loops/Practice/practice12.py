"""12. Tabla de multiplicar personalizada
Pida al usuario un número del 1 al 10
Muestre su tabla de multiplicar del 1 al 12:
Entrada:
"Ingrese un número:" 7
Salida:
7 x 1 = 7
7 x 2 = 14
"""
number = int(input("Enter a number for the multiplication table:\n"))

for num in range(1, 13):
    print(f"{number} x {num} = {number * num}")
