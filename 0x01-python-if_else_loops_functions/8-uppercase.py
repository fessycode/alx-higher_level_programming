#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) in range(97, 123):
            b = 32
        else:
            b = 0
        print("{:c}".format(ord(a) - b), end="")
    print()

