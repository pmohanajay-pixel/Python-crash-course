shark_1={ 'name' : 'hammerhead', 'age' : 12, 'weight' : 450, 'length' : 14 }
shark_2={ 'name' : 'great white', 'age' : 15, 'weight' : 2200, 'length' : 20 }
shark_3={ 'name' : 'tiger', 'age' : 10, 'weight' : 1400, 'length' : 16 }
shark_4={ 'name' : 'bull', 'age' : 8, 'weight' : 1200, 'length' : 11 }
shark_5={ 'name' : 'nurse', 'age' : 5, 'weight' : 400, 'length' : 9 }
shark_6={ 'name' : 'whale', 'age' : 20, 'weight' : 3000, 'length' : 25 }

shark_list = [shark_1, shark_2, shark_3, shark_4, shark_5, shark_6]
for shark in shark_list:
    print(f"The {shark['name']} shark is {shark['age']} years old, weighs {shark['weight']} pounds, and is {shark['length']} feet long.")

# This above code defines six dictionaries, each representing a different species of shark with attributes such as name, age, weight, and length.

sharks = []
for shark in range(6):
    name = input("Enter the shark's name: ")
    age = int(input("Enter the shark's age: "))
    weight = int(input("Enter the shark's weight in pounds: "))
    length = int(input("Enter the shark's length in feet: "))
    shark_dict = {'name': name, 'age': age, 'weight': weight, 'length': length}
    sharks.append(shark_dict)

# example 2
aliens = []
for alien_number in range(10):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
        
for alien in aliens[:5]:
    print(alien)    


