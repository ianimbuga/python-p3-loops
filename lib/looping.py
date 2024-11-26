#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    x = 10
    while x >= 0:
        
        if x == 0:
            print("Happy New Year!")
        else:
            print(f"{x}")
        x -= 1
    pass

def square_integers(int_list):
    newlist = []
    for integer in int_list:
        newlist.append(integer ** 2)
    return newlist


def fizzbuzz():
    numbers = 0
    while numbers < 100:
        numbers += 1
        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz")
        elif numbers % 3 == 0:
            print("Fizz")
        elif numbers % 5 == 0:
            print("Buzz")
        else:
            print(numbers)