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


def Exercise2(): #Ex 12
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


def Exercise3(): #Ex 13
    print("Fibonacci")
    print("--------------------------------")

    '''
    Write a program that asks the user how many Fibonnaci numbers to generate
    and then generates them. Take this opportunity to think about how you can
    use functions. Make sure to ask the user to enter the number of numbers in
    the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of
    numbers where the next number in the sequence is the sum of the previous
    two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5,
    8, 13, …)
    '''

    def user_input(text="Enter a number: "):
        return int(input(text))


    def fibonacci():
        count = user_input("Enter how many fibonacci numbers you'd like to generate: ")
        i = 1
        if count == 0:
            fib = []
        elif count == 1:
            fib = [1]
        elif count == 2:
            fib = [1,1]
        elif count > 2:
            fib = [1,1]
            #Adds the last two elements of fib together and appends the result to fib
            while i < (count - 1):
                fib.append(fib[i] + fib[i-1])
                i += 1
        return fib

    print(fibonacci())


    #Spacing for readability
    print()

    print("--------------------------------")


def Exercise4():
    print("List Remove Duplicates")
    print("--------------------------------")

    '''
    Write a program (function!) that takes a list and returns a new list that
    contains all the elements of the first list minus all the duplicates.

    Extras:

    * Write two different functions to do this - one using a loop and
    constructing a list, and another using sets.

    * Go back and do Exercise 5 using sets, and write the solution for that in
    a different function.
    '''

    print("List a:")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(a)
    print("List b:")
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(b)


    def uniq():
        c = []
        for item in b:
            if item in a and item not in c:
                c.append(item)
        return c

    print("List c:")
    print(uniq())

    def set_uniq():
        return set(b).intersection(set(a))
        #set(a) turns a into a set rather than a list
        #set(b) turns b into a set rather than a list
        #list(SET) turns some set into a list

    print("Intersection of sets, a & b: ")
    print(set_uniq())

    #Spacing for readability
    print()

    print("--------------------------------")


def Exercise5():
    print("Word Order")
    print("--------------------------------")

    '''
    Write a program (using functions!) that asks the user for a long string
    containing multiple words. Print back to the user the same string, except
    with the words in backwards order. For example, say I type the string:

        My name is Michele

    Then I would see the string:

        Michele is name My

    shown back to me.
    '''

    print("Enter a sentance you'd like to have reversed: ")
    sentance = str(input())

    def word_order(sentance = "Test sentance"):
        split_sentance = sentance.split()
        print(split_sentance)
        reversed_sentance = []
        n = len(split_sentance)
        while n > 0:
            reversed_sentance.append(split_sentance[n-1:n])
            n = n - 1
        print(reversed_sentance)
        result = ''.join(reversed_sentance)
        return result
    word_order(sentance)


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
        3) Fibonacci
        4) List Remove Duplicates
        5) Word Order
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