# # Numerical Data types
# # - Int, long, float, complex
# # These are numerical data types which we can use numerical operators.
#
# # Complex and Long we don't use as much
# # Complex bring an imaginary type of number
# # long - are integers of unlimited size
# #
#
# # int - Stands for integers
# # Whole numbers
# my_int = 10
# print(my_int)
# print(type(my_int))
#
# # Opperator - Add, Subtract, devide and multiply
#   # Exponential
# print(4 + 3)
# print(4 - 3)
# print(4/2) # Devisions automatically get converted to float
# print(4//2) # Keeps it as interger / drops the decimal
# print(10/3)
# print(5//2)
# print(4*2)
# print(3**2)
#
# #Modules looks for the number of remainder
# # % ##
# print(10%3) ## --> 3*3 = 9, so 1 is the remainder
# print(22%3) ## --> 3*7 = 21, so 1 is the remainder
# print(23%3) ## --> 3*7 = 21, so 2 is the remainder
#
# # Comparission Operators # --> boolean value
#
# #  ==  - Comparission Operator
# #  < / >  - Bigger and smaller than
# #  <=  - Smaller than or equal
# #  >=  - Bigger than or equal
# #  !=  - Not equal
# # is and is not
#
# my_variable1 = 10
# my_variable2 = 13
#
# print(my_variable1 == my_variable2)
# print(my_variable1 > my_variable2)
# print(my_variable1 < my_variable2)
# print(my_variable2 >= 13)
# print(my_variable2 is 13)
# print(my_variable2 is not 13)
#
#
# # Boolean Values
# # Defined by wither True or False
# print(type(True))
# print(type(False))
# print(0 == False)
# print(1 == True)
#
## None
print(None)
print(type(None))
print(bool(None))
print(0 == None)
print(False == None)
print(False == bool(None))

print('Logical and & or ------------')
# Logical AND & OR
a = True
b = False
# using *and* both sides have to be true for it to result in true
print(a and True)
print((1 == 1) and (True))
print((1==1) and False)

# use or, ONLY 1 side needs to be true
print('this will print true')
print(True or False)
print(True or 1 == 2)
print('this will print False')
print(False or 1 == 2)
