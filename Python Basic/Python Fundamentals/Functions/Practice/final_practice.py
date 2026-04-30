'''El Reto: "El Analizador de Inventario VIP"
Imagina que recibes una lista de ventas en bruto (un string largo) y necesitas organizar esa información para el dueño de una tienda.

El Objetivo:
Crea una función llamada analizar_ventas(datos_brutos) que reciba un string y devuelva un diccionario con el total de ventas por cada producto.
Reglas del juego:
Los productos en el string vienen separados por comas.
No debe importar si están en mayúsculas o minúsculas (ej: "Camisa" y "camisa" son lo mismo).
Debes limpiar los espacios en blanco que puedan quedar alrededor de las palabras.

Ejemplo de entrada:
"Pantalon, Camisa, pantalon, ZAPATOS, camisa, pantalon"
Salida esperada:
{'pantalon': 3, 'camisa': 2, 'zapatos': 1}

💡 Tu "Mapa de Batalla" (Algoritmo):
Normalización: Convierte todo el string a minúsculas (.lower()).
Fragmentación: Convierte el string en una lista usando .split(",").
Ojo: Al separar por coma, a veces quedan espacios como " camisa".
Limpieza: Crea una nueva lista limpia. Recorre la lista fragmentada y usa .strip() en cada palabra para quitarle esos espacios invisibles.
Conteo: Usa la lógica de diccionarios que perfeccionaste hoy (si no existe, lo creas con 1; si existe, sumas 1).
Retorno: Devuelve el diccionario final.'''

def analizar_ventas(datos_brutos):
    diccionario_ropa = {}
    lista_miniscula = datos_brutos.lower().split()
    
    for item in lista_miniscula:
        ropa = item.strip(",")
        if ropa not in diccionario_ropa:
            diccionario_ropa[ropa] = 1
        else:
            diccionario_ropa[ropa] += 1

    return diccionario_ropa

print(analizar_ventas("Pantalon, Camisa, pantalon, ZAPATOS, camisa, pantalon"))
