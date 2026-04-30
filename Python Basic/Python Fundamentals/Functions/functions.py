def print_hello_world():
	print("Hello World!")
	print("Mi primera funcion")

print_hello_world()

def calculate_salary():
	worked_hours = int(input("Ingrese sus horas trabajadas: "))
	hour_rate = int(input("Ingrese su tarifa por hora: "))
	
	salary = worked_hours * hour_rate
	
	print(f'Su salario sera de {salary}')

calculate_salary()

def get_max_of_two_numbers(number1, number2):
    if number1 > number2:
        return number1

    return number2


result = get_max_of_two_numbers(4, 15)
print(result)