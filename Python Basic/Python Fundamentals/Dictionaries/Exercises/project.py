"""1. Sistema de Control de Inventario (E-commerce) 📦
Este es un clásico. En lugar de tareas, manejas productos.
Estructura del Diccionario: {"ID": 1, "Nombre": "Teclado Mechanical", "Stock": 15, "Precio": 45.99}.
Lo nuevo que practicas: Lógica matemática.

Función especial: Opción de "Realizar Venta". El usuario ingresa el ID y la cantidad, y tu programa debe restar esa cantidad del Stock.
Alerta: Si el stock llega a menos de 3, mostrar un mensaje: "⚠️ ¡Reabastecer producto X!".
"""

product_list = []
menu_options = 0
counter = 0

while True:
    print("E-comerce - Stock Control")
    print("Menu Options.")
    print("1. Add products.")
    print("2. Make a sale.")
    print("3. Show inventory.")
    print("4. Exit program.")

    menu_options = int(input("Please select an option: \n"))

    if menu_options == 4:
        print("Closing program. \n")
        break

    match menu_options:
        case 1:
            name = input("Please enter the product name:\n")
            stock = int(input(f"How many {name} would you like to add?\n"))
            price = float(input("Please enter the price:\n"))
            counter += 1
            product = {"id": counter, "name": name, "stock": stock, "price": price}
            product_list.append(product)
            print("\nProduct added to inventory\n")
        case 2:
            product_code = int(
                input("Please enter the code product you want to sell:\n")
            )

            for product in product_list:
                updated_stock = product["stock"]
                if product["id"] == product_code:
                    sell = int(input("How many items do you need?\n"))
                    if sell <= 0 or sell > product["stock"]:
                        print(
                            "Invalid number, you cant sell that quantity. Exceeding the stock or number is 0\n"
                        )
                    else:
                        updated_stock -= sell
                        product["stock"] = updated_stock
                        print("\nSale completed. Inventory was succesfully updated\n")
        case 3:
            print("\nInventory:\n")

            if not product_list:
                print("\nInventory is Empty")
            else:
                print(product_list)
        case _:
            print("\nInvalid option\n")
