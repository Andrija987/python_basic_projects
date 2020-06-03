# Defining and executing simple 'for loops'

# simple for loop that displays the names from the list
# we defined
for name in ['Andrija', 'Ben', 'Marck']:
    print(name)

# simple disply of constant that is iterable
# over certain range
for i in range(0, 10):
    print(i)

# how to store values that you iterate?
simple_variable = []  # define as empy list
for i in range(0, 20):
    simple_variable.append(10)
print(simple_variable)

# another way to do it would be
simple_variable2 = [10 for i in range(0, 20)]
print(simple_variable2)


# Defining and executing simple 'while loope'
names = ['John', 'Wiliam', 'Dolores']
indx = 0
while indx < len(names):
    print(names[indx])  # print elements
    indx = indx + 1  # add one to indx
