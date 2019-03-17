#!/usr/bin/python3
#Logic in Action!
#Episode 4.5

#Write a program that takes two numbers and then prints "divisible" if
#one number is divisible by the other or vice versa

print("Enter a number")
a = int(input())

print("Enter another number")
b = int(input())

if (a % b) == 0:
    print("divisible")
elif (b % a) == 0:
    print("divisible")
else:
    print("a is not divisible by b nor is b by a")

#The above program can be shortened by use of logical opperators
#Ex.
print("Enter a number")
a = int(input())

print("Enter another number")
b = int(input())

if (a % b) == 0 or (b % a) == 0:
    print("divisible")
else:
    print("a is not divisible by b nor is b by a")


#Given input a & b, print a divided by b, if b is not equal to zero
print("Enter a number")
a = int(input())

print("Enter another number")
b = int(input())

if b == 0:
    print("Cannot divide by zero")
else:
    print("A divided by b is, ")
    print(int(a / b))

#Alternativly, you could also say,
#Ex.
if b != 0: print("blah")
if b is not 0: print("foo")
if not(b == 0): print("bar")
