'''Por ser el primero, estará relativamente sencillo. 
Vamos a crear un programa que sume los dígitos de un número entero no negativo. 
Por ejemplo, la suma de los dígitos del 3433 es 13.
Para darle un poco más de emoción, el programa no se limitará a escribir 
el resultado de la suma, sino que también escribirá todos los sumandos utilizados:
3 + 4 + 3 + 3 = 13.
Quedamos atentos a sus respuestas 🧠'''

def reto_suma_numeros(numero):
        total = 0   
        if int(numero) <= 0:
            return "Numero no valido"
        else:
            for num in numero:
                total += int(num)
        resultado = " + ".join(numero)
        
        return resultado + " = " + str(total) 

print(reto_suma_numeros("3433"))