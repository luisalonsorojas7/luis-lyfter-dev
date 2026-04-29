'''El Reto: "El Monitor de Entrenamiento"
" Juan:45, MARIA:60, juan:30, Pedro:90, maria:45 , JUAN:20 "
Tu Objetivo:
Crea una función llamada auditar_gimnasio(datos) que devuelva un diccionario donde:
La Clave sea el nombre del usuario (en minúsculas y sin espacios).
El Valor sea una lista con: [número_de_sesiones, total_minutos_entrenados, promedio_por_sesion].

Ejemplo de Salida para Juan:
Juan apareció 3 veces (45, 30 y 20 min).
Total minutos: 95.
Promedio: 31.66.

Registro: 'juan': [3, 95, 31.66]

💡 Tu "Mapa de Batalla":
Separar: Usa .split(",") para obtener cada "Usuario:Minutos".
Limpiar: Dentro del bucle, separa por : y usa .strip() y .lower().
Convertir: Los minutos deben ser int o float.

Lógica del Diccionario:
Si el usuario es NUEVO: Crea la lista con [1, minutos, minutos] (el promedio al principio es igual a los minutos de la primera sesión).

Si el usuario YA EXISTE:
Suma 1 a las sesiones: dicc[nombre][0] += 1.
Suma los minutos al total: dicc[nombre][1] += minutos.
EL GIRO: Recalcula el promedio y guárdalo en la posición [2].
Fórmula: promedio = total_minutos / sesiones.'''

def auditar_gimnasio(datos):
    diccionario = {}
    nueva_lista = datos.split(",")
    contador = 0
    
    for item in nueva_lista:
        if ":" in item:
            partes = item.split(":")
            usuario = partes[0].strip().lower()
            minutos = int(partes[1].strip().lower())

            if usuario not in diccionario:
                promedio = contador / minutos          
                diccionario[usuario] = [1, minutos, float(promedio)]
            else:
                contador += 1
                diccionario[usuario][0] = contador
                diccionario[usuario][1] += minutos    
                
                sesiones = diccionario[usuario][0]
                total = diccionario[usuario][1]
                diccionario[2] = total / sesiones 
                
    return diccionario

print(auditar_gimnasio(" Juan:45, MARIA:60, juan:30, Pedro:90, maria:45 , JUAN:20 "))