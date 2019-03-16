#!/usr/bin/python3
#String Manipulation

#These two types of strings are identical
single_quote_strings = 'single quotes'
double_quote_strings = "double quotes"

#Escaping quotation marks
#Ex.
string = 'He said \'Wow!\' with great surprise'

#Multi-line strings (often used to comment out code)
triple_quote_strings = '''
this is a
long paragraph
'''

#String Functions
#Use built in function var.upper to capitizle your string
#Ex.
var1 = "FOO"
var2 = "bar"

var1 = var1.lower()
print(var1)

var2 = var2.upper()
print(var2)

var3 = "       blah         "
print(var3.strip().title())

#For more string methods visit the python docs webpage
#https://docs.python.org/3/library/stdtypes.html#string-methods


#Advanced string manipulation

#String concatination
prefix = " Python is an "
suffix = "awesome language!"

#concatinate prefix and suffix
astr = prefix + suffix
print(astr)

#use .replace() to swap language w/ snake
astr = astr.replace("language!", "snake!")
print(astr)

#duplicate string
astr = prefix + suffix
astr = astr * 2
print(astr)

#replace only first instance or of language
astr = astr.replace("language", "snake", 1)
print(astr)

#Count function
print(astr.count("an"))


#String Formatting

#Format specifications
number = 11
float = 1.23456
string = "computer"

#print a decimal number
print("my number is {:d}".format(number))

#print a binary number
print("my number is {:b}".format(number))

# There are many formats types such as:
# e -- exponents
# b -- binary (base 2)
# o -- octal (base 8)
# d -- decimal (base 10)
# x -- hexadecimal (base 16)
# f -- floats (decimal numbers)
# s -- strings (default if not specified)

#print float
print("{:f}".format(float))

#only print to the third decimal place
print("{:.3f}".format(float))

#pad with spaces before a decimal
print("{:11.3f}".format(float))

#pad with zeros before a decimal
print("{:011.3f}".format(float))

#use .format with multiple items together
print("{0} {1} {2}".format(number,float,string))

#Advanced String Formatting Example
print("{name} own(s) {amount} of {object}".format(
    name = "William",
    amount = 5,
    object = "mangos"
))


#User Input
first_name = str(input("Please enter your first name: "))
middle_name = str(input("Please enter your middle name: "))
last_name = str(input("Please enter your last name: "))

first_name = first_name.capitalize()
middle_name = middle_name.capitalize()
last_name = last_name.capitalize()

name_format = "{first} {middle:.1s}{dot} {last}"
print(name_format.format(first=first_name, middle=middle_name, dot=".", last=last_name))
