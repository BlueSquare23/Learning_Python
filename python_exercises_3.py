#!/usr/bin/python3
#Exercises section 3 (Scratch Paper)

import random

#Find exercises here https://www.practicepython.org/
def Exercise0():
    quit = 0
    while quit != "q":
        print("Welcome to my python practice excercises!")
        print("Type q to quit and select another exercise")

        quit = str(input())

    print("--------------------------------")

def Exercise1(): #Really exercise 20
    print("Element Search")
    print("--------------------------------")

    '''
    Write a function that takes an ordered list of numbers (a list where the
    elements are in order from smallest to largest) and another number. The
    function decides whether or not the given number is inside the list and
    returns (then prints) an appropriate boolean.

    Extras: Use binary search.
    '''

    def list_compare():
        list1 = a = [1, 3, 5, 30, 42, 43, 100]
        list2 = []

        print("Enter an integer less than 100: ")
        user_input = int(input())

        list2.append(user_input)

        for x in list2:
            if x in list1:
                print("Value is in ordered list")
            else:
                print("Value not in ordered list")

    #list_compare()

    list1 = [1, 3, 5, 30, 42, 43, 99, 100]
    half_list1 = []
    half_list2 = []
    half_list3 = []

    print("Enter an integer less than 100: ")
    user_input = int(input())

    '''
    #Prints the index of a lists midpoint
    print((len(list1)+1)//2)

    #Prints the element at the midpoint of a list
    print(list1[(len(list1)+1)//2])
    '''

    #I created a function to find the index of the midpoint of a given list
    def midpoint(list):
        midpoint = list.index(list[(len(list)+1)//2])
        return midpoint
    #print(list1[midpoint(list1)])

    '''
    #Creates a new list out of the elements
    for x in list1[0:midpoint(list1)]:
        half_list1.append(x)
    print(half_list1)

    for x in half_list1[0:midpoint(half_list1)]:
        half_list2.append(x)
    print(half_list2)

    for x in half_list2[0:midpoint(half_list2)]:
        half_list3.append(x)
    print(half_list3)
    '''

    #For more information about the code within the binary_search function read
    #the description below.

    def binary_search():
        print(list1)
        if user_input == list1[midpoint(list1)]:
            print("element is in list")

        #For user_input less than midpoint
        elif user_input < list1[midpoint(list1)]:
            for x in list1[0:midpoint(list1)]:
                half_list1.append(x)
            print(half_list1)

            #Second layer deep
            if user_input == half_list1[midpoint(half_list1)]:
                print("element is in list")
            elif user_input < half_list1[midpoint(half_list1)]:
                for x in half_list1[0:midpoint(half_list1)]:
                    half_list2.append(x)
                print(half_list2)
                if user_input == half_list2[midpoint(half_list2)]:
                    print("element is in list")
            elif user_input > half_list1[midpoint(half_list1)]:
                for x in half_list1[midpoint(half_list1):]:
                    half_list2.append(x)
                print(half_list2)
                if user_input == half_list2[midpoint(half_list2)]:
                    print("element is in list")

                #Third layer deep
                elif user_input < half_list2[midpoint(half_list2)]:
                    for x in half_list2[0:midpoint(half_list2)]:
                        half_list3.append(x)
                    if user_input == half_list3[0]:
                        print("element is in list")
                    else:
                        print("element is not in list")
                elif user_input > half_list2[midpoint(half_list2)]:
                    for x in half_list2[midpoint(half_list2):]:
                        half_list3.append(x)
                    if user_input == half_list3[0]:
                        print("element is in list")
                    else:
                        print("element is not in list")

        #For user_input greater than midpoint
        elif user_input > list1[midpoint(list1)]:
            for x in list1[midpoint(list1):]:
                half_list1.append(x)
            print(half_list1)

            #Second layer deep
            if user_input == half_list1[midpoint(half_list1)]:
                print("element is in list")
            elif user_input > half_list1[midpoint(half_list1)]:
                for x in half_list1[midpoint(half_list1):]:
                    half_list2.append(x)
                print(half_list2)
                if user_input == half_list2[midpoint(half_list2)]:
                    print("element is in list")
            elif user_input < half_list1[midpoint(half_list1)]:
                for x in half_list1[0:midpoint(half_list1)]:
                    half_list2.append(x)
                print(half_list2)
                if user_input == half_list2[midpoint(half_list2)]:
                    print("element is in list")

                #Third layer deep
                elif user_input > half_list2[midpoint(half_list2)]:
                    for x in half_list2[midpoint(half_list2):]:
                        half_list3.append(x)
                    if user_input == half_list3[0]:
                        print("element is in list")
                    else:
                        print("element is not in list")
                elif user_input < half_list2[midpoint(half_list2)]:
                    for x in half_list2[0:midpoint(half_list2)]:
                        half_list3.append(x)
                    if user_input == half_list3[0]:
                        print("element is in list")
                    else:
                        print("element is not in list")

    '''
    * Binary Search Function

        The binary search function above is an implementation of a binary search
    algorithm. It works by looking for an element within a list by following
    the steps of a decision tree which is constructed out of if statements. The
    above approach to conducting a search is inteneded to be a demonstrations
    and is not the ideal way to go about conducting a search through a list.

    The binary search tree above works by first assessing whether the users
    guess is a list item. If it is not then the program assesses whether or not
    the users guess is greater than or less than the midpoint of the list. The
    function then splits the original list into a sub list of elements and again
    determins whether the guess is within the sublist. Once the original list
    has been split entirely to its last element it can be determined whether
    or not the guess is contained in the overall list.
    '''

    binary_search()


    '''
    def recursive_binary_search():
        #Basecase: If list cannot be split return
        if len(list#) > 1:
            return result

        if user_input == list1[midpoint(list1)]:
            print("element is in list")
        elif user_input < list1[midpoint(list1)]:
            for x in list1[0:midpoint(list1)]:
                half_list1.append(x)

    #recursive_binary_search()
    '''

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise2():
    print("")
    print("--------------------------------")

    '''
    '''

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise3():
    print("")
    print("--------------------------------")

    '''
    '''

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise4():
    print("")
    print("--------------------------------")

    '''
    '''

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise5():
    print("")
    print("--------------------------------")

    '''
    '''

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise6():
    print("")
    print("--------------------------------")

    '''
    '''

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise7():
    print("")
    print("--------------------------------")

    '''
    '''

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise8():
    print("")
    print("--------------------------------")

    '''
    '''

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise9():
    print("")
    print("--------------------------------")

    '''
    '''

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
        1) Element Search
        2)
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
