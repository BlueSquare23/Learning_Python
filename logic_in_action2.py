#!/usr/bin/python3
#Logic in Action pt.2

#This program demonstraits some of the simple conditional and logical operation
#we've learned by preforming simply arithmatic on user input.

import sys #sys.exit() quits the program
print("Enter in a simple arithmatic operation")
print("Ex. 4 + 5")
line = input()
split = line.split()

if len(split) != 3:
    print("Incorrect formatting. System exiting...")
    sys.exit()

left = int(split[0])
operator = split[1]
right = int(split[2])

val = 0

if operator == '+':
    val = left + right
elif operator == '-':
    val = left - right
elif operator == '*':
    val = left * right
elif operator == '/':
    if right == 0:
        print("I N0 d0 d1vidy by Z3RoZ! I HALTz n0w!")
        sys.exit()
    val = left / right
else:
    print("Unknown operator: {operator}".format(operator=operator))

print("{line_expr} = {value:.2f}".format(line_expr=line, value=val))
