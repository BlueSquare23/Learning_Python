#!/usr/bin/python3
#Prime number detector

#Challenge: Build a script that can detect prime numbers.
print("Hello and welcome to the prime number detector!")
num = int(input("Please enter a positive integer, ")) #Take user input

if num <= 0: #Detect if input is positive
    print("The number must be positive")
else:
    list = list(range(num)) #Use list & range methods to make a list of numbers b/w [0 & (num - 1)] aka [0 - num)
    array = (list[2:]) #Format list as an array of every number b/w [2 & num)
    #print(array)
    counter = 0 #Initialize counter
    #Iterate through that array using a for loop to test if num is evenly divisable.
    for x in array:
        if num % x == 0: #If num is evenly divisable by an element in the array, print message below.
            print("{:d} is a divisable by {:d}".format(num, x))
        else:
            counter = counter + 1 #Keep track of each number not divisable to see if any of the number in the array are evenly divisable
    #If no numbers are evenly divisable by any of the elements of the array then the number entered is prime!
    #print(counter)
    #print(len(array))
    if num == 1:
        print("1 is a special case!")
    else:
        if counter == len(array):
            print("{:d} is a prime number".format(num))
        else:
            print("{:d} is NOT a prime number".format(num))
