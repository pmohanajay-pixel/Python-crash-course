#positional arguments
def describe_pet(animal_type, pet_name): # def is used to define a function
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('dog', 'willie')

#multiple function calls
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('dog', 'rummy')
describe_pet('fish', 'red chiclid')
describe_pet('bird', 'african grey')
describe_pet('cat', 'whiskers')

#keyword arguments
def describe_pet(animal_type, pet_name):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='corn', animal_type='snake')
describe_pet(animal_type='lizard', pet_name='lizza')
describe_pet(pet_name='whitie', animal_type='rabbit')

#default values
def describe_pet(pet_name, animal_type='snake'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='greenie')
describe_pet(pet_name='rattle')
describe_pet(pet_name='water snake')
describe_pet(pet_name='python')

#avoiding argument errors
def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('willie')
describe_pet('harry', 'hamster')
describe_pet('coco', 'cat')
describe_pet('buddy')
describe_pet('max', animal_type='rabbit')
describe_pet('shadow', 'horse')
describe_pet('nibbles', 'hamster')
describe_pet() # This will raise an error because pet_name is missing


