#!/usr/bin/python3
#Introduction to functions
#Section 6.1

'''
Function Definition,
A function is a way to package code into discrete blocks
which each preform a specific task.

Functions are,
    * Easier to debug
    * Reusable

We've been using built in functions this whole time
For example,
    * len
    * min
    * str.join
    * list.append
'''

#Function Example,
#Calculate area of a circle (pi*(r^2))

#Creating a function
pi = 3.141592
def circle_area(r): #"r" is what is knonw as a parameter
    return pi*r*r

#Calling the function
print(circle_area(5)) #Pass it an argument

#Arguments and Parameters
def add(a, b, c): #"a, b, & c" are parameters
    return a + b + c

print(add(1, 2, 3)) #when the parameters are added they are called arguments

#Function with an unlimited number of parameters
def add_unlimited(*numbers):
    print(numbers)
    total = 0
    for n in numbers:
        total += n
    return total

#Call said function and pass it an unlimited number of arguments
print(add_unlimited(1,2,3,4,5,6))

#Date time example
import datetime as dt

def record_time( message, time = dt.datetime.now() ): #time is a default parameter because it already has a value
    print("{:}, time: {:}".format(message, time))

#When the above function is called it will print the value of the default parameter
record_time("It is the morning")
#This behavior can be overridden by specifying your own second argument
record_time("It is the morning", "And the bananas are ripe!")


#Return and Void Functions
'''
Return Functions,
These are functions which produce output and use the "return"
keyword. The word "return" here simply means the function is
returning a value to the program. The output of these functions
can be saved to a variable. For example the max() function can
be called like this.

max_value = max([3, 6, 2, 8])
'''
#Return Function in action

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(13))


'''
Void Functions,
These functions do not return a value. They simply preform an action.
Void function do not use the "return" keyword. An example of the
void functions is print.

print("I return nothing, I just print to the console.")

Other examples include the .sort() and . insert() methods.

[4, 7, 3, 2].sort()
[1, 2, 4, 5].insert(2, 3)
'''
#Void Function in action

def is_odd(number):
    if number % 2 != 0:
        print("{:d} is odd".format(number))
    else:
        print("{:d} is even".format(number))

print(is_odd(11))

#Tip: use the "pass" keyword as a code place holder when developing a function.
#Ex.

def funk(a):
    pass #Code placeholder

#Spaces for output clarity
print()

#Working with void and return functions,

#This function reverses a string
#Ex. => "123" --> "321"
def reverse(s):
    new_str = ""
    for i in range(len(s)):
        new_str += s[len(s) - i - 1] #The last element which has not yet been added
    return new_str

print(reverse("123"))
print(reverse("abcdefg"))

#Spaces for output clarity
print()

#For a brake down of the above function see the examples below,
#"range(len())" simply makes a list of all numbers b/w 0 & len(string)
z = "fuckaduck"
print(range(len(z)))
print(z[len(z) - 1]) #Simply the letter at position len(z) - 1 in the string

for n in [1,2,3,4,5]:
    n += n #The "+=" operator simply adds some value to itself
print(n)

#Spaces for output clarity
print()

#This function determins if a string is a palindrome
#Ex. => "abba" --> "abba"
def is_palindrome(p):

    for i in range(len(p)//2):
        if p[i] != p[len(p) - i - 1]:
            print("This is Not a palindrom!")
            return #AKA exit the function

    print("This is a palindrome!")

print(is_palindrome("1"))
print(is_palindrome("11211"))
print(is_palindrome("1234"))
print(is_palindrome("urmomgay"))

#Fun fact: printing this ^ function is redundant (hence the "none" in output)
#Ex.
is_palindrome("1221")
is_palindrome("1234")

#Spaces for output clarity
print()

#Recursion,
#Episode 6.6
#Functions calling themselves
def double(n):

    #base case
    if n == 0:
        return 0

    #recursive call
    return double(n - 1) + 2

print(double(3))

#Factorial
# n! = n * (n-1)!
# 0! = 1
# 5! = 5*4! = 5*4*3*2*1*1
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print(factorial(5))

def exponentiate(b, e):

    #base case
    if (e == 0): return 1

    #recursive call
    return exponentiate(b, e-1) * b

print(exponentiate(2, 3))


#Spaces for output clarity
print()

#More Recursion

#Recursivly count vowels in a string
def count_vowels(s, index = 0):

    #base case
    if (index == len(s)): return 0

    char = s[index]
    if char in 'aeiou':
        return count_vowels(s, index + 1) + 1
    return count_vowels(s, index + 1) + 0

print(count_vowels('hello'))

#Recursivly count the sum of the digits in a number
# 345 --> 3+4+5 = 12
def digit_sum(n):

    #base case
    if n == 0: return 0
    return digit_sum(n//10) + n % 10

print(digit_sum(345))

#Recursivly compute the n^th fibonacci number
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))
