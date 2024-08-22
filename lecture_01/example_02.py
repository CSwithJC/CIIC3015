# Addition
print("Addition Examples:")
print(1 + 1)  # Numbers
print(1 + 2.0)  # Implicit casting to a float because at least one of the numbers is a float
print("And" + "rea")  # Strings

# Subtraction
print("\nSubtraction Examples:")
print(0 - 1)
print(10 - 5.0)  # float
# Subtraction of strings is unsupported so this line throws an error:
#print("And" - "rea")

# Multiplication
print("\nMultiplication Examples:")
print(10 * 5)
print(10 * 5.0)  # float
print("yeah" * 10)
print("yeah" * 50)
# Multiplying strings by 0 or less just returns an empty string ("")
print("multiplying 'yeah' by 0 or less yields an empty string (''): ", "yeah" * 0)

# Division
print("\nDivision Examples:")
print("Division always returns floats, even if both numbers are ints")
print(10 / 5)

print("\nPEMDAS Examples:")
print("Notice how the parentheses change the results:")
print("3 + (1 + 4) * 2 vs. 3 + 1 + 4 * 2")
print(3 + (1 + 4) * 2)
print(3 + 1 + 4 * 2)
print("'lol' + 'ha' * 3 vs. ('lol' + ' ha') * 3")
print("lol" + "ha" * 3)
print(("lol" + " ha") * 3)
