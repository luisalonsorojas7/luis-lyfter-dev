'''Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. 
Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. 
Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”.
Ejemplos:
1040 → Mayor
140 → 460
600 → Igual
599 → 1'''
ten_minutes_to_secs = 600
seconds = int(input("Please enter the number of seconds that you want to calculate: \n"))
seconds_remaining = 0

if seconds == ten_minutes_to_secs:
    print("Equal")
elif seconds > ten_minutes_to_secs:
    print("Greater")
else:
    seconds_remaining = ten_minutes_to_secs - seconds
    print(f"Remaining seconds to reach 10 minutes: {seconds_remaining}")