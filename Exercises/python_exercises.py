#!/usr/bin/python3
#Exercises (Scratch Paper)

import random

#Find exercises here https://www.practicepython.org/
def Exercise0():
    quit = 0
    while quit != "q":
        print("Welcome to my python practice excercises!")
        print("Type q to quit and select another exercise")
        print("Here's a list of all of the exercises:")
        print('''
        1) Keeping it 100
        2) Odd or Even
        3) Simple Greater Than
        4) Divisor Finder
        5) List Compairison
        6) List Comprehension
        7) Rock, Paper, Scissors
        8) Guessing Game
        9) List Overlap Comprehensions
        ''')
        quit = str(input())

    print("--------------------------------")

def Exercise1():
#Ex 1. Character input
    print("Keeping it 100")
    print("--------------------------------")
    '''
    Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year they
    will turn 100 years old.
    '''

    print("Please enter your name: ")
    name = str(input())
    print("Please enter your age: ")
    age = int(input())
    print("It is 2019")

    years_till_100 = (100 - age)
    year_when_100 = (years_till_100 + 2019)
    years_till_100 = str(years_till_100)
    year_when_100 = str(year_when_100)
    print("You will be 100 in, " + years_till_100 + " years.")
    print(name + " will be 100 in the year " + year_when_100)

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise2():
#Ex 2. Odd or Even
    print("Odd or Even")
    print("--------------------------------")
    '''
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate message to the user.
    Hint: how does an even / odd number react differently when divided by 2?

    Extras:

    If the number is a multiple of 4, print out a different message.
    '''
    print("Enter a numer: ")
    number = int(input())

    if number % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")

    if number % 4 == 0:
        print("This number divides by four")
    else:
        print("This number does not divide by four")

    print("--------------------------------")

def Exercise3():
    print("Simple Greater Than")
    print("--------------------------------")
#Ex 3.
    '''
    Take a list, say for example this one:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements of the list
    that are less than 5.

    Extras:

    Instead of printing the elements one by one, make a new list that has all
    the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.

    Ask the user for a number and return a list that contains only elements
    from the original list a that are smaller than that number given by the
    user.
    '''
    print("Of this list,")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(a)
    print("these numbers are greater than five: ")

    #Thought process
    '''
    Iterate through the list and check if the element is greater
    than five. If it is print it.
    '''
    for element in a:
        if element > 5:
            print(element)

    print("--------------------------------")

def Exercise4():
    print("Divisor Finder")
    print("--------------------------------")
    '''
    Create a program that asks the user for a number and then prints out a list
    of all the divisors of that number.
    (If you don’t know what a divisor is, it is a number that divides evenly
    into another number. For example, 13 is a divisor of 26 because 26 / 13 has
    no remainder.)
    '''
    #Thought process
    '''
    Create an iterable list composed of numbers less than the entered value.
    Then split the list in half so as to eliminate duplicate answers.
    Finally see if the number can be evenly divided by an element in the halflist.
    (i.e. is number mod element of halflist equal to zero (i.e. has no remainder))
    If it can then print the divisor.
    '''

    print("This program determines an integers divisors")
    print("Please Enter a Number: ")
    number = int(input())

    set = range(1, number)
    print(set)

    list1 = []
    for item in set:
        list1.append(item)
    #print(list1)

    halflist = (len(list1) // 2)
    halflist = (halflist + 1)
    #print(halflist)

    for item in list1[0:halflist]:
        if(number % item) == 0 and item != 1:
            print("{:d} is divisable by {:d}".format(number, item))

    print("--------------------------------")

def Exercise5():
    print("List Compairison")
    print("--------------------------------")
    '''
    Take two lists, say for example the two below,
    and write a program that returns a list that contains only the elements
    that are common between the lists (without duplicates).
    Make sure your program works on two lists of different sizes.
    '''
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    print("List a:")
    print(a)
    print("List b:")
    print(b)

    c = []

    for element in a:
        if element in b and element not in c:
            c.append(element)

    print("List c:")
    print(c)
    print("The elements in list c are in both list a and b.")

    print("--------------------------------")

def Exercise6():
    print("List Comprehension")
    print("--------------------------------")
    '''
    Let’s say I give you a list saved in a variable:
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes a new list
    that has only the even elements of this list in it.
    '''

    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    list = []
    #Traditional method
    for x in a:
        if x % 2 == 0:
            print(x)

    #List comprehension
    evens = [x for x in a if x % 2 == 0]
    print(evens)

    print("--------------------------------")

def Exercise7():
    print("Rock, Paper, Scissors")
    print("--------------------------------")
    '''
    Make a two-player Rock-Paper-Scissors game.
    (Hint: Ask for player plays (using input), compare them,
    print out a message of congratulations to the winner,
    and ask if the players want to start a new game)
    '''
    print("Player one choose your wepon: Rock, Paper, or Scissors")
    player1_input = str(input())
    print("Player two choose your wepon: Rock, Paper, or Scissors")
    player2_input = str(input())

    #With If statments
    if player1_input == "Rock" and player2_input == "Scissors":
        print("Player one wins!")
    elif player1_input == "Scissors" and player2_input == "Paper":
        print("Player one wins")
    elif player1_input == "Paper" and player2_input == "Rock":
        print("Player one wins")
    elif player1_input == player2_input:
        print("Its a draw!")
    else:
        print("Player two wins!")

    print("--------------------------------")

def Exercise8():
    print("Guessing Game")
    print("--------------------------------")
    '''
    Generate a random number between 1 and 9 (including 1 and 9).
    Ask the user to guess the number, then tell them whether they guessed
    too low, too high, or exactly right. (Hint: remember to use the user
    input lessons from the very first exercise)
    '''

    play_again = "y"
    while play_again == "y":
        #Create Random Number
        a = random.randint(1, 9)

        #Take User Input
        print("Enter an integer between 1 and 9 (inclusive): ")
        num = int(input())

        #Test User Input
        if num < a:
            print("Your guess was lower than the number.")
        elif num > a:
            print("Your guess was higher than the number.")
        else:
            print("You guessed the number!")

        #Allow users to reply if they'd like
        print("Enter, y to play again or anything else to quit")
        play_again = str(input())

    print("--------------------------------")

def Exercise9():
    print("List Overlap Comprehensions")
    print("--------------------------------")
    '''
    This week’s exercise is going to be revisiting an old exercise
    (see Exercise 5), except require the solution in a different way.

    Take two lists, say for example the two below:

    and write a program that returns a list that contains only the elements
    that are common between the lists (without duplicates). Make sure your
    program works on two lists of different sizes. Write this in one line of
    Python using at least one list comprehension. (Hint: Remember list
    comprehensions from Exercise 6).
    '''
    print("List a:")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(a)
    print("List b:")
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    print(b)
    c = []
    #Traditional way
    '''
        for element in b:
            if element in a and element not in c:
                c.append(element)
    print(c)
    '''
    #List Comprehension
    c = [element for element in b if element in a and element not in c]
    print("List c:")
    print(c)

    print("The elements of list c are in both list a and b.")

    print("--------------------------------")


#Select Lesson
quit = 0
while quit != "q":
    print("Select the exercise you'd like to do, ")
    Ex = [Exercise0,Exercise1,Exercise2,Exercise3,Exercise4,Exercise5,Exercise6,Exercise7,Exercise8,Exercise9]
    print(list(range(10)))
    print("Enter 'q' at any time to quit!")
    selected = input()
    if selected == "q":
        quit = "q"
    elif int(selected) in range(10):
        selected = int(selected)
        print("--------------------------------")
        Ex[selected]()
    else:
        print("Unrecognized Input")
