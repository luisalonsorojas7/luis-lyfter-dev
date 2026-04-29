'''Tienes una lista de transacciones que entraron al sistema. Algunas son "ingresos" (dinero que entra) y 
otras son "egresos" (dinero que sale). Además, cada transacción tiene una categoría.

Tu misión es generar un reporte que diga:
Balance por Categoría: Un diccionario que sume los ingresos y reste los egresos para cada categoría (Ej: {"Comida": -50, "Salario": 2000}).
Alertas de Fraude: Una lista con los id de las transacciones que tengan un monto mayor a 5000, sin importar si es ingreso o egreso.
Total Neto: Una variable con el dinero total que quedó al final (Suma de todo lo que entró menos todo lo que salió).

Tu misión es generar un reporte que diga:

Balance por Categoría: Un diccionario que sume los ingresos y reste los egresos para cada categoría (Ej: {"Comida": -50, "Salario": 2000}).
Alertas de Fraude: Una lista con los id de las transacciones que tengan un monto mayor a 5000, sin importar si es ingreso o egreso.
Total Neto: Una variable con el dinero total que quedó al final (Suma de todo lo que entró menos todo lo que salió).'''

transacciones = [
    {"id": "TX001", "tipo": "ingreso", "monto": 1200, "cat": "Salario"},
    {"id": "TX002", "tipo": "egreso", "monto": 50, "cat": "Comida"},
    {"id": "TX003", "tipo": "egreso", "monto": 80, "cat": "Transporte"},
    {"id": "TX004", "tipo": "ingreso", "monto": 6000, "cat": "Premio"},
    {"id": "TX005", "tipo": "egreso", "monto": 150, "cat": "Comida"},
    {"id": "TX006", "tipo": "egreso", "monto": 5500, "cat": "Inversión"}
]

balance_categorias = {}
alertas_fraude = []
total_neto = 0
total = 0

for transaccion in transacciones:
    tipo = transaccion["tipo"]
    monto = transaccion["monto"]
    categoria = transaccion["cat"]
    id_code = transaccion["id"]
    
    if categoria not in balance_categorias:
            balance_categorias[categoria] = 0
    
    if tipo == "ingreso":
        balance_categorias[categoria] += monto
        total_neto+=monto
    else:
        balance_categorias[categoria] -= monto
        total_neto -= monto
    
    if monto > 5000:
        alertas_fraude.append(id_code)

for valor in balance_categorias.values():   
    if valor > 0:
        total += valor

print(total)
print(alertas_fraude)