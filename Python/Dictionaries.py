# dictionary is like list but it has key and value pair {"key": [value1, value2, value3]}
# dictionary is mutable
# dictionary is unordered

# create dictionary

employ = {"IT": ["John", "Bob", "Alice"], "HR": ["Jack", "Tom", "Jerry"]}


print(employ)

print(employ["IT"])

employ.update({"IT": ["John1", "Bob1", "Alice1", "Mike1"]})   #overwrites existing one 

print("Updated List 1:",employ)

my_dict = {"name": "John", "age": 25, "city": "New York"}

print(my_dict)

my_dict["email"] = ["johnkumar69@gmail.com", "haha@gmail.com"]
my_dict.update({"phone": "1234567890"})

print(my_dict)

my_dict["age"] = 26

print(my_dict["age"])
print(my_dict.get("age"))