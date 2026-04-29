nombre_academia = "Lyfter"

estudiantes = [
    {"nombre": "Luis", "notas": [100, 90, 95]},
    {"nombre": "Maria", "notas": [80, 70, 90]},
    {"nombre": "Jose", "notas": [50, 40, 60]},
]


# 1. LA CALCULADORA (Solo recibe la lista de números)
def calcularpromedio(lista_notas):
    suma_notas = 0
    for nota in lista_notas:  # 'nota' irá valiendo 100, luego 90, luego 95...
        suma_notas += nota  # Sumamos el número directamente

    return suma_notas / len(lista_notas)


# 2. LA MAESTRA (Abre los diccionarios)
def generar_reporte(lista_de_estudiantes):
    for alumno in lista_de_estudiantes:
        # Sacamos la lista de números del diccionario
        solo_las_notas = alumno["notas"]

        # Se la enviamos a la calculadora
        promedio = calcularpromedio(solo_las_notas)

        print(f"Estudiante: {alumno['nombre']} - Promedio: {promedio:.2f}")


# 3. EJECUCIÓN
generar_reporte(estudiantes)
# NOTA: No llames a calcularpromedio(estudiantes) al final,
# porque 'estudiantes' es una lista de diccionarios y la función espera números.


productos = [
    {"nombre": "Mouse Gamer", "precio": 25, "cantidad": 10},
    {"nombre": "Teclado Mecánico", "precio": 80, "cantidad": 0},  # Agotado
    {"nombre": "Monitor 4K", "precio": 300, "cantidad": 5},
    {"nombre": "Cable HDMI", "precio": 10, "cantidad": 0},  # Agotado
]


def calcular_valor_total(precio, cantidad):
    return precio * cantidad


def esta_disponible(cantidad):
    if cantidad > 0:
        return True
    elif cantidad == 0:
        return False
    
def generar_auditoria(lista_productos):
    for producto in lista_productos:
        precio = producto["precio"]
        cantidad = producto["cantidad"]
        nombre = producto["nombre"]
        
        if esta_disponible(cantidad):
            print(f"{nombre}: Hay Stock. Valor total: {calcular_valor_total(precio, cantidad)}")
        else:
            print(f"{nombre} AGOTADO. Pedir mas!")    
            

generar_auditoria(productos)

#Sistema de cine
nombre = "Nova Cinemas Costa Rica"

reservas = [
    {"cliente": "Luisa", "cantidad_entradas": 3, "precio_unitario": 3500},
    {"cliente": "Pedro", "cantidad_entradas": 1, "precio_unitario": 3500},
    {"cliente": "Ana", "cantidad_entradas": 5, "precio_unitario": 3500}
]

def aplicar_descuento(total_bruto, cantidad):
    if cantidad > 3:
        return total_bruto - 1000
    else:
        return total_bruto
    
def calcular_subtotal(cantidad, precio):
    return cantidad * precio

def imprimir_factura(reserva):
    for item in reserva:
        cliente = item["cliente"]
        cantidad_entradas = item["cantidad_entradas"]
        precio = item["precio_unitario"]

        aplicar_descuento(calcular_subtotal(cantidad_entradas, precio), cantidad_entradas)
        
        print(f"{nombre} | Cliente: {cliente} | Total pagar: {aplicar_descuento(calcular_subtotal(cantidad_entradas, precio), cantidad_entradas)}")
        
imprimir_factura(reservas)

#Sistema de gestion de pacientes
pacientes = [
    {"nombre": "Carlos", "temperatura": 36.5},
    {"nombre": "Lucía", "temperatura": 39.2},
    {"nombre": "Esteban", "temperatura": 38.5},
    {"nombre": "Mariana", "temperatura": 37.0}
]

def evaluar_prioridad(temp):
    if temp >= 38.0:
        return "URGENTE"
    else:
        return "Normal"
    
def gestionar_hospital(lista_pacientes):
    conteo_atendidos = 0
    
    for paciente in lista_pacientes:
        nombre = paciente["nombre"]
        temperatura = paciente["temperatura"]
        
        if evaluar_prioridad(temperatura) == "URGENTE":
            conteo_atendidos+=1
            print(f"{nombre}: ¡Prioridad URGENTE! Sala 1.")
        else:
            conteo_atendidos+=1
            print(f"{nombre}: ¡Prioridad Estable. Sala 2.") 
    
    print(f"--- Total de pacientes procesados: {conteo_atendidos} ---")    

gestionar_hospital(pacientes)

