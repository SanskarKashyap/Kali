money = int(input("How much money do you have? : "))
age = int(input("How old are you? : "))


def Drink(money,age):
    if money >= 5 and age >= 18:
        print("You can buy a beer")
    elif money >= 5 and age < 18:
        print("You can buy a coke")
    else:
        print("You can't buy anything")


Drink(money,age) 