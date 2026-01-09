#reading from the files
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)

#to remove extra blank line from output
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)

# or
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

# Relative or absolute file paths
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
print(contents)

#accessing a file lines
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
for line in lines:

    print(line)

#working with a files contents
from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line

print(pi_string)
print(len(pi_string))

#or

from pathlib import Path
path = Path('pi_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))

#large files one million digits
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

print(f"{pi_string[:52]}...")
print(len(pi_string))







