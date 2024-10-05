"""
Given a list of integers nums, create a function called
total_sum() that returns the total sum of numbers in nums.
"""
def total_sum(nums):
    tot_sum = 0
    for num in nums:
        tot_sum += num
    return tot_sum

print("Function that returns the total sum of numbers in a list:")
print(total_sum([1, 2, 3, 4, 5])) # 15
print(total_sum([])) # 0
print(total_sum([100, 1000, 10000])) # 11100

"""
Given a list of integers nums, create a function called
average() that returns the average of numbers in nums.
"""
def average(nums):
    if len(nums) == 0:
        return 0
    tot_sum = 0
    for num in nums:
        tot_sum += num
    return tot_sum / len(nums)

print("\nFunction that returns the average of numbers in a list:")
print(average([1, 2, 3, 4, 5])) # 3.0
print(average([])) # 0
print(average([100, 1000, 10000])) # 3700.0

"""
Given a list of integers nums, create a function called
even() that returns a list with only the even numbers in nums.
"""
def even(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result

print("\nFunction that returns only the even numbers from a list:")
print(even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # [2, 4, 6, 8, 10]
print(even([])) # []
print(even([11, 22, 33, 44, 55, 66, 77, 88, 99])) # [22, 44, 66, 88]

"""
Given a list of integers nums, create a function called 
positives() that returns a list with only the positive 
numbers in nums.
"""
def positives(nums):
    result = []
    for num in nums:
        if num > 0:
            result.append(num)
    return result

print("\nFunction that returns only the positive numbers from a list:")
print(positives([4, -1, -2, -3, 12])) # [4, 12]
print(positives([])) # []
print(positives([-1, -3, -5, -7])) # []

"""
Given a list of floats nums, create a function called 
map() that returns a list with with all of the floats 
in nums turned into strings.
"""
def map(nums):
    result = []
    for num in nums:
        result.append(str(num))
    return result

print("\nFunction that returns a list with all numbers in nums turned into strings:")
print(map([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
print(map([])) # []
print(map([11, 22, 33, 44, 55, 66, 77, 88, 99])) # ['11', '22', '33', '44', '55', '66', '77', '88', '99']

"""
Given a list of strings my_list, create a function 
called concat() that returns a string with with all 
of the strings in my_list concatenated.
"""
def concat(strings):
    result = ''
    for string in strings:
        result += string
    return result

print("\nFunction that returns a string that concatenates all stings in a list:")
print(concat(['hello', 'my', 'name', 'is', 'jc'])) # hellomynameisjc
print(concat([])) # ''
