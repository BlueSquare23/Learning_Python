#!/usr/bin/python3
#Intro to Dictionaries

#Dictionaries are like lists except that they store key value pairs

#Initializing dictionary
my_dictionary = {}

#Add items
my_dictionary["name"] = 'John'
my_dictionary["home town"] = 'Pittsburgh'
my_dictionary["age"] = 24
print(my_dictionary)

#Accessing item,
print(my_dictionary['name'])

#Changing items,
my_dictionary['name'] = "cat butt"
print(my_dictionary)

#Removing items,
del my_dictionary['home town']
print(my_dictionary)

#Iterate through a dictionary
for k, v in my_dictionary.items():
    print(k, '->', v)
