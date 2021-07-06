#!/usr/bin/env python3 

import os
import sys

myFile = sys.argv[1]

firstline = "This is the first line"
secondline = "This is the second"

print("[+] Preserving Original Data")
with open(myFile, 'r') as original: 
    data = original.read()

print("[+] Injecting New Lines")
with open(myFile, 'w') as modified: 
    modified.write(firstline + "\n" + secondline + "\n" + data)

print("[+] Done")
