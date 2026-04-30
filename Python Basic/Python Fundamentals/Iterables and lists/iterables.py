my_favorite_records = ['Dark Side Of The Moon','Fear of a Blank Planet','Signify']

#Recorrer la lista usando un ciclo For in
for record in my_favorite_records:
    print(f"Record using For in: {record}")

#Accediento un elemento de la lista usando su indice
print(my_favorite_records[0])

#Recorrer la lista usando ciclo For con la funcion Range()
for record in range(0, len(my_favorite_records)):
    name_record = my_favorite_records[record]
    print(f"Record: {record} - {name_record}")

#Recorrer la lista usando while (No recomendo pero es posible)
counter = 0
while counter < len(my_favorite_records):
    record_name = my_favorite_records[counter]
    counter+=1
    print(f"Using while: {counter} {record_name}")
    
#Usando enumerate para recorrer la lista podremos sacar el indice y el valor dentro del indice mas facil 
for index, name in enumerate(my_favorite_records):
    print(f"Using enumerate: {index} {name}")

#Recorriendo un String
movie = "Star Wars"
for char in movie:
    print(char)
print(movie[1])

'''Tienes una lista de correos_sin_formato = ["juan", "luisa", "pedro"].
Crea una lista nueva llamada correos_oficiales.
Usa un for para que cada nombre termine como "juan@empresa.com", "luisa@empresa.com", etc., y guárdalos en la lista nueva.'''
correos_sin_formato = ["juan", "luisa", "pedro"]
correos_oficiales = []

for empleado in correos_sin_formato:
    correo = empleado + "@empresa.com"
    correos_oficiales.append(correo)
print(correos_oficiales)

for emp in correos_oficiales:
    print(emp)

'''Tu Misión (Paso a paso):

Crea una lista vacía llamada usuarios_bloqueados.
Usa un for con range(len(usuarios)) para recorrer las listas (porque necesitas el índice para comparar el nombre con su número de intentos).
Condición (Filtro): Si los intentos_fallidos en esa posición son mayores a 3:
Transformación: Crea un mensaje que diga: "USUARIO: [nombre] - ESTADO: BLOQUEADO".
Guarda ese mensaje en tu lista usuarios_bloqueados usando .append().
Al final, fuera del bucle, imprime la lista de bloqueados.'''
usuarios = ["ana", "beto", "carla", "dani"]
intentos_fallidos = [2, 5, 1, 8]
usuarios_bloqueados = []

for usuario in range(len(usuarios)):
    if intentos_fallidos[usuario] > 3:
        mensaje = "USUARIO: " + usuarios[usuario] + " ESTADO: BLOQUEADO "
        usuarios_bloqueados.append(mensaje)

print(usuarios_bloqueados)