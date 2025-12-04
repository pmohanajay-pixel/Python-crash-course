message = input("Please enter a message: ")
print("You entered:", message)

# This code prompts the user to enter a message and then prints that message back to the console.
name = input("What is your name? ")
print("Hello, " + name + "!")
age = input("How old are you? ")
print("You are " + age + " years old.")
favorite_color = input("What is your favorite color? ")
print("Your favorite color is " + favorite_color + ".")
hobbies = input("What are your hobbies? ")
print("Your hobbies are: " + hobbies + ".")

# The code uses the input() function to gather user input and then displays it using print().

city = input("Which city do you live in? ")
print("You live in " + city + ".")
country = input("Which country is that in? ")
print("You live in " + country + ".")
occupation = input("What is your occupation? ")
print("You work as a " + occupation + ".")
favorite_food = input("What is your favorite food? ")
print("Your favorite food is " + favorite_food + ".")
print("Thank you for sharing your information!")

# This code collects various pieces of information from the user and acknowledges their input.
height = input("What is your height? ")
height = int(height)
if height >= 5:
    print("You are tall!")
else:
    print("You are not that tall.")
weight = input("What is your weight? ")
weight = int(weight)
if weight >= 150:
    print("You have a healthy weight!")
else:
    print("You might want to consider gaining some weight.")
print("Your height is {} and your weight is {}.".format(height, weight))

# The code gathers personal information and provides feedback based on the input values.
number = input("enter a number, and i will tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("The number " + str(number) + " is even.")
else:
    print("The number " + str(number) + " is odd.")

