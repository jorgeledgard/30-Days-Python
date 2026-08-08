# We use input() to obtain the grade
grade = int(input("Enter your grade (from 0 to 100): "))

# We are gonna use a lot of conidtionals elif
if grade > 0:
    if 90 <= grade <= 100:
        print("You got an A")
    elif 80 <= grade <= 89:
        print("You got a B")
    elif 70 <= grade <= 79:
        print("You got a C")
    elif 60 <= grade <= 69:
        print("You got a D")
    else:
        print("You got a F")
else:
    print("Enter a positive value")