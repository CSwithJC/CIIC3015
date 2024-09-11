# Print all numbers from 0 to N using a for loop.
N = 100
for num in range(0, N+1):
    print(num)


# Print out the multiplication table for a specific number num.
print("\nMultiplication table example.")

def multiplication_table_of(number):
    print(f"\nThe multiplication table of {number} is:")
    for i in range(1, 11):
        print(f"{number} * {i} = {number * i}")

multiplication_table_of(5)
multiplication_table_of(6)
multiplication_table_of(9)
