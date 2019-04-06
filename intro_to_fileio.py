#!/usr/bin/python3
#File Input/Output

#Open/open modes
'''
The open() function takes two arguments, first is the path
to the file and the second is the read/write/access mode.
There are several diffent file access modes,
* r  = open for read
* w  = open for write, truncate (wipe out existing data)
* rb = open read only (binary)
* r+ = open for read/write
* w+ = open for read/write, truncate (wipe out existing data)
* a+ = open for read/append
'''
#To open a file use the open() function
file = open("file.txt", "r+")
'''
Note ^ the above variable does not contain the contents of file.txt.
It simply contains the file object itself. To select the files contents
use alternative methods. See below,
'''
'''
#Read (Uncomment to see in action)
text = file.read()
print(text)
'''
#Iterate over line in a file
for line in file:
    print(line)

#Write/append
file = open("file.txt", "a+")
file.write('5\n')
file.write('6\n')
textnew = file.read()
print(textnew)

#close file
file.close()
