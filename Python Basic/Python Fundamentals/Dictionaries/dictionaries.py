course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information['description'])

course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information.get('description'))

course_information = {
	'title': 'Introduction to DBs',
	'description': 'Here we review the basics of SQL Databases',
	'length_in_minutes': 600,
}

print(course_information.get('episodes')) #Get facilita buscar cosas sin certeza de saber si existen o no

#Recorrer un diccionario usando For
europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for country, capital in europe_capitals_by_country.items():
    print(f'{country} : {capital}')

europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for country in europe_capitals_by_country.keys():
    print(country)
    
europe_capitals_by_country = {
	'spain' : 'madrid',
	'france' : 'paris',
	'germany' : 'berlin',
	'norway' : 'oslo',
}

for capital in europe_capitals_by_country.values():
    print(capital)
    
user_data = {
	'full_name': 'John Snow',
	'email': 'j.snow@gmail.com',
}

#Agregar un valor al diccionario
user_data['password'] = 'WinterIsComing2023'
print(user_data)

student_information = {
	'first_name': 'Harry',
	'last_name': 'Potter',
	'age': 17,
}

#Borrar un elemento del diccionario
deleted_item = student_information.pop('last_name')
print(student_information)
print(f'Deleted item: {deleted_item}')


hotel_information = {
    "name": "Continental",
    "stars": 5,
    "rooms": [
        {"number": 101, "floor": 1, "price_night": 250},
        {"number": 202, "floor": 2, "price_night": 350},
        {"number": 305, "floor": 3, "price_night": 550},
    ]
}

totalprice = 0

for room in hotel_information["rooms"]:
    price = room["price_night"]
    totalprice += price

print(totalprice)