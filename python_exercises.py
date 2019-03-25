#!/usr/bin/python3
#Exercises (Scratch Paper)

#Find exercises here https://www.practicepython.org/

def Exercise1():
#Ex 1. Character input

    '''
    Create a program that asks the user to enter their name and their age.
    Print out a message addressed to them that tells them the year that they will turn 100 years old.
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


def Exercise2():
#Ex 2. Odd or Even
    '''
    Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
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

    #Spacing for readability
    print()

def Exercise3():
#Ex 3.
    '''
    Take a list, say for example this one:

      a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    and write a program that prints out all the elements of the list that are less than 5.

    Extras:

    Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
    '''
    print("Of this list,")
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    print(a)
    print("these numbers are greater than five: ")

    #Thought process
    '''
    Iterate through the list and check if the element is greater than five. If it is print it.
    '''
    for element in a:
        if element > 5:
            print(element)


#Select Lesson
print("Select the exercise you'd like to do, ")
Ex = [Exercise1,Exercise2,Exercise3,4,5,6,7,8,9]
print(list(range(10)))
selected = int(input())
print("--------------------------------")
Ex[selected]()
