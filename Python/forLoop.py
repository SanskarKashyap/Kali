vegitable = ["carrot", "potato", "onion", "tomato", "cucumber", "lettuce", "cabbage", "broccoli", "cauliflower", "spinach"]
fruit = ["apple", "orange", "banana", "grape", "mango", "pineapple", "pear", "peach", "plum", "strawberry"]     

print("\nList of vegitables: ")
for x in vegitable:
    print(x)

print("\nList of fruits: ")
for x in fruit:
   print(x)

print("\nList of IP addresses: ")
for ip in range(1, 11):
    ping = f"ping 192.168.1.{ip}" # string formatting (python 3.6+)
    print(ping)
