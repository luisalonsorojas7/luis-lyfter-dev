'''Experimente con el concepto de scope:
Intente acceder a una variable definida dentro de una función desde afuera.
Intente acceder a una variable global desde una función y cambiar su valor.'''

global_variable = 25

def sum_two_numers(num1, num2):
    total = num1 + num2
    return total


def change_global_variable(num):
    global global_variable 
    global_variable = num * 10 # Modifyng global variable


print(total) #Triying to access local variable "total" from outside Error: "total" is not defined

change_global_variable(2) #Calling function to modify the global variable
print(global_variable) #print new global variable value

