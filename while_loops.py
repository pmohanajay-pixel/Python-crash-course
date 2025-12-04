#modulo operator example with while loop
number = 10
while number >= 0:
    if number % 2 == 0:
        print("The number " + str(number) + " is even.")
    else:
        print("The number " + str(number) + " is odd.")
    number -= 1
# This code counts down from 10 to 0 and checks if each number is even or odd using the modulo operator.

number = input("Enter a positive integer: ")
number = int(number)
while number >= 0:
    print(number)
    number -= 1

# parrot example with while loop
promt = "Enter a message and I will repeat it back to you: "
message = input(promt)
while message != "quit":
    print(message)
    message = input(promt)

# using a flag with while loop
promt = "Enter a message and I will repeat it back to you: "
promt += "\n(Enter 'quit' to end the program.) "
active = True
while active:
    message = input(promt)
    if message == "quit":
        active = False
    else:
        print(message)

# using break to exit a loop
promt = "Enter a city name u want to visit: "
promt += "\n(Enter 'quit' to end the program.) "
while True:
    city = input(promt)
    if city == "quit":
        break
    else:
        print(f"I'd love to visit {city.title()}!")
