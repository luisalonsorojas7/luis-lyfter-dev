"""2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
Pista: investigue de que otras maneras se puede usar el range.
Ejemplos:
my_string = "Pizza con piña" →
a
ñ
i
p

n
o
c

a
z
z
i
p"""
my_string = "Pizza con piña"

for char in range(len(my_string)-1, -1, -1):
    print(my_string[char])