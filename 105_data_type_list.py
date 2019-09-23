#List
# list keep object in order of index
# it's defined by []

# example of a list  - index
# list_name       = [    0    ,    1   ,    2   ,   3    ]
crazy_x_partners = ['Carolina', 'JSON', 'Arthur', 'Lana!']

#print and show type (Read ALL)
print(crazy_x_partners)
print(type(crazy_x_partners))

#Get a perticular record out (Read one)
#Lists are organized with index
print(crazy_x_partners[0]) # use the index inside square brackets [i]
print(type(crazy_x_partners[0]))


#How dpo I print the last one?
print(crazy_x_partners[-1])

# Maybe we want to change a record in a specific index?
    # Re-assign an index
print(crazy_x_partners[3])
crazy_x_partners[3] = 'LANAA!! (...) DANGER ZONE!!!'
print(crazy_x_partners[3])

#Add more people to the list ( Create one) - append()
print(crazy_x_partners)
crazy_x_partners.append('Cyral Figus')
print(crazy_x_partners)

#inser in index specific location
crazy_x_partners.insert(3, 'Malorie')
print(crazy_x_partners)
crazy_x_partners.insert(3, 'Malorie')
print(crazy_x_partners)


#Remove someone from the list (Destroy one)
crazy_x_partners.remove('JSON')
print(crazy_x_partners)
crazy_x_partners.remove('Malorie') # Removes based on object
print(crazy_x_partners)

#Remove using index
crazy_x_partners.pop() # Removes last entry
print(crazy_x_partners)

crazy_x_partners.pop(1) # Removes based on index
print(crazy_x_partners)


# Mixed data and List
 # Lists can have may data types
hybrid_list = ['this is a string', 12, 66, 'hello', [1,2,3], [1,2,2]]

# What happen when you have 3500000000 records? good question
 # Loops and other data formats

# Tuples --> Immutable lists
# They do not change
# syntax
# my_tuple = ()
# tuples are defined by (), not using square brackets
my_tuple = (2, 'hello', 22, 'more value')
print(my_tuple)
print(type(my_tuple))


