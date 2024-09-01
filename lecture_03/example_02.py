# Convert these two temperatures from Fahrenheit to Kelvin.
# The formulas are:
# - Celsius = (Fahrenheit − 32) × 5 ⁄ 9
# - Kelvin = Celsius + 273.15
fahrenheit_1 = 80
fahrenheit_2 = 95

# 1a. Create a function that converts Fahrenheit to Celsius and RETURNS
# the temperature in Celsius. Save one of the two in a variable celsius_1
print("1. Function that converts Fahrenheit to Celsius")
def convert_fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * (5 / 9)
  return celsius

# 1b. Call the function. Save the first conversion in a variable and
# print the second directly.
# Convert fahrenheit_1:
celsius_1 = convert_fahrenheit_to_celsius(fahrenheit_1)
# Convert fahrenheit_2:
print(convert_fahrenheit_to_celsius(fahrenheit_2))

# 2a. Create a function that converts Celsius to Kelvin.
print("\n2. Function that converts Celsius to Kelvin")
def convert_celsius_to_kelvin(celsius):
  kelvin = celsius + 273.15
  return kelvin

# 2b. Convert fahrenheit_1 and fahrenheit_2 into kelvin and save them
# both in kelvin_1 and kelvin_2. The conversion of fahrenheit_1 to
# kelvin_1 uses celsius_1. However, the conversion of fahrenheit_2 to
# kelvin_2 uses nested functions in the parameters.

# Uses celsius_1
kelvin_1 = convert_celsius_to_kelvin(celsius_1)
print("kelvin_1 was created using the saved celsius_1:")
print(kelvin_1)
# Uses nested function calls.
kelvin_2 = convert_celsius_to_kelvin(convert_fahrenheit_to_celsius(fahrenheit_2))
print("however, kelvin_2 was created nested function calls:")
print(kelvin_2)