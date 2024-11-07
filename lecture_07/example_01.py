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
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return nums[0]
        else:
            return nums[1]
    largest_first_two = recursive_largest_number_of_a_list(nums[:2])
    largest_remaining = recursive_largest_number_of_a_list(nums[2:])
    if largest_first_two > largest_remaining:
        return largest_first_two
    else:
        return largest_remaining

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

"""
Generate all permutations of a list.
For example, the permutations of [1, 2, 3] are:
[1,2,3]
[1,3,2]
[2,1,3]
[2,3,1]
[3,1,2]
[3,2,1]
"""
def permutations(nums):
    # Base case #1: nums is empty returns empty list (no permutations)
    if len(nums) == 0:
        return []
    # Base case #2: nums only has one number returns a list with only one permutation
    # (for example, [1] has only one number so the only perm is [1], so returns [[1]].
    if len(nums) == 1:
        return [nums]
    # If not a base case, iterate through each number in nums, get the permutations of the remaining numbers in the list
    # and add the original number alongside all the returned permutations as a new permutation.
    #
    # For example, if the list is [1, 2, 3], begin by saving 1. Get the permutations of the remaining numbers, which
    # are [2, 3] (this returns a list with [2, 3] and [3, 2]). Add the 1 at the start (or end) of [2, 3] and [3, 2]
    # and that creates the new permutations [1, 2, 3] and [1, 3, 2]. Continue the process by saving number 2,
    # generating the permutations of [1, 3], and repeating the process.
    perms = []
    for i in range(len(nums)):
        curr_num = nums[i]
        remaining_nums = nums[:i] + nums[i+1:]
        for perm in permutations(remaining_nums):
            new_perm = [curr_num] + perm
            perms.append(new_perm)
    return perms

print(permutations([1, 2, 3]))


