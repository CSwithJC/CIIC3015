# Create a 2D List
list_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate through the list and print each row using a while loop:
print("Iterate through 2D list using while loop.")
i = 0
while i < len(list_2d):
    print(list_2d[i])
    i += 1

# Iterate through the list and print each row using a for loop:
print("\nIterate through 2D list using for loop.")
for row in list_2d:
    print(row)

# Iterate through the list and print each item in each row using a for loop:
print("\nIterate through 2D list using for loop.")
for row in list_2d:
    for item in row:
        print(item)

# Iterate through the list and calculate the mean per row using a for loop:
print("\nCalculate mean per row using for loop.")
for row in list_2d:
    total = 0
    for item in row:
        total += item
    print(total / len(row))


# Iterate through the list and calculate the mean per row using a for loop:
print("\nCalculate mean of all numbers using for loop.")
total = 0
for row in list_2d:
    for item in row:
        total += item
num_rows = len(list_2d)
num_columns = len(list_2d[0])
print(total / (num_rows * num_columns))

