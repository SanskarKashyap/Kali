# tuple is just like list but immutable means you can't change it once it created 
# it can be used for security purpose

# tuple is created by using () brackets



tuple1 = (1,2,3,4,5,6,7,8,9,10)

print(tuple1)

print(tuple1.count(1))# count the number of occurance of 1 in tuple1

print(tuple1.index(7)) # return the index of 1 in tuple1

print(tuple.__sizeof__(tuple1)) # return the size of tuple1

print(type(tuple1)) # return the type of tuple1