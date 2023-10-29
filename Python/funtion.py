#!/bin/python3

def nl():
    print("\n") 

nl() # new line function

def who_am_i(): # this is a function with no arguments
    name = "Kris" # this is a local variable
    age = 30 # this is a local variable
    print(f"my name is {name}, and I am {age} years old")

    # veriables created in a function are not accessible outside of it


who_am_i() 

def add_one_hundred(num):
    print(num + 100)

add_one_hundred(100)


def add (x, y):
    print(x + y)

add(7, 7)

def multiply(x, y):
    return x * y

print(multiply(8, 7))
    

nl()

def square_root(x):
    print(x ** .5)

square_root(64)