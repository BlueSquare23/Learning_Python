#!/usr/bin/python3
#Combining Loops, Iterables, and Conditionals
#Episode 5.4

#Program 1,
#Sum up all of the even numbers in the list "numbers"
numbers = [1,2,3,4,5,6,7,8,9]

total = 0 #initialize total as 0
#Use for loop to go trough the array, "numbers"
for n in numbers:
    if n % 2 == 0: #if n is even
        total = total + n #add n to total (increment total by n)
#Can also ^ be written as "total += n"
print(total)


#Program 2,
#Extract all of the consonents from a string
alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
vowels = 'aeiouAEIOU'
my_string = "Packt publishing rocks!"

#Need to keep track of consonents
characters = [] #Create empty array to do this
#Then fill array with consonents using for loop
for ch in my_string:
    if ch not in vowels and ch in alpha: #Grag all characters which are not in vowls but are in the alphabet
        characters.append(ch) #Then add those characters to list "characters"
consonants = ''.join(characters) #Turn array "characters" into a string named "consonants"
print(consonants)
