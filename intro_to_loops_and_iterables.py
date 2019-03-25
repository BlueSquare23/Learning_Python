#!/usr/bin/python3
#Loops and Iterables Section 5

#How to use a for loop

#Structure
'''
for var in array
    run code
'''

s = "hello world"
a = [4, 6, 9]

# in keyword
print( 5 in a )
print( 4 in a )
print( "ello" in s )

#Ways to iterate over a list(array)
#Method 1: Include the array
for even_number in [2, 4, 6, 8, 10]:
    print(even_number)
    #add more code here...

#Method 2: Reference the array
odds = [1, 3, 5, 7, 9, 11]
for odd_number in odds:
    print(odd_number)
    #...

#Method 3: Referencing the index of the array (w/ formatting)
print(range(len(odds)))
for index in range(len(odds)):
    print("Index: {:d}, odd number: {:d}".format(index, odds[index]))


#How to use a while loop

#Structure
'''
while(condition):
    run code
'''

index = 0
names = ["Josh", "Harry", "Leah", "Micah"]

#Use while loop to loop through array "names"
#by referencing each element of the array's index
while index < len(names):
    name = names[index]
    print(name)
    index = index + 1

#Add all numbers from 1-10 inclusive using while loop
total = 0
v = 1
while v <= 10:
    total = total + v
    v = v + 1
print(total)

#Run a loop forever until a condition is met
#Ex. Run program until two added numbers = 20
''' Uncomment code to run in terminal
while True:
    print("Please make sure a + b = 20")
    a, b, = int(input("a: ")), int(input("b: "))
#Run until the break condition is met
    if a + b == 20:
        print("Stopping Loop")
        break
    else:
        print("Please make sure a + b = 20")
'''

#How to use iterables

#
my_list   = [1,2,3,4,5]
my_tuple  = (2,7,8,9,10)
my_string = "Hello World!"

print(dir(my_list)) #shows all of the list's properties
print('__iter__' in dir (my_list)) #check if list is iterable
print('__iter__' in dir (my_tuple)) #check if tuple is iterable
print('__iter__' in dir (my_string)) #check if string is iterable
#This means each of these can be iterated through
#Ex.

for element in my_list:
    print(element)

#Spaces for output clarity
print()

#How a for loop actually works,
#First create an iterator for list using built in "iter()" function
list_iterator = iter(my_list)
while True: #Create a while loop that iterates through elements until it can't iter no-mo!
    try: #Allows you to test things
        next_element = next(list_iterator) #"next()" is another built in function
        print(next_element)
    except StopIteration: #Catches "StopIteration" from stderr
        break
