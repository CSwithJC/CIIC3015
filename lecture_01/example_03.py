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
# Savings after one year earning interest compounded monthly
# Savings after one year earning interest continuously compounded
# Quadratic Formula
# Area of a triangle given the lengths of its 3 sides (Heron's Formula)

print('End of Examples')