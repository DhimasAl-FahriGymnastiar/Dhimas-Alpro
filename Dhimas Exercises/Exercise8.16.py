#Function
#Anggap nama file function adalah pizza.py
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza:")
    for topping in toppings:
        print(f"- {topping}")
        
#Main code
#import module
import pizza

pizza.make_pizza(16, 'pepperoni', 'cheese')

#import function
from pizza import make_pizza

make_pizza(16, 'pepperoni', 'cheese')

#import function with alias
from pizza import make_pizza as mp

mp(16, 'pepperoni', 'cheese')

#import module with alias
import pizza as p

p.make_pizza(16, 'pepperoni', 'cheese')

#import all function
from pizza import *

make_pizza(16, 'pepperoni', 'cheese')