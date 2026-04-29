'''El Reto: "El Contador de Medallas"
Imagina que eres el organizador de unas olimpiadas escolares. Tienes una lista de los resultados de las carreras y un valor de puntos por cada medalla.
Tu Objetivo:
Crea una función contar_puntos(tabla, lista_resultados) que devuelva un nuevo diccionario con el puntaje total de cada niño.

Ejemplo de Salida:{"Juan": 12, "Maria": 15, "Pedro": 10}

Pasos para que no te pierdas (Síguelos uno a uno):
Prepara el recipiente: Crea un diccionario vacío llamado puntajes_finales = {} fuera del bucle.
Recorre los resultados: Usa un for para leer la lista resultados.
Tip: Puedes usar for nombre, medalla in lista_resultados: para separar los datos de una vez.
Busca el valor: Crea una variable puntos_ganados que busque en la tabla_puntos cuánto vale la medalla que salió en ese turno.

Suma al niño correspondiente:
Si el niño NO está en puntajes_finales: Agrégalo con sus primeros puntos.
Si el niño YA está: Súmale los nuevos puntos a los que ya tenía.'''
tabla_puntos = {
    "oro": 10,
    "plata": 5,
    "bronce": 2
}

resultados = [
    ["Juan", "oro"],
    ["Maria", "plata"],
    ["Juan", "bronce"],
    ["Pedro", "oro"],
    ["Maria", "oro"]
]

def contarpuntos(diccionario_tabla, lista_resultados):
    diccionario_resultados_finales = {}
    
    for result in lista_resultados:
        nombre = result[0]
        medalla = result[1]
        suma_puntajes = diccionario_tabla[medalla]
        
        if nombre not in diccionario_resultados_finales:
            diccionario_resultados_finales[nombre] = suma_puntajes      
        else:
            diccionario_resultados_finales[nombre] += suma_puntajes
            
    return diccionario_resultados_finales

print(contarpuntos(tabla_puntos, resultados))