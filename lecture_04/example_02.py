# Create an infinite loop that does something inside.
# In order to create an infinite loop, we must pass a condition
# that always evaluates to True. Some examples are:
#
# while 1 == 1:, while 'a' == 'a':, while True, etc.

# while True:
#     print("Infinite loop")
#

# Create a function that counts down from any number to 0
# and prints the value.

countdown_number = 1000

while countdown_number > 0:
    print(countdown_number)
    countdown_number -= 1
