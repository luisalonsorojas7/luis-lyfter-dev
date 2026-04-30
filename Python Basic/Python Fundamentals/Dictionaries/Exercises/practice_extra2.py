employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
'''Agrupar empleados por departamento
Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario que agrupe los empleados por su departamento:'''

my_dictionary = {}

for person in employees:
    name = person["name"]
    dep = person["department"]
    
    if dep not in my_dictionary:
        my_dictionary[dep] = []
    
    my_dictionary[dep].append(name)    
    
print(my_dictionary)