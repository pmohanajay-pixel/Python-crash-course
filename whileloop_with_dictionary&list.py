# Managing users with a while loop and lists
unconfirmed_users=['manish','arun','kumar']
confirmed_users=[]
while unconfirmed_users:
    current_user=unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# Removing all occurrences of a specific item from a list using a while loop
pets=['dog','cat','dog','goldfish','cat','rabbit','cat']
print("\nOriginal list of pets:")
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print("\nList of pets after removing all 'cat':")
print(pets)

# Sorting a list temporarily and permanently
cars=['bmw','audi','toyota','subaru']
print("\nOriginal list of cars:")
print(cars)
cars.sort()
print("Sorted list of cars:")
print(cars)
cars.sort(reverse=True)
print("Reverse sorted list of cars:")
print(cars)


# Collecting survey responses using a dictionary and a while loop
responses={}
polling_active=True
while polling_active:
    name=input("\nWhat is your name? ")
    response=input("Which mountain would you like to climb someday? ")
    responses[name]=response
    repeat=input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower()=='no':
        polling_active=False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}.")

# Using a dictionary to store and display user information
user_info={}
user_info['first_name']='manish'
user_info['last_name']='kumar'
user_info['age']=25
user_info['city']='new york'
print("\nUser Information:")
for key, value in user_info.items():
    print(f"{key.title()}: {value.title() if isinstance(value, str) else value}")
    