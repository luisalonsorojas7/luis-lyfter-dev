"""1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
Ejemplos:
first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"] ->
Hay casos
en los
que la
iteracion por
indice es
muy util"""
first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
second_list = ["casos", "los", "la", "por", "es", "util"]

for element in range(len(first_list)):
    combined_lists = first_list[element] + " " + second_list[element]
    print(combined_lists)