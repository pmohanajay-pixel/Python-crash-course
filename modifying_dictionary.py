# Modifying a dictionary by adding a new key-value pair
transport_1 = {'vehicle': 'car', 'color': 'red', 'brand': 'Toyota'}
print(f'I have a {transport_1["color"]} {transport_1["brand"]} {transport_1["vehicle"]}')
transport_1['year'] = 2020
print(transport_1)
transport_1['color'] = 'blue'
print(transport_1)
print(f'I have a {transport_1["color"]} {transport_1["brand"]} {transport_1["vehicle"]} manufactured in {transport_1["year"]}.')

# Modifying a dictionary by updating an existing key-value pair
transport_2 = {'vehicle': 'bike', 'color': 'black', 'brand': 'Yamaha'}
print(f'I have a {transport_2["color"]} {transport_2["brand"]} {transport_2["vehicle"]}')
transport_2['color'] = 'green'
print(transport_2)
print(f'I have a {transport_2["color"]} {transport_2["brand"]} {transport_2["vehicle"]}.')

#lets play a small racing game
racing_game = {'player1': 'mani', 'player2': 'ajay', 'player3': 'vineeth'}
print(f'The players in the racing game are: {racing_game["player1"]} , {racing_game["player2"]} , {racing_game["player3"]}.')
racing_game['player4'] = 'rahul'
print(racing_game)
if racing_game['player2'] == 'ajay':
    racing_game['player2'] = 'ajay_the_speedster'
elif racing_game['player2'] != 'ajay':
    racing_game['player2'] = 'ajay_the_slow'
else:
    racing_game['player2'] = 'ajay'
print(racing_game)
print(f'The players in the racing game are now: {racing_game["player1"]} , {racing_game["player2"]} , {racing_game["player3"]} , {racing_game["player4"]}.')

players_scores = {'mani': 50, 'ajay': 70, 'vineeth': 60}
print(f"Initial scores: {players_scores}")
players_scores['mani'] += 10
players_scores['ajay'] += 20
players_scores['vineeth'] += 15
print(f"Updated scores: {players_scores}")

if players_scores['mani'] > players_scores['ajay']:
    print("Mani is leading the game!")
elif players_scores['mani'] < players_scores['ajay']:
    print("Ajay is leading the game!")
else:
    print("It's a tie between Mani and Ajay!")    