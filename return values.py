def name_format(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = name_format('ajay', 'varma')
musician = name_format('raghu', 'varma')
print(musician) 

# making an argument optional
def get_formatted_name(first_name, middle_name, Last_name):
    full_name = f"{first_name} {middle_name} {Last_name}"
    return full_name.title()
musician = get_formatted_name('ajay', 'mohan', 'varma')
print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('ajay', 'varma')
print(musician)

musician = get_formatted_name('ajay', 'mohan', 'varma')
print(musician)

# returning a dictionary
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('ajay', 'varma')
print(musician)

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('ajay', 'varma', age=25)
print(musician)

# using a function with a while loop
def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break
    
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
print(musician)  


