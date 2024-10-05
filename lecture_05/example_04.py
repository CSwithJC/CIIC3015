# Create a string to be used for multiple operations
s = "this string is funny"

# Slicing:
print("Show the first seven characters of the string using slicing:")
print(s[:7])

# Upper/Lower
print("\nTurn all of the string's letters to uppercase using upper():")
s = s.upper()
print(s)
print("\nTurn all of the string's letters to lowercase using lower():")
s = s.lower()
print(s)

# Replace a word in the string using replace()
print("\nReplace a word in the string using replace():")
print(f"The string BEFORE replacing: {s}")
s = s.replace("funny", "sad")
print(f"The string AFTER replacing: {s}")

# Split a string by a whitespace into a list of strings using split()
print("\nSplit the string into a list of strings using split():")
print(f"The string: {s}")
print(f"The string after splitting: {s.split()}")
