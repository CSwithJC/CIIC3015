# Create an empty list
names = []
print("Created an empty list:")
print(names)

# Add strings to the list using .append()
names.append("jean")
names.append("bienve")
names.append("agustin")
print("\nAdded elements to the list using append (one at a time):")
print(names)

# Add multiple strings to the list at one using .extend()
names.extend(["maria", "genesis", "jennifer"])
print("\nAdded elements to the list using append (one at a time):")
print(names)

# Add a name in the middle of the list using .insert()
names.insert(len(names) // 2, "mary")
print("\nAdded elements to the list using insert (multiple at a time):")
print(names)

# Remove the last element of the list and save it in a variable using .pop()
last_name_in_list = names.pop()
print("\nRemoved the last element in the list using pop:")
print(f"Popped element: {last_name_in_list}")
print(f"List after the pop(): {names}")

# Sort the list in alphabetical order using sort().
names.sort()
print("\nSorted the list in alphabetical order using sort():")
print(names)

# Created a new list with only the first 3 names of the list using slicing:
first_three_names = names[:3]
print(f"\nList with first three names: {first_three_names}")
print(f"Original list: {names}")

# Find the position in the list where "bienve" is:
print(f"\nFetched the location of \'bienve\' using index():")
print(names.index('bienve'))

# Create a list with numbers 0 through 1000
print(f"\nCreated a list with numbers 0 through 99:")
numbers = []
for num in range(100):
    numbers.append(num)
print(numbers)