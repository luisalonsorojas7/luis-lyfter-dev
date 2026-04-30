def main():
    my_list = ['2', 'Hello']
    index_to_use = 1
    
    try:
        list_element_to_convert = my_list[index_to_use]
        element_to_int = int(list_element_to_convert)
        print(element_to_int)
    except IndexError as error:
        print(f'El indice a usar no existe en la lista. Error: {error}')
    except ValueError as error:
        print(f'El elemento de la lista no es un numero valido. Error: {error}')

if __name__ == '__main__':
    main()
    
    
def main():
    my_list = [
        '2',
        'Hello'
    ]
    index_to_use = 4
    
    try:
        list_element_to_convert = my_list[index_to_use]
        element_to_int = int(list_element_to_convert)
        print(element_to_int)
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')


if __name__ == '__main__':
    main()
    
    
def main():
    my_list = [
        '2',
        'Hello'
    ]
    index_to_use = 4
    
    list_element_to_convert = '0'
    element_to_int = 0
    
    try:
        list_element_to_convert = my_list[index_to_use]
        element_to_int = int(list_element_to_convert)
        print(list_element_to_convert)
    except Exception as error:
        print(f'Ha ocurrido un error: {error}')
    
    # Este print se ejecutará siempre, independientemente de si hubo error o no
    print(list_element_to_convert)



def check_if_number_is_100(number):
	if number < 100:
		raise ValueError('El numero es muy bajo')
	elif number > 100:
		raise ValueError('El numero es muy alto')
	
	return True

def main():
	number = input('Ingrese un numero')
	try:
		number_int = int(number)
		check_if_number_is_100(number_int)
	except ValueError as ex:
		print(ex)


if __name__ == '__main__':
	main()


if __name__ == '__main__':
    main()
    
    
try:
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError()
except Exception as error:
    # unhappy path
    print("Su nombre no puede ser un numero!")

# happy path
edad = input(f"Gracias {name}! Ahora ingrese su edad: ")
empleo = input(f"Gracias {name}! Ahora ingrese su empleo: ")


def ask_for_user_information():
	try:
		age = int(input('Ingrese su edad'))
		if age < 1 or age > 100:
			raise ValueError()

	except ValueError as ex:
		print("Ingrese una edad valida!")
		raise ex


def main():
	try:
		ask_for_user_information()
		# create_order()

	except Exception as ex:
		exit()


if __name__ == '__main__':
	main()


def check_if_number_is_100(number):
	if number < 100:
		raise ValueError('El numero es muy bajo')
	elif number > 100:
		raise ValueError('El numero es muy alto')
	
	return True

def main():
	number = input('Ingrese un numero')
	try:
		number_int = int(number)
		check_if_number_is_100(number_int)
	except ValueError as ex:
		print(ex)


if __name__ == '__main__':
	main()


def function_1():
	try:
		some_logic_with_value_errors()
	except ValueError as ex:
		print(f'An error ocurred in function_1')


def function_2():
	try:
		some_logic_with_index_errors()
	except IndexError as ex:
		print(f'An error ocurred in function_2')


def main():
	try:
		function_1()
		function_2()

	except Exception as ex:
		print(f'An unexpected error ocurred: {ex}')


if __name__ == '__main__':
	main()

try:
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError()
except Exception as error:
    # unhappy path
    print("Su nombre no puede ser un numero!")

# happy path
edad = input(f"Gracias {name}! Ahora ingrese su edad: ")
empleo = input(f"Gracias {name}! Ahora ingrese su empleo: ")