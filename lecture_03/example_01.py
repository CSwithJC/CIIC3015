# 1a. Create a function that prints "Hello, World!" when called.
print("1. Function that prints Hello, World!")
def print_hello_world():
    print("Hello, World!")

# 1b. Call the function. Look at the console after calling this.
print_hello_world()

# 2a. Create a function that receives a name as a parameter and prints
# a greeting to the name.
print("\n2. Function that greets a person.")
def greet_a_person(name):
    print("Hello " + name + "!")

# 2b. Call the function with your name.
greet_a_person("Jean Carlos")

# 3a. Create a function receives a temperature in Celsius, converts to to
# Fahrenheit and prints the converted temperature.
print("\n3. Function that converts Celsius to Fahrenheit.")
def convert_celsius_to_fahrenheit(celsius):
  """Converts Celsius to Fahrenheit."""
  fahrenheit = 9 / 5 * celsius + 32
  print(fahrenheit)

# 3b. Call the function multiple times by passing different temperatures
# in Celsius. Look at the console for the converted temperatures.
convert_celsius_to_fahrenheit(20)
convert_celsius_to_fahrenheit(25)
convert_celsius_to_fahrenheit(19)
convert_celsius_to_fahrenheit(30)
convert_celsius_to_fahrenheit(21)
convert_celsius_to_fahrenheit(28)