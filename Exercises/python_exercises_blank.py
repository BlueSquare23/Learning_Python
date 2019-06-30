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

def Exercise1():
    print("")
    print("--------------------------------")
    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise2():
    print("")
    print("--------------------------------")
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
        1)
        2)
        3)
        4)
        5)
        6)
        7)
        8)
        9)
        ''')
    selected = input()
    if selected == "q":
        quit = "q"
    elif int(selected) in range(10):
        selected = int(selected)
        print("--------------------------------")
        Ex[selected]()
    else:
        print("Unrecognized Input")
