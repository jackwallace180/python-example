# Variables in Python
 # Variable is a box. You can give it a name and put stuff inside

# Assigning a Variable
# Giving box a name and putting stuff inside
box_variable = 'Books and stuff'

# looking inside the box
print(box_variable)

# Re Assigning a Variable
# Vatriable are mutable - Hence they can change/be re-assigned
box_variable = "CDs and other stuff"
print(box_variable)

# Re-assigning with a integer
# Variable can hold any data type inside
box_variable = 14
print(box_variable)

# Important python function
# print(arg)
print('hello') #Printing string
print(box_variable) # printing variable
print('hello', box_variable) #overloading with two arguments

# type(arg)
# output the data type of an object
print(type('hello'))
print(type(14))
print(type(14.0))
variable_num = '14'
my_list = [1,2,2,'hey']
print(type(my_list))
#print(type('10'*variable_num)) #This will break


#input()
# it promps user for input
print('What is your favorit color?')
user_response = input('Now really, what is your favorit color?')
print(user_response)
