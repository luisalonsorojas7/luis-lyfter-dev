'''Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.'''

def say_hello():
    print("Hello my name is Luis!")
    tell_your_age(30)


def tell_your_age(age):
    print(f"I'm {age} years old!")
    

say_hello()