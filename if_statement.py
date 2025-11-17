cars = ['masada', 'toyota', 'subaru', 'honda']
for car in cars:
    if car == 'subaru':
        print(car.upper())
    else:
        print(car.title())

car = 'audi'
car == 'audi'
print(car == 'audi')

print(car == 'bmw')

print(car == 'Audi')

print(car.lower() == 'audi')

favorite_fruit = 'mango'
if favorite_fruit == 'mango':
    print("You really like mango!")

if favorite_fruit != 'banana':
    print("You really don't like banana!")

number = 10
if number > 15:
    print("The number is greater than 5.")
if number < 15:
    print("The number is less than 15.")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")  
if 'tomatoes' not in requested_toppings:
    print("Sorry, we don't have tomatoes.") 

print('mushrooms' in requested_toppings)

fruits = ['mango', 'banana', 'orange']
fruit = 'banana'
if fruit in fruits:
    print('you like ' + fruit)

    