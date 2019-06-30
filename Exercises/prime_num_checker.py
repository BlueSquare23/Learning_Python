#!/usr/bin/python3
#Prime Number Checker
#Lesson 5.5

#This program checks whether a number is prime or not
#A prime number is a number that is not divisible by any number other than 1 and itself
#One is not considered a prime number

x = 13 #Set before running program
z = 0
#make array out of numbers < x and > 1
array = [2,3,4,5,6,7,8,9,10,11,12]

for a in array:
    #print(x % a)
    if x % a != 0:
        #check a off
        z = z + 1
print(z)
if z != len(array):
    print("Prime!")
