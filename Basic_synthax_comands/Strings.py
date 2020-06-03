# Basic comands to define constants and varbles
# of type string and manipulate with strings

first_name = 'Andrija'   # defining a string constant

last_name = 'Milojevic'  # defining a string constant

# disply and print first and last name
print(first_name + last_name)

# display and print first and last name with space
print(first_name + ' ' + last_name)

# print combination of strings
print('Hello ' + first_name + ' ' + last_name)

# charactersitics and manipluation with strings
sentance = 'The name of your cat is Sam'
print(sentance.upper())  # capitlized letters

print(sentance.lower())  # small letters

print(sentance.capitalize())  # first letter capitalized

print(sentance.count('a'))  # counting how many letters of 'a' in a sentance

# defining an input
first_name = input('What is your first name: ')
last_name = input('What is your last name: ')
# print results
print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())

# Different ways to format and print strings

output = f'Hello, {first_name} {last_name}'
print(output)
