# In this module, we will create a function to be called
# in example_03_file_that_uses_test_module.py

# Create a convert Celsius to Fahrenheit function to use in a different file.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = 9 / 5 * celsius + 32
    return fahrenheit
