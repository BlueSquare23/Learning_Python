#!/usr/bin/python3
#Into to Conditionals
#Python course section 4

#Intro to control flow
#The ability for a program to make decisions

age = 35
if age == 35:
    print("Age is equal to 35!")

name = "Megan"
if name == "Megan":
    print("Her name is Megan!")
    if age == 35:
        print("Megan is 35 years old!")

#Compairson Opperators
# ==, !=, <, >, <=, >=
tmp = """
(-100000, -30] Really Cold!
(-30, 0)       Pretty Cold!
0              Zero
(0, 20)        Warm
[20, 40)       Pretty Hot!
[40, 1000000)  Really Hot!
"""
print("What Temperature is it?")
print(tmp)

#t = int(input())
t = 5
if (t <= -30):
    print("Really Cold!")
if (t < 0):
    if (t > 20):
        print("Pretty Cold!")
if (t == 0):
    print("Zero")
if (t > 0):
    if (t < 20):
        print("Warm")
if (t >= 20):
    if (t < 40):
        print("Pretty Hot!")
if (t >= 40):
    print("Really Hot!")

#Else and Elif

#else
name = "Sarah"
if name == "John":
    print("Hi John")
else:
    print("The was not John")

#elif
if name == "Emily":
    print("Hi Emily")
elif name == "Mike":
    print("Hi Mike")
elif name == "Bob":
    print("Hi, Bob")
else:
    print("I don't know your name")

#Another example
n = 55
if n < 20:
    print("n < 20")
elif n < 40:
    print("n < 40")
elif n < 60:
    print("n < 60")
else:
    print("n >= 60")

#And, Or, & Not
T = True
F = False

statement1 = 3 > 4 #False
statement2 = 10 % 5 == 0 #True
statement3 = "A".lower() == "a" #True
print(statement1)
print(statement2)
print(statement3)
print("")
#Or Truth-table
if F or F: print("F or F")
if F or T: print("F or T")
if T or F: print("T or F")
if T or T: print("T or T")
print("")
#And Truth-table
if F and F: print("F and F")
if F and T: print("F and T")
if T and F: print("T and F")
if T and T: print("T and T")
#Not Truth-table
if not F: print("not F")
if not T: print("not T")

if not(3 == 6) == (3 != 6):
    print("True")


#Logic in Action!
#See script logic_in_action.py
