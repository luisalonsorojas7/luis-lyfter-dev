"""El Reto: "El Despachador de Almacén"
Tienes una lista de pedidos. Cada pedido es una lista con: [Nombre_Producto, Categoría, Peso_Kg].

Tu Objetivo:
Crea una función llamada organizar_almacen(lista_pedidos) que clasifique estos productos por categoría en un diccionario. El valor de cada categoría debe ser otro diccionario con estadísticas.

Ejemplo de Salida:

Python
{
    "Electrónica": {
        "cantidad_productos": 3,
        "peso_total": 8,
        "es_pesado": False
    },
    "Muebles": {
        "cantidad_productos": 2,
        "peso_total": 57,
        "es_pesado": True
    }
}

Reglas de Negocio:
cantidad_productos: Cuántos artículos hay de esa categoría.
peso_total: La suma de los pesos de todos los productos de esa categoría.
es_pesado: Es un booleano (True/False). Debe ser True si el peso_total de la categoría es mayor a 40 kg.

💡 ¿Por qué este ejercicio sube tu nivel?
Diccionarios Anidados: Estás guardando un diccionario dentro de otro diccionario. Esto es fundamental en APIs y bases de datos.
Lógica Condicional de Estado: El valor de es_pesado depende de un cálculo previo (peso_total).
Manejo de Estructuras: Tienes que saber acceder a pedido[1] para la clave y pedido[2] para el peso.

🛠️ Mapa de Batalla Sugerido:
Crea un diccionario vacío inventario.
Recorre la lista de pedidos con un for.

Para cada pedido:
Extrae la categoría y el peso.
Si la categoría NO está en inventario: Créala con los valores iniciales (cantidad 1, el peso del primer producto, y evalúa si ese peso > 40).
Si la categoría YA existe:
Suma 1 a cantidad_productos.
Suma el nuevo peso a peso_total.
Actualiza es_pesado: Vuelve a preguntar si el nuevo peso_total superó los 40 kg.
"""
pedidos = [
    ["Laptop", "Electrónica", 2],
    ["Sofá", "Muebles", 45],
    ["Monitor", "Electrónica", 5],
    ["Silla", "Muebles", 12],
    ["Teclado", "Electrónica", 1],
]

def organizar_almacen(lista_pedidos):
    diccionario_principal = {}
        
    for elemento in lista_pedidos:
        categoria= elemento[1]
        peso = elemento[2]


        if categoria not in diccionario_principal:
            diccionario_principal[categoria] = {"cantidad_productos": 1, "peso_total": peso, "es_pesado": peso > 40}    
        else:
            diccionario_principal[categoria]["cantidad_productos"] += 1
            diccionario_principal[categoria]["peso_total"] += peso

            if diccionario_principal[categoria]["es_pesado"] > 40:
                diccionario_principal[categoria]["es_pesado"] = True
            else:
                diccionario_principal[categoria]["es_pesado"] = False

    return diccionario_principal    

print(organizar_almacen(pedidos))

