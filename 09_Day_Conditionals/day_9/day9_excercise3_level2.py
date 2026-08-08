# We use input to obtain a fruit
fruit = input("Give me a fruit: ")
fruits = ['banana', 'orange', 'mango', 'lemon']

# We use the conditionals to see if it already exits or we need to include it
if fruit not in fruits:
    fruits.append(fruit)
    print(fruits)
elif fruit in fruits:
    print("That fruit already exist")