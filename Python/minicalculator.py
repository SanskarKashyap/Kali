x = int(input("Enter the value of 1st variable x: "))
y = int(input("Enter the value of 2nd variable y : "))

Opprator = input("Select Opperator +, -, *, /, **, //    : ")

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

else :
    print("Invalid Opperator")