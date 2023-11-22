str = "sanskriti is a good girl"

# Prints first character of the string
print(str[0])

print(str[0:9])
print(str[9:])
print(str[:9])

print(str.split(" "))
print(str.split(" ",1))
print(str.split(" ",2))

print(str.find("good"))
print(str.capitalize())
print(str.upper())

print(str.replace("good", "bad"))

str1 = "Once uPon a time. tHERe was a cleVar bitCH, SHe used to viIit everhOuse of the VIllage at miDNight"
word = "There"

# is a specic word is present in str1 for this .. we will use .lower fontion to bring them in same formate
print(bool(word in str1))
print(bool(word.lower() in str1.lower()))


#printing variable in a sentense
ver_1 = "Indian"
print("The moon is {}".format(ver_1))
print("The moon is %s"%ver_1)

#letest technique using f string
print(f"The moon is {ver_1}")

