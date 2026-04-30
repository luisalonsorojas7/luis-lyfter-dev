'''1. El Convertidor de Años Luz (Básico)Los astronautas necesitan calcular distancias. 
Crea una función que convierta "Años Luz" a "Kilómetros".Nombre: años_luz_a_km(años)
Lógica: 1 año luz son aproximadamente $9.46$ billones de km.Reto:
La función debe recibir los años y retornar el cálculo.

2. Generador de IDs de Tripulación (Strings)Cada astronauta necesita un código único.Nombre: generar_id(nombre, apellido)Lógica: 
Debe tomar la primera letra del nombre y el apellido completo, todo en mayúsculas.Ejemplo: generar_id("Luis", "Perez") debería retornar "LPEREZ".

3. Calculador de Oxígeno (Condicionales + Funciones)Nombre: alerta_oxigeno(nivel_actual)Lógica: * Si el nivel es mayor a 70, 
retorna "Estado Óptimo".Si está entre 30 y 70, retorna "Precaución: Nivel Moderado".
Si es menor a 30, retorna "⚠️ PELIGRO: Nivel Crítico".

4. El "Simulador de Despegue" (Funciones que llaman funciones)Este es el ejercicio de nivel "Expert".
Crea una función llamada chequeo_sistemas(combustible, oxigeno).Dentro de esa función, llama a tu función del ejercicio anterior (alerta_oxigeno).
Reto: La función solo debe imprimir "🚀 DESPEGUE AUTORIZADO" si el combustible es mayor a 80 Y si la función de oxígeno no devuelve un mensaje de "PELIGRO".'''

def años_luz_a_km(annios):
    return annios * 9.46 * 10 ** 12

print(años_luz_a_km(1))

def generar_id(nombre, apellido):
    return nombre[0] + apellido.upper()

print(generar_id("Luis", "Rojas"))

def alerta_oxigeno(nivel_actual):
    if nivel_actual < 30:
        return "Nivel Critico"
    elif nivel_actual >= 30 and nivel_actual <= 70:
        return "Nivel Moderado"
    
    return "Nivel Optimo"

print(alerta_oxigeno(90))


def chequeo_systemas(combustible):
    oxigeno = alerta_oxigeno(45)
    
    if combustible >= 80 and oxigeno == "Nivel Optimo":
        return "Despegue Seguro" 
    
    return "Despegue no autorizado, peligro!"

print(chequeo_systemas(75))