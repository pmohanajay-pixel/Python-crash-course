#greeing function

def greet_user():
    print("Hello! Welcome to Cruitbase.")
greet_user()

#personalized greeting function
def greet_user(username):
    print(f"Hello, {username.title()}! Welcome to Cruitbase.")
greet_user('manish')

# Function to display a message
def display_message(message):
    print(message)
display_message("I am learning about functions in Python.")

#positional arguments
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('willie')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet('coco', 'cat')

#multiple function calls
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('willie')
describe_pet('harry', 'hamster')
describe_pet('coco', 'cat')
describe_pet('buddy')
describe_pet('max', animal_type='rabbit')




