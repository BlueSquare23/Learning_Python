#!/usr/bin/python3
#Intro to Classes
#See intro_to_classes.py script which this one is meant to be use in conjunction with.

#Include a class the way you would import any other library.
from intro_to_classes import Person

#Create an instance of a class ie. an object
p = Person("John", 24)
#Call the methods defined by the class on the object
p.say_name()
p.say_age()
