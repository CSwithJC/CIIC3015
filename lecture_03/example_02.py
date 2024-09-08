# Create functions that convert Fahrenheit to Celsius, Celsius to
# Kelvin, and Fahrenheit to Kelvin. The formulas are:
# - Celsius = (Fahrenheit − 32) × 5 ⁄ 9
# - Kelvin = Celsius + 273.15

# 1. Create a function that converts Fahrenheit to Celsius and RETURNS
# the temperature in Celsius.
def convert_fahrenheit_to_celsius(fahrenheit):
  celsius = (fahrenheit - 32) * (5 / 9)
  return celsius

# 2. Create a function that converts Celsius to Kelvin.
def convert_celsius_to_kelvin(celsius):
  kelvin = celsius + 273.15
  return kelvin

# 3. Create a function that converts Fahrenheit to Kelvin, and it must reuse
# the one that converts from Celsius to Kelvin for convenience.
def convert_fahrenheit_to_kelvin(fahrenheit):
  celsius = convert_fahrenheit_to_celsius(fahrenheit)
  return convert_celsius_to_kelvin(celsius)

# Convert these two temperatures from Fahrenheit to Kelvin.
fahrenheit_1 = 80
fahrenheit_2 = 95

# Uses convert_fahrenheit_to_kelvin() directly
kelvin_1 = convert_fahrenheit_to_kelvin(fahrenheit_1)
print("kelvin_1 was created using convert_fahrenheit_to_kelvin():")
print(kelvin_1)

# Uses nested function calls.
kelvin_2 = convert_celsius_to_kelvin(convert_fahrenheit_to_celsius(fahrenheit_2))
print("kelvin_2 was created using nested function calls:")
print(kelvin_2)