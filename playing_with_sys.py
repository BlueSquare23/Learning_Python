#!/usr/bin/python3
#Playing with sys
import sys
import fileinput

#Playing with the sys library
'''
sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')
var = str(sys.stdin)
print(var)
'''
#trying to figure out .strip function (Didn't work)
'''
for line in sys.stdin:#.strip():
    print(line)
    line.strip()
    ls.append(line)

print(ls)

f = open('data.txt', 'r')
for line in f:
    line = line.replace('\n', '')    # remove '\n' only
    print(line)

f.close()
'''

#Working on converting lists to stings and stripping the new line character (Did work)
'''
print(ls)
print(ls[0:1])
#str = "".join(ls)
str1 ="".join(ls[0:1])
str2 ="".join(ls[1:2])
str3 = str1.strip("\n") + " " + str2.strip("\n")
#print(str.strip("\n")) #strip string's new line char
print(str3)
'''

'''
I'm trying to strip the damn new line character off of the elements of this list.
The list comes from stdin and is the output of a cat.
I'm trying to do this by converting the list to a set of strings, then stripping the
new line characters, then converting each of these strings back into a list.
I'm currenly struggeling to do this...
Update: I figured it out!!!
'''
#initialize empty lists
ls1 = []
ls2 = []
#initialize empty counters
counter = 0
counter1 = 1
#Break apart the lines in stdin
for line in sys.stdin:
    #Create a list of the lines in stdin
    ls1.append(line)
    #Take list1 at index of line and turn into a string
    str = "".join(ls1[counter:counter1])
    #Strip the damn new line character
    str = str.strip("\n")
    print(str)
    #Add the newly stripped string back to new list2 as first element
    ls2.append(str)
    #Iterate the counters
    counter += 1
    counter1 += 1

print(ls2)

#Final note
'''
Awesome! now that I've turned the line elements of stdin into a list,
(with no new line characters!) I can compare it to another list to
see if the elements of the two are different. I may eventually develop
this into a command line tool to compare the differences b/w two lists
of IP addresses to which IP's are repeate offenders.

* Keep in mind the below method of comparing two lists
>>> S1 = set(L1)
>>> S2 = set(L2)
>>> S1.intersection(S2)
set([2])
'''
