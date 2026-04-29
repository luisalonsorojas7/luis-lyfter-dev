'''11.Convertidor de unidades de temperatura Pida al usuario ingresar una temperatura en Celsius
Conviértala a Fahrenheit y Kelvin
Muestre los tres valores
Ejemplo:
"Ingrese temperatura en Celsius:"25
Salida:
Fahrenheit:77.0
Kelvin:298.15'''

celsius_temperature = float(input("Please enter the temperature (Celsius) you would like to convert: \n"))
farenheit = (celsius_temperature * 1.8) + 32
kelvin = celsius_temperature + 273.15

print(f"Celsius: {celsius_temperature}")
print(f"Fahrenheit: {farenheit}")
print(f"Kelvin: {kelvin}")
