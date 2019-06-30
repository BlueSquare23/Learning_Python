#!/usr/bin/python3
#Into to Lists
#Python course section 3


#Sample lists, can be numbers, or strings, or both
numbers = [5, -6, 2, 4, -5, 1]
names = ["Heather", "Micah", "Jane"]

#An index is the position of an element in a list
#Lists are 0 based indexes
#Ex.
print(names[0], names[1])

#delete element at specific index
print(names)
del names[1]
print(names)

#Strings similarities to lists
mystring = "Hello world"
print(mystring[0])
print(mystring[6])


#List methods
    #Appending
    #Removing

#Appending an element
alpha = ["a", "b", "c", "d"]
#Method 1, .append
alpha.append("e")
alpha.append("f")
print(alpha)
#Method 2, add strings
alpha = ["a", "b", "c", "d"]
alpha = alpha + ["e"]
print(alpha)

#Find the index of an element
d_index = alpha.index("d")
print("d's index is, " + str(d_index))

#Remove an element at an index
del alpha[d_index]
print(alpha)

#Use .remove method to both find and remove an element
alpha = ["a", "b", "c", "d"]
alpha.remove("d")
print(alpha)

#Long form of .append method
a = ["a", "b", "c", "d"]
print(len(a))
a[len(a):] = ["f"]
print(a)
#Explanation of ^ above
'''
B/c len(a) = 4 and indexes are 0 based,
setting index 4 to a new value is really just
appending that value to the list.

For more information on this and other list methods
visit the python3 docs webpage at the link below

https://docs.python.org/3.4/tutorial/datastructures.html
'''


#Advanced list methods

#Sorting the Alphabet
alpha1 = ["a", "f", "b", "e", "d"]
alpha2 = ["g", "i", "h"]
alpha3 = "jklmnopqrstuvwxyz"

#First sort the lists
alpha1.sort()
alpha2.sort()
print(alpha1)
print(alpha2)

#Next insert "c" at the correct index
alpha1.insert(2, "c")
print(alpha1)
print(alpha2)
print(alpha1 + alpha2)

#Then convert the lists to strings
alpha1 = ''.join(alpha1)
alpha2 = ''.join(alpha2)

#Finally add all the strings together
alphabet = alpha1 + alpha2 + alpha3
print(alphabet)


#Built in List Functions
numbers = [3.14, -5, 10, 10**4, 17]
hello_world = "HelloWorld"

#min, max, sum, len on list
print(min(numbers))
#Do not do number.min() b/c it is a methods not a function
print(max(numbers))
print(sum(numbers))
print(len(numbers))

#min, max, sum, len on strings
print(min(hello_world))
#Min returns H because is the youngest letter in the string
print(max(hello_world)) #Returs r because oldest letter in string
#print(sum(hello_world)) cant do b/c does not make sense
print(len(hello_world))



#2D Arays and Matrices

#import the pprint function from pprint module as a function called pretty_print
from pprint import pprint as pretty_print

#import the copy and deepcopy function from the copy module
from copy import copy, deepcopy

#An aray of arays, hence a 2 dimentional aray
nums_2d = [
    [1,2,3,4,5,6,7],
    [8,9,10,11,12,13,14,15],
    [16,17,18,19,20,21,22]
]

#Query element from matrix
#Get #11
print(nums_2d[1][3])
#Above ^ says get row 2 (ie index 1 of aray 1), and get element 4 of aray 2 (ie index 3)

#Use pretty_print function to get cleaner output
pretty_print(nums_2d)

#assign values to matrix
#Swap element #17 with #-5
nums_2d[2][1] = -5
pretty_print(nums_2d)

#Using copy Functions
'''
If we create a 2d array (array2) out of a number of arrays (array1),
any items within array1 which are changed will be changed gobally
throughout array2.
'''
#Ex.
letters = ["A", "B", "C", "D", "E"]
letters_2d = [letters, letters, letters]
#Make a change to list 'letters'
letters_2d[0][0] = 'F'
pretty_print(letters_2d) #Prints all 'F' for first column

#To fix this ^ copy list/array 'letters' into array 'letters_2d'
letters = ["A", "B", "C", "D", "E"]
#Use copy
letters_2d = [copy(letters), copy(letters), copy(letters)]
letters_2d[0][0] = 'F'
pretty_print(letters_2d) #Prints 'F' only in first element of the first array


#List Slicing
    #Query part of an array

#Use range to generate a list of numbers
a = list(range(0,10))
print(a)
#print first 5 elements of list 'a'
print(a[0:5])
#print from 2 to the end of the array
print(a[2:len(a)])
    #or by omit len(a) and by default it'll go to the end
print(a[2:])
#print entire array with
print(a[:])
#get every second element
print(a[::2])
#get every second element b/w 0 and 8
print(a[0:8:2])
#query from the end with negative numbers
#get every number b/w 2 to 2 from the end (ie 8)
print(a[2:-2])
#get all numbers from the last on in
print(a[::-1])
