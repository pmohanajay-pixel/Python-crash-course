favourite_color = {
    'raghu': 'blue',
    'vineeth': 'black',
    'ben': 'red'
    }
print(f"Raghu's favourite color is {favourite_color['raghu'].title()}.")
print(f"Vineeth's favourite color is {favourite_color['vineeth'].title()}.")
print(f"Ben's favourite color is {favourite_color['ben'].title()}.")

color = favourite_color['raghu']
print(f"Raghu's favourite color is {color.title()}.")

favourite_color['raghu'] = 'green'
print(f"Raghu's favourite color is now {favourite_color['raghu'].title()}.")