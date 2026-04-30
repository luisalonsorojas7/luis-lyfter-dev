products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]

'''Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría.'''
total_category = {}
for product in products:
    category = product["category"]
    price = product["price"]
    
    if category not in total_category:
        total_category[category] = price
    else:
        total_category[category] += price

print(total_category)