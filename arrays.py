courses = ["MIT","Cyber security","Data Science"]
print(courses)

# accessing an element
print( courses[2])

# looping through an array
for x in courses:
    print("Course is", x)

# adding a new element in an array
courses.append("Laravel")
print(courses)

# removing an element from an array
courses.remove("MIT")
print(courses)