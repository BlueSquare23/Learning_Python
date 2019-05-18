#!/usr/bin/python3
#Exercises section 2 (Scratch Paper)

import random

#Find exercises here https://www.practicepython.org/
def Exercise0():
    quit = 0
    while quit != "q":
        print("Welcome to my python practice excercises!")
        print("Type q to quit and select another exercise")

        quit = str(input())

    print("--------------------------------")

def Exercise1(): #Really exercise 11 on practicepython.org
    print("Check Primality Functions")
    print("--------------------------------")
    '''
    Ask the user for a number and determine whether the number is prime or not.
    (For those who have forgotten, a prime number is a number that has no
    divisors.). You can (and should!) use your answer to Exercise 4 to help you.
    Take this opportunity to practice using functions, described below.
    '''
    #Function used to collect user input
    def get_integer(help_text="Give me a number:"):
        return int(input(help_text))

    number = get_integer("Enter a number to see if its prime: ")

    #Function used to create a list containing all ints b/w 1 and 1/2 number +1
    #Used to save the effort of having to interate over list twice unecessarially.
    def half_list_maker():
        set = range(1, number)

        list1 = []
        for item in set:
            list1.append(item)

        halfway = (len(list1) // 2)
        halfway = (halfway + 1)
        return list1[0:halfway]

    var = 0
    #Tests if user input is 0, 1, or >1
    if number <= 0:
        print("Number must be a positive integer.")
    elif number == 1:
        print("One is a special case!")
    else:
        for item in half_list_maker(): #Finds divisors
            if(number % item) == 0 and item != 1:
                print("{:d} is divisable by {:d}".format(number, item))
                var = var + 1
        if var > 0: #If no divisors number must be prime
            print("{:d} is not prime.".format(number))
        else:
            print("{:d} is prime!".format(number))

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise2():
    print("List Ends")
    print("--------------------------------")

    '''
    Write a program that takes a list of numbers (for example, see list below)
    and makes a new list of only the first and last elements of the given list.
    For practice, write this code inside a function.
    '''
    print("Of list a, ")
    a = [5, 10, 15, 20, 25]
    print(a)

    def new_list(a):
        return [a[0], a[len(a)-1]]

    #Spacing for readability
    print("")
    print("-these are the first and last elements.")
    print(new_list(a))
    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise3():
    print("")
    print("--------------------------------")
    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise4():
    print("")
    print("--------------------------------")
    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise5():
    print("")
    print("--------------------------------")
    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise6():
    print("")
    print("--------------------------------")
    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise7():
    print("")
    print("--------------------------------")
    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise8():
    print("")
    print("--------------------------------")
    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise9():
    print("")
    print("--------------------------------")
    #Spacing for readability
    print()

    print("--------------------------------")


#Select Lesson
quit = 0
while quit != "q":
    Ex = [Exercise0,Exercise1,Exercise2,Exercise3,Exercise4,Exercise5,Exercise6,Exercise7,Exercise8,Exercise9]
    print("Select the exercise you'd like to do, ")
    #print(list(range(10)))
    print("Enter 'q' at any time to quit!")
    print("Here's a list of all of the exercises:")
    print('''
        1) Check Primality Functions
        2) List Ends
        3)
        4)
        5)
        6)
        7)
        8)
        9)
        ''')
    print("--------------------------------")
    selected = input()
    if selected == "q":
        quit = "q"
    elif int(selected) in range(10):
        selected = int(selected)
        print("--------------------------------")
        Ex[selected]()
    else:
        print("Unrecognized Input")
