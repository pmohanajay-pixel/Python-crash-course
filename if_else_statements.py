age = 21
if age >= 19:
    print("you can smoke")

# example of if-else    
age = 19
if age >= 23:
    print("you are eligible for marriage")
    print("have a great life")
else:
    print("you are not eligible for marriage")

ajay_age = 25
if ajay_age >= 30:
    print("ajay is eligible for marriage")
else:
    print("ajay is not eligible for marriage")

# example of if-elif-else
mani_age = 28
if mani_age >= 30:
    print("your entry fee is $45")
elif mani_age >= 20:
    print("your entry fee is $25")
else:
    print("your entry fee is $15")

# example of if-elif-else using multiple elif blocks
age = 65
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 25
elif age < 65:
    ticket_price = 40
else:
    ticket_price = 55
    print(f"Your ticket price is ${ticket_price}.")

# ommitting the else block
age = 45
if age < 4:
    ticket_price = 0
elif age < 18:
    ticket_price = 25
elif age < 65:
    ticket_price = 40
elif age >= 65:
    ticket_price = 55
print(f"Your ticket price is ${ticket_price}.")

# checking multiple conditions
requested_beverages = ['cola', 'juice', 'water']
if 'cola' in requested_beverages:
    print("Adding cola.")
if 'juice' in requested_beverages:
    print("Adding juice.")
if 'water' in requested_beverages:
    print("Adding water.")
print("\nFinished preparing your beverages!")

if 'tea' in requested_beverages:
    print("Adding tea.")
elif 'coffee' in requested_beverages:
    print("Adding coffee.")
else:
    print("Adding water.") 

# checking for special items
requested_pizzas = ['mushrooms', 'green peppers', 'extra cheese']
for requested_pizza in requested_pizzas:
    print(f"Adding {requested_pizza}.") 
    if requested_pizza == 'green peppers':
        print("Sorry, we are out of green peppers right now.")