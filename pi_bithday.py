#To Check your birthday contained in pi
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()11

print(f"{pi_string[:52]}...")
print(len(pi_string))

for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday in the form of mmddyy: ")
if birthday in pi_string: 
    print("your birthday appears in the first million digits of pi!")
else:
     print("your birthday does not appears in the first million digits of pi.")

