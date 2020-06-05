import example_module

# Single-line comment

"""
	Multi-line comment!
	Python Style guide at: https://www.python.org/dev/peps/pep-0008/
"""

print("Whoa, it just works??")
print(example_module.test_method())
print("\n")

print(example_module.SOME_CONSTANT)
example_module.SOME_CONSTANT = 34
print(example_module.SOME_CONSTANT)
print("But.. it's actually not a constant. Just don't go changing it like this..!")
print("\n")

name = input("What's your name? ")
print("You entered " + name + "!")

nameLength = len(name)
for i in range(nameLength):
	print("name[" + str(i) + "] = " + name[i])
print("\n")

import os

file_name = input("What file would you like to check? ")
while not os.path.exists(file_name):
	print(file_name + " does not exist.")
	file_name = input("What file would you like to check? ")
print("\n")

assert os.path.exists(file_name)
print("Opening file...")

with open(file_name) as file:
	file_data = file.read()
	print("\n\n\n")
	print(file_data)
	print("\n\n\n")

