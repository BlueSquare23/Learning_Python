#!/usr/bin/python3
#Modules
#Section 7.1

#Import the math module to have access to many math functions
import math

print(math.pi)
print(math.cos(math.pi))

#Import just pi
from math import pi
#Ex.
print(pi)

#Import everything from a Module
from math import *

#Import functions as a different name
from math import factorial as f
#Ex.
print(f(0))
print(f(1))
print(f(2))
print(f(3))
