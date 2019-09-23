# Dictionaries
# All fun and games keep our crazy_x list... but we also need more info.
# Introducing dictionaries!

# Dictionaries are defined using {}
# They are organized with keys that point to values
# Much like looking up something on a dictionary or information about a contact on our phones.
   # Thus in our phone, the contact Filipe Paiva will hold lot's of info for ththis entry. could be the phone number, work number, email, address and so on...

#Syntax
# dict_name = {'example_key': 'value', 'example_key': 'value'}

# #Difining a simple dictionary with two keys
# dictionary_craxy_x = {
#     'Carolina': 'she was actually nice',
#     'Arthur': 'bit of a drinker'
# }
#
# print(dictionary_craxy_x)
# print(type(dictionary_craxy_x))
#
# # Accessing values - use the key!
# print(dictionary_craxy_x['Carolina'])
# print(dictionary_craxy_x['Arthur'])
#
# #Adding a new key, pair value
# dictionary_craxy_x['Kile'] = 'Likes Monster'
# print(dictionary_craxy_x)
#
# dictionary_craxy_x['Kile'] = 'REALLY Likes Monster'
# print(dictionary_craxy_x)
#
# # Get out all of the keys
# print(dictionary_craxy_x.keys())
# #Get out all of the values
# print(dictionary_craxy_x.values())
#
# #remove item from dictionary
# dictionary_craxy_x.pop('Kile')
#
# print(dictionary_craxy_x)

# Better example of a ditionary

crazy1 = {
    'name': 'Caroliona',
    'phone': '07842715517',
    'address': 'Location 1, at places',
    'know place to avoid': ['Milan', 'Lisbon', 'Tavira']
}