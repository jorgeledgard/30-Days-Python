# Excercise 1
empty_tpl = ()

# Excercise 2
brothers = ("Kevin", "Alex", "Jacob", "Dokja")
sisters = ("Sooyoung", "Sangah", "Heewon")

# Excercise 3
siblings = brothers + sisters

# Excercise 4
print(len(siblings)) # 7

# Excercise 5
siblings_ls = list(siblings)
siblings_ls.append("Persefone") # Mother
siblings_ls.append("Hades") # Father
family_members = tuple(siblings_ls)
print(family_members)

# Level 2: Excercise 1
# I put it here because is related
siblings = family_members[0:7]
parents = family_members[-2:]
print(siblings)
print(parents)