#!/usr/bin/python3
#Exercises section 4 (Scratch Paper)

import random

#Find exercises here https://www.practicepython.org/
def Exercise0():
    quit = 0
    while quit != "q":
        print("Welcome to my python practice excercises!")
        print("Type q to quit and select another exercise")

        quit = str(input())

    print("--------------------------------")

def Exercise1(): #Actually exercise 31
    print("Guess Letters")
    print("--------------------------------")
    '''
    Let’s continue building Hangman. In the game of Hangman, a clue word is
    given by the program that the player has to guess, letter by letter. The
    player guesses one letter at a time until the entire word has been guessed.
    (In the actual game, the player can only guess 6 letters incorrectly before
    losing).

    Let’s say the word the player has to guess is “EVAPORATE”. For this
    exercise, write the logic that asks a player to guess a letter and displays
    letters in the clue word that were guessed correctly. For now, let the
    player guess an infinite number of times until they get the entire word.
    As a bonus, keep track of the letters the player guessed and display a
    different message if the player tries to guess that letter again. Remember
    to stop the game when all the letters have been guessed correctly! Don’t
    worry about choosing a word randomly or keeping track of the number of
    guesses the player has remaining - we will deal with those in a future
    exercise.
    '''

    #Starting word
    word = "evaporate"
    #print(word[1])
    #print(len(word))
    print("Welcome to the Word Guessing Game!")
    print("Your job is to guess the word I'm thinking of letter by letter.")

    #For formatting use later (non-essential)
    ordinals = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eight", "ninth"]

    #This function take a positional argument and then determins if the user input is at that position in the word
    def letter_guess(position):
        print("Guess a letter: ")
        letter = str(input()).lower()
        #print(letter)
        if len(letter) > 1:
            print("Guess one letter at a time!")
            return(letter_guess(position))
        #If letter is the same as the str at position in word return letter
        elif letter == word[position]:
            print("Correct!")
            return(letter)
        #If not the same function calls itself and until right letter is found
        elif letter != word[position]:
            print("Its not {:s}!".format(letter))
            print("Guess again!")
            return(letter_guess(position))

    #Function takes position and of word guessed so far and prints out letters of word up to that point
    def word_so_far(position):
        part_word = []
        for x in range(0, position):
            part_word.append(word[x])
        #print(part_word)
        return(''.join(part_word))

    #Main game loop, prints out partial word and invokes game for next letter.
    for i in range(0, len(word)):
        print("The word so far is: {:s}".format(word_so_far(i)))
        letter_guess(i)
        print("The {:s} letter was, '{:s}'".format(ordinals[i], word[i]))

    print("Congradulations the word is, '{:s}!'".format(word))

    #Spacing for readability
    print()

    print("--------------------------------")

def Exercise2():
    print("Hangman")
    print("--------------------------------")
    '''
    In this exercise, we will finish building Hangman. In the game of Hangman,
    the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms)
    before they lose the game.

    In Part 1, we loaded a random word list and picked a word from it. In Part
    2, we wrote the logic for guessing the letter and displaying that
    information to the user. In this exercise, we have to put it all together
    and add logic for handling guesses.

    Copy your code from Parts 1 and 2 into a new file as a starting point. Now
    add the following features:

    Only let the user guess 6 times, and tell the user how many guesses they
    have left.
    Keep track of the letters the user guessed. If the user guesses a letter
    they already guessed, don’t penalize them - let them guess again.
    '''
    '''
    with open('sowpods.txt', 'r') as open_file:
        line = open_file.readline().strip()
        #267750 is number of lines (from wc -l)
        int = random.randint(0,267750)
        #print(int)
        line_list = []
        while line:
            line_list.append(line)
            line = open_file.readline().strip()
    word = line_list[int].lower()
    '''
    #Test word
    word = "aardvark"
    print(word)
    #List of used letters (appended to after getting input from user)
    guessed_letters = []
    #Number of guesses so far
    number_of_guesses = 0
    #Number of guesses used
    false_guesses_left = 6

    list_word = []

    #Takes user input and sanatizes it
    def user_input():
        print("Guess a letter: ")
        guess = str(input().lower())
        #Makes sure input is only one letter
        if len(guess) > 1:
            print("Please only guess one letter at a time!")
            return(user_input())
        #Makes sure input has not already been guessed
        elif guess in guessed_letters:
            print("You've already guesses that letter.")
            return(user_input())
        #Ships it off if its all clear
        else:
            return(guess)

    #Whole function (heart of the program) needs reworked
    def word_print(letter):
        return(word)

        '''
    def word_print(letter):
        if number_of_guesses == 0:
            #Turn word into list of letters in word
            l_word = []
            for x in word:
                if letter == x:
                    l_word.append("{:s} ".format(x))
                elif letter != x:
                    l_word.append("_ ")
            l_word = "".join(l_word)
            return(l_word)
        elif number_of_guesses > 0:
            for x in new_word:
                if letter in guessed_letters:
                    print("test")
            return(l_word)
        '''
    #Draws the appropriate game board for the number of guesses left
    def game_board(false_guesses_left):
        if false_guesses_left == 0:
            a = "O"
            b = "/"
            c = "|"
            d = "\\"
            e = "/"
            f = "\\"
        elif false_guesses_left == 1:
            a = "O"
            b = "/"
            c = "|"
            d = "\\"
            e = "/"
            f = ""
        elif false_guesses_left == 2:
            a = "O"
            b = "/"
            c = "|"
            d = "\\"
            e = ""
            f = ""
        elif false_guesses_left == 3:
            a = "O"
            b = "/"
            c = "|"
            d = ""
            e = ""
            f = ""
        elif false_guesses_left == 4:
            a = "O"
            b = "/"
            c = ""
            d = ""
            e = ""
            f = ""
        elif false_guesses_left == 5:
            a = "O"
            b = ""
            c = ""
            d = ""
            e = ""
            f = ""
        elif false_guesses_left == 6:
            a = ""
            b = ""
            c = ""
            d = ""
            e = ""
            f = ""
        print("""
                 ___
                |   |
                |   {:s}
                |  {:s}{:s}{:s}
                |  {:s} {:s}
                |
             -------
        """.format(a,b,c,d,e,f))

    #Draws the blank game_board for starters
    game_board(false_guesses_left)

    #Main game loop (ends when no false guesses remain)
    while false_guesses_left > 0:
        #Calls user_input and defines it as varriable letters
        letter = user_input()
        #Appends letter (users guess) to the end of the guessed_letters list
        guessed_letters.append(letter)
        print(guessed_letters)
        #If the letter is in the word alert that its there and call word_print
        if letter in word:
            print("The letter '{:s}' is in the word!".format(letter))
            #Needs reworked
            word_print(letter)

            #Increments the number of guesses at the end
            number_of_guesses += 1
        #If the guess is false (i.e. not in the word) prints the appropriate game_board
        elif letter not in word:
            game_board(false_guesses_left - 1)
            #Decreases the number of false guesses left
            false_guesses_left = (false_guesses_left -1)
            #Increments guess counter
            number_of_guesses +=1
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
        1) Guess Letters
        2) Hangman
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
