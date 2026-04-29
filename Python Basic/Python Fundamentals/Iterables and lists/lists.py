my_pets_list = ["dog", "cat"]
my_pets_list.append("rabbit") #Agrega un elemento al final de la lista
print(my_pets_list)

courses_list = ['Computers', 'Algorithms', 'Python','Web Development']
courses_list.insert(2 ,'Data Base') #Agrega un elemento indicando el indice donde queremos que vaya y su valor
print(courses_list)

#extends junta la primera lista con la segunda y crea una sola lista 
first_list = ['A', 'B', 'C',]
second_list = ['D', 'E', 'F',]
first_list.extend(second_list)

print(first_list)

#Usamos pop para eliminar un elemento en un indice en especifico y retorna su valor
milky_way_planets = ['Mercury','Venus','Earth', 'Mars', 'Pluto', 'Jupiter', 'Saturn', 'Uranus','Neptune',]
deleted_item = milky_way_planets.pop(7)
print(milky_way_planets)
print(f"El elemento eliminado fue: {deleted_item}\n")

#Vamos a eliminar Mars recorriendo la lista
mars = 0
for index,planet in enumerate(milky_way_planets):
        if planet == "Mars":
                mars = index
                planet = milky_way_planets.pop(mars)
                print(f"El elemento eliminado fue: {planet}")
                break

my_list = [4, 3, 6, 1, 7, 10, 45, 5]
first_item = 0
last_item = 0

for index in range(len(my_list)):
        if index == 0:
                first_item = my_list.pop(0)
        elif index == (len(my_list)-1):
                last_item = my_list.pop(len(my_list)-1)

my_list.append(first_item)
my_list.insert(0, last_item)           
print(my_list)


'''.append(x): Agrega el elemento x al final de la lista.
.extend(iterable): Agrega todos los elementos de otro conjunto (como otra lista) al final.
.insert(i, x): Inserta el elemento x en la posición con índice i.
.remove(x): Elimina la primera aparición del valor x en la lista.
.pop(i): Elimina y devuelve el elemento en la posición i. Si no pones i, elimina el último.
.clear(): Elimina todos los elementos de la lista (la deja vacía).
.index(x): Devuelve la posición (índice) de la primera aparición el valor x.
.count(x): Cuenta cuántas veces aparece el valor x en la lista
.sort(): Ordena los elementos de la lista de forma ascendente(modifica la lista original).
.reverse(): Invierte el orden de los elementos de la lista "in situ".
.copy(): Devuelve una copia exacta (superficial) de la lista.

Funciones extra (No son métodos, pero son vitales)
Estas no se escriben con punto (como lista.append), sino que envuelven a la lista:
len(lista): Te dice cuántos elementos hay en total.
max(lista): Te da el valor más grande.
min(lista): Te da el valor más pequeño.
sum(lista): Suma todos los números de la lista.
sorted(lista): Te devuelve una nueva lista ordenada sin tocar la original.'''