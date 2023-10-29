quote = "India that is Bharat"
print(quote)
print(quote.upper()) # upper case
print(quote.lower()) # lower case
print(quote.title()) # title case

print(quote.__len__()) # length of string
print(len(quote)) # length of stringlindin
print(quote.find("is")) # find index of string

print(quote.replace("Bharat", "Hindustan")) # replace string

name = "Rahul"
age = 23

print("My name is " + name + " and I am " + str(age) + " years old") # concatenation
print("My name is {0} and I am {1} years old".format(name, age)) # string formatting

print("\n")

age += 1
print(f"My name is {name} and I am {age} years old        #AgeChanged ") # string formatting (python 3.6+)