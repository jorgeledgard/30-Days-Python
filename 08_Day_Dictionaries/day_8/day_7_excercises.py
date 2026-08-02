# Excercise 1
dog = {}

# Excercise 2
dog["name"] = "Max"
dog["color"] = "Brown"
dog["breed"] = "Golden retriver"
dog["legs"] = 4
dog["age"] = 2
print(dog)

# Excercise 3
student = {
    "first_name": "Kim",
    "last_name": "Dokja",
    "gender": "Male",
    "age": 28,
    "marital_status": "Single",
    "skills": [],
    "country": "South Korea",
    "city": "Seoul",
    "adress": "In my heart:("
}

# Excercise 4
print(len(student)) # 9

# Excercise 5
print("Value of skills:", student["skills"])
print("The data type of skills:", type(student["skills"]))

# Excercise 6
student["skills"].append("Reader")
student["skills"].append("Dying")
print("Skills:", student["skills"])

# Excercise 7
info = student.keys()
print(f"List of info available of the student:\n {info}")

# Excercise 8
act_info = student.values()
print(f"Actual info of the student:\n {act_info}")

# Excercise 9
info_re = student.items()
print(f"Related info:\n {info_re}")

# Excercise 10
del student["adress"]
print(f"Eliminateing adress:\n {student}")

# Excercise 11
del student
print(student)