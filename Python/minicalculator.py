from math import *
# import math as m 




x = int(input("Enter the value of 1st variable x: "))
y = int(input("Enter the value of 2nd variable y : "))

Opprator = input("Select Opperator +, -, *, /, **, //, sqrt,    : ")

if Opprator == '+' : 
    print("Addition of x and y is : "+ str(x+y))

elif Opprator == '-' : 
    print("Subtraction of x and y is : "+ str(x-y))

elif Opprator == '*' :
    print("Multiplication of x and y is : "+ str(x*y))

elif Opprator == '/' :
    print("Division of x and y is : "+ str(x/y))

elif Opprator == '**' :
    print("Exponent of x and y is : "+ str(x**y))

elif Opprator == '//' :
    print("Floor Division of x and y is : "+ str(x//y))

elif Opprator == 'sqrt' :
    print("Square Root of x is : "+ str(sqrt(x)))
    print("Square Root of y is : "+ str(sqrt(y)))

else :
    print("Invalid Opperator")