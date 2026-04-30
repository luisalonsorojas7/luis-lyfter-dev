"""El Reto: "El Auditor de Compras"
"  manzana:2.5 , PERA:1.5, manzana:2.5, uva:3.0,  Pera:1.5 , MANZANA:2.5  "

Tu Objetivo:
Crea una función llamada generar_ticket(datos_sucios) que devuelva un diccionario donde:
La Clave sea el nombre del producto (en minúsculas y sin espacios).
El Valor sea una lista con dos datos: [cantidad_de_veces, total_dinero_gastado].

Ejemplo de Salida:
{'manzana': [3, 7.5], 'pera': [2, 3.0], 'uva': [1, 3.0]}

Tu "Mapa de Batalla" (Paso a paso):
Separar: Usa .split(",") para obtener cada par de "producto:precio".

Preparar el Diccionario: Crea un diccionario vacío llamado ticket.
Bucle Principal: Recorre la lista de productos sucios.
Limpieza Doble (El truco): * Cada elemento se ve así: "  manzana:2.5 "
Usa .strip() para quitar espacios de los bordes.
Usa .split(":") para separar el nombre del precio.
Normalizar: Asegúrate de que el nombre esté en .lower() y el precio se convierta a float().

Lógica del Diccionario:
Si el producto NO está: Agrégalo con el valor [1, precio].
Si el producto YA está: * Suma 1 a la cantidad (posición 0 de la lista).
Suma el precio al total de dinero (posición 1 de la lista)."""


def generar_ticket(datos_sucios):
    mi_diccionario = {}
    nueva_lista = datos_sucios.split(",")

    for item in nueva_lista:
        if ":" in item:
            partes = item.split(":")
            nombre = partes[0].strip().lower()
            precio = float(partes[1].strip())
        
            if nombre not in mi_diccionario:
                mi_diccionario[nombre] = [1,precio]
            else:
                mi_diccionario[nombre][0] += 1
                mi_diccionario[nombre][1] += precio
                
    return mi_diccionario

print(generar_ticket("  manzana:2.5 , PERA:1.5, manzana:2.5, uva:3.0,  Pera:1.5 , MANZANA:2.5  "))