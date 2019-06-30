#!/usr/bin/python3
#prime_checker.py
#Episode 5.5 (example not written by John)

n = int(input("n = "))
if n >= 2:
    divisors = []
    for divisor in range(2, n):
        if n % divisor == 0:
            divisors.append(divisor)

    if len(divisors) == 0: #Means number is prime!
        print("{:d} is prime!".format(n))
    else:
        print("{:d} is Not prime because {:} divides {:d}".format(n, str(divisors), n))
elif n == 1:
    print("{:d} is a special case!".format(n))
else:
    print("{:d} is Not prime!".format(n))
