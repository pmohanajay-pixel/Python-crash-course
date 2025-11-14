players = ['mani', 'vineeth', 'ajay', 'rahul']
print("Here are the first three players on my team:")
print(players[0:2])
print(players[1:3])
print(players[:3])

print(players[-2:])
print("Here are the last three players on my team:")

for player in players[-3:]:
    print(player.title())

# copying a list

Ajay_fav_Foods = ['biryani', 'chicken', 'mutton', 'fish']
my_fav_Foods = Ajay_fav_Foods[:]
print("My favorite foods are:")
print(my_fav_Foods)

Ajay_fav_Foods.append('ice-cream')
my_fav_Foods.append('burger')

print("\nAjay's favorite foods are:")
print(Ajay_fav_Foods)
print("\nMy favorite foods are:")
print(my_fav_Foods)

my_fav_Foods.append('pasta')
my_fav_Foods.append('salad')

Ajay_fav_Foods = my_fav_Foods

print("\nAjay's favorite foods are now:")
print(Ajay_fav_Foods)

print("\nMy favorite foods are now:")
print(my_fav_Foods) 

# tuples

dimensions = (200, 50)
print("Original dimensions:") 

print(dimensions[0])

print(dimensions[1])

dimensions = (400, 100)
print("\nModified dimensions:")





