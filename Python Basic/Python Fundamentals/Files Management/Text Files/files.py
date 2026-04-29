#Sintaxis basica para abrir un archivo, r es read modo lectura
with open('quijote.txt', 'r') as file:
    content = file.read()

#El método read() toma todo el texto dentro del archivo y lo devuelve como una única cadena de texto (string). 
def read_complete_file(path):
    # Usamos 'with' para un manejo seguro del archivo y asegurarnos que el file se cierre
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)

read_complete_file('quijote.txt')

#Cuando un archivo es extenso, leerlo todo de una vez puede consumir demasiada memoria. 
# La función readlines() permite leer el archivo completo pero devuelve una lista, donde 
# cada elemento es una línea del archivo. Esto nos facilita iterar sobre el texto, procesando línea por línea.
def read_file_by_lines(path):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # Iteramos sobre la lista de líneas obtenida
        for number, line in enumerate(lines, start=1):
            # Usamos strip() para remover los saltos de línea y limpiar espacios
            print(f"Line {number}: {line.strip()}")

read_file_by_lines('quijote.txt')


#Sobreescribiendo el archivo usando modo de access write ´w´
def write_new_file(path, text):
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)

new_text = "Capítulo II. Que trata de la primera salida que de su tierra hizo el ingenioso Don Quijote."

write_new_file('quijote_capitulo2.txt', new_text)

#modo de adicion o append ´a´
def append_to_file(path, extra_text):
    with open(path, 'a', encoding='utf-8') as file:
        # Añadimos un salto de línea antes del nuevo texto para no pegarlo al anterior
        file.write("\\n" + extra_text)

additional_text = "Hechas, pues, estas prevenciones, no quiso aguardar más tiempo a poner en efeto su pensamiento..."

append_to_file('quijote_capitulo2.txt', additional_text)

#Usando el encodigin utf-8 para poder ver bien los caracteres especiales
def save_secure_text(path, text):
    # Agregamos encoding='utf-8' para manejar tildes de manera correcta
    with open(path, 'w', encoding='utf-8') as file:
        file.write(text)

text_with_accents = "En resolución, él se enfrascó tanto en su letura, que se le pasaban las noches leyendo de claro en claro, y los días de turbio en turbio."

save_secure_text('quijote_notas.txt', text_with_accents)
