"""1. Nivel Recluta: El Acumulador
Reto: Crea una función llamada sumar_pares(lista) que reciba una lista de números y devuelva la suma de solo los números que son pares.

Pista de lógica: Necesitas un bucle for y el operador módulo % 2 == 0 para saber si un número es par.

Por qué ayuda: Te enseña a filtrar datos mientras los procesas."""

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def sumar_pares(lista):
    suma = 0
    for num in lista:
        if num % 2 == 0:
            suma += num
    return suma


print(sumar_pares(lista_numeros))


'''2. Nivel Guerrero: El Inversor
Reto: Crea una función llamada invertir_cadena(texto) que reciba un string y lo devuelva al revés. Si recibe "python", debe devolver "nohtyp".
Pista de lógica: Crea un string vacío. Recorre el texto original y ve "sumando" cada letra al principio del nuevo string.
Por qué ayuda: Te ayuda a entender cómo se manipulan los índices y las secuencias.
'''

def invertir_cadena_manual(texto):
    invertida = ""              # 1. Creamos un contenedor vacío
    for letra in texto:         # 2. Empezamos el viaje letra por letra
        invertida = letra + invertida # 3. El truco de la "suma inversa"
    return invertida     # 4. Entregamos el resultado final


print(invertir_cadena_manual("Python"))

'''
3. Nivel Comandante: El Detector de Duplicados
Reto: Crea una función llamada eliminar_duplicados(lista) que reciba una lista con elementos repetidos y devuelva una nueva lista con cada elemento una sola vez.
Ejemplo: [1, 2, 2, 3] -> [1, 2, 3]
Pista de lógica: Crea una lista vacía. Recorre la lista original y, antes de agregar el elemento a la nueva lista, pregunta con un if si ese elemento ya no está ahí.
Por qué ayuda: Practicas la búsqueda y construcción dinámica de listas.
'''
lista_num = [1, 2, 2, 3]

def eliminar_duplicados(lista):
    nueva = []
    
    for num in lista:
        if num not in nueva:
            nueva.append(num)
    
    return nueva

print(eliminar_duplicados(lista_num))

'''
4. Nivel Maestro: El Contador de Palabras (Diccionarios)
Reto: Crea una función llamada frecuencia_palabras(frase) que reciba un texto y devuelva un diccionario 
donde las claves sean las palabras y los valores sean cuántas veces aparece cada una.
Pista de lógica: Usa .split() para convertir la frase en una lista de palabras. 
Luego, aplica la lógica de "si ya existe en el diccionario, suma 1; si no, créalo con valor 1".
Por qué ayuda: Es la base del análisis de datos y el manejo avanzado de diccionarios.'''

def frecuencia_palabras(frase):
    lista_dividida = frase.split()
    mi_dict = {}
    
    for elemento in lista_dividida:
        if elemento not in mi_dict:
            mi_dict[elemento] = 1
        else:
            mi_dict[elemento] += 1    
    
    return mi_dict

print(frecuencia_palabras("Hola estoy aprendiendo python y estoy aprendiendo programacion y de nuevo Hola"))    