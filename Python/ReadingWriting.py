print("Reading and Writing Files")

print("--" *25)
print("Name of Days")
print("--" *25)

days = open('Python/days.txt', 'r')

# print(days.read()) # to read the file
# print(days.readlines()) # to read the lines of the file
# days.seek(0) # to reset the cursor to the beginning of the file
# print(days.readlines()) 

for day in days:
    print(day.strip())
days.close()

print("--" *25)
print("Name of Months")
print("--" *25)

month = open('Python/month.txt', 'w') #opening file for writing and creating a new file if not exist
month.write("January\n")
month.write("February\n")

month.close()

month = open('Python/month.txt', 'r') #opening file for reading 

# month.readlines() # not printable
print(month.readlines()) # printing the lines

month.seek(0)

print(month.read()) # print in list format

month.close()

month = open('Python/month.txt', 'a') #opening file for appending

month.write("March\n")
month.write("April\n")
month.write("May\n")    

month.close()

month = open('Python/month.txt', 'r') #opening file for reading

print(month.read()) # print in list format

month.seek(0)
print(month.readlines()) # printing the lines  
# month.close()

with open('Python/month.txt', 'r') as month:
    print("\nIt is generally recommended to use the with statement when working with files. This ensures that the file is properly closed even if an exception occurs.")
    print(month.read())