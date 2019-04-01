#!/usr/bin/python3
#The Shift Cipher
#Section 6.5

#Implementing the shift cipher,
#Will only work on letters a-z lowercase
#Let the user specify a shift value

'''
Basic Idea,
Give some input and a shift value, the shift cipher will shift
a strings letters by that value.

Ex.
"bcde" with shift 1 --> "cdef"
"bcde" with shift 3 --> "efgh"
"cats" with shift 1 --> "dbut"
"cats" with shift 0 --> "cats"
'''

alpha = "abcdefghijklmnopqrstuvwxyz"

#Shift functions

def encrypt(s, shift = 3):
    encrypted_str = ""
    for c in s:
        index = alpha.index(c)
        shifted_index = (index + shift) % len(alpha) #Remember 25 % 26 = 25 but 26 % 26 = 0 and 27 % 26 = 1 etc...
        encrypted_str += alpha[shifted_index]
    return encrypted_str

def decrypt(e, shift = 3):
    decrypted_str = ""
    for c in e:
        index = alpha.index(c)
        shifted_index = (index - shift) % len(alpha)
        decrypted_str += alpha[shifted_index]
    return decrypted_str
print(encrypt("helloworld"))
print(decrypt("khoorzruog"))
