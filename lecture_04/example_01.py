# Print numbers 0 through 99 using a loop.
number_of_times = 100
index = 0
while index < number_of_times:
    print(index)
    index += 1

# Prompt user to enter password and keep retrying until
# the password matches.
password = ''
correct_password = 'helloworld'
while password != correct_password:
    password = input('Please input password. ')
    if password == correct_password:
        print("Great Job!")
    else:
        print("Password is incorrect. Please try again.")


