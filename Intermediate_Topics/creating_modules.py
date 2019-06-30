#!/usr/bin/python3
#Creating Modules
#Section 7.3
#See importing_homemade_modules.py script which the one works in conjunction with.

'''
All that a module is, is a function defined in another script which
is seperate from the script you're working in.
'''


#Create a simple module to compute the volume of various 3D shapes
from math import pi

#Sphere
def sphere_vol(r):
    return (4/3)*pi*r*r*r

#Cube
def cube_vol(l, w, h):
    return l*w*h

#Cone
def cone_vol(r, h):
    return (pi*r*r)*h/3
