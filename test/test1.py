from alpha_term import AlphaTerm


term1 = AlphaTerm()
term2 = AlphaTerm(1, "y", 1)
term3 = AlphaTerm(1, "z", 5)
term4 = AlphaTerm(4, "t", 1)
term5 = AlphaTerm(2, "c", 2)

print(term1)  # Desired value: x
print(term2)  # Desired value: y
print(term3)  # Desired value: z⁵
print(term4)  # Desired value: 4t
print(term5)  # Desired value: 2c²
