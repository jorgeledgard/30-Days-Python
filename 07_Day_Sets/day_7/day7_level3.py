# This is the list we will be using
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Excercise 1
lst = len(age)
st_age = set(age)
st = len(st_age)
print(f"If true lst is bigger than st if false st is bigger than lst: {lst > st}")

# Excercise 2
print("String is text, list is an ordered list of items, the tuple is an\nordered list of unique items and a set is an unordered list of a unique item")

# Excercise 3
string = "I am a teacher and I love to inspire and teach people."
# We are gonna use replace() and lower(), to see if anything is the same word
string_clean = string[:-1].lower()
lst_2 = string_clean.split()
# We transofrm it to set to see the unique words
st_2 = set(lst_2)
print(f"Number of unique words: {len(st_2)}")