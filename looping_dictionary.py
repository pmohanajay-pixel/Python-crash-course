user_1 = {
    'username': 'mani123',
    'first_name': 'Mani',
    'last_name': 'Kumar',
}
for key, value in user_1.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favourite_languages = {
    'mani': 'python',
    'ajay': 'java',
    'vineeth': 'c++',
    'rahul': 'javascript',
    'ben': 'ruby',
}   
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}.")
for name in favourite_languages.keys():
    print(name.title())

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")
    
friends = ['ajay', 'ben']
for name in favourite_languages.keys():
    print(name.title())
    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# checking if a key is not in the dictionary
if 'vineeth' not in favourite_languages.keys():
    print("Vineeth, please take our poll!")

# looping through all values in the dictionary
print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

# looping through all unique values in the dictionary
print("The following languages have been mentioned:")
for language in set(favourite_languages.values()):
    print(language.title()) 

#nesting
users = {
    'mani': {
        'first_name': 'Mani',
        'last_name': 'Kumar',
        'location': 'India',
    },
    'ajay': {
        'first_name': 'Ajay',
        'last_name': 'Sharma',
        'location': 'USA',
    },
    'vineeth': {
        'first_name': 'Vineeth',
        'last_name': 'Reddy',
        'location': 'UK',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# nesting a list in a dictionary
favorite_languages = {
    'mani': ['python', 'java'],
    'ajay': ['c++'],
    'vineeth': ['ruby', 'javascript'],
}
for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favourite languages are:")
    for language in languages:
        print(f"\t{language.title()}")

# nesting a dictionary in a dictionary
users = {
    'mani': {
        'first_name': 'Mani',
        'last_name': 'Kumar',
        'location': 'India',
    },
    'ajay': {
        'first_name': 'Ajay',
        'last_name': 'Sharma',
        'location': 'USA',
    },
    'vineeth': {
        'first_name': 'Vineeth',
        'last_name': 'Reddy',
        'location': 'UK',
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

