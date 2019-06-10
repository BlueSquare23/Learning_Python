#!/usr/bin/python3
#Exercises section 3 (Scratch Paper)

import random
import requests
from bs4 import BeautifulSoup
import time

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
    print("Write to a File")
    print("--------------------------------")

    '''
    Take the code from the How To Decode A Website exercise (if you didn’t do
    it or just want to play with some different code, use the code from the
    solution), and instead of printing the results to a screen, write the
    results to a txt file. In your code, just make up a name for the file you
    are saving to.
    '''

    #Turns webpage into html string and saves that as r_html using requests
    url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
    r = requests.get(url)
    r_html = r.text

    #Soupifies that webpage
    soup = BeautifulSoup(r_html, 'html.parser')

    string = ""

    #Finds all the <p> tags and prints out the text of those html subtitles
    print("Writing... ")#For spacing
    for article in soup.find_all('p'):
        string = string + article.text
        string = string + "\n"
        string = string + "\n"

    with open('file.txt', 'w') as open_file:
        open_file.write(string)


    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise3():
    print("Read from a File")
    print("--------------------------------")

    '''
    Given a .txt file that has a list of a bunch of names, count how many of
    each name there are in the file, and print out the results to the screen.
    '''

    #Reading from file explained
    '''
    #Use with to open the namelist file as a variable named open_file
    with open('namelist.txt', 'r') as open_file:
        #all_text = open_file.read()
        #Use readline() to read the file line by line
        line = open_file.readline()
        #Use a while loop to iterate through all of the lines and strip them of
        #surrounding characters till it reaches the end of the file
        while line:
            print(line.strip())
            line = open_file.readline()
    #Note you can only use .readline() and .strip() while the file is open under with open() as f:
    '''

    #Get a count of each name and store it in a dictionary

    counter_dict = {}

    with open('namelist.txt') as f:
        line = f.readline()
        while line:
            line = line.strip()
            if line in counter_dict:
                counter_dict[line] += 1
            else:
                counter_dict[line] = 1
            line = f.readline()

    print(counter_dict)

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise4():
    print("File Overlap")
    print("--------------------------------")

    '''
    Given two .txt files that have lists of numbers in them, find the numbers
    that are overlapping. One .txt file has a list of all prime numbers under
    1000, and the other .txt file has a list of happy numbers up to 1000.
    '''

    happynumbers = []
    primenumbers = []
    overlap = []

    with open('happynumbers.txt') as f:
        line = f.readline()
        while line:
            line = line.strip()
            happynumbers.append(line)
            line = f.readline()

    with open('primenumbers.txt') as p:
        line = p.readline()
        while line:
            primenumbers.append(line.strip())
            line = p.readline()

    #print(happynumbers)
    #print(primenumbers)

    for x in primenumbers:
        if x in happynumbers:
            overlap.append(x)

    print(overlap)

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise5():
    print("Tic Tac Toe")
    print("--------------------------------")

    '''
    Its the classic game of Tic Tac Toe!
    '''
    print("Welcome to the classic game of Tic Tac Toe!")

    #Game Rules
    print("""
    Rules:

    Select the cordinates on the game board where you'd like to place your mark.
    Player1 is an 'X' and Player2 is an 'O'
    The first person to get three in a row wins!

    The game board looks like this,

    ___|___|_X_
    ___|___|___
       |   |

    The 'X' is at the cordinates (1, 3). Where One is the row and Three is the
    column.
    """)


    game = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]


    #Conducts win checking
    def win_checker(player):
        #Column check
        #If the column of the 2d array 'game' is all the same value (the players value), return a win status
        if game[0][0] == player and game[1][0] == player and game[2][0] == player:
            print("Left column, player{:d} wins!".format(player))
            exit()
        elif game[0][1] == player and game[1][1] == player and game[2][1] == player:
            print("Middle column, player{:d}wins!".format(player))
            exit()
        elif game[0][2] == player and game[1][2] == player and game[2][2] == player:
            print("right column, player{:d} wins!".format(player))
            exit()
        #Row check
        elif game[0][0] == player and game[0][1] == player and game[0][2] == player:
            print("Top row, player{:d} wins!".format(player))
            exit()
        elif game[1][0] == player and game[1][1] == player and game[1][2] == player:
            print("Middle row, player{:d} wins!".format(player))
            exit()
        elif game[2][0] == player and game[2][1] == player and game[2][2] == player:
            print("Bottom row, player{:d} wins!".format(player))
            exit()
        #Diagonal check
        elif game[0][0] == player and game[1][1] == player and game[2][2] == player:
            print("Diagonal, player{:d} wins!".format(player))
            exit()
        elif game[0][2] == player and game[1][1] == player and game[2][0] == player:
            print("Diagonal, player{:d} wins!".format(player))
            exit()
        else:
            return "null"


    #Processes user input
    def player_move(player):
        #Tells the player to go
        print("Player{:d} choose your move,".format(player))
        player_row = int(input("Choose your row, ")) - 1
        player_col = int(input("Choose your column, ")) - 1
        #player_mov = [player_row, player_col]
        #return player_mov
        if game[player_row][player_col] != 0:
            print("The other player has already chosen that space!")
            print("Please enter a different set of cordinates, ")
            player_move(player)
        else:
            game[player_row][player_col] = player
            '''
            for x in game:
                print(x)
            '''
            game_board()

    #Print board
    def game_board():
        #First Row
        a = game[0][0]
        #print(a)
        if a == 0:
            a = '_'
        elif a == 1:
            a = 'X'
        elif a == 2:
            a = 'O'
        b = game[0][1]
        #print(b)
        if b == 0:
            b = '_'
        elif b == 1:
            b = 'X'
        elif b == 2:
            b = 'O'
        c = game[0][2]
        #print(c)
        if c == 0:
            c = '_'
        elif c == 1:
            c = 'X'
        elif c == 2:
            c = 'O'

        #Second Row
        d = game[1][0]
        #print(d)
        if d == 0:
            d = '_'
        elif d == 1:
            d = 'X'
        elif d == 2:
            d = 'O'
        e = game[1][1]
        #print(e)
        if e == 0:
            e = '_'
        elif e == 1:
            e = 'X'
        elif e == 2:
            e = 'O'
        f = game[1][2]
        #print(f)
        if f == 0:
            f = '_'
        elif f == 1:
            f = 'X'
        elif f == 2:
            f = 'O'

        #Third
        g = game[2][0]
        #print(g)
        if g == 0:
            g = '_'
        elif g == 1:
            g = 'X'
        elif g == 2:
            g = 'O'
        h = game[2][1]
        #print(h)
        if h == 0:
            h = '_'
        elif h == 1:
            h = 'X'
        elif h == 2:
            h = 'O'
        i = game[2][2]
        #print(i)
        if i == 0:
            i = '_'
        elif i == 1:
            i = 'X'
        elif i == 2:
            i = 'O'



        print('_{:s}_|_{:s}_|_{:s}_'.format(a, b, c))
        print('_{:s}_|_{:s}_|_{:s}_'.format(d, e, f))
        print(' {:s} | {:s} | {:s} '.format(g, h, i))

        '''
        #Player1's row
        if game[0][0] == 0 and game[1][0] == 0 and game[2][0] == 0:
            print('_{:s}_|_{:s}_|_{:s}_'.format('_', '_', '_'))
        elif game[0][0] == 1 and game[1][0] == 0 and game[2][0] == 0:
            print('_{:s}_|_{:s}_|_{:s}_'.format(player1, '_', '_'))
        elif game[0][0] == 1 and game[1][0] == 1 and game[2][0] == 0:
            print('_{:s}_|_{:s}_|_{:s}_'.format(player1, player1, '_'))
        elif game[0][0] == 1 and game[1][0] == 1 and game[2][0] == 1:
            print('_{:s}_|_{:s}_|_{:s}_'.format(player1, player1, player1))
        #Player2's row
        elif game[0][0] == 2 and game[1][0] == 0 and game[2][0] == 0:
            print('_{:s}_|_{:s}_|_{:s}_'.format(player2, '_', '_'))
        elif game[0][0] == 2 and game[1][0] == 2 and game[2][0] == 0:
            print('_{:s}_|_{:s}_|_{:s}_'.format(player2, player2, '_'))
        elif game[0][0] == 2 and game[1][0] == 2 and game[2][0] == 2:
            print('_{:s}_|_{:s}_|_{:s}_'.format(player2, player2, player2))
        #Mixed row
        elif game[0][0] == 1 and game[1][0] == 2 and game[2][0] == 2:
            print('_{:s}_|_{:s}_|_{:s}_'.format(player1, player2, player2))
        elif game[0][0] == 1 and game[1][0] == 1 and game[2][0] == 2:
            print('_{:s}_|_{:s}_|_{:s}_'.format(player1, player1, player2))
        elif game[0][0] == 2 and game[1][0] == 1 and game[2][0] == 1:
            print('_{:s}_|_{:s}_|_{:s}_'.format(player2, player1, player1))
        elif game[0][0] == 2 and game[1][0] == 2 and game[2][0] == 1:
            print('_{:s}_|_{:s}_|_{:s}_'.format(player2, player2, player1))
        '''


    game_board()
    #Game Loop
    def play_game():

        player_move(1)
        if win_checker(1) == 'null':
            player_move(2)
            if win_checker(2) == 'null':
                play_game()
        else:
            print("Game Over!")
            exit()

    play_game()

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise6():
    print("Guessing Game Two")
    print("--------------------------------")

    '''
    In a previous exercise, we’ve written a program that “knows” a number and
    asks a user to guess it.

    This time, we’re going to do exactly the opposite. You, the user, will have
    in your head a number between 0 and 100. The program will guess a number,
    and you, the user, will say whether it is too high, too low, or your
    number.

    At the end of this exchange, your program should print out how many guesses
    it took to get your number.

    As the writer of this program, you will have to choose how your program
    will strategically guess. A naive strategy can be to simply start the
    guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But
    that’s not an optimal guessing strategy. An alternate strategy might be to
    guess 50 (right in the middle of the range), and then increase / decrease
    by 1 as needed. After you’ve written the program, try to find the optimal
    strategy!
    '''

    print("Welcome to Guessing Game Two!")
    print()
    print("""
    Rules:

    Pick a number between 0 and 100. The program will attempt to guess the
    number you've choosen and after each guess you will tell the program if its
    guess is Higher than, 'h' or Lower than, 'l' your number or if it was
    correct (Yes) 'y'. Please don't cheat the poor program is too dumb to tell
    and you'll just end up playing the game forever.
    """)

    #Create list of potential guesses
    guesses = []
    for x in range(0, 101):
        guesses.append(x)
    #print(guesses)

    #Function for finding a given lists midpoint
    def midpoint(list):
        midpoint = list.index(list[(len(list)+1)//2])
        return midpoint

    #Recursive Guesser Function
    def guesser(list1):
        #Basecase: Checks if the list has only 2 items in it
        if len(list1) == 2:
            #If the list does only have two items then it prints the second item
            print("Your number is {:d}".format(list1[1]))
        #Else, it runs the main loop (does binary search)
        else:
            #Check if number is lists midpoint i.e. 51
            print("Is your number {:d}".format(list1[midpoint(list1)]))
            answer = input()
            #If is is game over
            if answer == 'y':
                print("Awesome! I Win!")
                print("Goodbye!")
                exit()
            #If users number is lower it recurs with list which is the lower half of the original list
            elif answer == 'l':
                new_guesses = list1[0:midpoint(list1)]
                guesser(new_guesses)
            #If users number is higher it recurs with a list which is the upper half of the original
            elif answer == 'h':
                new_guesses = list1[midpoint(list1):]
                guesser(new_guesses)
            else:
                print("I don't recognize your input.")
                print("Goodbye!")
                exit()

    #print(guesser(guesses))
    guesser(guesses)

    #print(guesses[midpoint(guesses):])
    '''
    print("Is your numer 1?")
    answer = input()
    if answer == 'h':
        print("Is your numer 2?")
        answer = input()
        if answer == 'h':
            print("Is your numer 3?")
            answer = input()
            if answer == 'h':
                print("Okay how about 4?")
                time.sleep(2)
                print("Lolz just kidding!")
                print("Lets start over for real this time :)")
            elif answer == 'l':
                print("It can't be!")
            elif answer == 'y':
                print("Awesome! I Win!")
                print("Goodbye!")
                exit()
            else:
                print("I don't recognize your input.")
                print("Goodbye!")
                exit()
        elif answer == 'l':
            print("It can't be!")
        elif answer == 'y':
            print("Awesome! I Win!")
            print("Goodbye!")
            exit()
        else:
            print("I don't recognize your input.")
            print("Goodbye!")
            exit()
    elif answer == 'l':
        print("It can't be!")
    elif answer == 'y':
        print("Awesome! I Win!")
        print("Goodbye!")
        exit()
    else:
        print("I don't recognize your input.")
        print("Goodbye!")
        exit()
    '''


    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise7():
    print("Check Tic Tac Toe")
    print("--------------------------------")

    '''
    As you may have guessed, we are trying to build up to a full tic-tac-toe
    board. However, this is significantly more than half an hour of coding,
    so we’re doing it in pieces.

    Today, we will simply focus on checking whether someone has WON a game of
    Tic Tac Toe, not worrying about how the moves were made.
    '''

    #Populate the game board with whatever test values you'd like
    game = [
    [1,1,0],
    [0,0,1],
    [1,1,1]
    ]
    print(game[1][1])

    def win_checker(player):
        #Column check
        if game[0][0] == player and game[1][0] == player and game[2][0] == player:
            print("Left column = player{:d}".format(player))
        elif game[0][1] == player and game[1][1] == player and game[2][1] == player:
            print("Middle column = player{:d}".format(player))
        elif game[0][2] == player and game[1][2] == player and game[2][2] == player:
            print("right column = player{:d}".format(player))
        #Row check
        elif game[0][0] == player and game[0][1] == player and game[0][2] == player:
            print("Top row = player{:d}".format(player))
        elif game[1][0] == player and game[1][1] == player and game[1][2] == player:
            print("Middle row = player{:d}".format(player))
        elif game[2][0] == player and game[2][1] == player and game[2][2] == player:
            print("Bottom row = player{:d}".format(player))
        else:
            print("Nobody's won yet!")

    win_checker(1)

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise8():
    print("Max Of Three")
    print("--------------------------------")

    '''
    Implement a function that takes as input three variables, and returns the
    largest of the three. Do this without using the Python max() function!

    The goal of this exercise is to think about some internals that
    Python normally takes care of for us. All you need is some variables and
    if statements!
    '''

    def max_of_three(a, b, c):
        if (a > b) and (a > c):
            return a
        elif (b > a) and (b > c):
            return b
        elif (c > b) and (c > a):
            return c
    print(max_of_three(1,28,16))

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
        2) Write to a File
        3) Read from a File
        4) File Overlap
        5) Tic Tac Toe
        6) Guessing Game Two
        7) Check Tic Tac Toe
        8) Max Of Three
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
