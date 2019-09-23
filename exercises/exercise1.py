# Define the following variables
# name, last_name, age, eye_color, hair_color
name = 'Boris'
last_name = 'Jamiroquai'
eye_color = 'bluish'
hair_color = 'bleach'
age = 60

# Prompt user for input and Re-assign these
name = input('What is your name ? ').capitalize()
last_name = input('what is your last name? ').capitalize()
eye_color = input('eye color? ')
hair_color = input('hair color? ')
age = int(input('age? '))

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
print(f'Hello {name} {last_name}! Welcome, your age is {age}, your eye are {eye_color.lower()} and your hair colour is {hair_color.lower()}')

#Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'

date_of_birth = 2019 - age

print(f'you said you were {age} , hence you were born in {date_of_birth}')

print(f'you said you were {age} , hence you were born in {2019 - age}')

#Extra - Cast your input
#
