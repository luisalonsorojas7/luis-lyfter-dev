inventario = {
    "manzana": {"stock": 10, "precio": 2.0},
    "pera": {"stock": 5, "precio": 3.0},
}

ventas = [
    ["manzana", 3],
    ["pera", 10],  # ¡Ojo! No hay suficiente stock
    ["manzana", 7],
    ["uva", 2]# ¡Ojo! Este producto no existe
]


def procesar_ventas(dic_inventario, lista_ventas):
    lista_agotados = []
    total = 0
    cantidad_fallitos = 0 # Importante: fuera del for

    for item in lista_ventas:
        producto = item[0]
        cantidad_vendida = item[1] 
        
        # 1. ¿El producto existe?
        if producto in dic_inventario:
            # 2. ¿Hay suficiente stock?
            if dic_inventario[producto]["stock"] >= cantidad_vendida:
                # Venta exitosa: restamos y sumamos dinero
                dic_inventario[producto]["stock"] -= cantidad_vendida
                total += cantidad_vendida * dic_inventario[producto]["precio"]
                
                # 3. ¿Se agotó con esta venta?
                if dic_inventario[producto]["stock"] == 0:
                    lista_agotados.append(producto)
            else:
                # No alcanza el stock
                cantidad_fallitos += 1
        else:
            # El producto no existe en el inventario
            cantidad_fallitos += 1
            
    return {
        "dinero_total": total,
        "ventas_fallidas": cantidad_fallitos,
        "productos_agotados": lista_agotados
    }

print(procesar_ventas(inventario, ventas))
