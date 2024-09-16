import time

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


# Implement a timer that prints the time remaining in a similar way to our smartphones.
def format_remaining_time(number):
    result = ''
    if number < 10:
        result += "0"
    result += str(number)
    return result

def get_time_left(seconds):
    minutes = seconds // 60
    seconds %= 60

    time_left = ''
    if minutes > 0:
        time_left += f"{format_remaining_time(minutes)}:"
    if seconds >= 0:
        time_left += f"{format_remaining_time(seconds)}"

    print(time_left)

seconds = 65
while seconds > 0:
    get_time_left(seconds)
    time.sleep(1)
    seconds -= 1
