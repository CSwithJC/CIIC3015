# Create two separate sets of numbers.
hello_letters_set = set('hello')
world_letters_set = set('world')
print('Create two sets, one from \'hello\' and the other from \'world\'')
print(hello_letters_set)
print(world_letters_set)

# Set Operations:
print('\nThe letters that both words have in common (intersection) are:')
print(hello_letters_set.intersection(world_letters_set))

print('\nThe combined letters across both strings (union) are:')
print(hello_letters_set.union(world_letters_set))

print('\nThe letters in \'hello\' but not in \'world\' (difference) are:')
print(hello_letters_set.difference(world_letters_set))
print('The letters in \'world\' but not in \'hello\' (difference) are:')
print(world_letters_set.difference(hello_letters_set))
