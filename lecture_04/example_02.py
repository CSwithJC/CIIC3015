import random
# Create an infinite loop that does something inside.
# In order to create an infinite loop, we must pass a condition
# that always evaluates to True. Some examples are:
#
# while 1 == 1:, while 'a' == 'a':, while True, etc.

# NOTE: You MUST comment this loop out to be able to run the following examples.
# while True:
#     print("Infinite loop")


# Create a function that counts down from any number to 0
# and prints the value.
countdown_number = 1000
while countdown_number > 0:
    print(countdown_number)
    countdown_number -= 1

# Create a function that calculates the factorial of a number.
def factorial(num):
    answer = 1
    if num < 2:
        return answer
    index = 1
    while index <= num:
        answer *= index
        index += 1
    return answer

print(factorial(4))  # 24

# Guess a random number between 1 to 10, with the code telling you how close you are.
random_number = random.randint(1, 10)
answer = ''

while answer != random_number:
    answer = int(input("Please enter a number between 1 to 10: "))
    if answer == random_number:
        print("You guessed right! Great job!")
    elif answer < random_number:
        print("You are close but the random number is a bit larger than ", answer)
    else:
        print("You are close but the random number is a bit smaller than ", answer)


# Play a rock-paper-scissors game against the computer.
user_score = 0
cpu_score = 0

user_command = ''
while user_command != 'n':
    user_command = input("rock, paper or scissors?")
    # 1 = rock, 2 = paper, 3 = scissors
    cpu_command = random.randint(1, 3)

    if user_command == "rock":
        if cpu_command == 1:
            print("Tie!")
        elif cpu_command == 2:
            print("CPU scores!")
            cpu_score += 1
        else:
            print("User scores!")
            user_score += 1
    elif user_command == 'paper':
        if cpu_command == 1:
            print("User scores!")
            user_score += 1
        elif cpu_command == 2:
            print("Tie!")
        else:
            print("CPU scores!")
            cpu_score += 1
    elif user_command == 'scissors':
        if cpu_command == 1:
            print("CPU scores!")
            cpu_score += 1
        elif cpu_command == 2:
            print("User scores!")
            user_score += 1
        else:
            print("Tie!")
    else:
        print(f'the command "{user_command}" is not valid, please try again.')

    print(f"the current score of the game is: User: {user_score}, CPU: {cpu_score}")
    user_command = input("do you want to play again? (y/n)")
