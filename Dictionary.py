superhero_1 = {'name': 'Spider', 'ability': 'Wall-Crawling', 'city': 'New York'}
print(superhero_1 ['name'])
print(superhero_1 ['ability'])

new_ability = 'Super Strength'
superhero_1['ability'] = new_ability
print(superhero_1['ability']) 
print(f'{superhero_1["name"]} has the ability of {superhero_1["ability"]}.')


superhero_2 = {'name': 'Flash', 'ability': 'Super Speed', 'city': 'Central City'}
print(superhero_2['name']) 
print(superhero_2['ability'])
print(f'{superhero_2["name"]} has the ability of {superhero_2["ability"]}.')

superhero_2['speed'] = 'Fastest in the world'
print(superhero_2)

superhero_2['ability'] = 'Time Travel'
print(superhero_2)
print(f'{superhero_2["name"]} has the ability of {superhero_2["ability"]}.')

dinosours = {}
dinosours['1'] = 't-rex'
dinosours['2'] = 'triceratops'
dinosours['3'] = 'flying t-rex'
print(dinosours)

cars = {}
cars['brand'] = 'Ford'
cars['model'] = 'Mustang'
cars['year'] = 1964
print(cars)
print(f"{cars['brand']} {cars['model']} was manufactured in {cars['year']}.")
cars['year'] = 2020
print(f"{cars['brand']} {cars['model']} was manufactured in {cars['year']}.")
print(cars)
