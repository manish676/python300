# Exercise 1: Manipulate Data in a Dictionary

person = {"name":"Jack", "age": 23 , "grade": "A"}

# Add New Value
# person["Address"] = "123 Delhi"

# Update Age
person["age"] = 25

# Remove grade
if "grade" in person:
    del person["grade"]
print(person)

