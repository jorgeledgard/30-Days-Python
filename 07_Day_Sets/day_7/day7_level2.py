# Sets we will be using 
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# Excercise 1
C = A.union(B)
print(C) # If the item its in both sets it inlcudes only one 

# Excercise 2
print(A.intersection(B))

# Excercise 3
sub = A.issubset(B)
print(f"Its A a subset of B: {sub}")

# Excercise 4
dis = A.isdisjoint(B)
print(f"Are A and B disjoint sets: {dis}")

# Excercise 5
st_A_B = A.union(B) # Union of A with B
print(A)

st_B_A = B.union(A) # Union of B with A
print(B)

# Excercise 6
print(A.symmetric_difference(B))

# Excercise 7
del A
del B