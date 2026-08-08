person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Excercise 1 
if "skills" in person:
    middle = len(person["skills"]) // 2
    print(f"Middle of the list skills: {person["skills"][middle]}")

# Excercise 2
if "skills" in person:
    if "Python" in person["skills"]:
        print("There it is Python skill")
    else:
        print("There isn't Python skill")

# Excercise 3
set_skills = set(person["skills"])
front_end = {"JavaScript", "React"}
back_end = {"Python", "Node", "MongoDB"}
full_stack = {"MongoDB", "React", "Node"}

if front_end == set_skills:
    print("He is a front end developer")
elif back_end == set_skills:
    print("He is a back end developer")
elif full_stack == set_skills:
    print("He is a full stack developer")
else:
    print("Unknown title")

# Excercise 4
if person["is_married"] == True and person["country"] == "Finland":
    print(f"{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is married")