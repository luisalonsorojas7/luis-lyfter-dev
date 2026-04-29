"""Cree una función que imprima el número de mayúsculas y el número de minúsculas en un string.
“I love Nación Sushi” → “There-s 3 upper cases and 13 lower cases”"""

def combine_phrase(phrase):
    new_text = phrase.replace(" ", "")
    phrase_counter(new_text)

    
def phrase_counter(phrase):
    upper_counter = 0
    lower_counter = 0
    for char in phrase:
        if char.isupper():
            upper_counter += 1
        elif char.islower(): 
            lower_counter += 1

    print(f"There are {upper_counter} upper cases and {lower_counter} lower cases")


combine_phrase("I love Nación Sushi")
