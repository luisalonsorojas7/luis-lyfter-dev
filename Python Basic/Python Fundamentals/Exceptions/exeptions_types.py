#ValueError: Cuando un argumento tiene el tipo correcto, pero un valor inapropiado
try:
    int("abc")
except ValueError as e:
    print(f"Error [ValueError]: No se pudo convertir el valor 'abc' a un entero. Detalles: {e}")

#TypeError: Cuando se realiza una operación con un tipo de dato incorrecto.
try:
    "2" + 2
except TypeError as e:
    print(f"Error [TypeError]: Intentaste combinar un string con un número. Detalles: {e}")

#KeyError: Al intentar acceder a una clave inexistente en un diccionario.
try:
    my_dict = {"a": 1}
    value = my_dict["b"]
except KeyError as e:
    print(f"Error [KeyError]: La clave 'b' no existe en el diccionario. Detalles: {e}")

#IndexError: Cuando se intenta acceder a un índice fuera del rango de una lista.
try:
    my_list = [1, 2, 3]
    value = my_list[10]
except IndexError as e:
    print(f"Error [IndexError]: El índice 10 está fuera del rango de la lista. Detalles: {e}")

#AttributeError: Cuando un objeto no tiene un atributo solicitado.
try:
    obj = 10
    obj.some_method()
except AttributeError as e:
    print(f"Error [AttributeError]: El objeto de tipo 'int' no tiene el atributo 'some_method'. Detalles: {e}")

#ZeroDivisionError: Cuando se intenta dividir un número por cero.
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error [ZeroDivisionError]: Intentaste dividir 10 entre 0. Detalles: {e}")
    

#Creando nuestra propia exeption
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        super().__init__(f"Fondos insuficientes: Intentaste retirar {amount}, pero solo tienes {balance} disponible.")

try:
    balance = 100
    amount_to_withdraw = 150
    if amount_to_withdraw > balance:
        raise InsufficientFundsError(balance, amount_to_withdraw)
except InsufficientFundsError as e:
    print(f"Error detectado: {e}")