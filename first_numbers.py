# Here are two loops that print numbers from 1 to 5 and from 1 to 10:

for value in range (1,6):
    print(value)  

for value in range (1,11):
    print(value)

# You can also create a list of numbers using the range() function:
numbers = list(range(1,11))
print(numbers)

# You can use the range() function to create a list of even numbers:
even_numbers = list(range(2,9,2))
print(even_numbers)

# You can create a list of squares of numbers using a for loop:
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# You can also create the same list of squares using a more concise approach:
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)

# You can find the minimum, maximum, and sum of a list of numbers:
digits = [1,2,3,4,5,6,7,8,9,0]

print(min(digits))

print(max(digits))

print(sum(digits))