"""
Tienes una lista de películas, cada una con un precio, un horario y una capacidad de asientos.
Tu misión es crear un script que:Tenga una lista de diccionarios con al menos 3 películas.

Permita al usuario elegir una película por su ID.
Pregunte cuántos boletos quiere comprar.Regla de Negocio:
Si hay suficientes asientos: Resta los asientos y muestra el total a pagar.

Si NO hay suficientes asientos: Muestra un mensaje de "Sold Out" o "Capacidad insuficiente".Descuento VIP: Si el usuario compra 4 o más boletos,
aplícale un 10% de descuento al total.


🛠️ ¿Qué vas a refrescar con esto?Búsqueda en Listas: Recorrer la lista para encontrar el ID correcto.
Actualización de Diccionarios: Modificar el valor de "seats".
Matemática en Python: Calcular el total y aplicar el descuento ($Total \times 0.90$).Condicionales: Validar si hay espacio disponible.💡
Tip de "vuelta al código":Recuerda usar una variable "bandera" (como found = False) para avisar
si el ID que puso el usuario no existe en tu lista de películas."""

peliculas = [
    {"id": 1, "name": "Avengers: Endgame", "price": 3500, "seats": 10},
    {"id": 2, "name": "Inside Out 2", "price": 2800, "seats": 5},
    {"id": 3, "name": "The Batman", "price": 3200, "seats": 2},
]
usuario = "admin"
password = "123"
opcion_menu = 4
asientos_extra = 0
asientos_vendidos = 0
codigo_pelicula = 0
costo_total_entrada = 0
cantida_boletos = 0
total_pagar = 0


while True:
    print("\nWelcome to NovaCinemas Plaza Real")
    print("1) Ver cartelera")
    print("2) Comprar boletos")
    print("3) Administración(ADMIN)")
    print("4) Salir\n")

    opcion_menu = int(input("Ingresa la opcion que deseas elegir: \n"))

    if opcion_menu == 4:
        print("Vuelve pronto. Hasta luego!")
        break

    match opcion_menu:
        case 1:
            print("Cartelera Disponible")
            for pelicula in peliculas:
                codigo = pelicula["id"]
                nombre = pelicula["name"]
                espacios = pelicula["seats"]
                print(f"Codigo: {codigo} Pelicula: {nombre}  | Espacios Disponibles: {espacios}")
        case 2:
            print("Bienvenido, ¿para cuál película te gustaría comprar boletos?\n")
            codigo_pelicula = int(input("Ingresa el código de la película:\n"))

            found_movie = False

            for peli in peliculas:
                if codigo_pelicula == peli["id"]:
                    found_movie = True
                    print(f"Has elegido la película: {peli['name']}")
                    cantida_boletos = int(input(f"Cantidad de boletos: "))

                    if cantida_boletos > peli["seats"]:
                        print("No hay suficiente espacio.")
                    elif cantida_boletos <= 0:
                        print("Cantidad no válida.")
                    else:
                        subtotal = cantida_boletos * peli["price"]

                        if cantida_boletos >= 4:
                            total = subtotal * 0.90
                            print("¡Descuento VIP del 10% aplicado!")
                        else:
                            total = subtotal

                        peli["seats"] -= cantida_boletos

                        print(f"\nCompra exitosa!")
                        print(f"Total a pagar: ₡{total}")
                        print(f"Asientos restantes: {peli['seats']}")
                    break 

            if not found_movie:
                print("Código de película no válido.")
                
        case 3:
            usuario = input("Ingresa tu nombre de usuario:\n")
            password = input("Ingresa tu contrasena:\n")
            if usuario == "admin" and password == "123":
                print("\nBienvenido Administrador\n")

            else:
                print("\nCREDENCIALES INCORRECTOS, regresando a menu principal!")
        case _:
            print("Opcion no valida, intenta de nuevo!\n")
