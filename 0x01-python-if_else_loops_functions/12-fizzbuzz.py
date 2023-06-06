#!/usr/bin/python3
def fizzbuzz():
    for buzz in range(1, 101):
        if buzz % 3 == 0 and buzz % 5 == 0:
            print("FizzBuzz", end='')
        elif buzz % 3 == 0:
            print("Fizz", end='')
        elif buzz % 5 == 0:
            print("Buzz", end='')
        else:
            print(buzz, end='')

        print(" ", end='')
