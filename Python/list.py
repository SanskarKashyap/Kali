movie = ["Massan","Gangs Of Wassepur","Article 21","The Dark Knight"]

print(movie.index("The Dark Knight"))  # indexing starts from 0

print(movie[-1]) # returns last element

print(movie[1:3]) # returns elements from index 1 and 2

print(movie[1:])

print(movie[:3])

movie.append("3 Idiots")

print(movie)

movie.insert(1,"The Shawshank Redemption")

print(movie)

movie.remove("Article 21")

print(movie)

movie.pop() # remove last element

print(movie)

Grades = [("Rahul",90),("Rohit",80),("Raj",70)]

print(Grades)

Rahul_grade = Grades[0][1]
Rohit_grade = Grades[1][1]

print(Rahul_grade)