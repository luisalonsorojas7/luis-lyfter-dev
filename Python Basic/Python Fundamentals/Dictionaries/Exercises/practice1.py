"""Cree un diccionario que guarde la siguiente información sobre un hotel:
nombre
numero_de_estrellas
habitaciones
El value del key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información:
numero
piso
precio_por_noche
"""
hotel_information = {
    "name": "Continental",
    "stars": 5,
    "rooms": [
        {"number": 101, "floor": 1, "price_night": 250},
        {"number": 202, "floor": 2, "price_night": 350},
        {"number": 305, "floor": 3, "price_night": 550},
    ]
}