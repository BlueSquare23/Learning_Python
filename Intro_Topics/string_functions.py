#!/usr/bin/python3
#Modules and Testing
#Section 7.4
#See modules_and_testing.py script which this file works in conjunction with.

#See which file this function is in
print(__name__)

#Creating a simple module
def first_half(s):
    return s[:len(s)//2]

def last_half(s):
    return s[len(s)//2:]

#Testing Modules

#See if we are currently running this script
#Using the below if statement simply says, "we are currently running this script what do you want me to do"
if __name__ == '__main__':
    print("Testing string functions")
    assert first_half("abcd") == "ab", "First half is failing"
    assert last_half("abcd") == "cd", "Last half is failing"
