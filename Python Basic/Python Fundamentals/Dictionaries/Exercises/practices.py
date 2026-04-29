"""Enunciado:
Tienes una lista de productos que entraron a bodega.
Algunos están repetidos. Crea un diccionario que diga cuántas unidades
hay de cada producto, pero solo si el producto es de la marca "Sony"."""

bodega = [
    {"nombre": "TV", "marca": "Sony"},
    {"nombre": "Radio", "marca": "Samsung"},
    {"nombre": "TV", "marca": "Sony"},
    {"nombre": "Audífonos", "marca": "Sony"},
    {"nombre": "Celular", "marca": "Apple"},
]

dic_unidades = {}
contador_articulos = 0


for articulo in bodega:
    nombre = articulo["nombre"]
    marca = articulo["marca"]

    if marca != "Sony":
        continue

    if nombre not in dic_unidades:
        dic_unidades[nombre] = 1
    else:
        dic_unidades[nombre] += 1

print(dic_unidades)


"""Tienes una lista de reportes de una fábrica. Cada reporte dice el nombre del producto y si pasó la prueba de calidad (True o False).
Tu misión es crear un diccionario que guarde únicamente los productos que fallaron (los que tienen False), y el valor debe ser cuántas veces falló cada uno.
Resultado esperado: {"Sensor": 2, "Microchip": 2}"""

reportes = [
    {"producto": "Microchip", "paso": True},
    {"producto": "Sensor", "paso": False},
    {"producto": "Microchip", "paso": False},
    {"producto": "Placa", "paso": True},
    {"producto": "Sensor", "paso": False},
    {"producto": "Microchip", "paso": False},
    {"producto": "Sensor", "paso": True},
]

my_dic = {}
cantidad = 0

for producto in reportes:
    prod = producto["producto"]
    paso = producto["paso"]

    if paso == False:
        if prod not in my_dic:
            my_dic[prod] = 1
        else:
            my_dic[prod] += 1

print(my_dic)

"""Trabajas en el equipo de TI y recibes un log (una lista) de eventos de diferentes servidores. 
Cada evento dice el nombre del servidor y cuántos "errores" detectó en ese momento.
Tu misión es crear un diccionario donde la llave sea el nombre del servidor y 
el valor sea el total de errores acumulados, pero solo para los servidores que tengan más de 0 errores
{"Srv-Web": 8, "Srv-Cache": 10, "Srv-DB": 2}.
"""
logs = [
    {"servidor": "Srv-Web", "errores": 5},
    {"servidor": "Srv-DB", "errores": 0},
    {"servidor": "Srv-Web", "errores": 3},
    {"servidor": "Srv-Cache", "errores": 10},
    {"servidor": "Srv-DB", "errores": 2},
    {"servidor": "Srv-Web", "errores": 0},
]

dic = {}

for server in logs:
    nombre = server["servidor"]
    error = server["errores"]

    if error > 0:
        if nombre not in dic:
            dic[nombre] = error
        else:
            dic[nombre] += error

print(dic)

"""Tienes una lista de libros que la gente ha leído. Tu misión es crear un diccionario donde 
la llave sea el género del libro y el valor sea otra lista con los nombres de los libros de ese género.
{"Terror": ["Drácula", "It", "El Resplandor"], "Ciencia Ficción": ["Dune", "Fundación"]}"""
biblioteca = [
    {"titulo": "Drácula", "genero": "Terror"},
    {"titulo": "Dune", "genero": "Ciencia Ficción"},
    {"titulo": "It", "genero": "Terror"},
    {"titulo": "Fundación", "genero": "Ciencia Ficción"},
    {"titulo": "El Resplandor", "genero": "Terror"},
]

libros_por_genero = {}

for libro in biblioteca:
    titulo = libro["titulo"]
    genero = libro["genero"]

    if genero not in libros_por_genero:
        libros_por_genero[genero] = []

    libros_por_genero[genero].append(titulo)

print(libros_por_genero)


ordenes = [
    {
        "cliente": "Luis",
        "ciudad": "San José",
        "items": [
            {"producto": "Teclado", "precio": 50},
            {"producto": "Monitor", "precio": 200},
        ],
    },
    {
        "cliente": "Ana",
        "ciudad": "Heredia",
        "items": [
            {"producto": "Laptop", "precio": 800},
            {"producto": "Teclado", "precio": 50},
        ],
    },
    {
        "cliente": "Diego",
        "ciudad": "San José",
        "items": [
            {"producto": "Mouse", "precio": 25},
            {"producto": "Monitor", "precio": 200},
        ],
    },
    {
        "cliente": "Marta",
        "ciudad": "Alajuela",
        "items": [
            {"producto": "Teclado", "precio": 50},
            {"producto": "Audífonos", "precio": 100},
        ],
    },
]

"""📋 Objetivos del Reporte:
ventas_por_ciudad: Un diccionario donde la llave es la ciudad y el valor es la suma de todos los precios de los productos vendidos en esa ciudad.
clientes_vip: Una lista que contenga solo los nombres de los clientes cuyo gasto total (la suma de sus items) sea estrictamente mayor a 500.
total_teclados: Una variable numérica que cuente cuántas veces aparece el producto "Teclado" en todas las órdenes."""

ventas_por_ciudad = {}
clientes_vip = []
total_clientes = {}
total_teclados = 0

for orden in ordenes:
    ciudad = orden["ciudad"]
    cliente = orden["cliente"]
    gasto_total = 0

    for item in orden["items"]:
        precio = item["precio"]
        producto = item["producto"]

        if producto == "Teclado":
            total_teclados += 1

        if ciudad not in ventas_por_ciudad:
            ventas_por_ciudad[ciudad] = precio
        else:
            ventas_por_ciudad[ciudad] += precio

        gasto_total += precio
    
    if gasto_total > 500:
        clientes_vip.append(cliente)

print(total_clientes)
print(ventas_por_ciudad)
print(clientes_vip)
print(total_teclados)
