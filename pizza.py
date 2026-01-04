def make_pizza(size, *toppings):
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def make_specialty_pizza(size, *toppings):
    print(f"\nMaking a specialty {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

def vegan_pizza(size, *toppings):
    print(f"\nMaking a vegan {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
