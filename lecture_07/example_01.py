# Print Numbers 0 through 99 using recursion.
def recursive_print_aux(i, n):
    if i == n:
        return
    print(i)
    recursive_print_aux(i + 1, n)

def recursive_print(n):
    recursive_print_aux(0, n)

print("\nPrint numbers 0 through 100 recursively!")
recursive_print(100)

# Return a list with numbers 0 through n-1 recursively.
def recursive_add_nums_to_list_aux(nums, n, i):
    if i == n:
        return
    nums.append(i)
    recursive_add_nums_to_list_aux(nums, n, i + 1)

def recursive_add_nums_to_list(n):
    nums = []
    recursive_add_nums_to_list_aux(nums, n, 0)
    return nums

print("\nAdd numbers 0 througn n-1 to a list recursively!")
print(recursive_add_nums_to_list(100))

# Return the power of a number recursively.
def recursive_power_function(base, exponent):
    if exponent == 0:
        return 1
    return base * recursive_power_function(base, exponent-1)

print("\nCalculate the power of a number recursively!")
print(recursive_power_function(2, 6))

# Find largest number of a list recursively.
def recursive_largest_number_of_a_list(nums):
    if len(nums) == 1:
        return nums[0]
    return max(nums[0], recursive_largest_number_of_a_list(nums[1:]))

print("\nLargest Number of a list recursively!")
print(recursive_largest_number_of_a_list([100, 500, 40, 700, -50, 800]))
print(recursive_largest_number_of_a_list([-100, -500, -40, -700, -50, -800]))

# Reverse a string recursively.
def recursive_reverse_a_string(string):
    if len(string) == 0:
        return ''
    return recursive_reverse_a_string(string[1:]) + string[0]

print("\nReverse a string recursively!")
print(recursive_reverse_a_string("word"))
print(recursive_reverse_a_string("task"))
print(recursive_reverse_a_string("crazy"))

