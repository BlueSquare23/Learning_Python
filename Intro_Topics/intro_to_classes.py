#!/usr/bin/python3
#Intro to Classes
#See use_classes.py script which this one is meant to be use in conjunction with.

#Classes are essentially just a set of related things.
#A class is a code template for creating objects.
#Objects have member variables and have behaviour associated with them.

#Define a class using the "class" keyword
class Person:

#Initialize class variables
    name = None
    age = None

#Define class functions
    '''
    Define inclusion function below w/ "__init__" keyword.
    This function allows the vars, name & age to be
    asigned when a function from this class is called.
    '''
    def __init__(self, name, age): #Note that the first argument is self
        self.name = name  #Access this class attribute with the "self" keyword
        self.age = age

#Define other
    def say_name(self):
        print("My name is %s" % self.name)

    def say_age(self):
        print("My age is %s" % self.age)
