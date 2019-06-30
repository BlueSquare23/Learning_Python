#!/usr/bin/python3
#Importing Homemade Modules
#Section 7.3
#See creating_modules.py script which the one works in conjunction with.

#To import a library simply provide the name of the other script (w/out .py)
import creating_modules

print(dir(creating_modules))

print(creating_modules.cube_vol(2,3,4))
