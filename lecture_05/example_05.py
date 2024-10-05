words = ['this', 'string', 'is', 'funny']
print(words)

# Iterate through list of strings using a while loop.
print("Print all words in the list using a while loop:")
i = 0
while i < len(words):
    print(words[i])
    i += 1

# Iterate through list of strings using a for loop.
print("\nPrint all words in the list using a for loop:")
for word in words:
    print(word)

# Iterate through all CHARACTERS of all words using a while loop.
print("\nPrint all characters of all words in the list using a while loop:")
i = 0
while i < len(words):
    j = 0
    while j < len(words[i]):
        print(words[i][j])
        j += 1
    print()
    i += 1

# Iterate through all CHARACTERS of all words using a for loop.
print("\nPrint all characters of all words in the list using a for loop:")
for word in words:
    for char in word:
        print(char)
    print()
