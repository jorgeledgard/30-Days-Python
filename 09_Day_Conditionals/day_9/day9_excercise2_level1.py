# Usin input() to get both ages
my_age = int(input("What is my age: "))
your_age = int(input("What is his/her age: "))

if my_age > your_age:
    print(f"I'm {my_age - your_age} years older than you")
elif my_age < your_age:
    print(f"You are {your_age - my_age} years older than me")
else:
    print("We are the same age")