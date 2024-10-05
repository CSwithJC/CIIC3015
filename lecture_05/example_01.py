# Create a list of ints.
numbers = [1, 2, 3, 4, 5]

# Iterate through the list and print each number.

# Using a while:
print("\nPrint all numbers using a while loop:")
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

# Using a for:
print("\nPrint all numbers using a for loop:")
for num in numbers:
    print(num)

# Print only even numbers.
print("\nPrint only the even numbers in the list using a for loop:")
for num in numbers:
    if num % 2 == 0:
        print(num)

# Access the last element of the list (with len()).
print("\nLast element of list (using len()):")
print(numbers[len(numbers)-1])

# Access the last element of the list (with negative indexing).
print("\nLast element of list (using negative indexing):")
print(numbers[-1])
