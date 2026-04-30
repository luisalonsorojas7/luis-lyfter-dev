'''1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
Si le salen errores, no se asuste. Lealos e intente comprender qué significan.
Los errores son oportunidades de aprendizaje.
Por ejemplo:
string + string → ?
string + int → ?
int + string → ?
list + list → ?
string + list → ?
float + int → ?
bool + bool → ?'''

name = "Luis"
last_name = "Rojas"
age = 30
level = 50
hobbies = ["Soccer, Gaming, Programming, Traveling"]
favorite_numbers = [7, 11, 19, 28]
is_smart = True
is_tall = False
result = 3.14

print(name + last_name) # No errors *Une los 2 strings*
print(last_name + age) # TypeError: can only concatenate str (not "int") to str *No puedo concatenar string con un int*
print(level + name) # TypeError: unsupported operand type(s) for +: 'int' and 'str' *No puedo sumarle un string a el valor int*
print(favorite_numbers + hobbies) #No errors *Crea una sola lista sin importar el tipo de lista tanto con datos int como strings*
print(name + hobbies) #TypeError: can only concatenate str (not "list") to str *No puedo concatenar un string con listas*
print(result + level) #No errors *Suma las 2 variables float + el dato int
print(is_smart + is_tall) #No errors *El resultado de sumar un True con un False es 1*