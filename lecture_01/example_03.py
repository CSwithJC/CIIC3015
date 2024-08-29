import math

# CIIC 3015 Intro to Programming
# Topic: Expressions and Variables
# Some common mathematical formulas used in everyday life

# Converting Fahrenheit to Celsius
# Using input() to prompt the user for the temperature:
# fahrenheit = int(input("what is the temperature in fahrenheit?"))
fahrenheit = 32
celsius = (fahrenheit - 32) * 5 / 9
print(fahrenheit, 'degrees Fahrenheit is equivalent to', celsius, 'Celsius')

# Converting Celsius to Fahrenheit
celsius = 0
fahrenheit = 9 / 5 * celsius + 32
print(celsius, 'degrees Celsius is equivalent to', fahrenheit, 'Fahrenheit')

# Perimeter of a rectangle
width = 10
height = 20
perimeter = 2 * width + 2 * height
print('The perimeter of a',width,'by',height,'rectangle is',perimeter)

# Area of a Circle
radius = 1
area = radius ** 2 * math.pi
print('The area of a circle of radius', radius, ' is ', area)

# Distance between two points (x1,y1) and (x2,y2)
x1 = 0.0
y1 = 0.0
x2 = 1.0
y2 = 0.0
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

# Savings after one year earning simple interest
annual_interest = 10
balance_before = 100
balance_after = balance_before * (1 + (annual_interest / 100))
print(f'After one year {balance_before} dollars will grow to {balance_after:.2f}',
      f'dollars at {annual_interest} percent annual interest')

# Savings after n years earning simple interest
annual_interest = 10
balance_before = 100
years = 5
balance_after = balance_before * ((1 + (annual_interest / 100)) ** years)
print(f'After {years} years {balance_before} dollars will grow to {balance_after:.2f}',
      f'dollars at {annual_interest} percent annual interest')

# Quadratic Formula to find zeros of polynomial ax^2 + bx + c
a = 1
b = 4
c = -5
discriminant = b*b - (4 * a * c)
first_root = (-b + math.sqrt(discriminant)) / (2 * a)
second_root = (-b - math.sqrt(discriminant)) / (2 * a)
print(f'Roots of polynomial {a}x^2 + {b}x + {c} are {first_root} and {second_root}')

# Area of a triangle given the lengths of its 3 sides a, b, and c (Heron's Formula)
a = 3
b = 4
c = 5
s = (a+b+c) / 2 # semiperimeter
area = math.sqrt(s * (s - a) * (s-b) * (s - c))
print(f'Area of triangle with sides {a}, {b}, and {c} is {area}')

print('End of Examples')
