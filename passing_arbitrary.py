# Using *args to pass an arbitrary number of arguments to a function
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('tomato')
make_pizza('onions')
make_pizza('chicken')
make_pizza('cheese')
make_pizza('bell peppers')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

#including a size parameter
def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(16, 'pepperoni')
make_pizza(10, 'chicken')
make_pizza(14, 'chicken', 'onions', 'peppers')

# Using **kwargs to pass an arbitrary number of keyword arguments to a function
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('muvva', 'yeshwanth',
                             location='india',
                             field='software engineering',
                             hobby='reading')
print(user_profile)
user_profile2 = build_profile('mani', 'kumar',
                              location='usa',
                              field='data science',
                              hobby='traveling')

#importing a entire module from "pizza.py file".
import pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
pizza.make_pizza(10, 'chicken')
pizza.make_pizza(14, 'chicken', 'onions', 'peppers')
pizza.make_pizza(18, 'sausage', 'bacon', 'extra cheese', 'jalapenos')

import pizza
pizza.make_specialty_pizza(16, 'artichokes', 'sun-dried tomatoes', 'feta cheese')
pizza.make_specialty_pizza(12, 'roasted red peppers', 'spinach', 'goat cheese', 'olives')
pizza.make_specialty_pizza(14, 'caramelized onions', 'tomatoes',  'cheese', 'pepper')

import pizza
pizza.vegan_pizza(16, 'vegan cheese', 'mushrooms', 'spinach', 'olives')
pizza.vegan_pizza(12, 'tofu', 'bell peppers', 'onions', 'tomatoes')

# Importing specific functions from a module
from pizza import make_pizza, make_specialty_pizza
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')    
make_specialty_pizza(12, 'roasted red peppers', 'spinach', 'goat cheese', 'olives')
make_specialty_pizza(14, 'BBq Chicken', 'tomatoes',  'cheese', 'pepper')

from pizza import vegan_pizza
vegan_pizza(16, 'vegan cheese', 'mushrooms', 'spinach', 'olives')
vegan_pizza(12, 'cucumber', 'bell peppers', 'onions', 'tomatoes')

# Using an alias for a function
from pizza import make_pizza as mp
mp(16, 'shrimp', 'garlic', 'extra cheese')

from pizza import make_specialty_pizza as msp
msp(14, 'chicken', 'onions', 'parmesan cheese')

from pizza import vegan_pizza as vp
vp(18, 'onions', 'spinach', 'mushrooms')

# Using an alias for a module
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_specialty_pizza(12, 'roasted red peppers', 'spinach', 'goat cheese', 'olives')
p.vegan_pizza(16, 'vegan cheese', 'mushrooms', 'spinach', 'olives')
p.make_pizza(14, 'BBq Chicken', 'tomatoes',  'cheese', 'pepper')
p.make_specialty_pizza(14, 'chicken', 'onions', 'parmesan cheese')
p.vegan_pizza(18, 'onions', 'spinach', 'mushrooms')

# Importing all functions from a module
from pizza import *
make_pizza(16, 'pepperoni')
make_specialty_pizza(12, 'roasted red peppers', 'spinach', 'goat cheese', 'olives')
vegan_pizza(16, 'vegan cheese', 'mushrooms', 'spinach', 'olives')
make_pizza(14, 'BBq Chicken', 'tomatoes',  'cheese', 'pepper')
make_specialty_pizza(14, 'chicken', 'onions', 'parmesan cheese')
vegan_pizza(18, 'onions', 'spinach', 'mushrooms')


