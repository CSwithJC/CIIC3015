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
