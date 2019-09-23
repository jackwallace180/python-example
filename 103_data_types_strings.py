# String
# these are a list of characters put together
# defined by '' or ""

# my_string = 'Amazing Grilled Fish'
# print(type(my_string))
# # you can print it
# print(my_string)

# Join of strings - concatenation
first_name = 'Boris'
last_name = 'Becker'
print(first_name[0]) # sting IS a list of characters. therefore behaves like a list
# concatenating 3 strings
full_name = first_name + ' ' + last_name
print(full_name)
print('string', 14)

#Interpolation
name = 'Rachel'
welcome_message = 'hey there, how youuu doin? ;)'
print(f'hey there, {name} how youuu doin? ;)')
# place an f on the left/beginning of the string
# then you can use {} to interpolated python variables inside


# Useful Methods for strings
my_string = ' HEllo this is an amazing string    '

#.count()
print(my_string.count('i'))
print(my_string.count(' '))

#.strip() # Strip trailling white spaces
print(my_string.strip())

#len() # Not a method - general method built in
print(len(my_string))

#.lower() # makes things lower case
print(my_string.lower())

#.upper()
print(my_string.upper())

#.capitalize()
print(my_string.strip().capitalize())

#.replace(arg_int, arg_two)
print(my_string.replace('an', 'THE'))

#.split(arg) --> list
print(my_string.split(' '))
print(type(my_string.split(' ')))
print(my_string.split('i'))



